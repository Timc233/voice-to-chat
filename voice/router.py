import os
from voice.services import DeepSpeechService

from flask import Blueprint, request

voice = Blueprint('voice', __name__)


@voice.route("/speechtotext", methods=['POST'])
def speechtotext():
    file_name = request.files['file'].filename
    save_path = os.path.join('test', file_name)
    request.files['file'].save(save_path)
    dss = DeepSpeechService()
    buffer = dss.wave_to_brate(save_path)
    text = dss.inference(buffer)

    return text
