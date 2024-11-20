from importlib.metadata import metadata

from flask import Blueprint, request, jsonify

# created the database name
audio_db = {
    "song": {},
    "podcast": {},
    "audiobook": {}
}

# created a module using Blueprint()
get_api = Blueprint("get_api", __name__)


def is_valid_audio_type(audio_type):
    return audio_type in audio_db.keys()


@get_api.route('/<audioFileType>/<int:audioFileID>', methods=['GET'])
def get_file(audioFileType, audioFileID):
    if request.method == "POST":

        if not is_valid_audio_type(audioFileType) or audioFileID not in audio_db[audioFileType]:
            return jsonify({"error": "Invalid request"}), 400

        meta_data = request.form.get("audioFileMetadata")  # Or use request.get_json() if sending JSON data

        if not meta_data:
            return jsonify({"error": "Invalid request"}), 400

        audio_db[audioFileType][audioFileID] = meta_data

        return jsonify({"message": "Action successful; 200 OK", "audio_id": audioFileID}), 200

    @get_api.route('/<audioFileType>', methods=['GET'])
    def get_file_type(audioFileType):
        if request.method == "POST":

            if not is_valid_audio_type(audioFileType):
                return jsonify({"error": "Invalid request"}), 400


            return jsonify({"message": "Action successful; 200 OK", "audio_id": audioFileID}), 200









