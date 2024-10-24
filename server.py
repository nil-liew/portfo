from flask import Flask, render_template, request
import csv

app = Flask(__name__)


@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/<string:path>")
def catch_all(path):
    return render_template(path)


def write_to_file(data):
    with open("database.txt", "a") as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f"\n{email},{subject},{message}")


def write_to_csv(data):
    with open("database.csv", mode="a", newline="") as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(
            database2,
            delimiter=",",
            quotechar='"',
            quoting=csv.QUOTE_MINIMAL,
        )
        csv_writer.writerow([email, subject, message])


@app.route("/submit_form", methods=["POST", "GET"])
def submit_form():
    if request.method == "POST":
        data = request.form.to_dict()
        # write_to_file(data)
        write_to_csv(data)
        return "form submitted, thanks!"
    else:
        return "something went wrong, try again!"


if __name__ == "__main__":
    app.run(debug=True)
