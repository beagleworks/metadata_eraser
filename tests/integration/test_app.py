import pytest
from app import create_app
from unittest.mock import patch, Mock
import io

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_upload_and_process_file(client):
    with patch('app.routes.upload.is_allowed_mime_type', return_value=True):
        with patch('app.services.file_storage.store_temporary_file') as mock_store:
            with patch('app.services.metadata.process_file') as mock_process:

                mock_store.return_value = ('test.jpg', '/tmp/test.jpg')
                mock_process.return_value = Mock(
                    success=True,
                    processed_file_path='/tmp/processed_test.jpg',
                    metadata_removed=['EXIF'],
                    original_size=1000,
                    processed_size=800
                )

                data = {
                    'files[]': (io.BytesIO(b"fake image data"), 'test.jpg')
                }

                response = client.post('/upload', data=data, content_type='multipart/form-data')

                assert response.status_code == 200
                json_data = response.get_json()
                assert len(json_data['processed_files']) == 1
                assert json_data['processed_files'][0]['original_name'] == 'test.jpg'

def test_download_file(client):
    with client.session_transaction() as sess:
        sess['processed_files'] = [{'original_name': 'test.jpg', 'processed_path': '/tmp/processed_test.jpg'}]

    with patch('os.path.exists') as mock_exists:
        mock_exists.return_value = True
        with patch('app.services.download.send_file') as mock_send:
            mock_send.return_value = "file content"
            response = client.get('/download/file/test.jpg')
            assert response.status_code == 200
            mock_send.assert_called_with('/tmp/processed_test.jpg', as_attachment=True, download_name='test.jpg')
