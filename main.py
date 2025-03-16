import streamlit as st

st.set_page_config(
    page_title="Álgebra Interactiva",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Bienvenido al Libro Interactivo de Álgebra")

st.markdown("""
### Contenido del Libro

Navega a través de las diferentes secciones utilizando el menú lateral.
""")

st.sidebar.success("Selecciona una página arriba.")

# Imagen o gráfico de bienvenida
#st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/La_G%C3%A9om%C3%A9trie.jpg/220px-La_G%C3%A9om%C3%A9trie.jpg",
#         caption="La Géométrie de Descartes (1637)",
#         width=400)

# Sección de introducción
#st.header("¿Por qué estudiar álgebra?")
#st.write("""
#[Aquí irá tu contenido introductorio en español sobre la importancia del álgebra]
#""")

# Sección de cómo usar este libro
#st.header("Cómo usar este libro interactivo")
#st.write("""
#[Aquí puedes agregar instrucciones sobre cómo navegar y usar las características interactivas del libro]
#""") 