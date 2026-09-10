from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return """
    <html>
        <head>
            <title>Examen Redes Virtuales</title>
            <style>
                body { font-family: Arial, sans-serif; background: #f4f7fb; color: #1f2933; text-align: center; padding-top: 80px; }
                h1 { color: #005baa; }
                .box { display: inline-block; background: white; padding: 24px 32px; border: 1px solid #d9e2ec; border-radius: 8px; }
            </style>
        </head>
        <body>
            <div class="box">
                <h1>Examen Redes Virtuales</h1>
                <p>Aplicacion Flask ejecutada por el grupo.</p>
                <p>DEVASC + CSR1000v + Docker</p>
            </div>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, threaded=False)
