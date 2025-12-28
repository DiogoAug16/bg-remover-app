import streamlit as st
from PIL import Image
from transparent_background import Remover
import warnings
warnings.filterwarnings("ignore", message="torch.meshgrid: in an upcoming release, it will be required to pass the indexing argument")

st.title("Background Remover")

uploaded_file = st.file_uploader("Choose an image file", type=["png", "jpg", "jpeg"])

device_option = st.selectbox('Select the device', ['cpu', 'cuda:0'])

# Mode selection dropdown
mode_option = st.selectbox('Select Mode', ['fast', 'base'])

# Background type dropdown
type_option = st.selectbox('Select Background Type', ['green', 'white', 'rgba', 'map', 'blur', 'overlay'])

# Threshold slider for removing the background
threshold = st.slider('Threshold for background removal (lower means less background removed)', 0.1, 0.9, 0.65)

# Check if an image file is uploaded
if uploaded_file is not None:
    # Display the uploaded image
    st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)
    
    # Convert the uploaded file to an image object
    img = Image.open(uploaded_file).convert('RGB')
    
    # Remove background button
    if st.button('Remove Background'):
        # Initialize the remover with selected options
        remover = Remover(mode=mode_option, jit=False, device=device_option)
        
        # Process the image
        out = remover.process(img, threshold=threshold, type=type_option)
        
        # Display the output image
        st.image(out, caption='Image with Background Removed', use_column_width=True)
        
        # Save the output image locally
        output_image_path = 'output_image.png'
        out.save(output_image_path)
        st.success(f"Background removed and saved as {output_image_path}")
        
        # Provide a download link for the processed image
        with open(output_image_path, "rb") as file:
            st.download_button(
                label="Download Image",
                data=file,
                file_name="background_removed_image.png",
                mime="image/png"
            )