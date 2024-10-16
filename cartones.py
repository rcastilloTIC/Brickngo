import random
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors

# Lista de piezas con los nombres proporcionados
# List of pieces with the provided names
piezas = ["Black_Brick_1x1", "Black_Brick_1x2", "Black_Brick_2x2", "Black_Brick_Modified_1x1_with_Stud_on_Side", "Black_Brick_Modified_1x2_with_Grille", "Black_Brick_Round_1x1", "Black_Brick_Round_2x2_with_Axle_Hole", "Black_Plate_1x2", "Black_Plate_2x2", "Black_Slope_45_2x1", "Black_Slope_45_2x2", "Black_Slope_65_2x1x2", "Black_Slope_Curved_1x2", "Bright_Green_Plant_Flower_2x2_Leaves-Angular", "Bright_Light_Orange_Brick_1x2", "Bright_Light_Orange_Brick_2x2", "Bright_Light_Orange_Slope__Curved_1x2", "Bright_Light_Yellow_Arch_1x4", "Bright_Light_Yellow_Brick_1x1", "Bright_Light_Yellow_Brick_1x2", "Bright_Light_Yellow_Brick_2x2", "Bright_Light_Yellow_Brick_Modified_1x2_with_Studs_on_1_Side", "Bright_Light_Yellow_Brick_Round_2x2_with_Axle_Hole", "Bright_Pink_Brick_1x1", "Bright_Pink_Brick_1x2", "Bright_Pink_Brick_2x2", "Bright_Pink_Slope_Curved_1x2", "Coral_Brick_1x2", "Coral_Brick_2x2", "Coral_Slope_Curved_1x2", "Dark_Azure_Brick_Modified_1x1_with_Headlight", "Dark_Blue_Brick_2x2", "Dark_Blue_Brick_Round_1x1", "Dark_Blue_Slope_45_2x2_Double", "Dark_Blue_Slope_Curved_1x2", "Dark_Green_Brick_2x2", "Dark_Green_Brick_Round_1x1", "Dark_Green_Slope_45_2x2", "Dark_Purple_Brick_2x2", "Dark_Purple_Brick_Round_1x1", "Green_Brick_2x2", "Lavender_Brick_1x2", "Lavender_Brick_2x2", "Light_Aqua_Brick_1x1", "Light_Aqua_Brick_1x2", "Light_Aqua_Slope_Inverted_45_2x1", "Medium_Azure_Brick_1x1", "Medium_Azure_Brick_1x2", "Medium_Azure_Brick_Round_1x1", "Medium_Azure_Brick_Round_2x2_with_Axle_Hole", "Medium_Azure_Slope_45_2x1", "Medium_Azure_Slope__Curved_3_x_1", "Pearl_Gold_Cone_1x1_with_Top_Groove", "Red_Brick_1x1", "Red_Brick_1x2", "Red_Brick_2x2", "Red_Brick_Modified_1x1_with_Headlight", "Red_Brick_Modified_1x1x1_2:3_with_Studs_on_Side", "Red_Brick_Round_1x1", "Red_Cone_1x1_with_Top_Groove", "Red_Plant_Flower_2x2_Rounded-Solid_Stud", "Red_Slope_33_3x1", "Red_Slope_65_2x1x2", "Red_Slope_Curved_1x2", "Red_Slope_Inverted_45_2x1", "White_Brick_1x1", "White_Brick_1x2", "White_Brick_2x2", "White_Brick_Modified_1x1_with_Stud_on_Side", "White_Brick_Modified_1x2_with_Studs_on_1_Side", "White_Brick_Round_1_x_1", "White_Brick_Round_2x2_with_Axle_Hole", "White_Slope_45_2x2", "White_Slope_Curved_1x2", "White_Slope_Curved_3x1", "White_Slope_Inverted_45_2x2_with_Hollow_Round_Bottom_Tube", "Yellow_Brick_1x1", "Yellow_Brick_1x2", "Yellow_Brick_2x2", "Yellow_Brick_Modified_1x1_with_Headlight", "Yellow_Brick_Modified_1x1_with_Stud_on_Side", "Yellow_Brick_Round_1x1", "Yellow_Plant_Flower_2x2_Rounded-Solid_Stud", "Yellow_Slope_45_2x1", "Yellow_Slope_45_2x2", "Yellow_Slope_Curved_1x2", "Yellow_Slope_Curved_2x1x1_1:3_with_Recessed_Stud", "Yellow_Slope_Curved_3x1", "Yellow_Slope_Inverted_45_2x1", "Yellow_Slope_Inverted_45_2x2_with_Flat_Bottom_Pin"]


