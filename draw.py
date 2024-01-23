from random import shuffle
from PIL import Image
import os

# Set dimensions of final collage image
width, height = 2256, 1504
# Set the number of rows in the final collage image
images_row = 5

images_size = height // images_row

# Get list of all image files in output folder
output_folder = "./output"
image_files = [os.path.join(output_folder, f) for f in os.listdir(
    output_folder) if f.endswith(".jpg") or f.endswith(".png")]


def create_collage():
    # Create new blank image. Add padding for another row and column
    collage = Image.new("RGB", (width + images_size, height + images_size))

    # Loop through each image file in random order and paste onto blank image
    x_offset, y_offset = 0, 0
    shuffle(image_files)
    for image_file in image_files:
        # Open image file
        image = Image.open(image_file)
        # Resize image to fit within collage dimensions
        image.thumbnail((images_size, images_size))
        # Paste image onto collage
        collage.paste(image, (x_offset, y_offset))
        # Update x and y offsets for next image
        x_offset += images_size
        if x_offset >= width:
            x_offset = 0
            y_offset += images_size

    # Trim image to remove extra padding
    actual_padding_horizontal = width % images_size

    crop_x = actual_padding_horizontal // 2
    crop_y = images_size // 2
    collage = collage.crop((crop_x, crop_x, width + crop_x, height + crop_y))

    return collage


def main():
    while True:
        collage = create_collage()
        collage.show()
        # ask user if it is okay
        user_input = input("Is this okay? (y/n): ")
        if user_input == "y":
            collage.save('collage.jpg')
            break


if __name__ == "__main__":
    main()
