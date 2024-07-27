from flask import Flask, request, render_template

from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

def format_output(output_dict):
    txt = "'anger': " + str(output_dict["anger"])
    txt += ", 'disgust': " + str(output_dict["disgust"])
    txt += ", 'fear': " + str(output_dict["fear"])
    txt += ", 'joy': " + str(output_dict["joy"])
    txt += " and 'sadness': " + str(output_dict["sadness"])
    txt += ". The dominant emotion is " + str(output_dict["dominant_emotion"])
    return txt

@app.route("/", methods =["GET", "POST"])
def home():
    return render_template("index.html")

@app.route("/emotionDetector")
def sent_detector():
    text_to_analyze = request.args.get('textToAnalyze')
    dominant_emotion = emotion_detector(text_to_analyze)

    if dominant_emotion is None:
        return "Invalid text! Please try again."
    else:
        return "The given text has been identified as {}.".format(format_output(dominant_emotion))

if __name__ == "__main__":
    app.run(host="localhost", port=5000)