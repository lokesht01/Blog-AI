from crewai import Task

def create_tasks(planner, writer, editor):
    plan_task = Task(
        description=("1. Prioritize trends, key players, and news on {topic}.\n"
                     "2. Identify target audience and their interests.\n"
                     "3. Develop a content outline with intro, key points, CTA.\n"
                     "4. Include SEO keywords and sources."),
        expected_output="Comprehensive content plan document with outline, audience, SEO, and sources.",
        agent=planner
    )

    write_task = Task(
        description=("1. Write blog post using content plan.\n"
                     "2. Incorporate SEO keywords naturally.\n"
                     "3. Proper sections/subtitles.\n"
                     "4. Engaging intro, body, and conclusion.\n"
                     "5. Proofread for grammar and brand voice."),
        expected_output="Well-written markdown blog post ready for publication.",
        agent=writer
    )

    edit_task = Task(
        description="Proofread and edit the blog post for grammar, style, and brand voice.",
        expected_output="Final polished blog post in markdown format.",
        agent=editor
    )

    return [plan_task, write_task, edit_task]
