from PIL import Image
import os

def convert_images_to_webp(input_folder):
    image_files = [f for f in os.listdir(input_folder) if f.endswith(('.png', '.jpg', '.jpeg'))]

    for image_file in image_files:
        # 이미지 파일 경로
        input_image_path = os.path.join(input_folder, image_file)

        # WebP로 변환된 이미지 파일 경로 (같은 폴더에 저장)
        output_image_path = os.path.splitext(input_image_path)[0] + ".webp"

        # 이미지를 WebP로 변환
        img = Image.open(input_image_path)
        img.save(output_image_path, "webp")

if __name__ == "__main__":
    input_folder = input("이미지 파일들이 있는 폴더 경로를 입력하세요: ")

    convert_images_to_webp(input_folder)