from ai import init_stockfish,predict_next_move,calculate_wdl
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def home():
  return "home"


@app.route('/next', methods=['POST'])
def next_move():
    json = request.json
    fen = json['fen'] 
    return predict_next_move(fen)

@app.route('/wdl', methods=['POST'])
def wdl_stats():
    json = request.json
    fen = json['fen']
    return calculate_wdl(fen)
