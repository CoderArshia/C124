from flask import Flask, request,jsonify
import jinja2
app = Flask(__name__)
@app.route("/")


def hello():
    return "Arshia"

tasks = [
    {
        "id":1,
        "title":"books",
        "description":"i like reading books",
        "done":False
    },

        {
        "id":2,
        "title":"[python]",
        "description":"python is fun to code",
        "done":False
    },
]

@app.route("/add-data",methods=["POST"])
def add_task():
    if not request.json:
        return jsonify ({
            "status":"error",
            "message":"please provide the data"
        },400)

    task = {
        "id":tasks[-1]["id"]+1,
        "title":request.json["title"],
        "description":request.json.get("description"),
        "done":False
            
    }
    tasks.append(task)
    return jsonify({
        "status":"success",
        "message":"task added successfuly"
    })

@app.route("/get-data")
def get_task():
    return jsonify({
        "data":tasks
    })
        


if __name__=="__main__":
    app.run()

