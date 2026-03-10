# 🤖 AI Resume Analyzer

AI Resume Analyzer is a **full-stack web application** that analyzes resumes using **Natural Language Processing (NLP)** techniques.
The system allows users to upload their resumes and compare them with a job description to evaluate how well their skills match the required role.

The application automatically extracts key skills from resumes, calculates a **resume match score**, and provides suggestions to improve the resume for better job opportunities and ATS (Applicant Tracking System) compatibility.

## 🚀 Features

* 📄 Upload resumes in **PDF format**
* 🧠 Automatic **resume text extraction**
* 🔍 **Skill extraction** using NLP techniques
* 🎯 **Job description matching**
* 📊 Resume **match score calculation**
* 💡 Suggestions for **missing skills and improvements**
* 📈 Dashboard showing **analysis results**

## 🛠️ Tech Stack

### Frontend

* React.js
* Tailwind CSS
* Axios

### Backend

* Python Flask
* REST APIs

### Database

* MongoDB

### AI / NLP

* spaCy
* PyPDF2
* Scikit-learn

## ⚙️ How It Works

1. The user uploads a **resume in PDF format**.
2. The system extracts **text data from the resume**.
3. NLP techniques identify **important skills** from the resume.
4. The user enters a **job description**.
5. The system compares resume skills with required job skills.
6. A **resume score** is generated along with improvement suggestions.

## 📂 Project Structure

```
AI-Resume-Analyzer
│
├── frontend
│   ├── components
│   ├── pages
│   ├── ResumeUpload.js
│   └── Dashboard.js
│
├── backend
│   ├── app.py
│   ├── resume_parser.py
│   ├── skill_matcher.py
│   └── database.py
│
└── README.md
```

## 🔧 Installation

### 1️⃣ Clone the Repository

```
git clone https://github.com/yourusername/AI-Resume-Analyzer.git
cd AI-Resume-Analyzer
```

### 2️⃣ Install Backend Dependencies

```
pip install flask
pip install spacy
pip install pymongo
pip install PyPDF2
pip install scikit-learn
```

Download NLP model:

```
python -m spacy download en_core_web_sm
```

### 3️⃣ Start the Backend Server

```
python app.py
```

### 4️⃣ Start the Frontend

```
cd frontend
npm install
npm start
```

## 🔮 Future Improvements

* ATS compatibility scoring
* Resume keyword highlighting
* AI-based resume improvement suggestions
* Support for multiple file formats
* Data visualization for skill analysis

## 👩‍💻 Author

**Palak Bhatia**

* Passionate about **Full-Stack Development**
* Interested in **AI-powered applications and scalable systems**

⭐ If you like this project, consider giving it a **star** on GitHub!

