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
        """
        Generate a travel plan.
        """
        prompt = build_prompt(
            destination=destination,
            days=days,
            budget=budget,
            travel_style=travel_style
        )

        print(f"\n[{self.agent_name}] Generating itinerary...\n")

        # Call LLM
        response = generate_response(prompt)

        return response