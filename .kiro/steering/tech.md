# Technology Stack

## Backend Framework
- **Python Flask**: Web framework for the application server
- **Python Environment**: Standard venv for virtual environment management
- **Package Management**: pip for dependency installation and management

## Core Dependencies
- **File Processing Libraries**:
  - `Pillow (PIL)`: Image processing and EXIF removal
  - `PyMuPDF (fitz)`: PDF metadata manipulation
  - `python-docx`: Word document processing
  - `openpyxl`: Excel file processing
  - `python-pptx`: PowerPoint file processing
- **Security**: Werkzeug for secure filename handling and file validation

## Frontend
- **Vanilla JavaScript**: No framework dependencies for simplicity
- **HTML5 & CSS3**: Modern web standards
- **File API**: Drag & drop upload functionality

## Development Environment

### Setup Commands
```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment (Linux/Mac)
source .venv/bin/activate

# Activate virtual environment (Windows)
.venv\Scripts\activate

# Install dependencies
pip install -e .[dev]

# Run development server
flask run

# Run tests
pytest
```

### Configuration Files
- `requirements.txt`: Python dependencies specification
- `setup.py` or `pyproject.toml`: Optional project configuration
- `.env`: Environment variables configuration

## Architecture Principles
- **Stateless Processing**: No persistent file storage
- **Session-based Cleanup**: Automatic temporary file removal
- **Security First**: File validation, size limits, timeout protection
- **Modular Design**: Separate processors for each file type