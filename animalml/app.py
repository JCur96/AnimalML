from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/CNNs")
def CNNs():
    return render_template("CNNs.html")

@app.route("/Diffusers")
def Diffusers():
    return render_template("diffusers.html")

@app.route("/inference_cnns")
def inference_cnns():
    return render_template("inference_CNNs.html")

@app.route("/training_cnns")
def training_cnns():
    return render_template("training_CNNs.html")

@app.route("/inference_diffusers")
def inference_diffusers():
    return render_template("inference_diffusers.html")

@app.route("/training_diffusers")
def training_diffusers():
    return render_template("training_diffusers.html")

@app.route("/datasets")
def datasets():
    return render_template("datasets.html")


if __name__ == "__main__":
    app.run()