import os
import glob
import re

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if 'href="education.html"' in content:
        print(f"Skipping {filepath}, already updated.")
        return

    pattern_desktop = r'(<a[^>]*class="[^"]*text-sm[^"]*"[^>]*href="contact\.html"[^>]*>CONTACT</a>)'
    replacement_desktop = r'<a class="text-sm font-semibold hover:text-primary transition-colors" href="education.html">EDUCATION</a>\n                        \1'
    content = re.sub(pattern_desktop, replacement_desktop, content)
    
    pattern_mobile = r'(<a[^>]*class="[^"]*mobile-link[^"]*"[^>]*href="contact\.html"[^>]*>CONTACT</a>)'
    replacement_mobile = r'<a class="text-2xl font-bold text-white hover:text-primary transition-colors mobile-link" href="education.html">EDUCATION</a>\n            \1'
    content = re.sub(pattern_mobile, replacement_mobile, content)
    
    pattern_footer = r'(<li>\s*<a[^>]*href="contact\.html"[^>]*>Contact(?: Us)?</a>\s*</li>)'
    replacement_footer = r'<li><a class="hover:text-white transition-colors" href="education.html">Education</a></li>\n                            \1'
    content = re.sub(pattern_footer, replacement_footer, content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Updated {filepath} with regex injection.")

if __name__ == "__main__":
    html_files = glob.glob('*.html')
    for file in html_files:
        if file not in ['article.html', 'education.html', 'index.html']: # I already did index.html
            update_file(file)
