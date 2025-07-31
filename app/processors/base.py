from abc import ABC, abstractmethod
from app.models.responses import ProcessResult, MetadataInfo

class BaseProcessor(ABC):
    """
    Abstract base class for file processors.
    Defines the common interface for all file-specific processors.
    """

    @abstractmethod
    def remove_metadata(self, file_path: str) -> ProcessResult:
        """
        Removes metadata from a file and returns the processing result.
        """
        pass

    @abstractmethod
    def get_metadata_info(self, file_path: str) -> MetadataInfo:
        """
        Extracts and returns metadata information from a file.
        """
        pass

    @abstractmethod
    def validate_file(self, file_path: str) -> bool:
        """
        Validates if the file is suitable for processing by this processor.
        """
        pass
