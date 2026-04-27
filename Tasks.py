from crewai import Task

def location_task(agent, from_city, destination, date_from, date_to):
    return Task(
        description=f"""
        Provide travel logistics from {from_city} to {destination}.
        Include transport, visa, and tips from {date_from} to {date_to}.
        """,
        expected_output="Travel logistics details",
        agent=agent
    )

def guide_task(agent, destination, interests, date_from, date_to):
    return Task(
        description=f"""
        Find attractions and food in {destination}.
        Interests: {interests}.
        Travel dates: {date_from} to {date_to}.
        """,
        expected_output="List of attractions and food",
        agent=agent
    )

def planner_task(context_tasks, agent, destination, interests, date_from, date_to):
    return Task(
        description=f"""
        Create a full itinerary for {destination}.
        Interests: {interests}
        Dates: {date_from} to {date_to}

        Combine all previous outputs.
        """,
        expected_output="Detailed day-by-day itinerary",
        agent=agent,
        context=context_tasks  # 🔥 IMPORTANT FIX
    )