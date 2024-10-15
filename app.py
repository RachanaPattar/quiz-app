from flask import Flask, render_template, request, redirect, url_for, jsonify
import json

app = Flask(__name__)

# Load quiz data from JSON file
def load_quiz_data():
    try:
        with open('quiz_data.json', 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

quiz_data = load_quiz_data()

@app.route('/')
def index():
    return render_template('quiz.html', quiz_data=quiz_data)

@app.route('/submit', methods=['POST'])
def submit_quiz():
    score = 0
    answers = request.form
    results = []
    
    for question in quiz_data:
        user_answer = answers.get(f'question_{question["id"]}')
        correct_answer_key = question['answerKey']
        correct_answer_text = next(option['text'] for option in question['options'] if option['key'] == correct_answer_key)
        is_correct = user_answer == correct_answer_key
        if is_correct:
            score += 1
        results.append({
            "question": question["question"],
            "user_answer": user_answer,
            "correct_answer": correct_answer_key,
            "correct_answer_text": correct_answer_text,
            "is_correct": is_correct
        })
    
    return render_template('result.html', score=score, total=len(quiz_data), results=results)

@app.route('/restart')
def restart():
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
