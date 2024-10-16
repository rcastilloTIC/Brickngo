# Brickngo 
# Generador de Cartones de Bingo LEGO® (Español/Spanish)

Este proyecto contiene un script en Python (`cartones.py`) y un script en Bash (`renombrar.sh`) que te permiten generar un PDF con cartones de bingo de piezas LEGO®. 
Los cartones se generan a partir de un conjunto de 90 piezas, divididas en tres grupos de 30. El proceso de creación sigue estos pasos:

1. **Primer grupo**: Se seleccionan 5 piezas de forma aleatoria del primer grupo (piezas 1 a 30) y ocupan la primera fila del cartón.
2. **Segundo grupo**: A continuación, se seleccionan 5 piezas del segundo grupo (piezas 31 a 60), también de manera aleatoria, pero estas ocuparán siempre la segunda fila del cartón, en el orden en que se elijan.
3. **Tercer grupo**: Por último, se eligen 5 piezas del tercer grupo (piezas 61 a 90), de nuevo de manera aleatoria, y estas piezas llenarán la tercera fila del cartón, respetando el orden en que fueron seleccionadas.

El resultado final es un cartón con 15 piezas seleccionadas de manera aleatoria, distribuidas en tres filas de 5 piezas cada una. Lo importante es que, si una pieza en particular es elegida, siempre aparecerá en la misma fila de acuerdo al grupo al que pertenece. Este método imita el comportamiento de los cartones numéricos tradicionales, donde los números de la primera fila provienen de un rango limitado (por ejemplo, del 1 al 29).

## Descripción

### `cartones.py`

El script de Python genera un archivo PDF (`cartones.pdf`) con los cartones de bingo pedidos (número par), cada uno con un conjunto de piezas LEGO seleccionadas de forma aleatoria. Además, cada cartón incluye imágenes de las piezas y el título "bingo.jpg" en la parte superior. El PDF también incluye una lista de las piezas utilizadas al final del documento.

- **Formato de los cartones**: Cada cartón tiene un formato de 10x3.
- **Imágenes**: El script intenta cargar las imágenes de cada pieza desde el directorio actual. Si la imagen no se encuentra, se mostrará un recuadro rojo con el texto "No image".
- **Título**: Se usa una imagen llamada `bingo.jpg` que debe estar en el directorio actual.
- **Nombre del archivo**: El PDF generado se guarda con el nombre `cartones.pdf`.


### `renombrar.sh`

Este script en Bash permite obtener una variable python con el nombre de los archivos de imágenes de un directorio. El script solicita un directorio y verifica su existencia antes de proceder. Posteriormente, realiza las operaciones necesarias para devolver la variable.


## Estructura del proyecto / Project Structure

├── README.md # Documentación del proyecto  
├── cartones.py  # Script principal en Python para generar el PDF  
├── renombrar.sh  # Script en Bash para generar una variable python  
├── bingo.jpg # Imagen del título que se muestra en cada cartó  
└── imagenes/ # Directorio que contiene las imágenes de las piezas LEGO  ​


## Dependencias

Para ejecutar `cartones.py`, necesitarás instalar las siguientes dependencias de Python:


- **ReportLab**: Biblioteca para la generación de PDFs.

Puedes instalarla utilizando `pip`:

```bash
pip install reportlab
```


## Ejecución

1. Obtener la variable python con los nombres de las imágenes

Para usar el script de creación de la variable python, ejecuta:

To use the renaming script, run:

```bash
bash renombrar.sh
```

El script te pedirá que introduzcas el directorio donde se encuentran las imágenes para obtener sus nombres y generar la variable.


2. Generar el PDF de cartones 

Para generar el PDF de cartones de bingo, simplemente ejecuta el siguiente comando:

```bash
python cartones.py
```

Esto generará un archivo cartones.pdf en el directorio actual con los cartones y la lista de piezas LEGO.

## Personalización

	- Piezas LEGO®: Puedes modificar la lista de piezas LEGO® en el archivo cartones.py para adaptarla a tus propias necesidades.
	- Imágenes: Las imágenes de cada pieza LEGO® deben estar en el directorio imagenes/ y seguir el formato de nombres definidos en el script (por ejemplo, Black_Brick_1x1.jpg).

## Contribución

Si deseas contribuir a este proyecto, por favor haz un fork del repositorio, realiza tus cambios y abre un pull request. ¡Las contribuciones son bienvenidas!

## Licencia

