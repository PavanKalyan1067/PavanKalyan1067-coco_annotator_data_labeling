from PIL import Image
import os

def resize_image(input_path, output_path, size):
    with Image.open(input_path) as image:
        # Resize the image while maintaining aspect ratio
        image.thumbnail(size)
        # Save the resized image
        image.save(output_path)

def batch_resize_images(input_folder, output_folder, size):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Loop through each file in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith('.jpg'):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)
            # Resize the image and save it to the output folder
            resize_image(input_path, output_path, size)

# Usage example
input_folder = 'Vehicle_images/Original_images'
output_folder = 'Vehicle_images/processed images'
size = (300, 500)  # Specify the desired width and height for resizing

batch_resize_images(input_folder, output_folder, size)
