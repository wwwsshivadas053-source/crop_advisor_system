import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# Load local knowledge

def load_json(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except:
        return []

crops = load_json("data/crops.json")
diseases = load_json("data/diseases.json")
fertilizers = load_json("data/fertilizers.json")


def get_local_context(question):

    context = []

    question = question.lower()

    # Crops

    for crop in crops:

        if crop["crop"].lower() in question:

            context.append(
                f"""
Crop: {crop['crop']}
Soil: {crop['soil']}
Season: {crop['season']}
Water Requirement: {crop['water_requirement']}
Description: {crop['description']}
"""
            )

    # Diseases

    for disease in diseases:

        if disease["crop"].lower() in question:

            context.append(
                f"""
Disease: {disease['disease']}
Crop: {disease['crop']}
Symptoms: {disease['symptoms']}
Treatment: {disease['treatment']}
"""
            )

    # Fertilizers

    for fert in fertilizers:

        if fert["fertilizer"].lower() in question:

            context.append(
                f"""
Fertilizer: {fert['fertilizer']}
Purpose: {fert['purpose']}
Usage: {fert['usage']}
"""
            )

    return "\n".join(context)


def get_chatbot_response(question, language="English"):

    try:

        local_context = get_local_context(question)

        prompt = f"""
You are AI Crop Advisor.

Use the agriculture information below whenever relevant.

Agriculture Data:
{local_context}

Rules:
1. Answer only agriculture questions.
2. Be farmer friendly.
3. Explain clearly.
4. Give practical advice.
5. Use bullet points.

Language:
{language}

Question:
{question}
"""

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:

        return f"Error: {str(e)}"