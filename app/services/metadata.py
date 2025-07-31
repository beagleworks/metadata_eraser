from app.processors.base import BaseProcessor
from app.processors.image import ImageProcessor
from app.processors.pdf import PdfProcessor
from app.processors.office import OfficeProcessor
from app.utils.validation import get_file_type
from app.models.responses import ProcessResult

def get_processor(mime_type: str) -> BaseProcessor:
    """
    Returns the appropriate processor based on the file's MIME type.
    """
    if mime_type.startswith('image/'):
        return ImageProcessor()
    elif mime_type == 'application/pdf':
        return PdfProcessor()
    elif 'openxmlformats-officedocument' in mime_type:
        return OfficeProcessor()
    else:
        raise ValueError(f"Unsupported file type: {mime_type}")

def process_file(file_path: str, mime_type: str) -> ProcessResult:
    """
    Selects the correct processor and removes metadata from the file.
    """
    try:
        processor = get_processor(mime_type)
        return processor.remove_metadata(file_path)
    except ValueError as e:
        return ProcessResult(
            success=False,
            original_file_path=file_path,
            processed_file_path=None,
            metadata_removed=[],
            original_size=0,
            processed_size=0,
            error_message=str(e)
        )
