import unittest
from sentiment_analysis import sentiment_analyzer, parse_sentiment_analyzer
from termcolor import colored

class TestEmotionDetection(unittest.TestCase):

    def check_emotion(self, text, expected_emotion=None):
        full_response = sentiment_analyzer(text)
        emotions, reasoning = parse_sentiment_analyzer(full_response)

        print()
        print(colored("TestText:", 'blue'))
        print(colored(text, 'blue'))
        print(colored("Server response:", 'light_red'))
        print(colored(full_response, 'magenta'))
        print(colored("Reasoning:", 'green'))
        print(colored(reasoning, 'green'))

        if emotions:
            if expected_emotion:
                self.assertEqual(dict(emotions)['dominant_emotion'].lower(), expected_emotion.lower())
                if not reasoning == None or reasoning == "```" or reasoning == "'":
                    None
                else:
                    self.assertIn(expected_emotion.lower(), reasoning.lower())                 
                print(colored("Expected Emotion:", 'cyan'))
                print(colored(expected_emotion, 'cyan'))
                print(colored("Detected Emotion:", 'yellow'))
                print(colored(emotions, 'yellow'))
            else:
                print(colored("Detected Emotion:", 'yellow'))
                print(colored(emotions, 'yellow'))
        else:
            self.fail(colored("Failed to get a valid response from the emotion analysis service", 'red'))
        
        # print OK using figlet and lolcat
        print("PASS")

    def test_happy_sentence(self):
        self.check_emotion("I am so happy I am doing this", "joy")

    def test_sad_sentence(self):
        self.check_emotion("I am very sad and depressed", "sadness")

    def test_fearful_sentence(self):
        self.check_emotion("I am scared and fearful", "fear")
    
    def test_angry_sentence(self):
        self.check_emotion("I am so angry and frustrated", "anger")

    def test_desgusted_sentence(self):
        self.check_emotion("I feel disgusted by this", "disgust")

if __name__ == "__main__":
    unittest.main(testRunner=unittest.TextTestRunner(verbosity=2))

