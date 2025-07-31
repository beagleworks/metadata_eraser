import os
import shutil
import time
from threading import Timer
from flask import current_app
from werkzeug.datastructures import FileStorage
from app.utils.security import generate_session_id, secure_filename_custom

SESSION_CLEANUP_DELAY = 3600  # 1 hour in seconds

def store_temporary_file(file: FileStorage, session_id: str) -> (str, str):
    """
    Stores a temporary file in a session-specific directory.
    Returns the file_id and the full path to the stored file.
    """
    filename = secure_filename_custom(file.filename)
    upload_folder = os.path.join(current_app.config['UPLOAD_FOLDER'], session_id)

    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)

    file_path = os.path.join(upload_folder, filename)
    file.save(file_path)

    schedule_cleanup(upload_folder, SESSION_CLEANUP_DELAY)

    return filename, file_path

def cleanup_session_files(session_id: str):
    """
    Removes all files and the directory for a given session.
    """
    session_path = os.path.join(current_app.config['UPLOAD_FOLDER'], session_id)
    if os.path.exists(session_path):
        shutil.rmtree(session_path)

def schedule_cleanup(path: str, delay: int):
    """
    Schedules a directory to be cleaned up after a certain delay.
    """
    timer = Timer(delay, shutil.rmtree, [path])
    timer.start()
