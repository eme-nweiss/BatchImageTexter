Add Text to Images 📸✍️
A Python script that automatically overlays custom text onto the center of multiple images using OpenCV.
🚀 Features

Batch image processing
Automatic text centering
Support for multiple image formats (PNG, JPG, JPEG, BMP, TIFF)
Customizable font and color settings
Automatic output folder creation
Robust error handling

📋 Requirements

Python 3.6 or higher
OpenCV (cv2)

⚙️ Installation

Clone this repository:
bashgit clone https://github.com/eme-nweiss/BatchImageTexter.git
cd BatchImageTexter

Install dependencies:
bashpip install opencv-python

Set up image folders:
⚠️ IMPORTANT: You need to create a folder for your input images. You can use either of these options:

Option A: Create the folder with the default name:
bashmkdir input_images

Option B: Use any name you prefer and modify the code:
pythonadd_text_to_images(input_folder="my_custom_folder")



Place your images in the folder you created.

🖥️ Usage
Basic usage
pythonpython main.py
Custom usage
pythonfrom main import add_text_to_images

# Custom configuration
add_text_to_images(
    input_folder="my_images",           # Your image folder
    output_folder="edited_images",      # Output folder
    text="My Custom Text"               # Text to add
)
📁 Project Structure
project/
│
├── main.py                 # Main script
├── README.md              # This file
├── input_images/          # Image folder (create manually)
│   ├── image1.jpg
│   ├── image2.png
│   └── ...
└── output/               # Output folder (created automatically)
    ├── edited_image1.jpg
    ├── edited_image2.png
    └── ...
🎨 Customization
You can modify the following text properties in the main.py file:
python# Text properties (lines 32-36)
font = cv2.FONT_HERSHEY_SIMPLEX  # Font type
font_scale = 2                   # Font size
font_thickness = 4               # Text thickness
text_color = (255, 0, 255)       # Color in BGR format (blue, green, red)
Available colors (BGR format):

Red: (0, 0, 255)
Green: (0, 255, 0)
Blue: (255, 0, 0)
White: (255, 255, 255)
Black: (0, 0, 0)
Magenta: (255, 0, 255) ← Current color

📝 Supported Image Formats

PNG
JPG/JPEG
BMP
TIFF

⚠️ Important Notes

Input folder: Make sure to create the input_images folder (or your chosen name) before running the script
Output images: Processed images are saved with the edited_ prefix to avoid overwriting originals
Error handling: The script will continue processing other images even if one fails

🐛 Troubleshooting
Error: "No images found in folder"

Verify that the input_images folder exists
Make sure it contains valid image files
Check that filenames don't contain special characters

Error: "Could not load image"

The file might be corrupted
Verify that the image format is supported
Try opening the image with another program to confirm it works

🤝 Contributing
Contributions are welcome! Please:

Fork the project
Create a feature branch (git checkout -b feature/new-feature)
Commit your changes (git commit -am 'Add new feature')
Push to the branch (git push origin feature/new-feature)
Open a Pull Request

📄 License
This project is licensed under the MIT License. See the LICENSE file for details.