# Metadata Eraser

A privacy-focused web application that allows users to upload files and removes all metadata (EXIF, author information, location data, etc.) to return clean files.

## Features

- **Multi-format Support**: Images (JPEG, PNG, TIFF), PDFs, Office documents (Word, Excel, PowerPoint)
- **Batch Processing**: Handle multiple files simultaneously with ZIP archive download
- **Privacy First**: Automatic file cleanup, no server-side storage, session-based temporary handling
- **User Control**: Custom filename options, processing reports showing removed metadata
- **Security**: File size limits (50MB), timeout protection, secure file validation

## Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd metadata-eraser
    ```

2.  **Create a virtual environment and install dependencies:**
    This project uses `uv` for package management.
    ```bash
    python -m venv .venv
    source .venv/bin/activate
    pip install -e .[dev]
    ```

## Running the Application

To run the development server:
```bash
flask run
```
The application will be available at `http://127.0.0.1:5000`.

## Running Tests

To run the test suite:
```bash
pytest
```
