# resize image to 512x512
import os
import cv2
import numpy as np

def resize_image(image_path, output_path, size=(512, 512)):
    """
    Resize an image to the specified size and save it to the output path.
    
    Args:
        image_path (str): Path to the input image.
        output_path (str): Path to save the resized image.
        size (tuple): Desired size for the resized image (width, height).
    """
    # Read the image
    image = cv2.imread(image_path)
    
    # Check if the image was loaded successfully
    if image is None:
        print(f"Error: Could not read image {image_path}")
        return
    
    # Resize the image
    resized_image = cv2.resize(image, size)
    
    # Save the resized image
    cv2.imwrite(output_path, resized_image)
    print(f"Resized image saved to {output_path}")

if __name__ == "__main__":
    # Example usage
    input_image_path = "images/me.jpg"  # Path to the input image
    output_image_path = "images/new_me.jpg"  # Path to save the resized image
    
    # Resize the image
    resize_image(input_image_path, output_image_path)