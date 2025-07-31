import pytest
from unittest.mock import Mock
from app.utils.validation import allowed_file, get_file_type, is_allowed_mime_type

def test_allowed_file():
    assert allowed_file('test.jpg') == True
    assert allowed_file('test.PDF') == True
    assert allowed_file('test.txt') == False
    assert allowed_file('test') == False

def test_get_file_type_from_filestorage():
    mock_file = Mock()
    mock_file.read.return_value = b'%PDF-1.5'
    assert get_file_type(mock_file) == 'application/pdf'
    mock_file.read.assert_called_once_with(2048)
    mock_file.seek.assert_called_once_with(0)

def test_is_allowed_mime_type():
    mock_file = Mock()
    mock_file.read.return_value = b'\xff\xd8\xff\xe0' # JPEG magic numbers
    assert is_allowed_mime_type(mock_file) == True

    mock_file.read.return_value = b'PK\x03\x04' # Not a valid magic number for our allowed types
    assert is_allowed_mime_type(mock_file) == False
