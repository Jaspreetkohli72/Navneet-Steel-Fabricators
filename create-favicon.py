#!/usr/bin/env python3
"""
Favicon Converter for Navneet Steel Fabricators
Downloads LinkedIn company logo and converts to favicon
"""

import urllib.request
import io
from PIL import Image

def create_favicon():
    """Download LinkedIn logo and convert to favicon"""
    
    linkedin_logo_url = "https://media.licdn.com/dms/image/v2/D4E0BAQEPq2p5fGvQvA/company-logo_200_200/B4EZfO1XUFGwAM-/0/1751521789118?e=2147483647&v=beta&t=W9_iRK7Sg7lfH44Y_OlZrOSbZPKDmWm7QFb_0Mi8weE"
    
    try:
        print("Downloading LinkedIn company logo...")
        with urllib.request.urlopen(linkedin_logo_url) as response:
            image_data = response.read()
        
        # Open image
        img = Image.open(io.BytesIO(image_data))
        print(f"Original image size: {img.size}")
        
        # Resize to 256x256 for favicon
        img = img.resize((256, 256), Image.Resampling.LANCZOS)
        
        # Convert to ICO (favicon format)
        favicon_path = "img/favicon.ico"
        img.save(favicon_path, format="ICO", sizes=[(256, 256)])
        
        print(f"✓ Favicon created successfully at: {favicon_path}")
        print(f"✓ Size: 256x256 pixels")
        
        # Also create PNG version as backup
        png_path = "img/favicon-192.png"
        img.save(png_path, format="PNG")
        print(f"✓ PNG version also created at: {png_path}")
        
        # Create manifest.json for progressive web app support
        manifest_content = """{
  "name": "Navneet Steel Fabricators",
  "short_name": "Navneet Steel",
  "description": "Professional Steel Fabrication Services",
  "start_url": "/",
  "display": "standalone",
  "background_color": "#ffffff",
  "theme_color": "#0066cc",
  "scope": "/",
  "icons": [
    {
      "src": "img/favicon-192.png",
      "sizes": "192x192",
      "type": "image/png"
    },
    {
      "src": "img/favicon.ico",
      "sizes": "256x256",
      "type": "image/x-icon"
    }
  ]
}"""
        
        with open("manifest.json", "w") as f:
            f.write(manifest_content)
        print(f"✓ Manifest created at: manifest.json")
        
    except Exception as e:
        print(f"✗ Error: {e}")
        print("\nAlternative: Manually convert favicon at:")
        print("  https://icoconvert.com/")
        print("  URL: https://media.licdn.com/dms/image/v2/D4E0BAQEPq2p5fGvQvA/company-logo_200_200/B4EZfO1XUFGwAM-/0/1751521789118")

if __name__ == "__main__":
    create_favicon()
