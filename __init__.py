import os

from flask import Flask, request, send_from_directory, jsonify
from task import TaxSolver
app = Flask(__name__)


def ui_dir():
    return os.path.join(os.path.dirname(__file__), "ui")


@app.route('/solve', methods=['POST'])
def solve():
    data = request.get_json(force=True)
    solver = TaxSolver()
    solver.__dict__.update(data)
    return jsonify(solver.solve())


@app.route('/')
def index():
    return send_from_directory(ui_dir(), "index.html")

if __name__ == "__main__":
    app.run()
