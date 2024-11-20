from importlib.metadata import metadata

from flask import Blueprint, request, jsonify

# created the database name
audio_db = {
    "song": {},
    "podcast":{},
    "audiobook":{}
}

# created a module using Blueprint()
create_api=Blueprint("create_api", __name__)

def is_valid_audio_type(audio_type):
    return audio_type in audio_db.keys()


# requestibg for audioFileType and audioFileMetadata
@create_api.route('/create', methods=['POST'])
def create_file():
    if request.method == "POST":

        data = request.get_json()

        # Extract the audio type and metadata from the request JSON
        audio_type = data.get("audioFileType")
        meta_data = data.get("audioFileMetadata")

        # Check if audio_type and meta_data are provided and valid
        if not audio_type or not meta_data or not is_valid_audio_type(audio_type):
            return jsonify({"error": "Invalid request"}), 400

        audio_id = len(audio_db[audio_type]) + 1
        audio_db[audio_type][audio_id] = meta_data

        return jsonify({"message": "Action successful; 200 OK", "audio_id": audio_id}), 200









