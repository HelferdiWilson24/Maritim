from flask import Flask, render_template, request

app = Flask(__name__)

# Import logika chatbot dari main.py
import random
import difflib

intents = {
    "sapaan": {
        "pertanyaan": ["halo", "hai", "hai bot", "halo bot"],
        "respon": ["Halo!", "Hai!", "Halo, ada yang bisa saya bantu?"]
    },
    "kabar": {
        "pertanyaan": ["apa kabar?", "gimana kabarnya?", "bagaimana kabar kamu?"],
        "respon": ["Saya baik-baik saja, terima kasih!", "Saya selalu siap membantu!", "Kabar saya baik, terima kasih!"]
    },
    "nama": {
        "pertanyaan": ["siapa namamu?", "boleh tahu namamu?", "nama kamu apa?"],
        "respon": ["Saya adalah chatbot AI.", "Anda bisa memanggil saya chatbot."]
    },
    "creator": {
        "pertanyaan": ["siapa penciptamu?", "siapa yang membuatmu?", "siapa developer kamu?"],
        "respon": ["Saya dibuat oleh seorang pengembang menggunakan Python.", "Saya adalah hasil karya seorang developer."]
    },
    "default": {
        "respon": ["Maaf, saya tidak mengerti pertanyaan Anda.", "Maaf, bisa Anda ulangi pertanyaannya?", "Mohon maaf, saya tidak bisa memberikan respons yang tepat."]
    }
}

def get_chatbot_response(pertanyaan_pengguna):
    pertanyaan_pengguna = pertanyaan_pengguna.lower()

    for intent, data in intents.items():
        if "pertanyaan" in data:
            if pertanyaan_pengguna in [p.lower() for p in data["pertanyaan"]]:
                return random.choice(data["respon"])
            else:
                closest_match = difflib.get_close_matches(pertanyaan_pengguna, data["pertanyaan"], n=1, cutoff=0.6)
                if closest_match:
                    return random.choice(data["respon"])
    return random.choice(intents["default"]["respon"])

# Route utama untuk tampilan web
@app.route('/')
def home():
    return render_template('index.html')

# Route untuk menerima permintaan dari pengguna
@app.route('/get_response', methods=['POST'])
def get_response():
    pertanyaan_pengguna = request.form['pertanyaan']
    jawaban_chatbot = get_chatbot_response(pertanyaan_pengguna)
    return jawaban_chatbot

if __name__ == '__main__':
    app.run(debug=True)
