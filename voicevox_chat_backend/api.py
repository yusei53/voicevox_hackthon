from dotenv import load_dotenv
import os
import io
from flask import Flask, request, jsonify,send_file
from chat.chat_gpt import callChatGPT
from chat.answerWav import playWav, makeWav
load_dotenv()
path = os.environ.get('PYTHONPATH')
basedir = os.path.dirname(__file__)
app = Flask(__name__)
@app.route('/api',methods=['GET','POST'])
def api():
    try:
        data = request.get_json()
        text = data['post_text']
        res = callChatGPT(text)
        playWav(makeWav(text))
        response = {'result':res}
        return jsonify(response)
    except Exception as e:
        res = "エラーなのだ。もう一度内容を入力してほしいのだ"
        response = {'result':res}
        return jsonify(response)
@app.route('/audio')
def get_audio():
    # オーディオファイルを読み込みます
    fpath= os.path.join(basedir, "chat/wav2/error.wav")
    with open(fpath, 'rb') as f:
        audio_data = f.read()
    # ファイルをレスポンスとして返します
    return send_file(
        fpath,
    )
app.run()