import os

from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify

from werkzeug.utils import secure_filename

from model.caption_model import generate_caption

app = Flask(__name__)

UPLOAD_FOLDER = os.path.join("static", "uploads")

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate-caption", methods=["POST"])
def caption():

    if "image" not in request.files:

        return jsonify({

            "error": "No image uploaded."

        }), 400

    image = request.files["image"]

    if image.filename == "":

        return jsonify({

            "error": "Please choose an image."

        }), 400

    filename = secure_filename(image.filename)

    filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        filename
    )

    image.save(filepath)

    try:

        result = generate_caption(filepath)

        return jsonify({

            "caption": result

        })

    except Exception as e:

        return jsonify({

            "error": str(e)

        }), 500

    finally:

        if os.path.exists(filepath):
            os.remove(filepath)


if __name__ == "__main__":

    app.run(debug=True)