import os
import sys
from PIL import Image

def optimize_images(directory, quality=85):
    """
    Optimize all images in the specified directory and its subdirectories.
    
    Args:
        directory (str): The directory to search for images
        quality (int): Quality of the optimized images (1-100)
    """
    print(f"Optimizing images in {directory}...")
    
    # Extensions to optimize
    extensions = ['.jpg', '.jpeg', '.png']
    
    # Count optimized images
    count = 0
    
    # Walk through the directory
    for root, _, files in os.walk(directory):
        for file in files:
            # Check if the file has an image extension
            if any(file.lower().endswith(ext) for ext in extensions):
                file_path = os.path.join(root, file)
                
                # Get the file size before optimization
                original_size = os.path.getsize(file_path)
                
                try:
                    # Open the image
                    with Image.open(file_path) as img:
                        # Check if the image is PNG and has alpha channel
                        if file.lower().endswith('.png') and img.mode == 'RGBA':
                            # Save as PNG with optimized settings
                            img.save(file_path, optimize=True, quality=quality)
                        elif file.lower().endswith(('.jpg', '.jpeg')):
                            # Save as JPEG with optimized settings
                            rgb_img = img.convert('RGB')
                            rgb_img.save(file_path, optimize=True, quality=quality)
                        
                        # Convert large PNGs to WebP if they're over 200KB
                        if file.lower().endswith('.png') and original_size > 200000:
                            webp_path = os.path.splitext(file_path)[0] + '.webp'
                            img.save(webp_path, 'WEBP', quality=quality)
                            print(f"Created WebP version: {webp_path}")
                            
                    # Get the file size after optimization
                    new_size = os.path.getsize(file_path)
                    
                    # Calculate the reduction percentage
                    reduction = (original_size - new_size) / original_size * 100
                    
                    print(f"Optimized: {file_path}")
                    print(f"  Size reduction: {original_size/1024:.1f} KB -> {new_size/1024:.1f} KB ({reduction:.1f}%)")
                    
                    count += 1
                    
                except Exception as e:
                    print(f"Error optimizing {file_path}: {e}")
    
    print(f"Finished optimizing {count} images.")

if __name__ == "__main__":
    # If a directory is provided as an argument, use it
    # Otherwise use the default directories
    if len(sys.argv) > 1:
        optimize_images(sys.argv[1])
    else:
        # Optimize common image directories in the project
        dirs_to_optimize = [
            'static/images',
            'about_images',
            'avatars',
            'skills',
            'projects',
            'certifications',
        ]
        
        for directory in dirs_to_optimize:
            if os.path.exists(directory):
                optimize_images(directory) 