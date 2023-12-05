import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def obtener_signo(valor):
    if valor > 0:
        return '+'
    elif valor < 0:
        return '-'
    else:
        return '0'

def graficar_recta(x1, y1, x2, y2, guardar_imagen=False):
    # Calcular la pendiente (m) y la ordenada al origen (b) de la recta
    m = (y2 - y1) / (x2 - x1)
    b = y1 - m * x1

    # Generar puntos para la recta
    x_values = [x1, x2]
    y_values = [y1, y2]

    # Graficar la recta
    plt.plot(x_values, y_values, label=f'Recta: y = {m}x + {b}')

    # Marcar los puntos
    plt.scatter([x1, x2], [y1, y2], color='red', label='Puntos')

    # Etiquetas y leyenda
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()

    if guardar_imagen:
        # Guardar la gráfica como una imagen con un tamaño personalizado
        plt.savefig('grafica.png', dpi=300, bbox_inches='tight')  # dpi controla la resolución

    # Mostrar el gráfico
    plt.show()

    return m, b

def crear_pdf(nombre_archivo, imagen_path, texto):
    # Crear un lienzo (canvas) PDF
    c = canvas.Canvas(nombre_archivo, pagesize=letter)

    # Definir el tamaño de la imagen en el PDF
    ancho_imagen = 400  # Ajusta según sea necesario
    alto_imagen = 300  # Ajusta según sea necesario

    # Obtener las dimensiones de la página
    ancho_pagina, alto_pagina = letter

    # Calcular las coordenadas para centrar la imagen verticalmente
    y_coordenada = (alto_pagina - alto_imagen) / 2

    # Agregar imagen con dimensiones personalizadas y coordenadas centradas
    c.drawInlineImage(imagen_path, (ancho_pagina - ancho_imagen) / 2, y_coordenada, width=ancho_imagen, height=alto_imagen)

    # Agregar texto
    c.drawString(100, 50, texto)  # Ajusta las coordenadas según sea necesario

    # Guardar el PDF
    c.save()

# Ejemplo de uso para graficar y crear un PDF
x1, y1 = 1, 2
x2, y2 = 4, 6

# Graficar la recta y obtener la ecuación, guardando la imagen
pendiente, ordenada_al_origen = graficar_recta(x1, y1, x2, y2, guardar_imagen=True)

# Crear un PDF con información personalizada
nombre_pdf = "output.pdf"
imagen_path = "grafica.png"  # Utilizar la imagen guardada
texto_personalizado = f"Ecuación de la recta: y = {pendiente}x + {ordenada_al_origen}"

crear_pdf(nombre_pdf, imagen_path, texto_personalizado)
