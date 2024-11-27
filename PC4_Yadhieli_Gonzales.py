# Este código sirve para instalar Streamlit en tu computadora y hacer un primer programa en Streamlit.
# Pero se ejecuta en la terminal de tu computadora, no en Jupyter Notebook.

# Primero, debes abrir el folder donde se encuentra tu archivo de Python en la terminal de tu computadora.
# Para hacerlo, debes escribir el siguiente comando en la terminal de tu computadora
# cd ruta_de_tu_carpeta
# o desde Visual Studio Code, seleccionas Open Folder y seleccionas la carpeta 
# donde se encuentra tu archivo de Python

# Segundo, debes instalar un entorno virtual en tu computadora.
# python -m venv .venv
# Este comando crea un entorno virtual en la carpeta actual con el nombre .venv.

# Para activar el entorno virtual, debes escribir el siguiente comando en la terminal de tu computadora
# .venv\Scripts\activate
# Para desactivar el entorno virtual, debes escribir el siguiente comando en la terminal de tu computadora
# deactivate

# Tercero, debes instalar Streamlit en tu entorno virtual.
# pip install Streamlit 

# Cuarto, puedes abrir el tutorial de Streamlit en tu navegador.
# streamlit hello o python -m streamlit hello

# Quinto, debes abrir el archivo de Python en la terminal de tu computadora.
# Este comando sirve para ejecutar un script de Python en Streamlit.
# Pero se ejecuta en la terminal de tu computadora, no en Jupyter Notebook.
# OJO: Debes antes tener instalado Streamlit en tu computadora, debes antes definir la ruta de tus archivos y 
##     tener un script de Python (your_script.py) que quieras ejecutar en Streamlit.
#  streamlit run your_script.py o python -m streamlit run your_script.py

# Este código sirve para hacer un primer programa en Streamlit.
import streamlit as st

# Creamos una barra lateral
sidebar = st.sidebar

# Si usas el siguiente código mostrará un título en la aplicación Streamlit. 
# st.title("Nombre de tu blog"): Esta línea está creando un título en la aplicación web.
# Pero, a diferencia de st.markdown, el texto estará alineado a la izquierda y no podrás cambiar el color del texto.

# La función st.markdown permite centrar y agrandar la letra del título de la web en Streamlit.
st.markdown("<h1 style='text-align: center;'>Quemándome las pestañas con Python. ¿Cómo amé algo que empecé odiando?</h1>", unsafe_allow_html=True)

# <h1 style='text-align: center;'>Nombre de tu blog</h1>: Esto es una cadena de código HTML. 
# La etiqueta <h1> se utiliza para el encabezado principal de una página web, y 
# el atributo style se utiliza para agregar estilos CSS. 
# En este caso, el texto está alineado al centro (text-align: center;). 
# El texto dentro de las etiquetas <h1> ("Aquí escribe un nombre creativo para tu blog") es el contenido del encabezado.

# unsafe_allow_html=True: Este es un argumento opcional en la función markdown. 
# Por defecto, streamlit no permite HTML en el texto de Markdown por razones de seguridad. 
# Sin embargo, establecer unsafe_allow_html en True permite el uso de HTML.

# Creamos dos columnas separadas para la imagen y el texto
col1, col2 = st.columns(2)

# col1, col2 = st.columns(2): Esta línea está creando dos columnas en la interfaz de usuario de la aplicación web. 
# La función st.columns toma un número entero como argumento que especifica el número de columnas que se deben crear. 
# Las columnas creadas se asignan a las variables col1 y col2.

# En la primera columna colocamos la imagen
col1.image("Foto.jpg", caption='Yadhielí Gonzales Palma', width=300)


# col1.image("ellie.png", caption='Ellie', width=300): Esta línea está colocando una imagen en la primera columna (col1). 
# La función image toma como primer argumento la ruta de la imagen que se va a mostrar. 
# En este caso, la imagen es "ellie.png". 
# El argumento caption se utiliza para proporcionar un pie de foto a la imagen, en este caso 'Ellie'. 
# El argumento width se utiliza para especificar el ancho de la imagen, en este caso 300 píxeles.

