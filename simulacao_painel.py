import tkinter as tk

def hex_to_rgb(hex_color):
    hex_color = hex_color.strip()
    if hex_color.startswith("0x"):
        hex_color = hex_color[2:]
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)
    return (r, g, b)

def ler_matriz_txt(arquivo):
    matriz = []
    with open(arquivo, 'r') as f:
        for linha in f:
            linha = linha.strip()
            if linha:
                cores = [c.strip() for c in linha.split(';') if c.strip() != '']
                matriz.append(cores)
    return matriz

def desenhar_matriz(matriz):
    tamanho_pixel = 30
    altura = len(matriz)
    largura = len(matriz[0]) if altura > 0 else 0

    root = tk.Tk()
    root.title("Simulador Matriz 10x10")

    canvas = tk.Canvas(root, width=largura*tamanho_pixel, height=altura*tamanho_pixel)
    canvas.pack()

    for y, linha in enumerate(matriz):
        for x, cor in enumerate(linha):
            r, g, b = hex_to_rgb(cor)
            cor_rgb = f'#{r:02x}{g:02x}{b:02x}'

            x0 = x * tamanho_pixel
            y0 = y * tamanho_pixel
            x1 = x0 + tamanho_pixel
            y1 = y0 + tamanho_pixel

            canvas.create_rectangle(x0, y0, x1, y1, fill=cor_rgb, outline='black')

    root.mainloop()

if __name__ == "__main__":
    matriz = ler_matriz_txt("Creeper/creeper.txt")  # Ajuste o caminho para seu arquivo
    desenhar_matriz(matriz)
