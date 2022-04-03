from deepspeech import Model
import wave
import numpy as np


class DeepSpeechService:
    def __init__(self):
        self.model_file_path = 'voice-models/deepspeech-0.9.3-models.pbmm'
        self.scorer_path = 'voice-models/deepspeech-0.9.3-models.scorer'

    def load_model(self):
        ds = Model(self.model_file_path)
        ds.enableExternalScorer(self.scorer_path)
        return ds

    def wave_to_brate(self, audio: str):
        w = wave.open(audio, 'r')
        frames = w.getnframes()
        buffer = w.readframes(frames)
        data16 = np.frombuffer(buffer, dtype=np.int16)
        return data16

    def inference(self, audio):
        ds = self.load_model()
        output = ds.stt(audio)
        return output
