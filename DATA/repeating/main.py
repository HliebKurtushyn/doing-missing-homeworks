from PIL import Image
import os


class ImageHashTable:
    def __init__(self):
        self.table = {}

    def compress_and_store(self, image_path, quality=60):
        if not os.path.exists(image_path):
            raise FileNotFoundError("Брат, такого файлу не існує.")

        dir_name, file_name = os.path.split(image_path)
        name, _ = os.path.splitext(file_name)
        compressed_path = os.path.join(dir_name, f"{name}_compressed.jpg")

        with Image.open(image_path) as img:
            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")
            img.save(compressed_path, "JPEG", quality=quality)

        self.table[image_path] = compressed_path
        return compressed_path

# Приклад:
# compressor = ImageHashTable()
# res_path = compressor.compress_and_store("photo.jpg")
# print(res_path)
# print(compressor.table)