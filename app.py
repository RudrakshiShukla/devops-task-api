
from flask import Flask, jsonify, render_template

app = Flask(__name__)

tasks = [
    {"id": 1, "task": "Learn Git", "completed": True},
    {"id": 2, "task": "Learn Docker", "completed": False},
    {"id": 3, "task": "Learn Jenkins", "completed": False}
]


# Home page
@app.route("/")
def home():
    return render_template("index.html", tasks=tasks)


# API: Get all tasks
@app.route("/tasks")
def get_tasks():
    return jsonify(tasks)


# API: Application health check
@app.route("/health")
def health():
    return jsonify({"status": "healthy"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
