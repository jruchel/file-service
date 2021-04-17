import json
from flask import request, Flask
from flask_cors import CORS

api = Flask(__name__)
api.config["DEBUG"] = True
CORS(api)


@api.route('/files', methods=['GET'])
def get_files():
    try:
        database = open('database.txt', 'r')
        files = []
        for line in database.readlines():
            files.append(json.loads(line))

        return create_response(files, 200)
    except Exception as e:
        return create_response(e, 500)


@api.route('/files', methods=['POST'])
def post_file():
    try:
        content = request.get_json()
        database = open('database.txt', 'w+')
        database.write(content)
        database.close()
        return create_response('Dodano', 200)
    except Exception as e:
        return create_response(e, 500)


def create_response(data, status):
    return api.response_class(response=json.dumps(data), status=status, mimetype='application/json')


if __name__ == "__main__":
    api.run(host='0.0.0.0')
