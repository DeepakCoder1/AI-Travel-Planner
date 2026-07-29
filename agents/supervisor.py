from agents.planner_agent import Planneragent


class SupervisorAgent:
    """
    Supervisor Agent

    Responsibilities:
    1. Receive the user's request.
    2. Decide which agents to use.
    3. Combine responses.
    """

    def __init__(self):
        self.planner = Planneragent()

    def plan_trip(self, destination, days, budget, travel_style):

        print("\n========== Supervisor Agent ==========")
        print("Received user request...")
        print(f"Destination : {destination}")
        print(f"Days        : {days}")
        print(f"Budget      : {budget}")
        print(f"Style       : {travel_style}")

        print("\nCalling Planner Agent...\n")

        itinerary = self.planner.plan_trip(
            destination,
            days,
            budget,
            travel_style
        )

        print("\nPlanner Agent Finished.")

        return itinerary