import streamlit as st
import json
import spacy
import pyttsx3

# Load Spacy model
nlp = spacy.load("en_core_web_sm")

# Load data from JSON file
with open('danish.json', 'r') as file:
    data = json.load(file)

# List of possible questions
questions = [
    "What is your name?",
    "What is your father's name?",
    "How old are you?",
    "What is your email?",
    "What are your hobbies?",
    "What is your birthdate?",
    "What is your address?",
    "What are you studying?",
    "Which semester are you in?",
    "What is your CGPA?",
    "When will you pass out?",
    "What languages do you speak?",
    "What are your favorite subjects?",
    "What are your favorite movies?",
    "What are your favorite books?",
    "What are your favorite foods?",
    "Who is your favorite singer?",
    "What is your favorite sport?",
    "What is your favorite animal?",
    "What is your favorite quote?",
    "Who is your favorite leader?",
    "What is your favorite programming language?",
    "What is your favorite technology?",
    "What is your job title?",
    "What skills do you have?",
    "What is your job history?",
    "What certifications do you have?",
    "Where is your hometown?",
    "What is your dream job?",
    "Do you have gf😁?",
    "What are your future goals?"
]

# Streamlit app
st.title("Personal Q&A Bot🤖")

st.write("Ask me anything about myself!")

question = st.selectbox("Select a question:", questions)

def answer_question(question):
    doc = nlp(question.lower())
    
    if any(token.lemma_ == "name" for token in doc):
        return f"My name is {data['personal_info']['name']}."
    elif any(token.lemma_ == "father" for token in doc):
        return f"My father's name is {data['personal_info']['father_name']}."
    elif any(token.lemma_ == "age" for token in doc):
        return f"I am {data['personal_info']['age']} years old."
    elif any(token.lemma_ == "email" for token in doc):
        return f"My email is {data['personal_info']['email']}."
    elif any(token.lemma_ == "hobby" for token in doc):
        return f"My hobbies are {', '.join(data['personal_info']['hobbies'])}."
    elif any(token.lemma_ == "birthdate" for token in doc):
        return f"My birthdate is {data['personal_info']['birthdate']}."
    elif any(token.lemma_ == "address" for token in doc):
        return f"My address is {data['personal_info']['address']}."
    elif any(token.lemma_ == "study" for token in doc):
        return f"I am studying {data['personal_info']['study']} at {data['personal_info']['university']}."
    elif any(token.lemma_ == "semester" for token in doc):
        return f"I am in my {data['personal_info']['semester']} semester."
    elif any(token.lemma_ == "cgpa" for token in doc):
        return f"My current CGPA is {data['personal_info']['cgpa']}."
    elif any(token.lemma_ == "passout" for token in doc):
        return f"I will pass out in {data['personal_info']['passout']}."
    elif any(token.lemma_ == "language" for token in doc):
        return f"I speak {', '.join(data['personal_info']['languages'])}."
    elif any(token.lemma_ == "favorite" for token in doc):
        if "subject" in question:
            return f"My favorite subjects are {', '.join(data['personal_info']['favorite_subjects'])}."
        elif "movie" in question:
            return f"My favorite movies are {', '.join(data['preferences']['favorite_movies'])}."
        elif "book" in question:
            return f"My favorite books are {', '.join(data['preferences']['favorite_books'])}."
        elif "food" in question:
            return f"My favorite foods are {', '.join(data['preferences']['favorite_food'])}."
        elif "singer" in question:
            return f"My favorite singer is {data['preferences']['favorite_singer']}."
        elif "sport" in question:
            return f"My favorite sport is {data['preferences']['favorite_sport']}."
        elif "animal" in question:
            return f"My favorite animal is {data['preferences']['favorite_animal']}."
        elif "quote" in question:
            return f"My favorite quote is: '{data['preferences']['favorite_quote']}'."
        elif "leader" in question:
            return f"My favorite leader is {data['preferences']['favorite_leader']}."
        elif "programming language" in question:
            return f"My favorite programming language is {data['preferences']['favorite_programming_language']}."
        elif "technology" in question:
            return f"My favorite technology is {data['preferences']['favorite_technology']}."
    elif any(token.lemma_ in ["job", "title"] for token in doc):
        return f"I work as a {data['professional_info']['job_title']}."
    elif any(token.lemma_ == "skill" for token in doc):
        return f"My skills include {', '.join(data['professional_info']['skills'])}."
    elif any(token.lemma_ in ["experience", "job history"] for token in doc):
        experience_details = "\n".join([f"{exp['position']} at {exp['company']} for {exp['years']} years - Responsibilities: {', '.join(exp['responsibilities'])}" for exp in data['professional_info']['experience']])
        return f"My job experience includes:\n{experience_details}"
    elif any(token.lemma_ == "certification" for token in doc):
        certification_details = "\n".join([f"{cert['name']} issued by {cert['issuer']} in {cert['year']}" for cert in data['professional_info']['certifications']])
        return f"My certifications are:\n{certification_details}"
    elif any(token.lemma_ == "hometown" for token in doc):
        return f"My hometown is {data['preferences']['hometown']}."
    elif any(token.lemma_ == "dream job" for token in doc):
        return f"My dream job is {data['preferences']['dream_job']}."
    elif any(token.lemma_ in ["lover", "girlfriend", "gf"] for token in doc):
        return data['preferences']['lover_or_girlfriend']
    elif any(token.lemma_ in ["future", "goal"] for token in doc):
        return f"My future goals are {', '.join(data['preferences']['future_goals'])}."
    else:
        return "I don't have an answer to that question."

