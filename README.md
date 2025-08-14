Here’s a polished and helpful **`README.md`** tailored for your **image-resizer-tool** repository. It provides a clear overview, setup instructions, usage guidelines, and potential improvements—perfect for anyone visiting your project on GitHub.

---

```markdown
# Image Resizer Tool

A lightweight Python script to batch-resize and convert images in a folder using the Pillow library.

##  Project Objective

Automate image resizing and format conversion for a collection of files—ideal for preparing web assets, creating thumbnails, or optimizing images for performance.

##  Built With

- **Python 3.x** – Core language for scripting  
- **Pillow (PIL)** – Image processing library for loading, resizing, and saving images  
- **OS Module** – File system operations like folder access and iteration

##  Folder Structure

```

image-resizer-tool/
│
├── images\_input/        ← Place your source images here
├── images\_output/       ← Resized (and optionally converted) images will be saved here
├── image\_resizer.py     ← Python script to process images
└── README.md            ← This file!

````

##  Getting Started

### Prerequisites

- Python 3.x installed  
- Basic familiarity with running Python scripts

### Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/abduladnan2628/image-resizer-tool.git
   cd image-resizer-tool
````

2. **Create and activate a virtual environment (recommended)**

   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install required library**

   ```bash
   pip install pillow
   ```

## Usage

1. Place the images you'd like to process in the `images_input/` directory (supports `.png`, `.jpg`, `.jpeg`, `.bmp`, `.gif`).

2. Configure your desired dimensions and output format in `image_resizer.py` by editing:

   ```python
   new_width = 800
   new_height = 600
   output_format = "JPEG"  # Options include "JPEG", "PNG", etc.
   ```

3. Run the script:

   ```bash
   python image_resizer.py
   ```

4. After successful execution, resized images will appear in the `images_output/` folder.

## Expected Output

* Console messages indicating processed images:

  ```
  ✅ Saved: images_output/photo1.jpeg
  ✅ Saved: images_output/photo2.jpeg
  ...
  🎯 All images processed successfully!
  ```

* Resized files in your `images_output/` directory.

## Future Enhancements

* Add support for **command-line arguments** (width, height, output format).
* Maintain aspect ratio automatically instead of fixed dimensions.
* Implement **batch formats**: apply different sizes based on sub-folders.
* Add logging and error handling for unsupported image files.
* Support **progress display** (e.g., progress bar for large batches).
* GUI integration (e.g., using Tkinter) for users less familiar with the terminal.

## License

This project is available under the **MIT License**. Feel free to use, modify, and contribute!

---

Let me know if you'd like to enrich the `README` further—maybe add badges, screenshots of before/after images, or a quick demo GIF for visual impact.
