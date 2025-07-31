import os
from flask import Flask

def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True, template_folder='templates')

    # Load default configuration
    app.config.from_mapping(
        SECRET_KEY=os.urandom(24),
        UPLOAD_FOLDER=os.path.join(app.instance_path, 'uploads'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.update(test_config)

    # ensure the instance folder and upload folder exists
    try:
        os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    except OSError:
        pass

    # Register blueprints
    from app.routes import upload, download
    app.register_blueprint(upload.bp)
    app.register_blueprint(download.bp, url_prefix='/download')

    return app
