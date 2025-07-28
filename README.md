🧩 gif2led_matrix
Scripts em Python para converter GIFs animados ou imagens em matrizes 10x10 de cores, ideais para displays de LED (como WS2812/NeoPixel) ou outros sistemas visuais com microcontroladores.

🎯 O que este projeto faz?
📤 Extrai os frames de um GIF animado

🖼️ Redimensiona cada frame para 10x10 pixels

🎨 Converte cada pixel para os formatos de cor:

RGB (r, g, b)

HEX (#rrggbb) e 0xRRGGBB (para uso em C/Arduino)

📝 Gera um arquivo .txt por frame, contendo a matriz de pixels, pronta para importar em código de Arduino, C++, Python, etc.

📁 Estrutura esperada
lua
Copiar
Editar
gif2led_matrix/
├── frames_extraidos/         ← Contém os frames extraídos do GIF
├── frames_redimensionados/  ← Contém os frames redimensionados para 10x10 (opcional)
├── matrizes_txt/             ← Saída dos arquivos .txt com cores HEX
├── extrair_frames.py         ← Extrai os frames do GIF
├── analisar_frames.py        ← Converte os frames em matrizes de cores
└── README.md                 ← Este arquivo
🛠️ Tecnologias usadas
Python 3

Biblioteca Pillow (PIL) para manipulação de imagens

💡 Aplicações
Exibição de GIFs em painéis LED

Projetos com Arduino, ESP32 ou Raspberry Pi

Conversão visual de imagens em dados

Estudo de manipulação de imagem e controle de hardware
