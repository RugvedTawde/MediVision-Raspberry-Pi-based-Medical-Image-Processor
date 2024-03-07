import os
import pydicom
from PIL import Image


def convert_dicom_to_jpeg(dicom_path, jpeg_path):
    # Read the DICOM file
    ds = pydicom.dcmread(dicom_path)

    # Convert pixel data to a NumPy array
    pixel_array = ds.pixel_array

    # Convert the NumPy array to a PIL Image
    image = Image.fromarray(pixel_array)

    # Convert image to an appropriate mode for JPEG (e.g., 'L' for grayscale or 'RGB' for color)
    if image.mode != 'RGB':
        image = image.convert('RGB')

    # Save the image as a JPEG file
    image.save(jpeg_path)


def convert_all_dicom_to_jpeg(input_dir, output_dir):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Process each DICOM file in the input directory
    for filename in os.listdir(input_dir):
        if filename.endswith('.dcm'):
            dicom_path = os.path.join(input_dir, filename)
            jpeg_path = os.path.join(output_dir, filename[:-4] + '.jpg')  # Change file extension to .jpg
            convert_dicom_to_jpeg(dicom_path, jpeg_path)


# Input and output directories
input_dir = r'C:\Users\rugve\OneDrive\Desktop\files\input dicom'
output_dir = r'C:\Users\rugve\OneDrive\Desktop\files\output jpg'

# Convert all DICOM files in the input directory to JPEG files in the output directory
convert_all_dicom_to_jpeg(input_dir, output_dir)
