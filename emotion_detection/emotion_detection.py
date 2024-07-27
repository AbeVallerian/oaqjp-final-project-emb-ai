"wrapper for emotion predict from Watson"
import json
import requests

def emotion_detector(text_to_analyze):
    "wrapper for emotion predict from Watson"
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/" + \
        "NlpService/EmotionPredict"
    myobj = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header, timeout=100)

    emotion_predictions = json.loads(response.text)["emotionPredictions"]
    emotions = {
        "anger": emotion_predictions[0]["emotion"]["anger"],
        "disgust": emotion_predictions[0]["emotion"]["disgust"],
        "fear": emotion_predictions[0]["emotion"]["fear"],
        "joy": emotion_predictions[0]["emotion"]["joy"],
        "sadness": emotion_predictions[0]["emotion"]["sadness"],
    }

    top_score = 0.0
    top_emotion = ""
    for emotion, score in emotions.items():
        if score > top_score:
            top_score = score
            top_emotion = emotion
    emotions["dominant_emotion"] = top_emotion

    return emotions
