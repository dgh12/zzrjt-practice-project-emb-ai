import requests, json
def sentiment_analyzer(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers=headers)
    f_res = json.loads(response.text)
    score = f_res["documentSentimet"]["score"]
    label = f_res["documentSentiment"]["label"]
    return {"score" : {{score}}, "label" : {{label}}}