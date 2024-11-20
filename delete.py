from importlib.metadata import metadata

from flask import Blueprint, request, jsonify

# created the database name
audio_db = {
    "song": {},
    "podcast":{},
    "audiobook":{}
}

# created a module using Blueprint()
delete_api=Blueprint("delete_api", __name__)

def is_valid_audio_type(audio_type):
    return audio_type in audio_db.keys()


# requestibg for audioFileType and audioFileMetadata
@delete_api.route('/<audioFileType>/<int:audioFileID>', methods=['DELETE'])
def delete_file(audioFileType,audioFileID):
    if request.method == "DELETE":

        if not is_valid_audio_type(audioFileType) or audioFileID not in audio_db[audioFileType]:
            return jsonify({"error": "Invalid request"}), 400

        del audio_db[audioFileType][audioFileID]

        return jsonify({"message": "Action successful; 200 OK", "audio_id": audioFileID}), 200










