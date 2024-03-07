import os
import cv2

def apply_gaussian_blur(input_dir, output_dir):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Process each JPEG file in the input directory
    for filename in os.listdir(input_dir):
        if filename.endswith('.jpg'):
            # Load the image
            image_path = os.path.join(input_dir, filename)
            image = cv2.imread(image_path)

            # Apply Gaussian blur
            blurred_image = cv2.GaussianBlur(image, (5, 5), 0)

            # Save the blurred image
            output_path = os.path.join(output_dir, filename)
            cv2.imwrite(output_path, blurred_image)

# Input and output directories
input_dir = r'C:\Users\rugve\OneDrive\Desktop\files\output jpg'
output_dir = r'C:\Users\rugve\OneDrive\Desktop\files\Gaussian blur for noise reduction'

# Apply Gaussian blur for noise reduction
apply_gaussian_blur(input_dir, output_dir)
