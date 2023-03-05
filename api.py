from flask import Flask, jsonify, request, abort, redirect
from langdetect import detect
import os
from core import translate
from gevent.pywsgi import WSGIServer
from gevent import monkey
monkey.patch_all()

env_auth_key = ''

try:
    env_auth_key = os.environ['AUTH_KEY']
    print('AUTH_KEY: ' + env_auth_key)
except KeyError:
    print('No AUTH_KEY specified.')

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_index():
    return redirect('https://github.com/t-rdp/tmt', 302)

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "online"})

@app.route('/translate', methods=['POST'])
def post_translation():
    auth_key = request.form.get('auth_key')

    if env_auth_key != '' and auth_key != env_auth_key:
        abort(401)

    text = request.form.get('text')
    target_lang = request.form.get('target_lang').lower()
    source_lang = detect(text)
    return jsonify({
        "translations": [{
            "detected_source_language": source_lang.upper(),
            "text": "[TMT] " + translate(text, target_lang, source_lang)
        }]
    })


if __name__ == '__main__':
    # app.run()
    http_server = WSGIServer(('0.0.0.0', 9300), app)
    http_server.serve_forever()