Este proyecto está bajo la licencia CC BY-NC-SA 4.0 . Puedes consultar [este enlace](https://creativecommons.org/licenses/by-nc-sa/4.0/?ref=chooser-v1) para más detalles.


## Notas adicionales

	- Asegúrate de que las imágenes de las piezas estén en el directorio imagenes/ y tengan el nombre adecuado para que sean cargadas correctamente en el PDF.
	- El archivo de título bingo.jpg debe estar en el directorio raíz del proyecto para que sea utilizado en la generación del PDF.


# LEGO® Bingo Card Generator (Inglés / English)

This project contains a Python script (`cartones.py`) and a Bash script (`renombrar.sh`) that allow you to generate a PDF with LEGO® bingo cards.

The cards are generated from a set of 90 items, divided into three groups of 30. The creation process follows these steps:

1. **First group**: 5 items are randomly selected from the first group (items 1 to 30), and they are always arranged in the first row of the card.
2. **Second group**: Next, 5 items are selected from the second group (items 31 to 60), also randomly, but these will always occupy the second row of the card, in the order in which they are chosen.
3. **Third group**: Finally, 5 items are selected from the third group (items 61 to 90), once again randomly, and these items will fill the third row of the card, maintaining the order in which they were selected.

The final result is a card with 15 randomly selected items, distributed in three rows of 5 items each. What’s important is that if a particular item is chosen, it will always appear in the same row according to the group it belongs to. This method mimics the behavior of traditional number cards, where the numbers in the first row come from a limited range (for example, 1 to 29).


## Description

### `cartones.py`

The Python script generates a PDF file (`cartones.pdf`) with the bingo cards wanted (even number), each with a random set of LEGO pieces. Additionally, each card includes images of the pieces and the title "bingo.jpg" at the top. The PDF also includes a list of the LEGO pieces used at the end of the document.

- **Card format**: Each card has a 10x3 format.
- **Images**: The script tries to load images of each part from the images directory. If an image is not found, a red box with "No image" text will be shown.
- **Title**: An image called `bingo.jpg` is used, and it must be in the current directory.
- **File name**: The generated PDF is saved as `cartones.pdf`.

### `renombrar.sh`

This Bash script allows you to get the names of image files to obtain a python variable. The script prompts for a directory and verifies its existence before proceeding. It then it reads the name on the files in that directory, ignores the extension and returns the python variable. Only needed if you change any image.

## Project Structure

├── README.md # Project documentation  
├── cartones.py  # Python script to generate the PDF  
├── renombrar.sh  # Bash script to obtain the list of parts in python format  
├── bingo.jpg # Title image shown on each bingo card  
└── imagenes/ # Directory containing LEGO piece images  ​

## Dependencies

To run `cartones.py`, you will need to install the following Python dependencies:

- **ReportLab**: Library for generating PDFs.

You can install it using `pip`:

```bash
pip install reportlab
```


## Usage

1. Obtain Image Files names python variable

To use the renaming script, run:

```bash
bash renombrar.sh
```

The script will prompt you to enter the directory where the files to be readed are located so it will generate the variable.


2. Generate the Bingo PDF

To generate the PDF with bingo cards, simply run the following command:

```bash
python cartones.py
```

This will generate a cartones.pdf file in the current directory with the bingo cards and the LEGO parts list.


## Customization

	- LEGO® Parts: You can modify the list of LEGO® parts in the cartones.py file to fit your needs.
	- Images: The images of each LEGO® part must be in the imagenes/ directory and follow the naming format defined in the script (e.g., Black_Brick_1x1.jpg).

## Contribution

If you wish to contribute to this project, please fork the repository, make your changes, and open a pull request. Contributions are welcome!

## License

This project is licensed under the CC BY-NC-SA 4.0 License. You can check [this link](https://creativecommons.org/licenses/by-nc-sa/4.0/?ref=chooser-v1)for more details.


## Additional Notes

	- Make sure that the images of the pieces are in the imagenes/ directory and have the correct name format to be loaded properly in the PDF.
	- The bingo.jpg title file must be in the root directory of the project to be used in the PDF generation.



# Disclaimer / Aviso Legal

Este programa no tiene ningún tipo de vinculación con LEGO® ni con THE LEGO® GROUP. No es un producto oficial ni está autorizado por THE LEGO® GROUP, y no tiene ningún propósito comercial. Este software se proporciona únicamente como una herramienta para facilitar la creación de juegos en el ámbito de los Grupos de Usuarios de LEGO Reconocidos (RLUG).

This program is not affiliated with LEGO® or THE LEGO® GROUP. It is not an official product nor is it endorsed by THE LEGO® GROUP, and it has no commercial intent. This software is provided solely as a tool to assist in the creation of games within the context of Recognized LEGO User Groups (RLUG).
