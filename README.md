# Metadata Eraser

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[**日本語版はこちら**](https://github.com/beagleworks/metadata_eraser/blob/master/README_ja.md)

A privacy-focused web application that allows users to upload files and removes all metadata (EXIF, author information, location data, etc.) to return clean, private files.

## 🌟 Why Use Metadata Eraser?

Every file you create—whether it's a photo, a PDF, or an Office document—contains hidden information called metadata. This can include sensitive data like your location, the author's name, company details, and editing history. Sharing files without removing this metadata can lead to unintentional privacy leaks.

Metadata Eraser provides a simple and secure way to scrub this data from your files before you share them.

## ✨ Key Features

-   **Multi-format Support**: Works with images (JPEG, PNG, TIFF), PDFs, and Microsoft Office documents (Word, Excel, PowerPoint).
-   **Privacy First**: No files are stored on the server. All processing is done in memory, and files are automatically deleted after processing.
-   **Batch Processing**: Upload and process multiple files at once, and download them as a convenient ZIP archive.
-   **User Control**: See a report of what metadata was removed and choose custom filenames for your cleaned files.
-   **Secure**: Implements file size limits (50MB) and secure validation to handle files safely.

## 🚀 Getting Started

Follow these instructions to get a local copy up and running for development and testing purposes.

### Prerequisites

-   Python 3.8+

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/beagleworks/metadata_eraser.git
    cd metadata_eraser
    ```

2.  **Create a virtual environment and install dependencies:**
    ```bash
    # Create and activate a virtual environment
    python -m venv .venv
    source .venv/bin/activate

    # On Windows, use:
    # .\.venv\Scripts\activate

    # Install the required packages
    pip install -e .[dev]
    ```

### Running the Application

To run the local development server:
```bash
flask run
```
The application will be available at `http://127.0.0.1:5000`.

### Running Tests

To run the test suite and ensure everything is working as expected:
```bash
pytest
```

## 🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

Please read our [Contributing Guidelines](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
