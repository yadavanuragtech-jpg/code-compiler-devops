from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess
import tempfile
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Backend is running"

@app.route('/run', methods=['POST'])
def run_code():
    data = request.get_json()
    code = data.get("code", "")

    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".py", mode="w") as temp:
            temp.write(code)
            temp.flush()

            result = subprocess.run(
                ["python", temp.name],
                capture_output=True,
                text=True,
                timeout=5
            )

        return jsonify({
            "output": result.stdout,
            "error": result.stderr
        })

    except Exception as e:
        return jsonify({
            "output": "",
            "error": str(e)
        })

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
