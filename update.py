from importlib.metadata import metadata

from flask import Blueprint, request, jsonify

# created the database name
audio_db = {
    "song": {},
    "podcast": {},
    "audiobook": {}
}

# created a module using Blueprint()
update_api = Blueprint("update_api", __name__)


def is_valid_audio_type(audio_type):
    return audio_type in audio_db.keys()



@update_api.route('/<audioFileType>/<int:audioFileID>', methods=['POST'])
def update_file(audioFileType, audioFileID):
    if request.method == "POST":

        if not is_valid_audio_type(audioFileType) or audioFileID not in audio_db[audioFileType]:
            return jsonify({"error": "Invalid request"}), 400

        meta_data = request.form.get("audioFileMetadata")  # Or use request.get_json() if sending JSON data

        if not meta_data:
            return jsonify({"error": "Invalid request"}), 400

        audio_db[audioFileType][audioFileID] = meta_data

        return jsonify({"message": "Action successful; 200 OK", "audio_id": audioFileID}), 200









