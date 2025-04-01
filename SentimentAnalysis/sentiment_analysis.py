import requests, json
def sentiment_analyzer(text_to_analyze):
    url = "http://"
    headers = {"Content-Type": "application/json"}
    prompt  =  f"""Analyze the emotion of the following text and return a JSON object with the following structure:
    {{
        "anger":<probability>,
        "disgust":<probability>,
        "fear":<probability>,
        "joy":<probability>,
        "sadness":<probability>,
        "dominant_emotion": "<emotion with highest probability>"
    }}
    
    Text to analyze: "{text_to_analyze}"
    """
    data = {
        "model": "llama3",
        "prompt": prompt,
        "stream": False
    }
    try:
        response = requests.post(url, json = data, headers=headers, timeout=10)
        response.raise_for_status()
        full_response = response.json()
        return full_response.get("response", "")
    except Exception as e:
        print (f"an error occured {str(e)}")
        
    return response.text