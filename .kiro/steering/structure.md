# Project Structure

## Directory Organization

```
/
├── requirements.txt        # Python dependencies (to be created)
├── pyproject.toml          # Current project configuration
├── uv.lock                 # Current lock file (to be removed)
├── README.md               # Project documentation
├── .gitignore              # Git ignore rules
├── .venv/                  # Virtual environment (created by venv)
├── app/                    # Main application package
│   ├── __init__.py         # Flask app factory
│   ├── routes/             # Route handlers
│   │   ├── __init__.py
│   │   ├── upload.py       # File upload endpoints
│   │   └── download.py     # File download endpoints
│   ├── processors/         # File processing modules
│   │   ├── __init__.py
│   │   ├── base.py         # BaseProcessor abstract class
│   │   ├── image.py        # ImageProcessor for EXIF removal
│   │   ├── pdf.py          # PDFProcessor for PDF metadata
│   │   └── office.py       # OfficeProcessor for Office docs
│   ├── services/           # Business logic services
│   │   ├── __init__.py
│   │   ├── file_storage.py # Temporary file management
│   │   ├── metadata.py     # Metadata processing coordination
│   │   └── download.py     # Download preparation service
│   ├── models/             # Data models and DTOs
│   │   ├── __init__.py
│   │   └── responses.py    # Response data classes
│   ├── utils/              # Utility functions
│   │   ├── __init__.py
│   │   ├── validation.py   # File validation utilities
│   │   └── security.py     # Security helpers
│   ├── static/             # Static web assets
│   │   ├── css/
│   │   │   └── style.css   # Main stylesheet
│   │   └── js/
│   │       └── main.js     # Main JavaScript file
│   └── templates/          # Jinja2 HTML templates
│       ├── base.html       # Base template
│       └── upload.html     # Upload page template
├── tests/                  # Test suite
│   ├── __init__.py
│   ├── unit/               # Unit tests
│   │   └── test_validation.py
│   └── integration/        # Integration tests
│       └── test_app.py
└── temp/                   # Temporary file storage (auto-created)
```

## Code Organization Principles

### Modular Architecture

- **Separation of Concerns**: Routes, business logic, and data processing are
  separated
- **Processor Pattern**: Each file type has its own dedicated processor class
- **Service Layer**: Business logic abstracted into reusable services

### File Processing Flow

1. **Upload** → `routes/upload.py` → `services/file_storage.py`
2. **Process** → `services/metadata.py` → `processors/{type}.py`
3. **Download** → `routes/download.py` → `services/download.py`

### Naming Conventions

- **Classes**: PascalCase (e.g., `ImageProcessor`, `FileStorageService`)
- **Functions/Methods**: snake_case (e.g., `remove_metadata`, `validate_file`)
- **Files/Modules**: snake_case (e.g., `file_storage.py`, `metadata.py`)
- **Constants**: UPPER_SNAKE_CASE (e.g., `MAX_FILE_SIZE`, `SUPPORTED_FORMATS`)

### Import Organization

- Standard library imports first
- Third-party imports second
- Local application imports last
- Use absolute imports within the app package