def speak_answer(answer):
    engine = pyttsx3.init()
    engine.say(answer)
    engine.runAndWait()

if question:
    answer = answer_question(question)
    st.write(answer)
    speak_answer(answer)

st.sidebar.markdown("""
    <div style="background-color: ; padding: 10px; border-radius: 5px; border: 1px solid #e5b200; text-align: center;">
        <h3 style="color: black;">About the Creator</h3>
        <div style="display: flex; flex-direction: column; align-items: center;">
            <img src="https://media.licdn.com/dms/image/D4D03AQELllA0lPk4aA/profile-displayphoto-shrink_400_400/0/1715315331343?e=2147483647&v=beta&t=b1lBAk60t37uv2901yndcly7-R0t7E7AGcalM0Ho7rE" alt="Profile Picture" style="width: 120px; height: 120px; border-radius: 50%; border: 3px solid navy; margin-bottom: 15px;">
            <h2 style="color: navy; font-size: 26px;">Danish Mubashar</h2>
            <p style="color: black;">I am a Data Scientist specializing in machine learning and natural language processing, with a passion for creating innovative solutions that leverage data to solve complex problems.</p>
            <div style="margin-top: 20px;">
                <p style="color: navy; font-size: 16px; font-weight: bold;">Connect with me:</p>
                <a href="https://www.linkedin.com/in/muhammad-danish-mubashar-002b912a0/?originalSubdomain=pk" target="_blank" style="display: inline-block; background-color: #0077B5; color: #fff; text-decoration: none; padding: 10px 20px; border-radius: 5px; margin: 5px;">LinkedIn</a>
                <a href="https://github.com/DanishMUbashar" target="_blank" style="display: inline-block; background-color: #333; color: #fff; text-decoration: none; padding: 10px 20px; border-radius: 5px; margin: 5px;">GitHub</a>
                <a href="https://www.kaggle.com/danishmubashar" target="_blank" style="display: inline-block; background-color: #20BEFF; color: #fff; text-decoration: none; padding: 10px 20px; border-radius: 5px; margin: 5px;">Kaggle</a>
            </div>
            <div style="margin-top: 10px;">
                <a href="mailto:danishmubashar81@gmail.com" style="display: inline-block; background-color: #DB4437; color: #fff; text-decoration: none; padding: 10px 20px; border-radius: 5px; margin: 5px;">Email</a>
                <a href="tel:+923042193281" style="display: inline-block; background-color: #4CAF50; color: #fff; text-decoration: none; padding: 10px 20px; border-radius: 5px; margin: 5px;">Phone</a>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)