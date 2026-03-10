from flask import Flask, request, jsonify
from flask_cors import CORS
from resume_parser import extract_text_from_pdf
from skill_matcher import match_skills

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "AI Resume Analyzer API is running"

@app.route("/analyze", methods=["POST"])
def analyze_resume():

    file = request.files["resume"]
    skills = request.form["skills"].split(",")

    text = extract_text_from_pdf(file)
    result = match_skills(text, skills)

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)