from flask import Flask, render_template, jsonify
import animalml.documents.datasets

app = Flask(__name__)

## basic navigation ##
@app.route("/")
def main():
    return render_template("index.html")

@app.route("/CNNs")
def CNNs():
    return render_template("CNNs.html")

@app.route("/Diffusers")
def Diffusers():
    return render_template("diffusers.html")

## CNNs ##
@app.route("/inference_cnns")
def inference_cnns():
    return render_template("inference_CNNs.html")

@app.route("/training_cnns")
def training_cnns():
    return render_template("training_CNNs.html")

## Diffusers ##
@app.route("/inference_diffusers")
def inference_diffusers():
    return render_template("inference_diffusers.html")

@app.route("/training_diffusers")
def training_diffusers():
    return render_template("training_diffusers.html")


## Dataset functionality ##
@app.route("/datasets")
def datasets():
    return render_template("datasets.html")

@app.route("/select_dataset")
def select_dataset():
    # probably want to import the datasets.py module
    # then use the logic in there? 
    return None
@app.route("/build_database")
def build_lila_database():
    try:
        destination_dir = "data/"
        all_article_list = animalml.documents.datasets.build_dataset_database()
        animalml.documents.datasets.save_to_json(destination_dir,all_article_list)
        return jsonify({"message": "Database build started successfully."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
@app.route("/build_lila_metadata")
def build_lila_metadata_db():
    try:
        animalml.documents.datasets.build_lila_metadata('data/lila/')
        return jsonify({"message": "Lila metadata build started successfully."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run()