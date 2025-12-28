# 🖼️ Removedor de Background com Streamlit

Este é um mini projeto em **Python + Streamlit** que permite remover o fundo de imagens de forma simples e rápida, utilizando **CPU ou GPU (CUDA)** automaticamente quando disponível.

O projeto usa a biblioteca **transparent-background**, que é baseada em modelos de deep learning para segmentação de imagens.

---

## ✨ Funcionalidades

- Upload de imagens (`.png`, `.jpg`, `.jpeg`)
- Remoção automática de background
- Escolha entre **CPU** ou **GPU (CUDA)** se disponível
- Modos de processamento:
  - `base` → melhor qualidade
  - `rápido` → mais velocidade
- Tipos de saída:
  - `green`
  - `white`
  - `rgba`
  - `map`
  - `blur`
  - `overlay`
- Ajuste de **threshold** para controlar o nível de remoção
- Visualização do resultado
- Download da imagem final

---

## 🧠 Como funciona a GPU

- O app detecta automaticamente se há uma GPU CUDA disponível usando `torch.cuda.is_available()`
- Caso exista, o usuário pode escolher usar **cuda**
- Caso contrário, o processamento ocorre em **CPU**

⚠️ Se o PyTorch não estiver instalado com suporte a CUDA, a opção GPU não aparecerá.

---

## 📦 Requisitos

### Python
- Python **3.9 ou superior** (recomendado)

### Dependências (`requirements.txt`)

```txt
streamlit
torch
torchvision
pillow
transparent-background
opencv-python-headless
```

- 💡 opencv-python-headless é usado para evitar dependências gráficas desnecessárias.

## 🚀 Como executar

### 1️⃣ Clone o repositório

```bash
git clone https://github.com/DiogoAug16/bg-remover-app.git

cd bg_remover_app
```

### 2️⃣ Crie um ambiente virtual (opcional, mas recomendado)

```bash
python -m venv venv

source venv/bin/activate  # Linux / Mac

venv\Scripts\activate     # Windows
```

### 3️⃣ Instale as dependências

```bash
pip install -r requirements.txt
```

### 4️⃣ Execute o app

```bash
streamlit run bg_remover_app.py
```

## 🖥️ Interface do App

1.  Envie uma imagem
2.  Escolha:
    * CPU ou GPU 
    * Modo de processamento
    * Tipo de background
    * Threshold
3. Clique em **Remover Background**
4. Visualize e faça o download da imagem final

## 📌 Possíveis melhorias futuras

* Suporte a múltiplas imagens

* Barra de progresso

* Escolha de resolução de saída

* Cache de modelo para melhor performance

* Versão Docker