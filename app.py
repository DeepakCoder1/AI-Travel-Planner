from flask import Flask, request, render_template
from agents.supervisor import SupervisorAgent


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def Home():
    return render_template('index.html')

@app.route("/plan", methods=["POST"])
def plan_trip():

    destination = request.form["destination"]
    days = request.form["days"]
    budget = request.form["budget"]
    travel_style = request.form["travel_style"]

    supervisor = SupervisorAgent()

    result = supervisor.plan_trip(
        destination,
        days,
        budget,
        travel_style
    )

    return render_template(
        "index.html",
        result=result
    )


if __name__ == "__main__":
    app.run(debug=True)