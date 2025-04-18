
from flask import Flask, render_template, request, jsonify
from logic import invoice as invoice_utils
from logic import ledger as ledger_utils
from logic import ocr as ocr_utils
from logic import drive as drive_utils
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    msg = request.json.get("message")
    # Placeholder response
    return jsonify({"response": f"You said: {msg}"})

if __name__ == "__main__":
    app.run(debug=True)
