import magic

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'tiff', 'pdf', 'docx', 'xlsx', 'pptx'}
ALLOWED_MIME_TYPES = {
    'image/jpeg',
    'image/png',
    'image/tiff',
    'application/pdf',
    'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
    'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    'application/vnd.openxmlformats-officedocument.presentationml.presentation'
}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_file_type(file_obj):
    """
    Get the MIME type of a file from a FileStorage object or a file path.
    """
    try:
        if hasattr(file_obj, 'read') and hasattr(file_obj, 'seek'):
            # It's a FileStorage-like object
            mime_type = magic.from_buffer(file_obj.read(2048), mime=True)
            file_obj.seek(0)
            return mime_type
        elif isinstance(file_obj, str):
            # It's a file path
            return magic.from_file(file_obj, mime=True)
    except Exception:
        return None

def is_allowed_mime_type(file_obj):
    mime_type = get_file_type(file_obj)
    return mime_type in ALLOWED_MIME_TYPES
