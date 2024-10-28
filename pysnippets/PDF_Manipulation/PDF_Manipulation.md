# Python PDF Manipulation Guide

This module provides a comprehensive guide for working with PDF files using `pypdf` and `ReportLab`. It covers essential PDF manipulation techniques, including reading, splitting, merging, securing, and creating PDFs.

## Table of Contents
- [Installation](#installation)
- [1. Reading PDF Files](#1-reading-pdf-files)
- [2. Splitting PDFs](#2-splitting-pdfs)
- [3. Merging PDFs](#3-merging-pdfs)
- [4. Page Manipulation](#4-page-manipulation)
- [5. PDF Security](#5-pdf-security)
- [6. Creating PDFs with ReportLab](#6-creating-pdfs-with-reportlab)

---

## Installation

```bash
pip install pypdf
pip install reportlab
```

## 1. Reading PDF Files

Reading PDFs is fundamental to PDF processing, whether for extracting text, retrieving metadata, or analyzing page structure.

### 1.1 Basic PDF Reading
This function demonstrates how to read and extract text from each page in a PDF file.

```python
from pypdf import PdfReader

def read_pdf(file_path):
    reader = PdfReader(file_path)
    num_pages = len(reader.pages)
    print(f"Total pages: {num_pages}")
    
    for page_num in range(num_pages):
        page = reader.pages[page_num]
        text = page.extract_text()
        print(f"\nPage {page_num + 1}:")
        print(text)

read_pdf("sample.pdf")
```

### 1.2 Reading PDF Metadata
Metadata includes details about the document, such as the author and title. This function retrieves and displays the metadata from a PDF file.

```python
from pypdf import PdfReader

def read_pdf_metadata(file_path):
    reader = PdfReader(file_path)
    metadata = reader.metadata
    
    print("PDF Metadata:")
    print(f"Author: {metadata.author}")
    print(f"Creator: {metadata.creator}")
    print(f"Producer: {metadata.producer}")
    print(f"Subject: {metadata.subject}")
    print(f"Title: {metadata.title}")

read_pdf_metadata("sample.pdf")
```

---

## 2. Splitting PDFs

Splitting PDFs is useful when you want to break down a large document into smaller parts, either by page or in custom-defined chunks.

### 2.1 Split PDF into Individual Pages
This function creates a separate PDF for each page in the original document.

```python
from pypdf import PdfReader, PdfWriter

def split_pdf(input_path, output_directory):
    reader = PdfReader(input_path)
    
    for page_num in range(len(reader.pages)):
        writer = PdfWriter()
        writer.add_page(reader.pages[page_num])
        output_path = f"{output_directory}/page_{page_num + 1}.pdf"
        with open(output_path, "wb") as output_file:
            writer.write(output_file)
        print(f"Created: {output_path}")

split_pdf("input.pdf", "output_directory")
```

### 2.2 Split PDF into Chunks
Instead of individual pages, this function splits the PDF into chunks with a specified number of pages.

```python
from pypdf import PdfReader, PdfWriter

def split_pdf_chunks(input_path, pages_per_chunk):
    reader = PdfReader(input_path)
    total_pages = len(reader.pages)
    
    for chunk_start in range(0, total_pages, pages_per_chunk):
        writer = PdfWriter()
        chunk_end = min(chunk_start + pages_per_chunk, total_pages)
        
        for page_num in range(chunk_start, chunk_end):
            writer.add_page(reader.pages[page_num])
        
        output_path = f"chunk_{chunk_start//pages_per_chunk + 1}.pdf"
        with open(output_path, "wb") as output_file:
            writer.write(output_file)
            
        print(f"Created chunk {chunk_start//pages_per_chunk + 1} with pages {chunk_start + 1}-{chunk_end}")

split_pdf_chunks("input.pdf", 5)
```

---

## 3. Merging PDFs

Merging allows combining multiple PDFs into a single document.

### 3.1 Basic PDF Merger
This function takes a list of PDF files and merges them into one PDF.

```python
from pypdf import PdfMerger

def merge_pdfs(pdf_files, output_path):
    merger = PdfMerger()
    
    for pdf in pdf_files:
        merger.append(pdf)
    
    with open(output_path, "wb") as output_file:
        merger.write(output_file)
    
    print(f"Created merged PDF: {output_path}")

pdf_files = ["file1.pdf", "file2.pdf", "file3.pdf"]
merge_pdfs(pdf_files, "merged.pdf")
```

### 3.2 Advanced PDF Merger with Page Selection
This version allows specifying which pages from each PDF to include in the merge.

```python
from pypdf import PdfMerger

def merge_pdfs_with_pages(pdf_config, output_path):
    merger = PdfMerger()
    
    for pdf_path, pages in pdf_config:
        if pages:
            merger.append(pdf_path, pages=pages)
        else:
            merger.append(pdf_path)
    
    with open(output_path, "wb") as output_file:
        merger.write(output_file)

pdf_config = [
    ("file1.pdf", [0, 2]),  
    ("file2.pdf", None),    
    ("file3.pdf", [1])      
]
merge_pdfs_with_pages(pdf_config, "merged_custom.pdf")
```

---

## 4. Page Manipulation

Page manipulation covers operations like rotating and cropping pages, which can be useful for reformatting documents.

### 4.1 Rotating Pages
This function rotates each page by a specified degree.

```python
from pypdf import PdfReader, PdfWriter

def rotate_pdf_pages(input_path, output_path, rotation):
    reader = PdfReader(input_path)
    writer = PdfWriter()
    
    for page in reader.pages:
        page.rotate(rotation)
        writer.add_page(page)
    
    with open(output_path, "wb") as output_file:
        writer.write(output_file)

rotate_pdf_pages("input.pdf", "rotated.pdf", 90)
```

### 4.2 Cropping Pages
This function crops each page according to the specified crop box dimensions.

```python
from pypdf import PdfReader, PdfWriter

def crop_pdf_pages(input_path, output_path, crop_box):
    reader = PdfReader(input_path)
    writer = PdfWriter()
    
    for page in reader.pages:
        page.cropbox.left = crop_box[0]
        page.cropbox.bottom = crop_box[1]
        page.cropbox.right = crop_box[2]
        page.cropbox.top = crop_box[3]
        writer.add_page(page)
    
    with open(output_path, "wb") as output_file:
        writer.write(output_file)

crop_box = (50, 50, 550, 750)
crop_pdf_pages("input.pdf", "cropped.pdf", crop_box)
```

---

## 5. PDF Security

Securing PDFs helps protect the document's content from unauthorized access or modifications.

### 5.1 Encrypting PDF
This function adds password protection to a PDF file.

```python
from pypdf import PdfReader, PdfWriter

def encrypt_pdf(input_path, output_path, user_password, owner_password):
    reader = PdfReader(input_path)
    writer = PdfWriter()
    
    for page in reader.pages:
        writer.add_page(page)
    
    writer.encrypt(user_password=user_password, 
                  owner_password=owner_password,
                  use_128bit=True)
    
    with open(output_path, "wb") as output_file:
        writer.write(output_file)

encrypt_pdf("input.pdf", "encrypted.pdf", "user123", "owner456")
```

### 5.2 Decrypting PDF
Decrypts a PDF file that was previously encrypted.

```python
from pypdf import PdfReader, PdfWriter

def decrypt_pdf(input_path, output_path, password):
    reader = PdfReader(input_path)
    
    if reader.is_encrypted:
        reader.decrypt(password)
    
    writer = PdfWriter()
    
    for page in reader.pages:
        writer.add_page(page)
    
    with open(output_path, "wb") as output_file:
        writer.write(output_file)

decrypt_pdf("encrypted.pdf", "decrypted.pdf", "user123")
```

---

## 6. Creating PDFs with ReportLab

ReportLab is a versatile library that allows you to create custom PDFs from scratch.

### 6.1 Creating a Simple PDF
Creates a basic PDF with text and shapes using ReportLab.

```python
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def create_simple_pdf(output_path):
    c = canvas.Canvas(output_path, pagesize=letter)
    c.setFont("Helvetica", 16)
    c.drawString(100, 750, "Sample PDF Created with ReportLab")
    
    c.setFont("Helvetica", 12)
    c.drawString(100, 700, "This is a simple PDF created using ReportLab.")
    
    c.rect(100, 600, 400, 50, stroke=1, fill=0)
    c.circle(300, 500, 50, stroke=1, fill=0)
    c.save()

create_simple_pdf("reportlab_sample.pdf")
```

### 6.2 Creating a PDF with Tables
Demonstrates creating a PDF with a table, including cell styling.

```python
from reportlab.platypus import SimpleDocTemplate

, Table, TableStyle
from reportlab.lib import colors

def create_pdf_with_table(output_path):
    doc = SimpleDocTemplate(output_path, pagesize=letter)
    data = [
        ["Header 1", "Header 2", "Header 3"],
        ["Row 1, Col 1", "Row 1, Col 2", "Row 1, Col 3"],
        ["Row 2, Col 1", "Row 2, Col 2", "Row 2, Col 3"]
    ]
    
    table = Table(data)
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
        ("BACKGROUND", (0, 1), (-1, -1), colors.beige)
    ]))
    
    elements = [table]
    doc.build(elements)

create_pdf_with_table("table_sample.pdf")
```

--- 

By following this guide, you'll be equipped with a comprehensive understanding of PDF manipulation in Python using `pypdf` and `ReportLab`.