texto_0 = """
¡Hola! Me llamo Yadhielí Enalith Gonzales Palma (nombre complicado), soy una estudiante de sexto ciclo de la carrera de Publicidad en la Pontifica Universidad Católica del Perú. Algo que me gusta de mi carrera es que, puedes encontrar detalles que otros no pueden percibir con facilidad, es mirar el mundo con otros ojos y decir ¡Hey, no lo viste venir!, me gusta explorar nuevas alternativas, no solo para poder vender un producto, sino también poder hacerlo memorable. Como dice Rafiki ‘mira más allá de lo que ven tus ojos’.
"""
col1.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto_0}</div>", unsafe_allow_html=True)

# En la segunda columna colocamos el texto: Debe contener una presentación de ustedes
# Deben presentarse: ¿Quién eres?, ¿De dónde eres?, ¿Qué estudias?, ¿Qué te gusta de tu carrera?, 
# ¿Qué te gustaría hacer en el futuro?, ¿Qué te gusta hacer en tu tiempo libre?

texto = """
SI hablará de mis gustos personales, diría que soy una persona a la que le gusta cualquier tipo de actividad que involucre la creatividad, soy directa y honesta. Me gustan los animales en general, (aunque eso sería un poco hipócrita ya que me dan miedo los bichos), tengo 3 gatos llamados Romeo, Micho y Mushu, 6 perros llamados Lola, Lily, Puki, Zenitsu, Niko y Tiffany, he tenido un ganso llamado Lucio, dos conejos llamados Haru y Dan Oh, y un cuy llamado Alfonso. Me gusta el color azul porque me recuerda a mi mamá, pero los colores que más amo son el coral, amarrillo y negro. Me gusta escribir en journals y diarios,ahí cuento sobre mis mejores días y experiencias que no quiero olvidar. Me gustan las películas del año 2000, sobretodo ‘Fat Albert’, ‘Van Helsing’ y ‘Balto’, también las películas indú. Mi playlist de spotify tiene un poco de todo, desde cumbias hasta música clásica, aunque mis artistas favoritos son Lindsey Stirling, Aurora y One Direction.
En el futuro, me gustaría poder tener un trabajo estable, especialmente en el equipo creativo o de producción, y formar parte de alguna agencia. Abrir una página web para poder vender la papelería, recursos e ilustraciones que realizo. También desearía poder abrir otras sedes de SHIBUI, mi tienda de comida coreana en provincia, y me gustaría poder escribir un libro contando mi experiencia de cómo es que decidí seguir con vida. Por último, quisiera ayudar más a mi familia.
En mi tiempo libre, me gusta hacer de todo un poco. Leo mangas o manhwas, especialmente si son del género romántico, amo sentirme enamorada. Veo películas que tengo en mi lista, y si se da el caso, me preparo un bowl gigante de ramén, edito algunos videos para subirlos a mi cuenta de TikTok, escribo en mi journal mientras escucho música, juego videojuegos como Fortnite, Minecraft o Call Of Duty. Cuando me siento demasiado ansiosa, suelo preparar cupcakes para mi familia, lo gracioso es que me salen más ricos cuando estoy deprimida. 
"""

# Las comillas triples (""") en Python se utilizan para definir cadenas multilínea.
# Mostramos el texto
col2.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto}</div>", unsafe_allow_html=True)

# <div style='text-align: justify; font-size: 15px;'>{texto}</div>: Esta es una cadena de código HTML. 
# La etiqueta <div> se utiliza para agrupar contenido en HTML. 
# En este caso, el texto está justificado (text-align: justify;). 
# El tamaño de la fuente se establece en 15 píxeles (font-size: 15px;).
# El texto dentro de las etiquetas <div> es la variable texto.

