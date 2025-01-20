from PIL import Image, ImageEnhance, ImageFilter
import os

# Create a Folder for image store use as path

path = './imgs'
PathOut = './editedImgs'

if not os.path.exists(path):
    os.makedirs(path)
    print(f"Created missing directory: {path}. Add images to this folder and rerun the script.")

os.makedirs(PathOut, exist_ok=True)

for filename in os.listdir(path):
    if filename.endswith(('.png', '.jpg', '.jpeg')):
        img = Image.open(f"{path}/{filename}")
        
        factor = 1.5
        edit = img.filter(ImageFilter.SHARPEN)
        enhancer = ImageEnhance.Brightness(edit)
        edit = enhancer.enhance(factor)
        
        clean_name = os.path.splitext(filename)[0]
        edit.save(f"{PathOut}/{clean_name}_edited.jpg")
