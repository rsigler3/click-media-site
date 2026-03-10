import os
from PIL import Image

def convert_images_and_update_html():
    image_dir = "images"
    image_files = []
    
    # Extensions to convert
    exts = ['.png', '.jpg', '.jpeg']
    
    for root, dirs, files in os.walk(image_dir):
        for f in files:
            file_ext = os.path.splitext(f)[1].lower()
            if file_ext in exts:
                image_files.append(os.path.join(root, f))
    
    # Store old to new mapping
    mappings = {}
    
    for img_path in image_files:
        path_without_ext, ext = os.path.splitext(img_path)
        new_path = path_without_ext + '.webp'
        
        try:
            # Convert using Pillow
            with Image.open(img_path) as im:
                # Convert to RGB if necessary (e.g. for some P modes or RGBA to WebP without alpha if saving as lossy, though webp supports RGBA)
                # But WebP supports RGBA natively! Let's just save.
                im.save(new_path, format="webp")
            
            print(f"Successfully converted {img_path} to {new_path}")
            
            # Remove original file
            os.remove(img_path)
            
            # Map the old filename to the new filename for html replacement
            # Also just the basename (e.g. "image.png" -> "image.webp")
            old_base = os.path.basename(img_path)
            new_base = os.path.basename(new_path)
            
            mappings[img_path] = new_path
            mappings[img_path.replace(os.path.sep, '/')] = new_path.replace(os.path.sep, '/')
            mappings[old_base] = new_base
            
            # Also handle URL encoded bases just in case
            mappings[old_base.replace(' ', '%20')] = new_base.replace(' ', '%20')
            mappings[img_path.replace(os.path.sep, '/').replace(' ', '%20')] = new_path.replace(os.path.sep, '/').replace(' ', '%20')

        except Exception as e:
            print(f"Failed to convert {img_path}: {e}")

    # Now update all HTML files
    html_files = []
    for root, dirs, files in os.walk('.'):
        for f in files:
            if f.endswith('.html'):
                html_files.append(os.path.join(root, f))
                
    for html_file in html_files:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        original_content = content
        
        # Sort mappings by length descending so longer paths are replaced first
        # This prevents replacing part of a path prematurely
        sorted_mappings = sorted(mappings.keys(), key=len, reverse=True)
        
        for old_str in sorted_mappings:
            new_str = mappings[old_str]
            content = content.replace(old_str, new_str)
                
        if content != original_content:
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated references in {html_file}")

if __name__ == '__main__':
    convert_images_and_update_html()
