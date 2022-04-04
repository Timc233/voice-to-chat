import unittest
from voice.services import deep_speech_wrapper


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

    def test_speech_to_text_service(self):
        test_file_path = 'test/output.wav'
        res = deep_speech_wrapper(test_file_path)
        self.assertIsInstance(res, str)


if __name__ == '__main__':
    unittest.main()
