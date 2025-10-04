from EmotionDetection.emotion_detect import emotion_detector
import unittest

class TestSentimentAnalyzer(unittest.TestCase):
    def test_emotion_detector(self):

        result_1 = emotion_detector('I am glad this happened')
        dominant_emotion = max(result_1, key=result_1.get)
        print("dominant emotion " + dominant_emotion)
        self.assertEqual(dominant_emotion, 'joy')

        result_2 = emotion_detector('I am really mad about this')
        dominant_emotion = max(result_1, key=result_2.get)
        print("dominant emotion: " + dominant_emotion)
        self.assertEqual(dominant_emotion, 'anger')

        result_3 = emotion_detector('I feel disgusted just hearing about this')
        dominant_emotion = max(result_1, key=result_3.get)
        print("dominant emotion: " + dominant_emotion)
        self.assertEqual(dominant_emotion, 'disgust')

        result_4 = emotion_detector('I am so sad about this')
        dominant_emotion = max(result_1, key=result_4.get)
        print("dominant emotion: " + dominant_emotion)
        self.assertEqual(dominant_emotion, 'sadness')

        result_5 = emotion_detector('I am really afraid that this will happen')
        dominant_emotion = max(result_1, key=result_5.get)
        print("dominant emotion: " + dominant_emotion)
        self.assertEqual(dominant_emotion, 'fear')
        
        
unittest.main()