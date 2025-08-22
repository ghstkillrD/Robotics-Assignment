# object_detection.py
import cv2
import numpy as np

def detect_apple(image_path):
    """
    This function will take the path to an image and return the (x, y) coordinates of the center of a red apple.
    """
    # 1. Load the image from the specified path
    image = cv2.imread(image_path)
    # Make a copy for drawing on later
    output_image = image.copy()

    # 2. Convert the image from BGR to HSV color space (Better for color filtering)
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # 3. Define the range for the color "Red" in HSV.
    # These values will need to be adjusted! This is just a starting point.
    #lower_red = np.array([160, 100, 100])   # Lower bound for Hue, Saturation, Value
    #upper_red = np.array([180, 255, 255])  # Upper bound for Hue, Saturation, Value
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])

    # 4. Create a mask: a black and white image where white pixels are within the red range
    mask = cv2.inRange(hsv_image, lower_red, upper_red)

    # 5. Find contours (outlines) of the white blobs in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 6. If we found any contours, find the largest one (assumed to be the apple)
    if contours:
        largest_contour = max(contours, key=cv2.contourArea)
        # Calculate the center and radius of the smallest circle that encloses the contour
        (x, y), radius = cv2.minEnclosingCircle(largest_contour)
        center = (int(x), int(y))
        radius = int(radius)

        # 7. Draw a green circle and a dot at the center on the output image
        cv2.circle(output_image, center, radius, (0, 255, 0), 2)  # Green outline
        cv2.circle(output_image, center, 3, (0, 255, 0), -1)      # Green center dot

        # 8. Print the center coordinates to the console
        print(f"Apple detected at center coordinates: {center}")

        # 9. Display the original image, the mask, and the output image with the detection
        cv2.imshow('Original Image', image)
        cv2.imshow('Mask', mask)
        cv2.imshow('Apple Detection', output_image)
        cv2.waitKey(0) # Wait for a key press to close the windows
        cv2.destroyAllWindows()

        # 10. Return the center coordinates for use in the navigation system
        return center

    else:
        print("No apple detected.")
        return None

# Test the function immediately when this script is run
if __name__ == "__main__":
    # Test on the simulated world first (the easiest case)
    detect_apple('../data/simulated_world.png')