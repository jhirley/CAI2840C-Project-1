import cv2 as cv
import os
import json
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
# cameras list from the .env file is in the format
# Example: '[{"name":  "camera1", "low_res": "rtsp://", "high_res": "rtsp://"}]'
# Debugging: Print the value of the CAMERAS environment variable


def open_video(video_path):
    """
    Opens a video file for reading.

    Args:
        video_path (str): The path to the video file to be opened.

    Returns:
        cv2.VideoCapture: A VideoCapture object if the video is successfully opened, 
                        None if there is an error opening the video stream or file.
    """
    # Check if the video file exists
    cap = cv.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error opening video stream or file")
        return None
    return cap

def scale_capture_stream(cap, height, width, fps):
    # Set the video capture stream to the desired height, width, and fps
    # Common resolutions:
    # 240p = 426x240
    # 480p = 640x480
    # 720p = 1280x720
    # 1080p = 1920x1080
    # 4k = 3840x2160
    cap.set(cv.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv.CAP_PROP_FRAME_HEIGHT, height)
    cap.set(cv.CAP_PROP_FPS, fps)
    return cap



if __name__ == "__main__":
    # Get the cameras list from the .env file
    cameras_json = os.getenv("CAMERAS")
    if not cameras_json:
        raise ValueError("CAMERAS environment variable is not set or is empty")

    try:
        cameras = json.loads(cameras_json)
    except json.JSONDecodeError as e:
        raise ValueError(f"Error parsing CAMERAS environment variable: {e}")

    # Open video streams for all cameras
    caps = {}
    for camera in cameras:
        cap = open_video(camera.get("low_res"))
        if cap:
            cap = scale_capture_stream(cap, 480, 640, 1)
            caps[camera.get("name")] = cap

    # Display frames from all cameras
    while True:
        for name, cap in caps.items():
            ret, frame = cap.read()
            if not ret:
                print(f"Error reading frame from camera: {name}")
                continue
            cv.imshow(name, frame)

        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    # Release all video captures and close windows
    for cap in caps.values():
        cap.release()
    cv.destroyAllWindows()