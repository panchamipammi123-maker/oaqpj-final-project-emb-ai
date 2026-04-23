from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector", methods=["GET"])
def sent_emotion():
    text_to_analyze = request.args.get('textToAnalyze')
    if not text_to_analyze or not text_to_analyze.strip():
        return jsonify({'error': 'No text provided'}), 400
    response = emotion_detector(text_to_analyze)
    return jsonify(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
