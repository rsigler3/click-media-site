import os
import glob

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Skip if already added
    if 'href="seo.html"' in content:
        print(f"Skipping {filepath}, already updated.")
        return

    # Update Desktop Nav Dropdown
    desktop_str = '<a class="block px-4 py-3 text-sm hover:bg-white/10" href="social-media.html">Social\n                                        Media</a>'
    desktop_str_fallback = '<a class="block px-4 py-3 text-sm hover:bg-white/10" href="social-media.html">Social Media</a>'
    
    new_desktop_str = '<a class="block px-4 py-3 text-sm hover:bg-white/10" href="seo.html">SEO Services</a>'

    if desktop_str in content:
        content = content.replace(desktop_str, desktop_str + '\n                                    ' + new_desktop_str)
    elif desktop_str_fallback in content:
        content = content.replace(desktop_str_fallback, desktop_str_fallback + '\n                                    ' + new_desktop_str)

    # Update Mobile Nav
    mobile_str = '<a class="text-2xl font-bold text-white hover:text-primary transition-colors mobile-link"\n                href="social-media.html">SOCIAL MEDIA</a>'
    mobile_str_fallback = '<a class="text-2xl font-bold text-white hover:text-primary transition-colors mobile-link" href="social-media.html">SOCIAL MEDIA</a>'
    
    new_mobile_str = '<a class="text-2xl font-bold text-white hover:text-primary transition-colors mobile-link" href="seo.html">SEO SERVICES</a>'

    if mobile_str in content:
        content = content.replace(mobile_str, mobile_str + '\n            ' + new_mobile_str)
    elif mobile_str_fallback in content:
        content = content.replace(mobile_str_fallback, mobile_str_fallback + '\n            ' + new_mobile_str)

    # Update Footer
    footer_str = '<li><a class="hover:text-white transition-colors" href="social-media.html">Social Media</a>\n                            </li>'
    footer_str_fallback = '<li><a class="hover:text-white transition-colors" href="social-media.html">Social Media</a></li>'
    
    new_footer_str = '<li><a class="hover:text-white transition-colors" href="seo.html">SEO Services</a></li>'

    if footer_str in content:
        content = content.replace(footer_str, footer_str + '\n                            ' + new_footer_str)
    elif footer_str_fallback in content:
        content = content.replace(footer_str_fallback, footer_str_fallback + '\n                            ' + new_footer_str)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Updated {filepath}")

if __name__ == "__main__":
    html_files = glob.glob('*.html')
    for file in html_files:
        update_file(file)