# f"": Esta es una cadena de formato en Python. 
# Permite la interpolación de variables, lo que significa que puedes insertar el valor de una variable directamente en la cadena. 
# En este caso, {texto} se reemplaza por el valor de la variable texto.

# Debajo de las columnas colocamos un subtítulo que describa tu experiencia aprendiendo a programar
# Deben presentar tu experiencia aprendiendo a programar: ¿Cómo te sentiste al principio?, 
# ¿Qué te ha enseñado la programación?, ¿Qué te gusta de programar?, 
# ¿Qué te gustaría hacer con la programación en el futuro? 


# Agregamos un subtítulo
st.markdown("<h2 style='text-align: center;'>Mi experiencia aprendiendo a programar 💻</h2>", unsafe_allow_html=True)

# <h2 style='text-align: center;'>Mi experiencia aprendiendo a programar 💻</h2>: Esta es una cadena de código HTML.
# La etiqueta <h2> se utiliza para el encabezado secundario de una página web.
# El texto está centrado (text-align: center;).
# El texto dentro de las etiquetas <h2> ("Mi experiencia aprendiendo a programar 💻") es el contenido del encabezado
# unsafe_allow_html=True: Este es un argumento opcional en la función markdown.
# Por defecto, streamlit no permite HTML en el texto de Markdown por razones de seguridad.
# Sin embargo, establecer unsafe_allow_html en True permite el uso de HTML.
# Puedes agregar emojis en el texto de Markdown utilizando códigos de emoji.

# Agregar un  texto para la respuesta
texto_2 = """
Al inicio del semestre, ignorantemente creí que Python no me serviría para nada. Aproximadamente, hasta la cuarta semana, me di cuenta de que sería complicado para mí, porque por más que intentaba entender no llegaba a nada. Me sentí frustrada y desanimada, incluso sentí que sería un curso pesado en el cual no me podría aportar nada a mi formación profesional, pero me equivoqué. 
Pasada ya la primera PC, me dije a mi misma que debía esforzarme más, mis resultados no superaban mis expectativas. En ese punto, quería aprender y enfocarme más, entendí que siempre hay más formas para poder resolver problemas, de manera práctica e incluso fácil. Empecé viendo tutoriales y cursos gratuitos en YouTube para poder comprender y sumar lo avanzado en clase. Puedo decir que, para las PC’s me quemé las pestañas, no por irresponsabilidad o por procrastinadora, sino porque quería que mi código fuera perfecto (no hay código perfecto, lo aprendí tarde). Los resultados me motivaron muchísimo, había evolucionado la manera en la que podía resolver los problemas y me tomaba menos tiempo poder realizarlos. 
Si podría mencionar una cosa que no me gusta de la programación es la interfaz de Visual Studio Code, de por sí, es el campo en el que realizas tus códigos, pero sigue sin gustarme. Sinceramente, prefiero Google Collab, ya que muestra un espacio más amigable. No podría quejarme de algo específico de la programación, porque es interesante cómo cada pequeña cosa te da un resultado asombroso. 
En el futuro, estaría encantada de poder diseñar y programar páginas webs. Estas variarán en diferentes ámbitos. No necesariamente algo apegado a mi carrera, por ejemplo, desearía poder crear una página titulada ‘Adopta tu perrihijo’, páginas que me ayuden a contar historias para y todo el mundo la pueda ver, páginas con un interfaz o diseño creativo.
Finalmente, estoy agradecida. Gracias al curso, y los aportes del docente y la JP Luisa, he logrado comprender y avanzar en la programación. Han despertado el interés en mí, incluso quiero seguir llevando cursos externos para poder mejorar en mis habilidades, explanear mis conocimientos y crear proyectos únicos. Quiero seguir aprendiendo a programar. 
"""

# Mostramos el texto
st.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto_2}</div>", unsafe_allow_html=True)

