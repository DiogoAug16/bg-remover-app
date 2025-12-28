import streamlit as st
from PIL import Image
from transparent_background import Remover
import torch
import warnings

# Ignorar avisos desnecessários
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", message="torch.meshgrid")

st.title("Removedor de Background")

uploaded_file = st.file_uploader(
    "Escolha o formato da imagem",
    type=["png", "jpg", "jpeg"]
)

# Detectar se tiver GPU disponível para acelerar o processo
has_cuda = torch.cuda.is_available()

device_option = st.selectbox(
    "Escolha o modo de processamento",
    ["cpu", "cuda:0"] if has_cuda else ["cpu"]
)

mode_option = st.selectbox("Escolha o modo", ["rápido", "base"])
type_option = st.selectbox(
    "Escolha o tipo de Background da imagem a ser removido",
    ["green", "white", "rgba", "map", "blur", "overlay"]
)

threshold = st.slider(
    "Threshold (menor = menos background removido)",
    0.1, 0.9, 0.65
)

if uploaded_file is not None:
    st.image(uploaded_file, caption="Imagem Enviada", width=700)

    img = Image.open(uploaded_file).convert("RGB")

    if st.button("Remover Background"):
        remover = Remover(
            mode=mode_option,
            jit=False,             
            device=device_option
        )

        out = remover.process(
            img,
            threshold=threshold,
            type=type_option
        )

        st.image(out, caption="Background Removido", width=700)

        output_path = "output_image.png"
        out.save(output_path)

        st.success("Background removido com sucesso!")

        with open(output_path, "rb") as f:
            st.download_button(
                "Download Imagem",
                data=f,
                file_name="background_removed.png",
                mime="image/png"
            )
