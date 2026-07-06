from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os

from parser import extract_resume_data
from database import create_database, save_candidate

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

create_database()

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():

    if "resume" not in request.files:
        return "No file uploaded"

    file = request.files["resume"]

    if file.filename == "":
        return "Please select a PDF file"

    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)

    file.save(filepath)

    data = extract_resume_data(filepath)

    save_candidate(
        data["name"],
        data["email"],
        data["phone"],
        data["skills"],
        data["education"]
    )

    return render_template(
        "index.html",
        result=data
    )


if __name__ == "__main__":
    app.run(debug=True)