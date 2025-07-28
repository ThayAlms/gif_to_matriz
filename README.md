<h2>🧩 gif2led_matrix</h2>

<p><strong>Scripts em Python para converter GIFs animados ou imagens em <code>matrizes 10x10</code> de cores, ideais para displays de LED (como WS2812/NeoPixel) ou outros sistemas visuais com microcontroladores.</strong></p>

<h3>🎯 O que este projeto faz?</h3>
<ul>
  <li>📤 Extrai os <strong>frames de um GIF animado</strong></li>
  <li>🖼️ Redimensiona cada frame para <strong>10x10 pixels</strong></li>
  <li>🎨 Converte cada pixel para os formatos de cor:
    <ul>
      <li><code>RGB (r, g, b)</code></li>
      <li><code>HEX (#rrggbb)</code> e <code>0xRRGGBB</code> (para uso em C/Arduino)</li>
    </ul>
  </li>
  <li>📝 Gera um <strong>arquivo <code>.txt</code> por frame</strong>, contendo a matriz de pixels, pronta para importar em código de Arduino, C++, Python, etc.</li>
</ul>

<h3>📁 Estrutura esperada</h3>
<pre>
gif2led_matrix/
├── frames_extraidos/         ← Contém os frames extraídos do GIF
├── frames_redimensionados/  ← Contém os frames redimensionados para 10x10 (opcional)
├── matrizes_txt/             ← Saída dos arquivos .txt com cores HEX
├── extrair_frames.py         ← Extrai os frames do GIF
├── analisar_frames.py        ← Converte os frames em matrizes de cores
└── README.md                 ← Este arquivo
</pre>

<h3>🛠️ Tecnologias usadas</h3>
<ul>
  <li>Python 3</li>
  <li>Biblioteca <a href="https://python-pillow.org" target="_blank">Pillow (PIL)</a> para manipulação de imagens</li>
</ul>

<h3>💡 Aplicações</h3>
<ul>
  <li>Exibição de GIFs em painéis LED</li>
  <li>Projetos com Arduino, ESP32 ou Raspberry Pi</li>
  <li>Conversão visual de imagens em dados</li>
  <li>Estudo de manipulação de imagem e controle de hardware</li>
</ul>
