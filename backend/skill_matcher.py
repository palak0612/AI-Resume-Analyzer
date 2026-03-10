import spacy

nlp = spacy.load("en_core_web_sm")

skills_list = [
    "python",
    "java",
    "c++",
    "javascript",
    "react",
    "node",
    "sql",
    "mongodb",
    "machine learning",
    "data science",
    "flask",
    "spring boot",
    "aws",
    "docker",
]

def extract_skills(text):

    text = text.lower()
    detected_skills = []

    for skill in skills_list:
        if skill in text:
            detected_skills.append(skill)

    return detected_skills


def match_skills(resume_text, job_skills):

    resume_skills = extract_skills(resume_text)

    matched = list(set(resume_skills) & set(job_skills))

    score = (len(matched) / len(job_skills)) * 100 if job_skills else 0

    return {
        "resume_skills": resume_skills,
        "matched_skills": matched,
        "score": score
    }