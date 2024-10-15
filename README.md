# Quiz Application

This is a simple quiz application built using Python and Flask that displays a set of 5 questions with multiple choice answers. The user selects one answer per question, and upon submission, the score and the correct/incorrect answers are displayed.

## Features
- Displays 5 questions
- Each question has 4 multiple choice answers
- Validates that all questions are answered before submission
- Shows the score and correct answers after submission
- Option to restart the quiz

## Requirements
- Python 3.8 or above
- Flask 2.0.3

## Running the Application Locally

1. Clone the repository from GitHub:
   ```bash
   git clone <url>
   cd quiz-app
   
2. Install dependencies:
    pip install -r requirements.txt

3. Run the Flask application:
    python app.py
	
4. Open your browser and go to http://127.0.0.1:5000/ to view the quiz.

## Running the Application on Docker:

1. Build the Docker image:
    docker build -t quiz-app .

2. Run the Docker container:
    docker run -p 5000:5000 quiz-app