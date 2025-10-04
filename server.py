"""
Flask server for emotion detection using Watson NLP.
Serves the index page and handles AJAX requests from the frontend.
"""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detect

app = Flask(__name__)


@app.route("/emotionDetector", methods=["GET"])
def handle_emotion_detection():
    """Handle GET requests for emotion detection."""
    statement = request.args.get("textToAnalyze", "").strip()

    # Call the emotion detector
    scores = emotion_detect.emotion_detector(statement)

    # Determine dominant emotion safely
    if not scores or all(value is None for value in scores.values()):
        dominant_emotion = None
    else:
        dominant_emotion = max(scores, key=scores.get)

    # Prepare response string
    if dominant_emotion is None:
        response_text = "Invalid text! Please try again!"
    else:
        response_text = (
            f"For the given statement, the system response is "
            f"'anger': {scores['anger']}, 'disgust': {scores['disgust']}, "
            f"'fear': {scores['fear']}, 'joy': {scores['joy']} and "
            f"'sadness': {scores['sadness']}. "
            f"The dominant emotion is {dominant_emotion}."
        )

    return response_text


@app.route("/")
def render_index_page():
    """Render the main index page."""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
