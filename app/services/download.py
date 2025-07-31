import os
import zipfile
from flask import send_file, current_app

def prepare_download(file_path: str, custom_name: str = None):
    """
    Prepares a file for download, optionally with a custom name.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError("Processed file not found.")

    download_name = custom_name or os.path.basename(file_path)
    return send_file(file_path, as_attachment=True, download_name=download_name)

def create_zip_archive(file_paths: list[str], session_id: str) -> str:
    """
    Creates a ZIP archive from a list of file paths.
    Returns the path to the created ZIP file.
    """
    zip_folder = os.path.join(current_app.config['UPLOAD_FOLDER'], session_id)
    zip_path = os.path.join(zip_folder, "processed_files.zip")

    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for file_path in file_paths:
            if os.path.exists(file_path):
                zipf.write(file_path, os.path.basename(file_path))

    return zip_path
