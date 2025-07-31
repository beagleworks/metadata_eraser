import os
from PIL import Image
from app.processors.base import BaseProcessor
from app.models.responses import ProcessResult, MetadataInfo

class ImageProcessor(BaseProcessor):
    """Processor for image files (JPEG, PNG, TIFF)."""

    def remove_metadata(self, file_path: str) -> ProcessResult:
        try:
            img = Image.open(file_path)

            # Remove EXIF data
            data = list(img.getdata())
            img_without_exif = Image.new(img.mode, img.size)
            img_without_exif.putdata(data)

            # Preserve color profile if it exists
            if 'icc_profile' in img.info:
                img_without_exif.info['icc_profile'] = img.info['icc_profile']

            processed_file_path = file_path.replace(os.path.basename(file_path), "processed_" + os.path.basename(file_path))
            img_without_exif.save(processed_file_path, format=img.format)

            original_size = os.path.getsize(file_path)
            processed_size = os.path.getsize(processed_file_path)

            return ProcessResult(
                success=True,
                original_file_path=file_path,
                processed_file_path=processed_file_path,
                metadata_removed=["EXIF"],
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
