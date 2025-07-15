import PyPDF2
import docx
import openai
import json
import re

client = openai.OpenAI(api_key="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") 

def extract_text(uploaded_file):
    if uploaded_file.name.endswith(".pdf"):
        reader = PyPDF2.PdfReader(uploaded_file)
        return " ".join(page.extract_text() for page in reader.pages if page.extract_text())
    elif uploaded_file.name.endswith(".docx"):
        doc = docx.Document(uploaded_file)
        return "\n".join(para.text for para in doc.paragraphs)
    return ""

def extract_json_block(text):
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if match:
        try:
            return json.loads(match.group())
        except:
            print("error parsing json")
            return None
    return None

def get_field_suggestions(resume_text):
    prompt = f"""Read the resume below and suggest 4 technology-related career fields/jobs that match the candidate's experience. 
If there are no matching fields, respond with an empty list.
Respond in this JSON format:
{{
  "suggested_fields": [
    {{"field": "Field Name", "description": "What the field/job is all about", "skills_required": ["Skill1", "Skill2"]}}
  ]
}}

Resume:
{resume_text}
"""
    res = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    raw = res.choices[0].message.content
    parsed = extract_json_block(raw)
    if parsed:
        return parsed
    else:
        print("error generating fields")
        return None
    

def generate_quiz(field, role, skills):
    skill_str = ", ".join(skills)
    prompt = f"""Create a short 3-question quiz (no multiple choice) to assess a beginner applicant for the role of {role} in the {field} field.
Base the questions on the following required technical skills: {skill_str}
Respond in this JSON format:
{{
  "questions": [
    {{
      "question": "Text",
      "answer": "Correct answer"
    }}
  ]
}}"""
    res = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    try:
        return json.loads(res.choices[0].message.content)["questions"]
    except:
        print("could not generate quiz.")
        return []

def generate_upskilling_roadmap(skills):
    prompt = f"""Suggest a free learning roadmap for the following skills: {', '.join(skills)}.
Include a step-by-step guide and at least one free course or learning resource per skill. Respond in this JSON format:
{{
  "roadmap": [
    {{
      "skill": "Skill Name",
      "steps": ["Step 1", "Step 2"],
      "resources": ["Free resource link"]
    }}
  ]
}}"""
    res = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    try:
        parsed = extract_json_block(res.choices[0].message.content)
        return parsed["roadmap"] if parsed and "roadmap" in parsed else []
    except:
        print("failed to generate upskilling roadmap.")
        return []

def is_answer_similar(user_answer, correct_answer):
    prompt = f"""You are a grading assistant. Compare the user's answer to the correct answer and return only \"yes\" or \"no\".

Correct answer: "{correct_answer}"
User's answer: "{user_answer}"

Is the user's answer close enough in meaning to be considered correct? Answer with \"yes\" or \"no\" only.
"""
    try:
        res = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        result = res.choices[0].message.content.strip().lower()
        return "yes" in result
    except:
        return False