# Modificación para añadir listado de piezas al final del PDF
# Modification to add a parts list at the end of the PDF

# Función para dibujar el listado de piezas al final del PDF
# Function to draw the list of parts at the end of the PDF
def dibujar_listado_piezas(c, piezas):
    # Agregar una nueva página para el listado de piezas
    # Add a new page for the parts list
    c.showPage()

    # Ajustes para la casilla
    # Adjustments for the cell
    x_offset = 50
    y_offset = 750  # Iniciar desde la parte superior / Start from the top
    cell_width = 50
    cell_height = 60
    espacio_vertical = 20

    c.setFont("Helvetica", 10)
    c.drawString(x_offset, y_offset + 20, "Listado de Piezas LEGO:")
    c.drawString(x_offset, y_offset + 40, "LEGO Parts List:")
    
    for pieza in piezas:
        # Dibujar la imagen de la pieza
        # Draw the image of the part
        ruta_imagen = obtener_imagen(pieza)
        try:
            c.drawImage(ruta_imagen, x_offset, y_offset - cell_height, width=cell_width, height=cell_height, preserveAspectRatio=True)
        except Exception as e:
            # Si la imagen no se encuentra / If the image is not found
            c.setStrokeColor(colors.red)
            c.rect(x_offset, y_offset - cell_height, cell_width, cell_height, fill=0)
            c.setFont("Helvetica", 6)
            c.drawCentredString(x_offset + (cell_width / 2), y_offset - (cell_height / 2), "No image")

        # Dibujar el nombre de la pieza junto a la imagen
        # Draw the name of the part next to the image
        c.setFont("Helvetica", 10)
        c.drawString(x_offset + cell_width + 10, y_offset - (cell_height / 2), pieza)

        # Ajustar la posición para la siguiente pieza
        # Adjust the position for the next part
        y_offset -= (cell_height + espacio_vertical)

        # Si se llega al final de la página, añadir una nueva página
        # If the end of the page is reached, add a new page
        if y_offset < 50:
            c.showPage()
            y_offset = 750  # Reiniciar el offset vertical para la nueva página


# Función para generar un cartón de bingo de 10x3 con piezas en posiciones específicas
# Function to generate a 10x3 bingo card with pieces in specific positions
def generar_carton():
    carton = [[''] * 10 for _ in range(3)]  # Cartón 3x10 inicialmente vacío / Initially empty 3x10 card

    # Seleccionar 5 piezas de cada rango especificado / Select 5 pieces from each specified range
    piezas_grupo_1 = random.sample(piezas[0:30], 5)  # 5 piezas del rango 0 a 29 / 5 pieces from range 0 to 29
    piezas_grupo_2 = random.sample(piezas[30:60], 5) # 5 piezas del rango 30 a 59 / 5 pieces from range 30 to 59
    piezas_grupo_3 = random.sample(piezas[60:90], 5) # 5 piezas del rango 60 a 89 / 5 pieces from range 60 to 89

    # Colocar el primer grupo en la primera fila / Place the first group in the first row
    for col_idx in [0, 2, 4, 6, 8]:   # Columnas pares (2, 4, 6, 8, 10) / Even columns (2, 4, 6, 8, 10)
        carton[0][col_idx] = piezas_grupo_1.pop(0)

    # Colocar el segundo grupo en la segunda fila / Place the second group in the second row
    for col_idx in [1, 3, 5, 7, 9]:   # Columnas impares (1, 3, 5, 7, 9) / Odd columns (1, 3, 5, 7, 9)
        carton[1][col_idx] = piezas_grupo_2.pop(0)

    # Colocar el tercer grupo en la tercera fila / Place the third group in the third row
    for col_idx in [0, 2, 4, 6, 8]:   # Columnas pares (2, 4, 6, 8, 10) / Even columns (2, 4, 6, 8, 10)
        carton[2][col_idx] = piezas_grupo_3.pop(0)

    return carton

# Función para obtener la ruta de la imagen correspondiente a la pieza
# Function to get the image path corresponding to the piece
def obtener_imagen(pieza):
    nombre_archivo = pieza + ".jpg"  # Ejemplo / Example: "Black_Brick_1x1" -> "Black_Brick_1x1.jpg"
    return f"imagenes/{nombre_archivo}"

