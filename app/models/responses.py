from dataclasses import dataclass, field
from typing import List, Optional, Any, Dict
from datetime import datetime

@dataclass
class ProcessResult:
    success: bool
    original_file_path: str
    processed_file_path: str
    metadata_removed: List[str]
    original_size: int
    processed_size: int
    error_message: Optional[str] = None

@dataclass
class MetadataInfo:
    file_type: str
    detected_metadata: Dict[str, Any]
    metadata_count: int
    has_sensitive_data: bool

@dataclass
class FileInfo:
    original_name: str
    file_id: str
    file_type: str
    size: int
    status: str  # 'uploaded', 'processing', 'completed', 'error'

@dataclass
class UploadResponse:
    session_id: str
    uploaded_files: List[FileInfo]
    total_files: int
    success: bool
    errors: List[str] = field(default_factory=list)

@dataclass
class ErrorResponse:
    error_code: str
    error_message: str
    user_message: str
    suggested_action: str
    timestamp: datetime = field(default_factory=datetime.utcnow)
