from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return {"""<p>Hello, I'm MoodJournal Please go to /mood to view your data!</p>
                <form>
                </form>
            """}