# <div style='text-align: justify; font-size: 15px;'>{texto_2}</div>: Esta es una cadena de código HTML.
# La etiqueta <div> se utiliza para agrupar contenido en HTML.
# En este caso, el texto está justificado (text-align: justify;).
# El tamaño de la fuente se establece en 15 píxeles (font-size: 15px;).
# El texto dentro de las etiquetas <div> es la variable texto_2.
# f"": Esta es una cadena de formato en Python.
# Permite la interpolación de variables, lo que significa que puedes insertar el valor de una variable directamente en la cadena.
# En este caso, {texto_2} se reemplaza por el valor de la variable texto_2.

# Ahora agregamos un video a mi blog donde explico algún tema de las clases
# Agregamos un subtítulo
st.markdown("<h2 style='text-align: center;'>Explicación de dos temas vistos en clases 📚</h2>", unsafe_allow_html=True)
# <h2 style='text-align: center;'>Explicación de un tema de las clases 📚</h2>: Esta es una cadena de código HTML
# La etiqueta <h2> se utiliza para el encabezado secundario de una página web.
# El texto está centrado (text-align: center;).
# El texto dentro de las etiquetas <h2> ("Explicación de un tema de las clases 📚") es el contenido del encabezado
# unsafe_allow_html=True: Este es un argumento opcional en la función markdown.

# Agregamos un video a la aplicación web ( menor a 20 MB)
st.video("Video_01.mp4")
# st.video("ppc-2024-1.mp4"): Esta línea está agregando un video a la aplicación web.


# Agregamos un enlace a la página web donde está el video.
enlace = f'<a href="https://drive.google.com/drive/folders/1h4peUL70G5xrKNDe0Pumlyy5PsQ0VeeB?usp=sharing"><button>Clase: Bucles en Python</button></a>'
st.markdown(enlace, unsafe_allow_html=True)
# f'<a href="URL" target="_blank"><button>Nombre</button></a>':
# La etiqueta <a> se utiliza para crear un enlace en HTML.
# El atributo href se utiliza para especificar la URL de destino del enlace.
# El atributo target="_blank" se utiliza para abrir el enlace en una nueva pestaña del navegador.
# La etiqueta <button> se utiliza para crear un botón en HTML.
# El texto dentro de las etiquetas <button> ("Nombre creativo para el botón") es el contenido del botón.
# La variable enlace contiene la cadena de código HTML para el enlace y el botón.

#APara el segundo video
# Agregamos un video a la aplicación web ( menor a 20 MB)
st.video("Video_02.mp4")
# st.video("ppc-2024-1.mp4"): Esta línea está agregando un video a la aplicación web.


# Agregamos un enlace a la página web donde está el video.
enlace = f'<a href="https://drive.google.com/drive/folders/1Eyrc0RTn2AVoELrOgkleOdBzWQP6i1jX?usp=sharing"><button>Clase: ¿Para qué se utiliza WordCloud?</button></a>'
st.markdown(enlace, unsafe_allow_html=True)

# Agregamos un subtítulo en la barra lateral
sidebar.markdown("<h1 style='text-align: center;'>Gráficos utilizados en prácticas</h1>", unsafe_allow_html=True)

# <h1 style='text-align: center;'>Los análisis de Ellie</h1>: Esta es una cadena de código HTML.
# La etiqueta <h1> se utiliza para el encabezado principal de una página web.
# El texto está centrado (text-align: center;).
# El texto dentro de las etiquetas <h1> ("Los análisis de Ellie") es el contenido del encabezado.

# Creamos una lista de gráficos
graficos = ['Nube de Palabras', 'Goles Anotados por el equipo Lecce como visitante y como local', 'Promedio de Tarjetas Rojas como equipo Visitante']

