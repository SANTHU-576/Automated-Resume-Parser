import pdfplumber
import re

SKILLS = [
    "Python",
    "Java",
    "C",
    "C++",
    "SQL",
    "HTML",
    "CSS",
    "JavaScript",
    "Flask",
    "Machine Learning",
    "AI",
    "Data Science",
    "React",
    "Node.js"
]

EDUCATION = [
    "B.Tech",
    "Bachelor of Technology",
    "M.Tech",
    "Bachelor of Engineering",
    "B.E",
    "MCA",
    "BCA",
    "B.Sc",
    "M.Sc",
    "MBA",
    "Diploma",
    "Intermediate",
    "SSC"
]

def extract_resume_data(pdf_path):

    text = ""

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    # Email
    email = ""
    email_match = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', text)

    if email_match:
        email = email_match.group()

    # Phone
    phone = ""
    phone_match = re.search(r'\+?\d[\d\s-]{8,15}', text)

    if phone_match:
        phone = phone_match.group()

    # Name
    name = text.split("\n")[0]

    # Skills
    skills = []

    for skill in SKILLS:
        if skill.lower() in text.lower():
            skills.append(skill)

    # Education
    education = []

    for course in EDUCATION:
        if course.lower() in text.lower():
            education.append(course)

    return {
        "name": name,
        "email": email,
        "phone": phone,
        "skills": ", ".join(skills),
        "education": ", ".join(education)
    }