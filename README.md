# TouchFreeGame 🖐️🎮

**TouchFreeGame** é um jogo interativo desenvolvido em Python que utiliza **visão computacional** para permitir que alunos com **necessidades especiais** interajam com o computador **sem usar o toque físico**.

O jogador usa **bolas coloridas físicas** para apontar na tela (através da webcam), escolhendo entre **elementos visuais como alienígenas, frutas, palavras, formas geométricas e muito mais**.

---

## 🧠 Objetivo

Oferecer uma ferramenta lúdica, inclusiva e acessível que:

- Estimule o aprendizado e a coordenação motora;
- Dê autonomia a alunos com mobilidade reduzida;
- Use tecnologia acessível (webcam comum e objetos físicos coloridos).

---

## 🚀 Tecnologias Utilizadas

- Python 3
- OpenCV (para detecção via câmera)
- Pygame (para a interface gráfica e elementos do jogo)
- NumPy
- [Outras dependências conforme evolução do projeto]

---

## 📦 Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/TouchFreeGame.git
   cd TouchFreeGame
   ```

2. Crie e ative um ambiente virtual (opcional mas recomendado):

   ```bash
   python -m venv venv
   source venv/bin/activate  # ou venv\Scripts\activate no Windows
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Como Rodar

```bash
python main.py
```

Certifique-se de que sua webcam está conectada e funcionando.

---

## 📚 Estrutura Inicial

```
TouchFreeGame/
├── main.py
├── camera/
│   └── tracker.py
├── assets/
│   ├── sprites/
│   └── sounds/
├── game/
│   └── scenes.py
├── utils/
│   └── helpers.py
├── requirements.txt
└── README.md
```

---

## ♿ Inclusão e Acessibilidade

Este projeto foi pensado especialmente para **educação inclusiva**. Ele pode ser utilizado por:

- Alunos com paralisia cerebral  
- Autistas com dificuldades motoras  
- Crianças em reabilitação física  
- Qualquer aluno que se beneficie de interações sem toque  

---

## 🤝 Contribuições

Contribuições são bem-vindas! 👾🍇📚  
Sinta-se à vontade para abrir *issues*, enviar *pull requests* ou sugerir melhorias.

---
