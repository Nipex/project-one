import os.path

ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(ROOT, 'static', 'photos')
ALLOWED_EXTENSIONS = set(['jpg', 'jpeg'])