from flask import Blueprint, session, jsonify
from app.services import download as download_service

bp = Blueprint('download', __name__)

@bp.route('/file/<filename>')
def download_file(filename):
    processed_files = session.get('processed_files', [])
    file_to_download = next((f for f in processed_files if f['original_name'] == filename), None)

    if not file_to_download:
        return jsonify({'error': 'File not found or not processed'}), 404

    try:
        return download_service.prepare_download(file_to_download['processed_path'], custom_name=filename)
    except FileNotFoundError as e:
        return jsonify({'error': str(e)}), 404

@bp.route('/zip')
def download_zip():
    processed_files = session.get('processed_files', [])
    if not processed_files:
        return jsonify({'error': 'No processed files to zip'}), 400

    file_paths = [f['processed_path'] for f in processed_files]
    session_id = session.get('session_id')

    try:
        zip_path = download_service.create_zip_archive(file_paths, session_id)
        return download_service.prepare_download(zip_path, "processed_files.zip")
    except Exception as e:
        return jsonify({'error': str(e)}), 500
