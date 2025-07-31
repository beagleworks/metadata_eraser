import os
import fitz  # PyMuPDF
from app.processors.base import BaseProcessor
from app.models.responses import ProcessResult, MetadataInfo

class PdfProcessor(BaseProcessor):
    """Processor for PDF files."""

    def remove_metadata(self, file_path: str) -> ProcessResult:
        try:
            doc = fitz.open(file_path)

            if doc.is_encrypted:
                raise Exception("Encrypted PDFs are not supported.")

            metadata = doc.metadata
            removed_keys = list(metadata.keys())

            # Clear all metadata fields
            new_metadata = {key: None for key in metadata}
            doc.set_metadata(new_metadata)

            processed_file_path = file_path.replace(os.path.basename(file_path), "processed_" + os.path.basename(file_path))
            doc.save(processed_file_path, garbage=4, deflate=True, clean=True)
            doc.close()

            original_size = os.path.getsize(file_path)
            processed_size = os.path.getsize(processed_file_path)

            return ProcessResult(
                success=True,
                original_file_path=file_path,
                processed_file_path=processed_file_path,
                metadata_removed=removed_keys,
                original_size=original_size,
                processed_size=processed_size
            )
        except Exception as e:
            return ProcessResult(
                success=False,
                original_file_path=file_path,
                processed_file_path=None,
                metadata_removed=[],
                original_size=os.path.getsize(file_path),
                processed_size=0,
                error_message=str(e)
            )

    def get_metadata_info(self, file_path: str) -> MetadataInfo:
        # Implementation for metadata info extraction
        pass

    def validate_file(self, file_path: str) -> bool:
        # Implementation for file validation
        pass
