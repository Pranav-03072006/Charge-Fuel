import os
from PIL import Image

def compress_images(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            
            if file.lower().endswith('.png'):
                try:
                    with Image.open(filepath) as img:
                        if img.width > 1080:
                            ratio = 1080 / img.width
                            new_size = (1080, int(img.height * ratio))
                            img = img.resize(new_size, Image.Resampling.LANCZOS)
                        img.save(filepath, "PNG", optimize=True)
                        print(f"Compressed PNG: {file}")
                except Exception as e:
                    pass
                    
            elif file.lower().endswith('.gif'):
                try:
                    with Image.open(filepath) as img:
                        first_frame = img.copy()
                        if first_frame.width > 1080:
                            ratio = 1080 / first_frame.width
                            new_size = (1080, int(first_frame.height * ratio))
                            first_frame = first_frame.resize(new_size, Image.Resampling.LANCZOS)
                        first_frame.save(filepath, "GIF", optimize=True)
                        print(f"Compressed GIF to static: {file}")
                except Exception as e:
                    pass

if __name__ == "__main__":
    static_dir = os.path.join(os.path.dirname(__file__), 'development', 'static', 'images')
    if os.path.exists(static_dir):
        compress_images(static_dir)
