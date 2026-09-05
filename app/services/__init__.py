import os
from google import genai

client = genai.Client()

def analyze_incident(description: str):
    prompt = f"""
Clasifica esta incidencia de una comunidad de vecinos:

{description}

Devuelve:
- categoría
- prioridad
- recomendación
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return {
        "category": "IA",
        "priority": "Analizado",
        "recommendation": response.text
    }


def generate_minute(data):
    prompt = f"""
Redacta un acta profesional para una comunidad de vecinos.

Título:
{data.title}

Asistentes:
{data.attendees}

Temas tratados:
{data.topics}

Acuerdos:
{data.agreements}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text