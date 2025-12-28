import streamlit as st
from PIL import Image
from transparent_background import Remover
import torch
import warnings

# Silence safe warnings
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", message="torch.meshgrid")

st.title("Background Remover")

uploaded_file = st.file_uploader(
    "Choose an image file",
    type=["png", "jpg", "jpeg"]
)

# Detect GPU availability
has_cuda = torch.cuda.is_available()

device_option = st.selectbox(
    "Select device",
    ["cpu", "cuda:0"] if has_cuda else ["cpu"]
)

mode_option = st.selectbox("Select Mode", ["fast", "base"])

type_option = st.selectbox(
    "Select Background Type",
    ["green", "white", "rgba", "map", "blur", "overlay"]
)

threshold = st.slider(
    "Threshold (lower = less background removed)",
    0.1, 0.9, 0.65
)

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image", width=700)

    img = Image.open(uploaded_file).convert("RGB")

    if st.button("Remove Background"):
        remover = Remover(
            mode=mode_option,
            jit=False,             # 🔥 stability > speed
            device=device_option
        )

        out = remover.process(
            img,
            threshold=threshold,
            type=type_option
        )

        st.image(out, caption="Background Removed", width=700)

        output_path = "output_image.png"
        out.save(output_path)

        st.success("Background removed successfully!")

        with open(output_path, "rb") as f:
            st.download_button(
                "Download Image",
                data=f,
                file_name="background_removed.png",
                mime="image/png"
            )
