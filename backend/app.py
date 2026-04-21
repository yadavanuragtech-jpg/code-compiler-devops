import os
from flask import Flask, request, jsonify
import subprocess
import tempfile
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/run', methods=['POST'])
def run_code():
    code = request.json['code']

    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".py") as temp:
            temp.write(code.encode())
            temp.flush()

            result = subprocess.run(
                ["python3", temp.name],
                capture_output=True,
                text=True,
                timeout=5
            )

        return jsonify({
            "output": result.stdout,
            "error": result.stderr
        })

    except Exception as e:
        return jsonify({"error": str(e)})

import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
