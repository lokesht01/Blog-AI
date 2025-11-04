from crewai import Agent
from langchain_openai import AzureChatOpenAI
from config import AZURE_API_KEY, AZURE_ENDPOINT, AZURE_DEPLOYMENT_NAME, AZURE_API_VERSION

def create_llm():
    return AzureChatOpenAI(
        azure_endpoint=AZURE_ENDPOINT,
        api_key=AZURE_API_KEY,
        api_version=AZURE_API_VERSION,
        deployment_name=AZURE_DEPLOYMENT_NAME,
        temperature=0.7
    )

def create_agents():
    llm = create_llm()
    
    planner = Agent(
        role="Content Planner",
        goal="Plan engaging and factually accurate content on {topic}",
        backstory="You're planning a blog article about {topic}. Your work guides the Content Writer.",
        allow_delegation=False,
        verbose=True,
        llm=llm
    )

    writer = Agent(
        role="Content Writer",
        goal="Write insightful and factually accurate article about {topic}",
        backstory="You write the article based on the Planner's outline. Provide objective insights and acknowledge opinions.",
        allow_delegation=False,
        verbose=True,
        llm=llm
    )

    editor = Agent(
        role="Editor",
        goal="Edit blog posts to align with brand style and clarity",
        backstory="Review posts for grammar, style, and balanced viewpoints.",
        allow_delegation=False,
        verbose=True,
        llm=llm
    )

    return planner, writer, editor