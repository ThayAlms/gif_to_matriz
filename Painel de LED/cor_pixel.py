from PIL import Image
import os

def rgb2hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

filename = "creeper"
input_path = f"imagens/{filename}.png"
output_path = f"txts/{filename}.txt"
resized_path = f"imagens/{filename}_10x10.png"

os.makedirs("txts", exist_ok=True)

try:
    im = Image.open(input_path).convert("RGB")
except FileNotFoundError:
    print(f"[ERRO] Imagem '{input_path}' não encontrada.")
    exit(1)

# Redimensiona para 10x10 pixels
im = im.resize((10, 10), Image.Resampling.LANCZOS)

# Salva a imagem redimensionada para visualização
im.save(resized_path)
print(f"[OK] Imagem redimensionada salva em: {resized_path}")

pixel = im.load()
column, row = im.size

with open(output_path, 'w') as file:
    n = 0
    for j in range(row): 
        for i in range(column):
            r, g, b = pixel[i, j]
            string = rgb2hex(r, g, b)
            if j % 2:
                x = j * column + (column - i) - 1
            else:
                x = n
            file.write(f"leds[{x}] = 0x{string[1:]};")
            n += 1
        file.write("\n")

print(f"[OK] Arquivo gerado em: {output_path}")
