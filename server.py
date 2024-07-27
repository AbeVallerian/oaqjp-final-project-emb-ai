"server file flask"
from flask import Flask, request, render_template

from emotion_detection.emotion_detection import emotion_detector

app = Flask(__name__)

def format_output(output_dict):
    "format output as required"
    txt = "'anger': " + str(output_dict["anger"])
    txt += ", 'disgust': " + str(output_dict["disgust"])
    txt += ", 'fear': " + str(output_dict["fear"])
    txt += ", 'joy': " + str(output_dict["joy"])
    txt += " and 'sadness': " + str(output_dict["sadness"])
    txt += ". The dominant emotion is " + str(output_dict["dominant_emotion"])
    return txt

@app.route("/", methods =["GET", "POST"])
def home():
    "return index file"
    return render_template("index.html")

@app.route("/emotionDetector")
def sent_detector():
    "send input to the emotion detector"
    text_to_analyze = request.args.get('textToAnalyze')
    if text_to_analyze == "":
        emotion = {
            "anger": None, "disgust": None, "fear": None, "joy": None, "sadness": None,
            "dominant_emotion": None
        }
    else:
        emotion = emotion_detector(text_to_analyze)

    if emotion["dominant_emotion"] is None:
        return "Invalid text! Please try again.", 400

    return f"The given text has been identified as {format_output(emotion)}."

if __name__ == "__main__":
    app.run(host="localhost", port=5000)
