import cv2
import numpy as np
import winsound

# Set up video capture from the default camera (usually the webcam)
cap = cv2.VideoCapture(0)

# Define region of interest (ROI) for lane detection
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # Get the width of the video frame
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # Get the height of the video frame

# Define ROI as a polygonal region within the frame
roi = np.array([[
    (0, height),
    (0.45 * width, 0.6 * height),
    (0.55 * width, 0.6 * height),
    (width, height)
]], dtype=np.int32)

# Define kernel size for image processing
kernel_size = 5  # Corrected variable name

# Define parameters for Canny edge detection and Hough transform
canny_low_threshold = 50  # Low threshold for Canny edge detection
canny_high_threshold = 150  # High threshold for Canny edge detection

hough_rho = 1  # Rho resolution in pixels for the Hough transform
hough_theta = np.pi / 180  # Theta resolution in radians for the Hough transform
hough_threshold = 50  # Threshold for Hough transform to detect lines
hough_min_line_length = 100  # Minimum line length to be detected
hough_max_line_gap = 50  # Maximum gap between line segments to be considered a single line

# Define lane departure alert parameters
alert_count = 0  # Counter for consecutive frames without detected lanes
alert_threshold = 5  # Number of frames to trigger the alert

# Define function for processing each frame
def process_frame(frame):
    global alert_count

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise
    blur = cv2.GaussianBlur(gray, (kernel_size, kernel_size), 0)

    # Apply Canny edge detection
    edges = cv2.Canny(blur, canny_low_threshold, canny_high_threshold)

    # Apply ROI mask to focus on the region of interest
    mask = np.zeros_like(edges)  # Create a mask with the same dimensions as edges
    cv2.fillPoly(mask, roi, 255)  # Fill the ROI in the mask
    masked_edges = cv2.bitwise_and(edges, mask)  # Apply the mask to the edges

    # Apply Hough transform to detect lines
    lines = cv2.HoughLinesP(masked_edges, hough_rho, hough_theta, hough_threshold, np.array([]), minLineLength=hough_min_line_length, maxLineGap=hough_max_line_gap)

    # Draw detected lines on a blank image
    line_image = np.zeros((height, width, 3), dtype=np.uint8)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]  # Unpack the line coordinates
            cv2.line(line_image, (x1, y1), (x2, y2), (0, 0, 255), 2)  # Draw the line in red

    # Combine line image with the original frame
    result = cv2.addWeighted(frame, 0.8, line_image, 1, 0)  # Blend the original frame with the lines image

    # Check for lane departure
    if lines is not None and len(lines) > 0:
        alert_count = 0  # Reset the alert count if lanes are detected
    else:
        alert_count += 1  # Increment the alert count if no lanes are detected

    # Display alert if lane departure is detected
    if alert_count >= alert_threshold:
        cv2.putText(result, 'Lane Departure Detected!', (int(width * 0.4), int(height * 0.9)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)  # Show alert text
        winsound.Beep(1000, 500)  # Play a beep sound for 500ms

    return result

# Process each frame of video
while True:
    ret, frame = cap.read()  # Read a frame from the video feed
    if ret:
        result = process_frame(frame)  # Process the frame
        cv2.imshow('LDWS', result)  # Display the result in a window named 'LDWS'

        # Check if the 'q' key is pressed to exit the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release the video capture and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
