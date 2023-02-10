import openai

from flask import Flask, request
from flask import render_template

openai.api_key = "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"

def generate_sql(validation_logic):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Generate SQL query to validate {validation_logic}",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    return response.choices[0].text

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        validation_logic = request.form["validation_logic"]
        sql_query = generate_sql(validation_logic)
        return render_template("index.html", sql_query=sql_query)
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
