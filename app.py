
from flask import Flask, request, jsonify
from flask_cors import CORS
from stockfish import Stockfish
from os.path import join

app = Flask(__name__)
CORS(app)


PATH=str(join('data', 'stockfish-ubuntu-20.04-x86-64'))
def init_stockfish(path=PATH):
  fish = Stockfish(path)
  fish.update_engine_parameters({"Hash": 2048})

  return fish

def predict_next_move(fen):
  fish.set_fen_position(fen)
  next_move = fish.get_best_move()
  wdl_stats = fish.get_wdl_stats()
  new_fen = fish.get_fen_position()
  return jsonify({
      "next_move": next_move,
      "wdl_stats": wdl_stats,
  })

def calculate_wdl(fen):
  fish.set_fen_position(fen)
  if fish.does_current_engine_version_have_wdl_option():
      try:
          wdl_stats = fish.get_wdl_stats()
          return jsonify({"wdl_stats": wdl_stats})
      except Exception as e:
          print(e)
  return  jsonify({"wdl_stats": [None,None,None]})

print('fish init')
fish=init_stockfish()
print(fish)

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
