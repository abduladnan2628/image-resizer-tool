import os
from PIL import Image

input_folder = "images_input"  
output_folder = "images_output" 
new_width = 800                 
new_height = 600                
output_format = "JPEG"          

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + f".{output_format.lower()}")

        try:
            with Image.open(input_path) as img:
                resized_img = img.resize((new_width, new_height))
                resized_img.save(output_path, output_format)
                print(f"✅ Saved: {output_path}")
        except Exception as e:
            print(f"❌ Failed to process {filename}: {e}")

print("🎯 All images processed successfully!")
