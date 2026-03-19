import os
import glob

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Skip if already added
    if 'href="education.html"' in content:
        print(f"Skipping {filepath}, already updated.")
        return

    # Update Desktop Nav Dropdown
    desktop_str = '<a class="text-sm font-semibold hover:text-primary transition-colors" href="contact.html">CONTACT</a>'
    
    new_desktop_str = '<a class="text-sm font-semibold hover:text-primary transition-colors" href="education.html">EDUCATION</a>\n                        '

    if desktop_str in content:
        content = content.replace(desktop_str, new_desktop_str + desktop_str)

    # Update Mobile Nav
    mobile_str = '<a class="text-xl font-bold text-white mobile-link" href="contact.html">CONTACT</a>'
    mobile_str_fallback = '<a class="text-2xl font-bold text-white hover:text-primary transition-colors mobile-link" href="contact.html">CONTACT</a>'
    
    new_mobile_str = '<a class="text-xl font-bold text-white mobile-link" href="education.html">EDUCATION</a>\n            '
    new_mobile_str_fallback = '<a class="text-2xl font-bold text-white hover:text-primary transition-colors mobile-link" href="education.html">EDUCATION</a>\n            '

    if mobile_str in content:
        content = content.replace(mobile_str, new_mobile_str + mobile_str)
    elif mobile_str_fallback in content:
        content = content.replace(mobile_str_fallback, new_mobile_str_fallback + mobile_str_fallback)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Updated {filepath}")

if __name__ == "__main__":
    html_files = glob.glob('*.html')
    for file in html_files:
        update_file(file)
