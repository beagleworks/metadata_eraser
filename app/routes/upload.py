import os
from flask import Blueprint, request, jsonify, session, render_template
from werkzeug.utils import secure_filename
from app.services import file_storage, metadata
from app.utils.validation import is_allowed_mime_type

bp = Blueprint('upload', __name__) # Removed url_prefix to use root

@bp.route('/', methods=['GET'])
def index():
    return render_template('upload.html')

@bp.route('/upload', methods=['POST'])
def upload_files():
    if 'files[]' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    files = request.files.getlist('files[]')
    processed_files = []
    errors = []

    if 'session_id' not in session:
        session['session_id'] = os.urandom(24).hex()

    for file in files:
        if file.filename == '':
            errors.append({'filename': 'unknown', 'error': 'No selected file'})
            continue

        if not is_allowed_mime_type(file.stream):
            errors.append({'filename': file.filename, 'error': 'File type not allowed'})
            continue

        try:
            stored_filename, stored_path = file_storage.store_temporary_file(file, session['session_id'])

            result = metadata.process_file(stored_path, file.mimetype)

            if result.success:
                processed_info = {
                    'original_name': file.filename,
                    'processed_path': result.processed_file_path,
                    'report': {
                        'metadata_removed': result.metadata_removed,
                    }
                }
                processed_files.append(processed_info)
            else:
                errors.append({'filename': file.filename, 'error': result.error_message})
        except Exception as e:
            errors.append({'filename': file.filename, 'error': str(e)})

    session['processed_files'] = processed_files
    return jsonify({
        'processed_files': processed_files,
        'errors': errors
    })
