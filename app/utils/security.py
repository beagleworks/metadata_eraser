import uuid
from werkzeug.utils import secure_filename

def generate_session_id():
    """Generates a unique session ID."""
    return str(uuid.uuid4())

def secure_filename_custom(filename):
    """
    Generates a secure filename, ensuring it's not empty and handles edge cases.
    """
    if not filename:
        return None

    # Use Werkzeug's secure_filename as a base
    s_filename = secure_filename(filename)

    # If secure_filename returns an empty string (e.g., for '..'), generate a random one
    if not s_filename:
        s_filename = str(uuid.uuid4())

    return s_filename
