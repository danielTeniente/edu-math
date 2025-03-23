import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Descartes y El Plano Cartesiano", page_icon="📐")

st.title("René Descartes y El Plano Cartesiano")
st.header("René Descartes (1596-1650)")
# Imagen de Descartes
st.image("https://upload.wikimedia.org/wikipedia/commons/7/73/Frans_Hals_-_Portret_van_Ren%C3%A9_Descartes.jpg",
         caption="René Descartes",
         width=300)
# add the source of the image
st.caption("Fuente: [Wikipedia](https://en.wikipedia.org/wiki/Ren%C3%A9_Descartes)")

# Sección sobre Descartes
st.markdown("""
La vida tiene varias sorpresas, 
Descartes se graduó como abogado, aunque nunca ejerció.*         
Y tenemos que agradecerle porque
su huella en la filosofía y la matemática es enorme.
            
Aunque muchos conozcan su famosa frase "Cogito, ergo sum" (Pienso, luego existo), 
para mí, Descartes es un héroe de la matemática. Su gran aporte es la geometría analítica.
            
La geometría analítica es mi herramienta favorita para enteder
cualquier problema matemático. El plano cartesiano te permite
visualizar las ecuaciones y jugar con ellas.
       
\* *Nota: Esto me recuerda a Newton, quien consideraba la física como un pasatiempo 
y la biblia como su vocación. En el caso de Descartes, su vocación era el pensamiento
y la abogacía una mera excusa.* 
"""
)


# El Plano Cartesiano
st.header("El Plano Cartesiano")
st.markdown("""
El plano cartesiano, llamado así en honor a Descartes (él no le dio ese nombre),
es un espacio de dos dimensiones representado por dos líneas (x,y)
que son perpendiculares y establecen un punto de origen (0,0) cuando se cruzan.
            
Estas líneas se conocen como eje de coordenadas.
            
Cada eje está dividido en distintas unidades y
como un tablero, podemos usar este plano para representar puntos donde cada uno
tiene una posición que corresponde a un par de números (x,y).
            
Generalmente, el eje horizontal (x) se conoce como eje de las abscisas y el eje vertical (y) como eje de las ordenadas.
Los ejes no siempre van a tener las mismas letras, pero el concepto se mantiene.

Ahora vamos a empezar posicionando algunos puntos en el plano.
""")

# Plano Cartesiano Interactivo
st.subheader("Plano Cartesiano Interactivo")

# Crear tres columnas para los puntos
st.markdown("""
Tienes tres puntos para mover.
Cada punto tiene una coordenada (x,y) que lo posiciona en el plano.
Puedes cambiar el valor de cada coordenada para ver cómo se comporta el punto.
""")
st.markdown("**Coordenadas de los Puntos**")
col1, col2, col3 = st.columns(3)

# Punto A
with col1:
    st.markdown("**Punto A**")
    x_point_a = st.slider("X del punto A", -10, 10, 2)
    y_point_a = st.slider("Y del punto A", -10, 10, 3)

# Punto B
with col2:
    st.markdown("**Punto B**")
    x_point_b = st.slider("X del punto B", -10, 10, -4)
    y_point_b = st.slider("Y del punto B", -10, 10, 1)

# Punto C
with col3:
    st.markdown("**Punto C**")
    x_point_c = st.slider("X del punto C", -10, 10, 0)
    y_point_c = st.slider("Y del punto C", -10, 10, -2)


# Crear el plano cartesiano con Matplotlib
fig, ax = plt.subplots(figsize=(8, 6))

# Configurar el aspecto del plano
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.grid(True, linestyle='--', alpha=0.7)
ax.axhline(y=0, color='k', linestyle='-', linewidth=1)
ax.axvline(x=0, color='k', linestyle='-', linewidth=1)
ax.set_aspect('equal')

# Agregar los tres puntos con diferentes colores y etiquetas
ax.scatter(x_point_a, y_point_a, color='red', s=100, label='Punto A')
ax.text(x_point_a, y_point_a + 0.5, 'A', ha='center', va='bottom')

ax.scatter(x_point_b, y_point_b, color='blue', s=100, label='Punto B')
ax.text(x_point_b, y_point_b + 0.5, 'B', ha='center', va='bottom')

ax.scatter(x_point_c, y_point_c, color='green', s=100, label='Punto C')
ax.text(x_point_c, y_point_c + 0.5, 'C', ha='center', va='bottom')

# Configurar etiquetas y título
ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.set_title('Plano Cartesiano')
ax.legend()

# Crear dos columnas para el plot y las coordenadas
col1, col2 = st.columns([1, 2])

# Mostrar las coordenadas en la primera columna
with col1:
    st.markdown("**Coordenadas Actuales**")
    st.markdown(f"""
    - Punto A: $({x_point_a}, {y_point_a})$
    - Punto B: $({x_point_b}, {y_point_b})$
    - Punto C: $({x_point_c}, {y_point_c})$
    """)

# Mostrar el plano en la segunda columna
with col2:
    st.pyplot(fig)

# Ejercicios interactivos
st.header("Ejercicios Interactivos")
st.markdown("""
* ¿Qué pasa cuando todos los puntos tienen los mismos valores de coordenadas?
* ¿Qué pasa cuando todos los puntos tienen la misma coordenada x, pero distinta coordenada y?
* ¿Qué pasa cuando todos los puntos tienen la misma coordenada y, pero distinta coordenada x?
* ¿Qué pasa cuando A es (1,1), B es (2,2) y C es (3,3)?
* ¿Qué pasa cuando un punto tiene sólo coordenadas positivas?
* ¿Qué pasa cuando un punto tiene sólo coordenadas negativas?
* ¿Qué pasa cuando un punto tiene como coordenadas (x positivo, y negativo)?
* ¿Qué pasa cuando un punto tiene como coordenadas (x negativo, y positivo)?
""") 