import cv2

# Function to calculate the absolute difference between two frames
def get_frame_difference(frame1, frame2):
    frame_diff = cv2.absdiff(frame1, frame2)
    gray_diff = cv2.cvtColor(frame_diff, cv2.COLOR_BGR2GRAY)
    _, threshold_diff = cv2.threshold(gray_diff, 30, 255, cv2.THRESH_BINARY)
    return threshold_diff

# Main function for motion detection
def motion_detection():
    video_capture = cv2.VideoCapture(0)  # Use 0 for the default webcam or provide the path to a video file

    # Initialize the first two frames
    _, prev_frame = video_capture.read()
    _, current_frame = video_capture.read()

    while True:
        diff = get_frame_difference(prev_frame, current_frame)
        cv2.imshow('Motion Detection', diff)

        # Update frames
        prev_frame = current_frame
        _, current_frame = video_capture.read()

        # Press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    motion_detection()
