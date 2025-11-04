from crewai import Crew

def run_crew(agents, tasks, topic):
    crew = Crew(agents=agents, tasks=tasks, verbose=2)
    result = crew.kickoff(inputs={"topic": topic})
    return result