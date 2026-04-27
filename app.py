from agent import guide_expert, location_expert, planner_expert
from Tasks import location_task, guide_task, planner_task
from crewai import Crew, Process
import streamlit as st

st.set_page_config(page_title="AI Trip Planner", layout="centered")

st.title("🌍 AI-Powered Trip Planner")

from_city = st.text_input("From City", "India")
destination_city = st.text_input("Destination City", "Rome")
date_from = st.date_input("Departure Date")
date_to = st.date_input("Return Date")
interests = st.text_area("Interests", "food, sightseeing")

if st.button("🚀 Generate Travel Plan"):

    if date_from > date_to:
        st.error("Return date must be after departure date")
        st.stop()

    with st.spinner("🤖 Planning your trip..."):

        # Convert dates to string
        df = str(date_from)
        dt = str(date_to)

        # Tasks
        loc_task = location_task(location_expert, from_city, destination_city, df, dt)
        guid_task = guide_task(guide_expert, destination_city, interests, df, dt)
        plan_task = planner_task([loc_task, guid_task], planner_expert, destination_city, interests, df, dt)

        # Crew
        crew = Crew(
            agents=[location_expert, guide_expert, planner_expert],
            tasks=[loc_task, guid_task, plan_task],
            process=Process.sequential,
            verbose=True
        )

        try:
            result = crew.kickoff()
        except Exception as e:
            st.error(f"Error: {str(e)}")
            st.stop()

    st.subheader("✅ Your Travel Plan")
    st.markdown(f"```markdown\n{result}\n```")

    st.download_button(
        label="📥 Download Plan",
        data=str(result),
        file_name=f"{destination_city}_trip.txt",
        mime="text/plain"
    )