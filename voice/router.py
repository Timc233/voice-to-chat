import os
from voice.services import deep_speech_wrapper
from flask import Blueprint, request
from rq import Queue
import redis


voice = Blueprint('voice', __name__)

r = redis.Redis()
q = Queue(connection=r)


@voice.route("/speechtotext", methods=['POST'])
def speechtotext():
    file_name = request.files['file'].filename
    save_path = os.path.join('test', file_name)
    request.files['file'].save(save_path)
    job = q.enqueue(deep_speech_wrapper, save_path)
    return f"Task ({job.id}) added to queue at {job.enqueued_at}"