# Creamos un cuadro de selección en la barra lateral
grafico_seleccionado = sidebar.selectbox('Selecciona un gráfico', graficos)
# El cuadro de selección se crea con la función selectbox.
# El primer argumento es el texto que se muestra en el cuadro de selección.
# El segundo argumento es una lista de opciones que se pueden seleccionar.
# En este caso, las opciones son los elementos de la lista graficos.
# La opción seleccionada se asigna a la variable grafico_seleccionado.
# La variable grafico_seleccionado se utiliza para mostrar el gráfico correspondiente en la aplicación web.
# La función selectbox se utiliza para crear un cuadro de selección en la barra lateral.

# Mostramos el gráfico seleccionado
if grafico_seleccionado == 'Nube de Palabras':
    sidebar.markdown("<div style='text-align: justify; font-size: 20px;'>Gráfico realizado con la librería WordCloud. Para la realización de dicho gráfico, se utilizó el archivo de texto ‘A donde va el viento’. Después de una depuración total del archivo txt, se creó un diccionario vacío y un bucle for para contabilizar cuántas veces se repite una palabra. Como resultado, se crea una nube de palabras, en la que mientrás más veces se repita una palabra, más grande es esta en el gráfico.</div>", unsafe_allow_html=True)
    sidebar.image("Nube_Palabras.png", caption='Nube de Palabras con WordCloud', width=500)
    pass
elif grafico_seleccionado == 'Goles Anotados por el equipo Lecce como visitante y como local':
    sidebar.markdown("<div style='text-align: justify'>Gráfico realizado con la librería Matplotlib. Para la realización de dicho gráfico, se utilizó una base de datos de la primera división de la Liga Italiana (Serie A). Luego de una filtración del equipo Lecce, se calculó la frecuencia de goles anotados tanto como equipo local y visitante. Como resultado, mediante la librería Matplotlib, se crea un gráfico de barras evidenciado los goles anotados por Lecce..</div>", unsafe_allow_html=True)
    sidebar.image("Lecce.png", caption='Goles Anotados por el equipo Lecce', width=500)
    pass
elif grafico_seleccionado == 'Promedio de Tarjetas Rojas como equipo Visitante':
    sidebar.markdown("<div style='text-align: justify'>Gráfico realizado con la librería Matplotlib y Seaborn. Para la realización de dicho gráfico, se filtraron las tarjetas rojas de los equipos como visitantes para, posteriormente, ser promediados. Finalmente, se crea el gráfico con un diseño colorido hecho por Seaborn con la paleta ‘Spectral’..</div>", unsafe_allow_html=True)
    sidebar.image("Tarjetas_Rojas.png", caption='Promedio de Tarjetas Rojas', width=500)
    pass

# if grafico_seleccionado == 'Gráfico de Macroareas': Esta línea verifica si la opción seleccionada es 'Gráfico de Macroareas'.
# Si es así, se ejecuta el código dentro del bloque if.
# En este caso, se muestra un texto y una imagen correspondientes al gráfico de Macroareas.
# El texto y la imagen se muestran en la barra lateral.
# La función markdown se utiliza para mostrar el texto en la barra lateral.
# La función image se utiliza para mostrar la imagen en la barra lateral.
# El argumento caption se utiliza para proporcionar un pie de foto a la imagen.
# El argumento width se utiliza para especificar el ancho de la imagen.
# La palabra clave pass se utiliza para indicar que no se debe hacer nada en caso de que la opción seleccionada no sea 'Gráfico de Macroareas'.

# Agregamos un subtítulo
st.markdown("<h2 style='text-align: center;'>Mis Mascotas 🌟</h2>", unsafe_allow_html=True)

# Creamos dos columnas separadas para la imagen y el texto
col1, col2, col3 = st.columns(3)
#Agregamos más fotos
col1.image("Niko.png", caption='Niko', width=200)
col2.image("Zenitsu.png", caption='Zenitsu', width=200)
col3.image("Micho.png", caption='Micho', width=200)

st.image("Mushu.png", caption='Mushu', width=300)
st.image("Martin.png", caption='Martin', width=300)