import streamlit as st

st.set_page_config(
    page_title="Importancia del Álgebra",
    page_icon="📝",
    layout="wide"
)

# Configuración de tamaños de fuente en la barra lateral
st.sidebar.header("Configuración de Visualización")
text_size = st.sidebar.select_slider(
    "Tamaño del texto",
    options=["pequeño", "normal", "grande", "muy grande"],
    value="normal"
)

equation_size = st.sidebar.select_slider(
    "Tamaño de ecuaciones",
    options=["pequeño", "normal", "grande", "muy grande"],
    value="normal"
)

# Diccionario de tamaños de fuente para texto
text_sizes = {
    "pequeño": "14px",
    "normal": "16px",
    "grande": "18px",
    "muy grande": "20px"
}

# Diccionario de tamaños para ecuaciones
equation_sizes = {
    "pequeño": r"\small",
    "normal": r"\normalsize",
    "grande": r"\large",
    "muy grande": r"\huge"
}

# Función para envolver texto con el tamaño de fuente seleccionado
def styled_text(text):
    return f'<div style="font-size: {text_sizes[text_size]};">{text}</div>'

# Función para envolver ecuaciones con el tamaño seleccionado
def styled_equation(eq):
    return f"{equation_sizes[equation_size]} {eq}"

st.title("La Importancia del Álgebra")

# Sección 1: Introducción
st.header("¿Por qué aprender álgebra?")
st.markdown(styled_text("""

El álgebra es importante porque nos permite ver
relaciones numéricas en lugar de limitarnos a problemas
con números específicos.
Nos permite ver el bosque y no los árboles.
**Entender lo general y no distraernos en lo particular**.
         
En el pasado, las relaciones numéricas eran
**representadas en palabras**. 

Por ejemplo, el
libro: El Hombre más rico de Babilonia,* 
ofrece el siguiente consejo para ahorrar:

\* *Nota: El libro mencionado no es antiguo ni matemático, pero 
muestra una relación numérica de forma práctica.*

Debes ahorrar el diez por ciento del dinero que ganes.

Esto significa que debes multiplicar el dinero que ganas por diez
y dividirlo para cien. 

* Entonces, si consigues **\$100**, debes ahorrar **\$10**.
         
* Y si ganas **\$200**, debes ahorrar **\$20**.

Pero no importa que tan grande o que tan pequeño sea la cantidad que ganes,
la relación con el ahorro no va a cambiar.

Así que esto se puede representar de forma general como una ecuación algebraica:
"""), unsafe_allow_html=True)

st.latex(styled_equation(r"\text{ahorro} = 10\% \times \text{dinero}"))
         
st.markdown(styled_text("""
Y como escribir esto en palabras es bastante cansado,
sobre todo si consideramos que los primeros matemáticos
resolvían estos problemas usando su puño y no una máquina,
es más fácil utilizar letras:
"""), unsafe_allow_html=True)
      
st.latex(styled_equation(r"a = 0.10 d"))

st.markdown(styled_text("""

Donde:
- **a** representa el ahorro
- y **d** representa cualquier cantidad de dinero ganado

"""), unsafe_allow_html=True)

st.markdown(styled_text("""

Finalmente, existe un acuerdo entre matemáticos para
darle cierto nombre a las cantidades que usan.

En este ejemplo, **a** es una cantidad (variable) que depende de otra,
es decir, el ahorro viene del dinero que se gana, no puede haber ahorro
si no se gana dinero primero. Una variable no existe sin la otra.

Así que lo más normal sería representar esta relación así:

"""), unsafe_allow_html=True)

st.latex(styled_equation(r"y = 0.10 x"))

st.markdown(styled_text("""

Donde:
- **y** representa el ahorro
- y **x** representa cualquier cantidad de dinero ganado

"""), unsafe_allow_html=True)

st.markdown(styled_text("""
Pero es sólo una convención. No está escrito en piedra.
Usar una convención facilita entender lo que otros matemáticos
hacen sin necesidad de pensar demasiado.

"""), unsafe_allow_html=True)



