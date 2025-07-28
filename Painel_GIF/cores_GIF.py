from PIL import Image
import os

def rgb2hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

# Caminhos
pasta_entrada = "frames_extraidos"
pasta_saida = "matrizes_txt"
pasta_redimensionadas = "frames_redimensionados"

# Cria pastas de saída, se não existirem
os.makedirs(pasta_saida, exist_ok=True)
os.makedirs(pasta_redimensionadas, exist_ok=True)

# Lista todos os arquivos de imagem da pasta de frames
arquivos = sorted([f for f in os.listdir(pasta_entrada) if f.endswith(('.png', '.jpg'))])

if not arquivos:
    print("[ERRO] Nenhum frame encontrado na pasta 'frames_extraidos'.")
    exit(1)

for nome_arquivo in arquivos:
    caminho_entrada = os.path.join(pasta_entrada, nome_arquivo)
    nome_base = os.path.splitext(nome_arquivo)[0]

    try:
        im = Image.open(caminho_entrada).convert("RGB")
    except Exception as e:
        print(f"[ERRO] Falha ao abrir '{nome_arquivo}': {e}")
        continue

    # Redimensiona para 10x10
    im = im.resize((10, 10), Image.Resampling.LANCZOS)

    # Salva imagem redimensionada (opcional, para visualização)
    caminho_redimensionado = os.path.join(pasta_redimensionadas, f"{nome_base}_10x10.png")
    im.save(caminho_redimensionado)

    # Gera matriz em .txt
    caminho_saida = os.path.join(pasta_saida, f"{nome_base}.txt")
    pixel = im.load()
    coluna, linha = im.size

    with open(caminho_saida, 'w') as file:
        for j in range(linha):  # linha
            linha_hex = []
            for i in range(coluna):  # coluna
                r, g, b = pixel[i, j]
                cor_hex = rgb2hex(r, g, b)
                linha_hex.append("0x" + cor_hex[1:])  # tira o "#" e adiciona "0x"
            file.write(", ".join(linha_hex) + "\n")

    print(f"[OK] Matriz salva: {caminho_saida}")

print("\n✅ Processamento finalizado!")
