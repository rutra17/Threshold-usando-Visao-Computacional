# 🌓 Threshold Dinâmico com Histograma (Visão Computacional)

Este projeto foi desenvolvido para a disciplina de Visão Computacional. O objetivo é demonstrar como o computador processa imagens em tempo real através da técnica de **Threshold (Limiarização)**, transformando frames da webcam em imagens binárias (preto e branco).

## 🚀 Tecnologias e Versões

* **Python 3.13** (Versão específica utilizada no desenvolvimento)
* **OpenCV (opencv-python)**: Para captura e processamento de imagem.
* **NumPy**: Para manipulação de matrizes e dados do histograma.

## 🛠️ Instalação e Requisitos

Certifique-se de ter o Python 3.13 instalado. Para instalar as bibliotecas necessárias, execute o comando abaixo no seu terminal:

```bash
pip install opencv-python numpy
```

## 📂 Como rodar o projeto

1. Clone o repositório ou baixe o arquivo `.py`.
2. No terminal, navegue até a pasta do projeto.
3. Execute o comando:

```bash
python app.py
```

4. Utilize o **Trackbar** na janela "Parametros" para ajustar o limiar em tempo real.
5. Pressione a tecla **'q'** para encerrar a aplicação.

---

## 🧠 Investigação e Conceitos (Relatório da Atividade)

Durante o desenvolvimento e testes do programa, foram observados os seguintes pontos fundamentais para a compreensão da Visão Computacional:

### 1. O que acontece quando o limite é muito baixo (ex: 50)?

A imagem fica majoritariamente **branca**. Isso ocorre porque o "filtro" é muito permissivo; quase todos os pixels possuem intensidade maior que 50, fazendo com que o computador os converta para o valor máximo (255 - Branco).

### 2. O que acontece quando é muito alto (ex: 200)?

A imagem fica majoritariamente **preta**. Apenas os pixels que representam fontes de luz direta ou reflexos muito intensos (brilhos) conseguem ultrapassar o valor 200 para virar branco. O restante é "cortado" para o valor mínimo (0 - Preto).

### 3. A iluminação do ambiente influencia? Por quê?

**Sim, totalmente.** A luz altera diretamente o valor numérico de intensidade de cada pixel.

* Em ambientes **escuros**, o "pico" de dados no histograma se move para a esquerda (perto do 0).
* Em ambientes **claros**, ele se move para a direita (perto do 255).
  Isso exige que o valor do *Threshold* seja ajustado dinamicamente para que o objeto de interesse não "desapareça".

### 4. Existe um valor ideal?

Não existe um valor fixo "mágico". O valor ideal depende do contexto da imagem. Matematicamente, o valor ideal costuma estar localizado no **vale** entre dois picos do histograma, conseguindo separar com precisão o que é fundo (background) do que é objeto (foreground).

---

## 📊 Visualização do Histograma

O projeto inclui uma janela de histograma em tempo real com uma **linha vermelha indicadora**.

* **Gráfico Branco:** Representa a distribuição dos tons de cinza na imagem atual.
* **Linha Vermelha:** Representa a posição exata do seu Threshold. Tudo o que está à esquerda da linha no gráfico vira preto na tela, e tudo o que está à direita vira branco.

---

**Desenvolvido por:** [Artur Tabosa]
                      [Gabriel Loyo]