# Función para dibujar un cartón en una página PDF usando imágenes y agregar un borde alrededor de cada casilla
# Function to draw a bingo card on a PDF page using images and add a border around each cell
def dibujar_carton(c, carton, x_offset, y_offset):
    # Ajustes para la casilla
    # Adjustments for the cell
    cell_width = 50   # Ancho de cada casilla / Width of each cell
    cell_height = 50  # Altura de cada casilla / Height of each cell
    x = x_offset
    y = y_offset

    # Dibujar la imagen del título "bingo.jpg" sobre el cartón
    # Draw the "bingo.jpg" title image above the card
    c.drawImage("./bingo.jpg", x_offset, y_offset+20 , width=200, height=40, preserveAspectRatio=True)

    for fila in carton:
        for pieza in fila:
            # Dibujar el borde de la casilla / Draw the border of the cell
            c.setStrokeColor(colors.black)
            c.rect(x, y - cell_height, cell_width, cell_height, fill=0)

            if pieza:  # Solo dibujar si la casilla tiene una pieza / Only draw if the cell has a piece
                # Obtener la ruta de la imagen
                ruta_imagen = obtener_imagen(pieza)
                try:
                    # Dibujar la imagen de la pieza en la casilla / Draw the image of the piece in the cell
                    c.drawImage(ruta_imagen, x+5, y - cell_height+5, width=cell_width-10, height=cell_height-10, preserveAspectRatio=True)
                except Exception as e:
                    # Si no se encuentra la imagen, dibujar un recuadro vacío o un mensaje de error
                    # If the image is not found, draw an empty box or error message
                    c.setStrokeColor(colors.red)
                    c.rect(x, y - cell_height, cell_width, cell_height, fill=0)
                    c.setFont("Helvetica", 6)
                    c.drawCentredString(x + (cell_width / 2), y - (cell_height / 2), "No image")

            x += cell_width # Espacio entre columnas / Space between columns
        x = x_offset
        y -= cell_height  # Espacio entre filas / Space between rows

# Función para agregar el pie de página con la información proporcionada
# Function to add the footer with the provided information
def agregar_pie_pagina(c, ancho_pagina, y_offset):
    c.setFont("Helvetica", 8)  # Fuente más pequeña para el pie de página / Smaller font for the footer
    pie_pagina = "© Rafa Castillo 2024 CC BY-NC-SA 4.0\nImages © LEGO® Group\nLEGO® is a trademark of the LEGO Group, which does not sponsor, authorize, or endorse this work.\nOnly for non-commercial use - Not for resale"
    
    # Añadir cada línea del pie de página, ajustando el espacio vertical
    # Add each line of the footer, adjusting the vertical spacing
    lineas_pie = pie_pagina.split('\n')
    for i, linea in enumerate(lineas_pie):
        c.drawString(50, y_offset - (i * 10), linea)  # 10 es el espacio entre líneas / 10 is the space between lines

# Función principal para generar el PDF con los 200 cartones
# Main function to generate the PDF with 200 bingo cards
def generar_pdf(nombre_archivo):
    c = canvas.Canvas(nombre_archivo, pagesize=A4)
    ancho, alto = A4

    num_cartones = 200

    for i in range(num_cartones):
        if i % 2 == 0 and i != 0:  # Añadir una nueva página después de cada 2 cartones / Add a new page after every 2 cards
            c.showPage()

        # Generar dos cartones por página / Generate two cards per page
        carton1 = generar_carton()
        carton2 = generar_carton()

        # Dibujar el primer cartón en la parte superior de la página / Draw the first card at the top of the page
        dibujar_carton(c, carton1, 50, alto - 150)
        
        # Dibujar una línea discontinua en el centro de la página, entre los dos cartones
        # Draw a dashed line in the center of the page, between the two bingo cards
        c.setDash(6, 3)  # Establecer la línea discontinua (6 puntos de línea, 3 puntos de espacio) / Set the dashed line (6 points line, 3 points gap)
        c.line(50, alto - 350, ancho - 50, alto - 350)  # Dibujar la línea horizontal en el centro / Draw the horizontal line in the center
        c.setDash()  # Restablecer a línea continua / Reset to continuous line
        
        # Dibujar el segundo cartón en la parte inferior de la página / Draw the second card at the bottom of the page
        dibujar_carton(c, carton2, 50, alto - 500)
        
        # Añadir el pie de página en la parte inferior de cada página
        # Add the footer to the bottom of each page
        agregar_pie_pagina(c, ancho, 30)  # 30 es la distancia desde la parte inferior de la página / 30 is the distance from the bottom of the page

    # Añadir el listado de piezas al final del PDF / Add the parts list at the end of the PDF
    dibujar_listado_piezas(c, piezas)
    
    c.save()

# Generar el PDF con los cartones llamado "cartones.pdf"
# Generate the PDF with the cards named "cartones.pdf"
generar_pdf("cartones.pdf")
