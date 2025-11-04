# Blog AI App

An AI-powered blog content generation application using CrewAI agents.

## Features

- Automated blog post generation
- AI agents for content creation and management
- Task automation

## Project Structure
```
├── agents.py           # AI agent definitions
├── blogaiapp.py        # Main application
├── config.py           # Configuration settings
├── crew_manager.py     # Crew management logic
├── tasks.py            # Task definitions
├── requirements.txt    # Python dependencies
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/lokesht01/Blog-AI.git
cd Blog-AI
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file and add your API keys:
```bash
# Add your environment variables here
API_KEY=your_api_key_here
```

## Usage
```bash
python blogaiapp.py
```

## Requirements

- Python 3.x
- See `requirements.txt` for all dependencies

## Configuration

Update `config.py` with your specific settings before running the application.
