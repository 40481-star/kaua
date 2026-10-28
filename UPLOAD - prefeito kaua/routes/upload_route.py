from flask import Blueprint
from controllers.upload_controller import UploadsController

upload_bp = Blueprint('upload_bp', _name_)

@upload_bp.route('/upload', methods=['POST'])
def upload_file():
    return UploadsController.upload_file()