import streamlit as st
import google.generativeai as genai

# Configurar la API de Gemini
API_KEY="AIzaSyBxmabeWto76IrAZkJmfrHwWrxJ1j2uD8o"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

# Función para resumir texto con control de nivel de resumen
def resumir_texto(texto, nivel):
    modelo = genai.GenerativeModel("gemini-pro")
    prompt = f"Resume este texto en un nivel de {nivel} palabras: {texto}"
    respuesta = modelo.generate_content(prompt)
    return respuesta.text if respuesta else "Error al generar resumen."

# Interfaz con Streamlit
st.set_page_config(page_title="Resumidor de Textos", layout="centered")
st.title("📝 Resumidor de Textos con Gemini")

# Sidebar para configuración
st.sidebar.header("Configuración")
nivel_resumen = st.sidebar.slider("Nivel de resumen (cantidad de palabras aproximadas)", 20, 300, 100)

# Input del usuario
texto_usuario = st.text_area("✍️ Ingresa el texto a resumir:")

if st.button("✨ Generar Resumen"):
    if texto_usuario:
        resumen = resumir_texto(texto_usuario, nivel_resumen)
        st.subheader("📌 Resumen:")
        st.write(resumen)

        # Botón para descargar el resumen
        st.download_button("📥 Descargar Resumen", resumen, "resumen.txt", "text/plain")
    else:
        st.warning("⚠️ Por favor, ingresa un texto.")
