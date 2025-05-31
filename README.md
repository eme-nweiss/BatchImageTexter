# Add Text to Images 📸✍️

![Python](https://img.shields.io/badge/python-v3.6+-blue.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

A Python script that automatically overlays custom text onto the center of multiple images using OpenCV.

---

## 🚀 Features

- ✅ **Batch image processing** - Process multiple images at once
- 🎯 **Automatic text centering** - Perfect text placement every time
- 🖼️ **Multiple format support** - PNG, JPG, JPEG, BMP, TIFF
- 🎨 **Customizable styling** - Font, color, and size options
- 📁 **Auto folder creation** - Output directories created automatically
- 🛡️ **Robust error handling** - Continues processing even if one image fails

---

## 📋 Requirements

- **Python 3.6** or higher
- **OpenCV (cv2)**

---

## ⚙️ Installation

### 1. Clone this repository
```bash
git clone https://github.com/eme-nweiss/BatchImageTexter.git
cd BatchImageTexter
```

### 2. Install dependencies
```bash
pip install opencv-python
```

### 3. Set up image folders

> ⚠️ **IMPORTANT**: You need to create a folder for your input images.

**Option A:** Create the folder with the default name
```bash
mkdir input_images
```

**Option B:** Use any name you prefer and modify the code
```python
add_text_to_images(input_folder="my_custom_folder")
```

### 4. Add your images
Place your images in the folder you created.

---

## 🖥️ Usage

### Basic usage
```python
python main.py
```

### Custom usage
```python
from main import add_text_to_images

# Custom configuration
add_text_to_images(
    input_folder="my_images",       # Your image folder
    output_folder="edited_images",  # Output folder
    text="My Custom Text"           # Text to add
)
```

---

## 📁 Project Structure

```
BatchImageTexter/
│
├── main.py                 # Main script
├── README.md              # This file
├── input_images/          # Image folder (create manually)
│   ├── image1.jpg
│   ├── image2.png
│   └── ...
└── output/                # Output folder (created automatically)
    ├── edited_image1.jpg
    ├── edited_image2.png
    └── ...
```

---

## 🎨 Customization

You can modify the following text properties in the `main.py` file:

```python
# Text properties (lines 32-36)
font = cv2.FONT_HERSHEY_SIMPLEX    # Font type
font_scale = 2                     # Font size
font_thickness = 4                 # Text thickness
text_color = (255, 0, 255)         # Color in BGR format
```

### Available colors (BGR format):
| Color   | BGR Value       | Preview |
|---------|-----------------|---------|
| Red     | `(0, 0, 255)`   | 🔴      |
| Green   | `(0, 255, 0)`   | 🟢      |
| Blue    | `(255, 0, 0)`   | 🔵      |
| White   | `(255, 255, 255)` | ⚪    |
| Black   | `(0, 0, 0)`     | ⚫      |
| Magenta | `(255, 0, 255)` | 🟣 ← Current |

---

## 📝 Supported Image Formats

- **PNG** - Portable Network Graphics
- **JPG/JPEG** - Joint Photographic Experts Group
- **BMP** - Bitmap Image File
- **TIFF** - Tagged Image File Format

---

## ⚠️ Important Notes

- **Input folder**: Make sure to create the `input_images` folder (or your chosen name) before running the script
- **Output images**: Processed images are saved with the `edited_` prefix to avoid overwriting originals
- **Error handling**: The script will continue processing other images even if one fails

---

## 🐛 Troubleshooting

### Error: "No images found in folder"
- ✓ Verify that the `input_images` folder exists
- ✓ Make sure it contains valid image files
- ✓ Check that filenames don't contain special characters

### Error: "Could not load image"
- ✓ The file might be corrupted
- ✓ Verify that the image format is supported
- ✓ Try opening the image with another program to confirm it works

---

## 🤝 Contributing

Contributions are welcome! Please:

1. **Fork** the project
2. Create a **feature branch** (`git checkout -b feature/new-feature`)
3. **Commit** your changes (`git commit -am 'Add new feature'`)
4. **Push** to the branch (`git push origin feature/new-feature`)
5. Open a **Pull Request**

---

## 📄 License

This project is licensed under the **MIT License**. See the LICENSE file for details.

---

