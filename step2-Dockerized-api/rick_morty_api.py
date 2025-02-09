from flask import Flask, jsonify
import requests as re
app = Flask(__name__)
@app.route('/', methods=['GET'])
def filter_chars():
    filtered_chars = []
    data = re.get('https://rickandmortyapi.com/api/character').json()['results']
    for char in data:
        if char['species'] == 'Human' and char['status'] == 'Alive' and 'Earth' in  char['origin']['name']:
            char = {
                'Name' : char['name'],
                'Location' : char['location']['name'],
                'Image': char['image']
            }
            filtered_chars.append(char)
    return jsonify(filtered_chars)

@app.route('/healthcheck', methods=['GET'])
def healthcheck():
    return jsonify({'status': 'OK'}),200 

@app.errorhandler(404)
def page_not_found(e):
    return jsonify({'Error': 'Page not found',
                     'Message': '''Page not found only avilable path at the moment are:
                      / - get filtered human charachters from Earth
                      /healthcheck -  to check server is responsive'''}), 404

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)