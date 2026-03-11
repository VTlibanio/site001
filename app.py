from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <meta charset="utf-8">
            <title>Pra você</title>
        </head>
        <body style="text-align:center; font-family: Arial;">
            <h1>Oi, meu amor ❤️</h1>
            <p>Esse site é só pra você.</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)