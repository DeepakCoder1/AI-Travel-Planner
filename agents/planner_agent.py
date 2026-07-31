import re

from llm.model import generate_response
from llm.prompts import build_prompt


class Planneragent:
    """
    Planner Agent

    Responsibilities:
    - Receive trip details
    - Build the LLM prompt
    - Generate a travel itinerary
    """

    def __init__(self):
        self.agent_name = "Planner Agent"

    def plan_trip(self, destination, days, budget, travel_style):

        prompt = build_prompt(
            destination=destination,
            days=days,
            budget=budget,
            travel_style=travel_style
        )

        print(f"\n[{self.agent_name}] Generating itinerary...\n")

        response = generate_response(prompt)

        # Convert Day headings
        response = re.sub(
            r"Day\s*(\d+)\s*:",
            r"</div><div class='day-card'><h2>📅 Day \1</h2>",
            response
        )

        # Format sections
        response = response.replace(
            "Morning:",
            "<h3>🌅 Morning</h3><p>"
        )

        response = response.replace(
            "Afternoon:",
            "</p><h3>🌞 Afternoon</h3><p>"
        )

        response = response.replace(
            "Evening:",
            "</p><h3>🌙 Evening</h3><p>"
        )

        response = response.replace(
            "Estimated Cost:",
            "</p><p><b>💰 Estimated Cost:</b> "
        )

        response = response.replace(
            "Packing Tips:",
            "</p><hr><h2>🎒 Packing Tips</h2><p>"
        )

        response = response.replace(
            "Transportation Tips:",
            "</p><hr><h2>🚖 Transportation Tips</h2><p>"
        )

        response = response.replace(
            "Food Recommendations:",
            "</p><hr><h2>🍽 Food Recommendations</h2><p>"
        )

        response = "<div class='day-card'>" + response + "</p></div>"

        return response