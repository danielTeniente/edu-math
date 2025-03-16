# Libro Interactivo de Álgebra

Este es un libro interactivo creado con Streamlit para enseñar conceptos de álgebra, con un enfoque especial en René Descartes y el plano cartesiano.

## Requisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

## Instalación

1. Crea un entorno virtual (opcional pero recomendado):
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

## Ejecutar la aplicación

Para iniciar la aplicación, ejecuta:
```bash
streamlit run main.py
```

La aplicación se abrirá automáticamente en tu navegador predeterminado.

## Estructura del Proyecto

```
.
├── main.py                 # Página principal
├── pages/                  # Páginas adicionales
│   └── 1_📐_Descartes_y_El_Plano_Cartesiano.py
├── requirements.txt        # Dependencias del proyecto
└── README.md              # Este archivo
```

## Personalización del Contenido

Para modificar el contenido:

1. Edita los archivos .py en la carpeta principal y en la carpeta pages/
2. Busca las secciones marcadas con [Aquí irá tu contenido...] y reemplázalas con tu propio contenido en español
3. Puedes agregar más páginas en la carpeta pages/ siguiendo el formato de nomenclatura: número_emoji_nombre.py

## Características

- Interfaz interactiva con Streamlit
- Visualización del plano cartesiano con Plotly
- Ejercicios interactivos
- Soporte para múltiples páginas
- Diseño responsivo 