from PIL import Image
import os

def convert_images_to_webp(input_folder):
    image_files = [f for f in os.listdir(input_folder) if f.endswith(('.png', '.jpg', '.jpeg'))]

    for image_file in image_files:
        # image path
        input_image_path = os.path.join(input_folder, image_file)

        # output path to WebP (same diraction)
        output_image_path = os.path.splitext(input_image_path)[0] + ".webp"

        # convert to WebP
        img = Image.open(input_image_path)
        img.save(output_image_path, "webp")

if __name__ == "__main__":
    input_folder = input("please input your images path: ")
    convert_images_to_webp(input_folder)