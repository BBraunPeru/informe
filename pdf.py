from PIL import Image, ImageDraw, ImageFont
import datetime

def make_pdf(textos, checks, name_dir, n_informe=1):
    img = Image.open('scr/imgformato.jpg')
    draw = ImageDraw.Draw(img)

    font_size = 40
    font = ImageFont.truetype("arial.ttf", font_size)

    for i in range(len(ubicacion_text1)):
        loc = ubicacion_text1[i]
        draw.text(loc, textos[i], fill=colorLetra, font=font)
        loc2 = ubicacion_text2[i]
        draw.text(loc2, textos[i], fill=colorLetra, font=font)

    for check, ubicacion in zip(checks, ubicacion_checks1):
        if check:
            draw.text(ubicacion, "X", fill=colorLetra, font=font)

    for check, ubicacion in zip(checks, ubicacion_checks2):
        if check:
            draw.text(ubicacion, "X", fill=colorLetra, font=font)

    img.save(f'./{name_dir}/informe_{textos[3]}.jpg')

date = str(datetime.date.today())
tamanoLetra = 2
grosorLetra = 2
colorLetra = (0, 0, 0)
space_x = 1760

ubicacion_text1 = [
    (250, 335), (1300, 335),
    (200, 405), (670, 405), (1030, 405), (1350, 405),
    (1250, 825),
    (540, 1219),
    (1220, 970),
    (1100, 1610),
    (80, 1895),
    (1100, 2115)
]

ubicacion_checks1 = [
    (80, 500), (610, 500),
    (80, 650), (525, 650), (875, 650), (1280, 650),
    (80, 715), (525, 715), (875, 715), (1280, 715),
    (80, 780), (525, 780), (875, 780),
    (80, 835), (525, 835), (875, 835),
    (80, 979), (488, 979),
    (80, 1039), (488, 1039),
    (80, 1099), (488, 1099),
    (80, 1159),
    (80, 1219),
    (1455, 982), (1590, 982),
    (1455, 1044), (1590, 1044),
    (1455, 1104), (1590, 1104),
    (1455, 1164), (1590, 1164),
    (1455, 1224), (1590, 1224),
    (80, 1365), (527, 1370), (931, 1370), (1323, 1370),
    (80, 1425), (527, 1430), (931, 1430), (1323, 1430),
    (80, 1485), (527, 1490), (931, 1490), (1323, 1490),
    (80, 1545), (527, 1550), (931, 1550),
    (80, 1605), (527, 1610),
    (80, 1755), (535, 1755), (1000, 1755)
]

ubicacion_text2 = [(x + space_x, y) for x, y in ubicacion_text1]
ubicacion_checks2 = [(x + space_x, y) for x, y in ubicacion_checks1]
