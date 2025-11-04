import streamlit as st
from agents import create_agents
from tasks import create_tasks
from crew_manager import run_crew

st.set_page_config(page_title="Multi-Agent Blog Generator", layout="wide")

st.title("Multi-Agent Blog Generator")
st.write("Generate high-quality blog articles using AI agents!")

# Input section
topic = st.text_input("Enter the topic for the article:", placeholder="e.g., Artificial Intelligence, Climate Change, etc.")

if st.button("Generate Article", type="primary"):
    if topic.strip() == "":
        st.warning("Please enter a topic.")
    else:
        # Create agents and tasks
        planner, writer, editor = create_agents()
        tasks = create_tasks(planner, writer, editor)
            
        # Show progress
        with st.spinner("Planning content structure..."):
            st.info("Agents are working on your article...")
            
        # Run the crew
        result = run_crew([planner, writer, editor], tasks, topic)
            
        # Display results
        st.success("Article generated successfully!")
            
        # Convert result to string if it's not already
        if hasattr(result, 'raw'):
            article_content = result.raw
        elif hasattr(result, 'output'):
            article_content = result.output
        else:
            article_content = str(result)
            
        # Remove markdown code block wrapper if present
        if article_content.startswith('```markdown\n'):
            article_content = article_content[12:]  # Remove ```markdown\n
        if article_content.endswith('\n```'):
            article_content = article_content[:-4]  # Remove \n```
            
        # Display the formatted article
        st.markdown("---")
        st.markdown(article_content, unsafe_allow_html=True)
            
        # Add download option
        st.markdown("---")
        st.download_button(
            label="📥 Download Article as Markdown",
            data=article_content,
            file_name=f"{topic.replace(' ', '_').lower()}_article.md",
            mime="text/markdown"
        )

