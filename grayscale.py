import os
from PIL import Image

def convert_to_grayscale(input_dir, output_dir):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Process each JPEG file in the input directory
    for filename in os.listdir(input_dir):
        if filename.endswith('.jpg'):
            # Load the image
            image_path = os.path.join(input_dir, filename)
            image = Image.open(image_path)

            # Convert to grayscale
            grayscale_image = image.convert('L')

            # Save the grayscale image
            grayscale_path = os.path.join(output_dir, filename)
            grayscale_image.save(grayscale_path)

# Input and output directories
input_dir = r'C:\Users\rugve\OneDrive\Desktop\files\output jpg'
output_dir = r'C:\Users\rugve\OneDrive\Desktop\files\grayscale output'

# Convert JPEG images to grayscale
convert_to_grayscale(input_dir, output_dir)
