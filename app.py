from flask import Flask, render_template, request
import json
from patterns import detect_pattern

app = Flask(__name__)

with open('problem_data.json') as f:
    problems = json.load(f)

@app.route('/')
def index():
    return render_template('index.html', problems=problems)

@app.route('/analyze', methods=['POST'])
def analyze():
    problem_id = int(request.form['problem_id'])
    problem = next(p for p in problems if p['id'] == problem_id)
    patterns = detect_pattern(problem)
    return render_template('result.html', problem=problem, patterns=patterns)

if __name__ == '__main__':
    app.run(debug=True)
