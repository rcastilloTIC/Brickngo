import random
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors

# Lista de piezas con los nombres proporcionados
piezas = ["Black_Brick_1x1", "Black_Brick_1x2", "Black_Brick_2x2", "Black_Brick_Modified_1x1_with_Stud_on_Side", "Black_Brick_Modified_1x2_with_Grille", "Black_Brick_Round_1x1", "Black_Brick_Round_2x2_with_Axle_Hole", "Black_Plate_1x2", "Black_Plate_2x2", "Black_Slope_45_2x1", "Black_Slope_45_2x2", "Black_Slope_65_2x1x2", "Black_Slope_Curved_1x2", "Bright_Green_Plant_Flower_2x2_Leaves-Angular", "Bright_Light_Orange_Brick_1x2", "Bright_Light_Orange_Brick_2x2", "Bright_Light_Orange_Slope__Curved_1x2", "Bright_Light_Yellow_Arch_1x4", "Bright_Light_Yellow_Brick_1x1", "Bright_Light_Yellow_Brick_1x2", "Bright_Light_Yellow_Brick_2x2", "Bright_Light_Yellow_Brick_Modified_1x2_with_Studs_on_1_Side", "Bright_Light_Yellow_Brick_Round_2x2_with_Axle_Hole", "Bright_Pink_Brick_1x1", "Bright_Pink_Brick_1x2", "Bright_Pink_Brick_2x2", "Bright_Pink_Slope_Curved_1x2", "Coral_Brick_1x2", "Coral_Brick_2x2", "Coral_Slope_Curved_1x2", "Dark_Azure_Brick_Modified_1x1_with_Headlight", "Dark_Blue_Brick_2x2", "Dark_Blue_Brick_Round_1x1", "Dark_Blue_Slope_45_2x2_Double", "Dark_Blue_Slope_Curved_1x2", "Dark_Green_Brick_2x2", "Dark_Green_Brick_Round_1x1", "Dark_Green_Slope_45_2x2", "Dark_Purple_Brick_2x2", "Dark_Purple_Brick_Round_1x1", "Green_Brick_2x2", "Lavender_Brick_1x2", "Lavender_Brick_2x2", "Light_Aqua_Brick_1x1", "Light_Aqua_Brick_1x2", "Light_Aqua_Slope_Inverted_45_2x1", "Medium_Azure_Brick_1x1", "Medium_Azure_Brick_1x2", "Medium_Azure_Brick_Round_1x1", "Medium_Azure_Brick_Round_2x2_with_Axle_Hole", "Medium_Azure_Slope_45_2x1", "Medium_Azure_Slope__Curved_3_x_1", "Pearl_Gold_Cone_1x1_with_Top_Groove", "Red_Brick_1x1", "Red_Brick_1x2", "Red_Brick_2x2", "Red_Brick_Modified_1x1_with_Headlight", "Red_Brick_Modified_1x1x1_2:3_with_Studs_on_Side", "Red_Brick_Round_1x1", "Red_Cone_1x1_with_Top_Groove", "Red_Plant_Flower_2x2_Rounded-Solid_Stud", "Red_Slope_33_3x1", "Red_Slope_65_2x1x2", "Red_Slope_Curved_1x2", "Red_Slope_Inverted_45_2x1", "White_Brick_1x1", "White_Brick_1x2", "White_Brick_2x2", "White_Brick_Modified_1x1_with_Stud_on_Side", "White_Brick_Modified_1x2_with_Studs_on_1_Side", "White_Brick_Round_1_x_1", "White_Brick_Round_2x2_with_Axle_Hole", "White_Slope_45_2x2", "White_Slope_Curved_1x2", "White_Slope_Curved_3x1", "White_Slope_Inverted_45_2x2_with_Hollow_Round_Bottom_Tube", "Yellow_Brick_1x1", "Yellow_Brick_1x2", "Yellow_Brick_2x2", "Yellow_Brick_Modified_1x1_with_Headlight", "Yellow_Brick_Modified_1x1_with_Stud_on_Side", "Yellow_Brick_Round_1x1", "Yellow_Plant_Flower_2x2_Rounded-Solid_Stud", "Yellow_Slope_45_2x1", "Yellow_Slope_45_2x2", "Yellow_Slope_Curved_1x2", "Yellow_Slope_Curved_2x1x1_1:3_with_Recessed_Stud", "Yellow_Slope_Curved_3x1", "Yellow_Slope_Inverted_45_2x1", "Yellow_Slope_Inverted_45_2x2_with_Flat_Bottom_Pin"]


# Modificación para añadir listado de piezas al final del PDF

