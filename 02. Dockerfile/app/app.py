from flask import Flask, request, make_response, jsonify
import nltk
from transformers import pipeline

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def welcome():
    return make_response(
        "Welcome in NLP API Server", 200
    )

@app.route('/text-cleaning/remove-number', methods=['GET', 'POST'])
def remove_numbers():
    sentence = request.args.get("sentence").split("_")
    sentence = " ".join(sentence)
    return make_response(
        jsonify(
            {"sentence" : ''.join([i for i in sentence if not i.isdigit()])}
        ), 200
    )

@app.route('/text-cleaning/lower-case', methods=['GET', 'POST'])
def lower_case():
    sentence = request.args.get("sentence").split("_")
    sentence = " ".join(sentence)
    return make_response(
        jsonify(
            {"sentence" : str(sentence.lower())}
        ), 200
    )

@app.route('/text-cleaning/stemming', methods=['GET', 'POST'])
def stemming():
    sentence = request.args.get("sentence").split("_")
    sentence = " ".join(sentence)
    stemmer = nltk.porter.PorterStemmer()
    return make_response(
        jsonify(
            {"sentence" : str(' '.join([stemmer.stem(word) for word in sentence.split()]))}
        )
    )

@app.route('/prediction/sentiment-analysis', methods=['GET', 'POST'])
def sentiment_analysis():
    sentiment_pipeline = pipeline("sentiment-analysis")
    sentence = request.args.get("sentence").split("_")
    return make_response(
        jsonify(
            sentiment_pipeline(" ".join(sentence))[0]
        ), 200
    )

@app.errorhandler(404)
def error_handler_404(e):
    return make_response(
        jsonify(
            {
                "message":"url not found", 
             }
        ), 404
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)