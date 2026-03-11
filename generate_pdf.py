import asyncio
from playwright.async_api import async_playwright
import os

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        file_path = f"file://{os.path.abspath('seo-audit.html')}"
        
        # Go to the local HTML file and wait for it to be fully rendered
        await page.goto(file_path, wait_until="networkidle")
        
        # Print to PDF
        await page.pdf(
            path="seo-audit.pdf", 
            format="A4", 
            print_background=True, 
            margin={"top": "0", "bottom": "0", "left": "0", "right": "0"}
        )
        
        await browser.close()
        print("Successfully generated seo-audit.pdf!")

if __name__ == "__main__":
    asyncio.run(main())
