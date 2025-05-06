import requests, json
def sentiment_analyzer(text_to_analyze):
        url = "http://127.0.0.1:11434/api/generate"
        headers = {"Content-Type": "application/json"}
        prompt  =  f"""Analyze the emotion of the following text and return a JSON object with the following structure:
        {{
            "anger": "<probability>",
            "disgust": "<probability>",
            "fear": "<probability>",
            "joy": "<probability>",
            "sadness": "<probability>",
            "dominant_emotion": "<emotion with highest probability>",
        }},
        
        Text to analyze: "{text_to_analyze}"
        """
        data = {
            "model": "llama3.2",
            "prompt": prompt,
            "stream": False
        }
        try:
            response = requests.post(url, headers=headers, json=data, timeout=240)
            response.raise_for_status()
            full_response = response.json()
            return full_response.get("response", ""), 
        except Exception as e:
            print (f"an error occured {str(e)}")
            return None

def parse_sentiment_analyzer(full_res):
    full_response = str(full_res)
    if not full_res:
        return None, None
    
    start_index = full_response.find("{")
    end_index = full_response.rfind("}")
    json_result = str(full_response[start_index:end_index]).strip()
    emotion_lines = [line.strip("\\n") for line in json_result.split()]
    Emotions = " ".join(emotion_lines)
    emotions = Emotions + "}"
    
    try:
        result = json.loads(emotions)
        if dict(result)['dominant_emotion'].lower() == "neutral" or not dict(result)['dominant_emotion']:
            Result = None
            print(f"emotion = {dict(result)['dominant_emotion']}")
        else:
            Result = result
    except json.JSONDecodeError:
        Result = None
    
    if Result:
        reasoning_part = full_response[end_index+1:].strip()
        Reasoning_lines = [line.strip("\\n\\n").strip("*") for line in reasoning_part.split("\\n\\n") if line.strip("\\n\\n").strip("*")]
        Reasoning = " ".join(Reasoning_lines)
        reason = Reasoning.strip("',)")
        reasoning_Part = reason.strip("```")
        reasoning_lines = [line.strip("\\n").strip("*") for line in reasoning_Part.split("\\n") if line.strip("\\n").strip("*")]
        reaSoning = " ".join(reasoning_lines)
        reasoning_Lines = [line.strip("\\") for line in reaSoning.split("\'") if line.strip("\\")]
        reasoning = "'".join(reasoning_Lines)
    else:
        reasoning = None

    return Result, reasoning

def test(text): 
    response = sentiment_analyzer(text)
    emotions, reasoning = parse_sentiment_analyzer(response)
    print(emotions)
    print(reasoning)

if __name__ == "__main__":
    test_text = "I am so happy I am doing this."
    full_response = ('Based on the text, I would analyze the emotions as follows:\n\n```\n{\n  "anger": "0",\n  "disgust": "0",\n  "fear": "0",\n  "joy": "1",\n  "sadness": "0",\n  "dominant_emotion": "joy"\n}\n```\n\nThe reason for this analysis is that the word "fun" is a clear indicator of joy. The tone of the sentence is also positive and enthusiastic, suggesting that the speaker is experiencing a strong sense of happiness. There is no indication of any negative emotions such as anger, disgust, or fear in the text.\n\nNote: The probabilities are subjective and based on my analysis of the text. They may vary depending on the context and individual interpretation.',)
    emotions, reasoning = parse_sentiment_analyzer(full_response)

    print("Emotions", emotions)
    print("Reasoning", reasoning)
  