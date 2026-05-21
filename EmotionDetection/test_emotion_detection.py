import unittest
from emotion_detection import emotion_detector   # adjust path if needed

class TestEmotionAnalyzer(unittest.TestCase):

    def test_emotion_detector(self):
        
        # Test case 1: Joy
        result_1 = emotion_detector("I am glad this happened")
        print("\nTest 1 Result:", result_1)
        self.assertEqual(result_1['dominant_emotion'], 'joy')

        # Test case 2: Anger
        result_2 = emotion_detector("I am really mad about this")
        print("\nTest 2 Result:", result_2)
        self.assertEqual(result_2['dominant_emotion'], 'anger')

        # Test case 3: Disgust
        result_3 = emotion_detector("I feel disgusted just hearing about this")
        print("\nTest 3 Result:", result_3)
        self.assertEqual(result_3['dominant_emotion'], 'disgust')

        # Test case 4: Sadness
        result_4 = emotion_detector("I am so sad about this")
        print("\nTest 4 Result:", result_4)
        self.assertEqual(result_4['dominant_emotion'], 'sadness')

        # Test case 5: Fear
        result_5 = emotion_detector("I am really afraid that this will happen")
        print("\nTest 5 Result:", result_5)
        self.assertEqual(result_5['dominant_emotion'], 'fear')

if __name__ == "__main__":
 unittest.main()
