from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.route('/api/data')
def get_data():
    # TODO: Ajouter des paramètres de filtre (ex: date, utilisateur)
    with open('data/data.json') as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)