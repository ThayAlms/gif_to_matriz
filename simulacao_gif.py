import tkinter as tk
import os
import time

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
                cores = [c.strip() for c in linha.split(',') if c.strip()]
                matriz.append(cores)
    return matriz

class SimuladorGIF:
    def __init__(self, pasta, intervalo_ms=200):
        self.pasta = pasta
        self.frames = self.carregar_frames()
        self.intervalo = intervalo_ms
        self.index_frame = 0

        self.altura = len(self.frames[0])
        self.largura = len(self.frames[0][0])
        self.pixel = 30

        self.root = tk.Tk()
        self.root.title("Simulador de GIF 10x10")
        self.canvas = tk.Canvas(self.root, width=self.largura*self.pixel, height=self.altura*self.pixel)
        self.canvas.pack()

        self.quadrados = [
            [self.canvas.create_rectangle(
                x*self.pixel, y*self.pixel, (x+1)*self.pixel, (y+1)*self.pixel,
                outline='black'
            ) for x in range(self.largura)]
            for y in range(self.altura)
        ]

        self.atualizar_frame()
        self.root.mainloop()

    def carregar_frames(self):
        arquivos = sorted([
            os.path.join(self.pasta, arq)
            for arq in os.listdir(self.pasta)
            if arq.endswith(".txt")
        ])
        return [ler_matriz_txt(arq) for arq in arquivos]

    def atualizar_frame(self):
        frame = self.frames[self.index_frame]
        for y, linha in enumerate(frame):
            for x, cor in enumerate(linha):
                r, g, b = hex_to_rgb(cor)
                cor_hex = f'#{r:02x}{g:02x}{b:02x}'
                self.canvas.itemconfig(self.quadrados[y][x], fill=cor_hex)

        self.index_frame = (self.index_frame + 1) % len(self.frames)
        self.root.after(self.intervalo, self.atualizar_frame)

if __name__ == "__main__":
    SimuladorGIF("Carinha_animada", intervalo_ms=200)  # Altere o nome da pasta se necessário
