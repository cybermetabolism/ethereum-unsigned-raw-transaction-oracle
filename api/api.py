# -*- coding: utf-8 -*-


from flask import Flask, jsonify

app = Flask(__name__)

# See http://flask.pocoo.org/snippets/57/
@app.route('/', defaults={'path': ''}, methods=['GET'])
@app.route('/<path:path>', methods=['GET'])

def catch_all(path):
    return jsonify({'path': path})
    
if __name__ == '__main__':
    app.run(debug=True)