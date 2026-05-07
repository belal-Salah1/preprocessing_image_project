from fpdf import FPDF
from fpdf.enums import XPos, YPos

PRIMARY = (30, 80, 160)
DARK    = (20, 20, 20)
GRAY    = (90, 90, 90)
LIGHT   = (240, 242, 246)
WHITE   = (255, 255, 255)
ACCENT  = (220, 53, 69)


class DocPDF(FPDF):
    def header(self):
        self.set_fill_color(*PRIMARY)
        self.rect(0, 0, 210, 18, "F")
        self.set_font("Helvetica", "B", 10)
        self.set_text_color(*WHITE)
        self.set_y(5)
        self.cell(0, 8, "CS.383 - Image Processing Pipeline Documentation", align="C")
        self.set_text_color(*DARK)
        self.ln(16)

    def footer(self):
        self.set_y(-13)
        self.set_font("Helvetica", "", 8)
        self.set_text_color(*GRAY)
        self.cell(0, 6, f"Page {self.page_no()}", align="C")

    def section_title(self, text):
        self.ln(4)
        self.set_fill_color(*PRIMARY)
        self.set_text_color(*WHITE)
        self.set_font("Helvetica", "B", 12)
        self.cell(0, 9, f"  {text}", new_x=XPos.LMARGIN, new_y=YPos.NEXT, fill=True)
        self.set_text_color(*DARK)
        self.ln(3)

    def subsection(self, text):
        self.set_font("Helvetica", "B", 10)
        self.set_text_color(*PRIMARY)
        self.cell(0, 7, text, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_text_color(*DARK)

    def body_text(self, text):
        self.set_font("Helvetica", "", 10)
        self.set_text_color(*DARK)
        self.multi_cell(0, 6, text)
        self.ln(1)

    def bullet(self, text, indent=8):
        self.set_font("Helvetica", "", 10)
        self.set_text_color(*DARK)
        x = self.get_x()
        self.set_x(self.l_margin + indent)
        self.cell(5, 6, "-")
        self.multi_cell(0, 6, text)
        self.set_x(x)

    def code_block(self, lines):
        self.set_fill_color(*LIGHT)
        self.set_draw_color(200, 200, 200)
        total_h = len(lines) * 5.5 + 6
        self.rect(self.l_margin, self.get_y(), 190, total_h, "FD")
        self.set_font("Courier", "", 9)
        self.set_text_color(50, 50, 50)
        self.set_y(self.get_y() + 3)
        for line in lines:
            self.set_x(self.l_margin + 4)
            self.cell(0, 5.5, line, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_text_color(*DARK)
        self.ln(3)

    def table(self, headers, rows, col_widths):
        # Header row
        self.set_fill_color(*PRIMARY)
        self.set_text_color(*WHITE)
        self.set_font("Helvetica", "B", 9)
        for h, w in zip(headers, col_widths):
            self.cell(w, 8, f"  {h}", border=1, fill=True)
        self.ln()
        # Data rows
        self.set_text_color(*DARK)
        self.set_font("Helvetica", "", 9)
        for i, row in enumerate(rows):
            fill = i % 2 == 0
            self.set_fill_color(248, 249, 252) if fill else self.set_fill_color(*WHITE)
            for cell, w in zip(row, col_widths):
                self.cell(w, 7, f"  {cell}", border=1, fill=True)
            self.ln()
        self.ln(2)


def build():
    pdf = DocPDF()
    pdf.set_margins(15, 22, 15)
    pdf.set_auto_page_break(auto=True, margin=18)
    pdf.add_page()

    # -- Title block ----------------------------------------------------------
    pdf.set_font("Helvetica", "B", 22)
    pdf.set_text_color(*PRIMARY)
    pdf.cell(0, 12, "Image Processing Pipeline", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
    pdf.set_font("Helvetica", "", 13)
    pdf.set_text_color(*GRAY)
    pdf.cell(0, 8, "MNIST JPG Dataset - CS.383 Group Project", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
    pdf.ln(6)

    # Divider
    pdf.set_draw_color(*PRIMARY)
    pdf.set_line_width(0.8)
    pdf.line(15, pdf.get_y(), 195, pdf.get_y())
    pdf.ln(6)

    # -- Overview -------------------------------------------------------------
    pdf.section_title("1. Project Overview")
    pdf.body_text(
        "This project implements a four-stage image processing pipeline on the MNIST handwritten "
        "digit dataset (JPG format). Each stage builds on the previous one, taking an image from "
        "raw collection through preprocessing, filtering, and finally edge detection and segmentation. "
        "The project is part of CS.383 and is split across four team members."
    )

    # -- Project Structure -----------------------------------------------------
    pdf.section_title("2. Project Structure")
    pdf.table(
        headers=["File", "Description"],
        rows=[
            ("project_pipeline.py", "Full pipeline - runs all 4 stages end-to-end"),
            ("dataset_collection.py", "Stage 1 - Dataset exploration and visualization"),
            ("preprocessing.py",      "Stage 2 - Resize, grayscale, normalize, invert"),
            ("filtering.py",          "Stage 3 - Gaussian blur, median filter, sharpening"),
            ("edge_detection.py",     "Stage 4 - Sobel, Canny, Otsu segmentation"),
        ],
        col_widths=[70, 120],
    )

    # -- Pipeline Stages -------------------------------------------------------
    pdf.section_title("3. Pipeline Stages")

    pdf.subsection("Stage 1 - Dataset Collection  (dataset_collection.py)")
    pdf.bullet("Scans the mnist_jpg/ directory (subfolders 0-9)")
    pdf.bullet("Reports the image count per digit class")
    pdf.bullet("Displays one sample image per digit in a 2x5 matplotlib grid")
    pdf.ln(2)

    pdf.subsection("Stage 2 - Preprocessing  (preprocessing.py)")
    pdf.bullet("Resizes images to 28x28 pixels using anti-aliasing")
    pdf.bullet("Converts RGB images to grayscale with skimage.color.rgb2gray")
    pdf.bullet("Normalizes pixel values to the range [0, 1]")
    pdf.bullet("Applies intensity inversion (image_inv = 1.0 - image_norm)")
    pdf.ln(2)

    pdf.subsection("Stage 3 - Image Filtering  (filtering.py)")
    pdf.bullet("Gaussian Blur  - smooths noise using a Gaussian kernel (sigma=1)")
    pdf.bullet("Median Filter  - removes salt-and-pepper noise, disk structuring element (radius=1)")
    pdf.bullet("Sharpening     - enhances edges with a 3x3 Laplacian-based kernel via cv2.filter2D")
    pdf.ln(2)

    pdf.subsection("Stage 4 - Edge Detection & Segmentation  (edge_detection.py)")
    pdf.bullet("Sobel          - gradient magnitude in X and Y directions")
    pdf.bullet("Canny          - multi-stage edge detector (thresholds: 50 / 150)")
    pdf.bullet("Otsu Threshold - automatic binary segmentation (cv2.THRESH_OTSU)")
    pdf.ln(2)

    # -- Requirements ----------------------------------------------------------
    pdf.section_title("4. Requirements")
    pdf.body_text("Install all dependencies with:")
    pdf.code_block(["pip install scikit-image opencv-python matplotlib numpy"])
    pdf.ln(1)
    pdf.table(
        headers=["Library", "Used For"],
        rows=[
            ("scikit-image",  "I/O, resize, color conversion, Gaussian/median filtering"),
            ("opencv-python", "Sharpening, Sobel, Canny, Otsu thresholding"),
            ("matplotlib",    "Visualization of results at each stage"),
            ("numpy",         "Array operations and type conversions"),
        ],
        col_widths=[55, 135],
    )

    # -- Dataset ---------------------------------------------------------------
    pdf.section_title("5. Dataset Setup")
    pdf.body_text(
        "Place the MNIST JPG dataset in the project root directory as mnist_jpg/. "
        "Each digit (0-9) must have its own subfolder containing .jpg image files."
    )
    pdf.code_block([
        "mnist_jpg/",
        "  0/  img_1.jpg  img_2.jpg  ...",
        "  1/  img_1.jpg  ...",
        "  ...",
        "  9/  img_1.jpg  ...",
    ])

    # -- Usage -----------------------------------------------------------------
    pdf.section_title("6. Usage")
    pdf.subsection("Run the full pipeline (recommended):")
    pdf.code_block(["python3 project_pipeline.py"])
    pdf.subsection("Run each stage individually:")
    pdf.code_block([
        "python3 dataset_collection.py",
        "python3 preprocessing.py",
        "python3 filtering.py",
        "python3 edge_detection.py",
    ])
    pdf.body_text(
        "For the individual scripts (stages 2-4), update the image_path variable "
        "at the top of each file to point to a valid .jpg image in your dataset. "
        "The pipeline script selects the first image from the digit-0 folder automatically."
    )

    # -- Output ----------------------------------------------------------------
    pdf.section_title("7. Expected Output")
    pdf.table(
        headers=["Stage", "Matplotlib Figure"],
        rows=[
            ("Dataset Collection", "2x5 grid - one sample digit image per class"),
            ("Preprocessing",      "4 panels: Original / Resized / Normalized / Inverted"),
            ("Filtering",          "4 panels: Grayscale / Gaussian / Median / Sharpened"),
            ("Edge Detection",     "4 panels: Grayscale / Sobel / Canny / Otsu"),
        ],
        col_widths=[55, 135],
    )

    # -- Known Bugs Fixed ------------------------------------------------------
    pdf.section_title("8. Bug Fixes Applied")
    pdf.subsection("Division-by-zero in normalization (preprocessing.py, project_pipeline.py)")
    pdf.body_text("Original code divided by image_gray.max() without checking for zero:")
    pdf.code_block([
        "# Before (unsafe):",
        "image_norm = image_gray / image_gray.max()",
        "",
        "# After (safe):",
        "image_norm = image_gray / image_gray.max() if image_gray.max() > 0 else image_gray",
    ])

    out = "documentation.pdf"
    pdf.output(out)
    print(f"PDF saved -> {out}")


if __name__ == "__main__":
    build()
