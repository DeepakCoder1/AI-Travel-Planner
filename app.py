from flask import Flask, request, render_template, Response
from agents.supervisor import SupervisorAgent
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

API_KEY = os.getenv("hotel_api_key")


@app.route("/")
def home():
    return render_template("index.html")


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


@app.route("/hotel-photo")
def hotel_photo():

    photo = request.args.get("photo")

    url = f"https://places.googleapis.com/v1/{photo}/media?maxHeightPx=300&key={API_KEY}"

    r = requests.get(url, allow_redirects=True)

    print("Status:", r.status_code)
    print("Headers:", r.headers)
    print("Body:", r.text[:300])

    return Response(
        r.content,
        content_type=r.headers.get("Content-Type", "image/jpeg")
    )


if __name__ == "__main__":
    app.run(debug=True, port=8000)