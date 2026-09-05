import os
import json
from google import genai
from google.genai import types

def obtener_cliente():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("Falta la variable GEMINI_API_KEY")
    return genai.Client(api_key=api_key)

def analizar_incidencia_ia(descripcion: str) -> dict:
    try:
        client = obtener_cliente()

        prompt = f"""
        Eres un asistente experto para administradores de fincas y comunidades de propietarios.
        Analiza la siguiente incidencia reportada por un vecino:
        "{descripcion}"

        Debes responder ÚNICAMENTE con un objeto JSON válido con la siguiente estructura exacta:
        {{
            "categoria": "Fontanería | Electricidad | Ascensores | Limpieza | Cerrajería | Obras y Reformas | General",
            "prioridad": "Alta | Media | Baja",
            "recomendacion": "Explicación breve de 2-3 frases con los pasos inmediatos sugeridos a seguir"
        }}
        """

        response = client.models.generate_content(
            model="gemini-3.6-flash",  # <--- ACTUALIZADO
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
            ),
        )

        return json.loads(response.text)

    except Exception as e:
        print(f"Error procesando IA: {str(e)}")
        return {
            "categoria": "General",
            "prioridad": "Media",
            "recomendacion": f"No se pudo completar el análisis automático. Detalle: {str(e)}"
        }

def redactar_acta_ia(
    title: str,
    date: str = "",
    attendees: str = "",
    topics: str = "",
    agreements: str = "",
    community_name: str = ""
) -> str:
    try:
        client = obtener_cliente()

        prompt = f"""
        Eres un secretario y administrador de fincas profesional.
        Redacta el texto formal completo de un ACTA DE REUNIÓN DE COMUNIDAD DE PROPIETARIOS.
        
        REGLA IMPORTANTE:
        - NO uses corchetes, plantillas ni texto como "[Insertar Localidad]", "[Insertar Hora]", "[Insertar Dirección]".
        - Integra de forma fluida y directa la información proporcionada. Si un dato secundario (como la hora o el lugar exacto) no se especifica, redacta la frase de forma natural omitiéndolo o asumiendo el formato estándar del documento sin dejar marcas de edición.

        DATOS DE LA REUNIÓN:
        - Comunidad: {community_name if community_name else "Residencia Santa Rosa"}
        - Título / Tipo de Junta: {title}
        - Fecha: {date if date else "05/09/2026"}
        - Asistentes: {attendees if attendees else "No especificado"}
        - Orden del día / Temas: {topics if topics else "No especificado"}
        - Acuerdos alcanzados: {agreements if agreements else "No especificado"}

        Estructura la respuesta en:
        1. CONVOCATORIA Y ASISTENCIA
        2. ORDEN DEL DÍA
        3. ACUERDOS ADOPTADOS
        4. CIERRE Y FIRMAS
        """

        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt,
        )

        return response.text
    except Exception as e:
        print(f"Error redactando acta: {str(e)}")
        return f"Error al generar el acta con IA: {str(e)}"


analizar_incidencia = analizar_incidencia_ia
redactar_acta = redactar_acta_ia