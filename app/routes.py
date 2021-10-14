from flask import Blueprint

hello_world_bp = Blueprint("hello_word", __name__)

@hello_world_bp.route('/hello-world', methods=["GET"])
def get_hello_world():
    my_response = "Hello, World!"
    return my_response

@hello_world_bp.route('/hello-world/JSON', methods=["GET"])
def hello_world_json():
    return {
        "name": "Starseed",
        "message": "Wassup",
        "hobbies": ["Coding", "Music", "Art", "Reading", "Food Anthropology"]

    }, 200






