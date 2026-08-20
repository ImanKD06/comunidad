import ollama


# ==========================================
# INCIDENTS
# ==========================================

def analyze_incident(description: str):

    prompt = f"""
Clasifica esta incidencia de una comunidad de vecinos:

{description}

Devuelve:
- categoría
- prioridad
- recomendación
"""

    response = ollama.chat(
        model="llama3.1:8b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return {
        "category": "IA",
        "priority": "Analizado",
        "recommendation": response["message"]["content"]
    }


# ==========================================
# MINUTES
# ==========================================

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

    response = ollama.chat(
        model="llama3.1:8b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]