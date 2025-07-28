from PIL import Image
import os

def extrair_frames(gif_path, pasta_saida):
    # Abre o GIF
    gif = Image.open(gif_path)

    # Cria a pasta de saída, se não existir
    if not os.path.exists(pasta_saida):
        os.makedirs(pasta_saida)

    # Loop para salvar cada frame
    frame = 0
    while True:
        try:
            gif.seek(frame)
            frame_image = gif.convert('RGB')  # remove transparência, se houver

            frame_path = os.path.join(pasta_saida, f"frame_{frame:03d}.png")
            frame_image.save(frame_path)
            print(f"Salvo: {frame_path}")

            frame += 1
        except EOFError:
            break  # fim dos frames

    print(f"\nTotal de frames extraídos: {frame}")


caminho_gif = "Carinha_animada.gif"     
pasta_dos_frames = "frames_extraidos"
extrair_frames(caminho_gif, pasta_dos_frames)
