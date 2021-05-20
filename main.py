from flask import Flask, jsonify, request  # import objects from the Flask model
import json

app = Flask(__name__)  # define app using Flask

#languages = [{'name': 'JavaScript'}, {'name': 'Python'}, {'name': 'Ruby'}]


@app.route('/', methods=['GET'])
def test():
    return jsonify({'message': 'It works!'})


@app.route('/lang', methods=['GET'])
def returnAll():
    with open("data.json", "r") as languages:
        languages = json.load(languages)
        return jsonify(languages)


@app.route('/lang/<string:name>', methods=['GET'])
def returnOne(name):
    with open("data.json", "r") as languages:
        langs = [language for language in languages if language['name'] == name]
        return jsonify({'language': langs[0]})


@app.route('/lang', methods=['POST'])
def addOne():
    with open("data.json") as languages:
        language = {'name': request.json['name']}
        data = json.load(languages)
        data.update(language)
    return jsonify({'message': 'It works!'})

#@app.route('/lang/<string:name>', methods=['PUT'])
#def editOne(name):
#    langs = [language for language in languages if language['name'] == name]
#    langs[0]['name'] = request.json['name']
#    return jsonify({'language': langs[0]})
#

if __name__ == '__main__':
    app.run()
