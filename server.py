from flask import Flask, request, jsonify, render_template
from EmotionDetection import emotion_detect

app = Flask(__name__)

@app.route('/emotionDetector', methods=['GET'])
def emotion_detector():
    statement = request.args.get('textToAnalyze')
    scores = emotion_detect.emotion_detector(statement)
    dominant_emotion = max(scores, key=scores.get)


    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {scores['anger']}, 'disgust': {scores['disgust']}, "
        f"'fear': {scores['fear']}, 'joy': {scores['joy']} and 'sadness': {scores['sadness']}. "
        f"The dominant emotion is {dominant_emotion}."
    )

    return response_text


@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)