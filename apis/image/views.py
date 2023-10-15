 import json
import cv2

def detect_traffic_density(video_path):
    # Load the video from a file or a camera
    cap = cv2.VideoCapture(video_path)

    # Initialize variables to keep track of the number of vehicles and their speed
    vehicle_count = 0
    vehicle_speed = 0

    # Get the time stamp of the first frame
    ret, frame = cap.read()
    if not ret:
        return json.dumps({'traffic_density': 0, 'vehicle_speed': 0})
    first_frame_time = cap.get(cv2.CAP_PROP_POS_MSEC)

    # Loop through each frame of the video
    while True:
        # Read the next frame
        ret, frame = cap.read()

        # If there are no more frames, break out of the loop
        if not ret:
            break

        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Apply a Gaussian blur to the grayscale image to reduce noise
        blur = cv2.GaussianBlur(gray, (5, 5), 0)

        # Apply a Canny edge detection algorithm to the blurred image
        edges = cv2.Canny(blur, 50, 150)

        # Find contours in the edges image
        contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Loop through each contour
        for contour in contours:
            # Calculate the area of the contour
            area = cv2.contourArea(contour)

            # If the area is too small, ignore the contour
            if area < 100:
                continue

            # Draw a bounding box around the contour
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Increment the vehicle count
            vehicle_count += 1

            # Calculate the speed of the vehicle
            vehicle_speed = calculate_vehicle_speed(x, y, w, h, cap.get(cv2.CAP_PROP_FPS), 10)

        # Display the resulting image with bounding boxes around the detected vehicles
        cv2.imshow('frame', frame)

        # Wait for a key press to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture object and close all windows
    cap.release()
    cv2.destroyAllWindows()

    # Calculate the traffic density as the number of vehicles per minute
    last_frame_time = cap.get(cv2.CAP_PROP_POS_MSEC)
    total_time = (last_frame_time - first_frame_time) / 1000
    if total_time == 0:
        traffic_density = 0
    else:
        traffic_density = vehicle_count / total_time * 60

    # Return the traffic density and the average vehicle speed as a JSON string
    return json.dumps({'traffic_density': traffic_density, 'vehicle_speed': vehicle_speed})

def calculate_vehicle_speed(x, y, w, h, fps, distance):
    # Calculate the midpoint of the bounding box
    x_mid = x + w / 2
    y_mid = y + h / 2

    # Calculate the speed of the vehicle based on its position in the frame and the distance to the camera
    speed = (x_mid - distance) * fps / 100

    return speed

if __name__ == '__main__':
    video_path = '../../static/Delhi traffic nightmare_ Tailback traffic near Vasant Kunj crossing (1).mp4'
    result = detect_traffic_density(video_path)
    print(result)
