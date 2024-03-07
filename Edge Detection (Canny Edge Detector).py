import os
import cv2

def apply_canny_edge_detection(input_dir, output_dir):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Process each JPEG file in the input directory
    for filename in os.listdir(input_dir):
        if filename.endswith('.jpg'):
            # Load the image
            image_path = os.path.join(input_dir, filename)
            image = cv2.imread(image_path)

            # Convert the image to grayscale
            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            # Apply Canny edge detection
            edges = cv2.Canny(gray_image, 50, 150)

            # Save the edge-detected image
            output_path = os.path.join(output_dir, filename)
            cv2.imwrite(output_path, edges)

# Input and output directories
input_dir = r'C:\Users\rugve\OneDrive\Desktop\files\output jpg'
output_dir = r'C:\Users\rugve\OneDrive\Desktop\files\Edge Detection (Canny Edge Detector)'

# Apply Canny edge detection
apply_canny_edge_detection(input_dir, output_dir)