# Función para dibujar el listado de piezas al final del PDF
def dibujar_listado_piezas(c, piezas):
    # Agregar una nueva página para el listado de piezas
    c.showPage()

    # Ajustes para la casilla
    x_offset = 50
    y_offset = 750  # Iniciar desde la parte superior
    cell_width = 50
    cell_height = 60
    espacio_vertical = 20

    c.setFont("Helvetica", 10)
    c.drawString(x_offset, y_offset + 20, "Listado de Piezas LEGO:")

    for pieza in piezas:
        # Dibujar la imagen de la pieza
        ruta_imagen = obtener_imagen(pieza)
        try:
            c.drawImage(ruta_imagen, x_offset, y_offset - cell_height, width=cell_width, height=cell_height, preserveAspectRatio=True)
        except Exception as e:
            c.setStrokeColor(colors.red)
            c.rect(x_offset, y_offset - cell_height, cell_width, cell_height, fill=0)
            c.setFont("Helvetica", 6)
            c.drawCentredString(x_offset + (cell_width / 2), y_offset - (cell_height / 2), "No image")

        # Dibujar el nombre de la pieza junto a la imagen
        c.setFont("Helvetica", 10)
        c.drawString(x_offset + cell_width + 10, y_offset - (cell_height / 2), pieza)

        # Ajustar la posición para la siguiente pieza
        y_offset -= (cell_height + espacio_vertical)

        # Si se llega al final de la página, añadir una nueva página
        if y_offset < 50:
            c.showPage()
            y_offset = 750  # Reiniciar el offset vertical para la nueva página


# Función para generar un cartón de bingo de 10x3 con piezas en posiciones específicas
def generar_carton():
    carton = [[''] * 10 for _ in range(3)]  # Cartón 3x10 inicialmente vacío
    piezas_disponibles = random.sample(piezas, 15)  # Elegir 15 piezas aleatorias sin repetición

    # Colocar piezas en las casillas impares de las filas impares (1, 3)
    for fila_idx in [0, 2]:  # Fila 1 y 3 (índices 0, 2)
        for col_idx in [0, 2, 4, 6, 8]:  # Columnas impares 1, 3, 5, 7, 9 (índices 0, 2, 4, 6, 8)
            carton[fila_idx][col_idx] = piezas_disponibles.pop(0)

    # Colocar piezas en las casillas pares de la fila par (2)
    for col_idx in [1, 3, 5, 7, 9]:  # Columnas pares 2, 4, 6, 8, 10 (índices 1, 3, 5, 7, 9)
        carton[1][col_idx] = piezas_disponibles.pop(0)

    return carton

# Función para obtener la ruta de la imagen correspondiente a la pieza
def obtener_imagen(pieza):
    nombre_archivo = pieza + ".jpg"  # Ejemplo: "Black_Brick_1x1" -> "Black_Brick_1x1.jpg"
    return f"imagenes/{nombre_archivo}"

# Función para dibujar un cartón en una página PDF usando imágenes y agregar un borde alrededor de cada casilla
def dibujar_carton(c, carton, x_offset, y_offset):
    # Ajustes para la casilla
    cell_width = 50  # Ancho de cada casilla (ajustado a 50 para 10 columnas)
    cell_height = 60  # Altura de cada casilla
    x = x_offset
    y = y_offset

    # Dibujar la imagen del título "bingo.jpg" sobre el cartón
    c.drawImage("imagenes/bingo.jpg", x_offset, y_offset , width=200, height=40, preserveAspectRatio=True)

    for fila in carton:
        for pieza in fila:
            # Dibujar el borde de la casilla
            c.setStrokeColor(colors.black)
            c.rect(x, y - cell_height, cell_width, cell_height, fill=0)

            if pieza:  # Solo dibujar si la casilla tiene una pieza
                # Obtener la ruta de la imagen
                ruta_imagen = obtener_imagen(pieza)
                try:
                    # Dibujar la imagen de la pieza en la casilla
                    c.drawImage(ruta_imagen, x, y - cell_height, width=cell_width, height=cell_height, preserveAspectRatio=True)
                except Exception as e:
                    # Si no se encuentra la imagen, dibujar un recuadro vacío o un mensaje de error
                    c.setStrokeColor(colors.red)
                    c.rect(x, y - cell_height, cell_width, cell_height, fill=0)
                    c.setFont("Helvetica", 6)
                    c.drawCentredString(x + (cell_width / 2), y - (cell_height / 2), "No image")

            x += cell_width  # Espacio entre columnas
        x = x_offset
        y -= cell_height  # Espacio entre filas

# Función principal para generar el PDF con los 200 cartones
def generar_pdf(nombre_archivo):
    c = canvas.Canvas(nombre_archivo, pagesize=A4)
    ancho, alto = A4

    num_cartones = 200

    for i in range(num_cartones):
        if i % 2 == 0 and i != 0:  # Añadir una nueva página después de cada 2 cartones
            c.showPage()

        # Generar dos cartones por página
        carton1 = generar_carton()
        carton2 = generar_carton()

        # Dibujar el primer cartón en la parte superior de la página
        dibujar_carton(c, carton1, 50, alto - 150)

        # Dibujar el segundo cartón en la parte inferior de la página
        dibujar_carton(c, carton2, 50, alto - 450)
    # Añadir el listado de piezas al final del PDF
    dibujar_listado_piezas(c, piezas)
    
    c.save()

# Generar el PDF con los cartones
generar_pdf("cartones_bingo_lego_10x3_con_titulo.pdf")