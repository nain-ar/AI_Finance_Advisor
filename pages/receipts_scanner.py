import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Receipt Scanner",
    page_icon="🧾",
    layout="wide"
)

st.title("🧾 Receipt Scanner")

st.write(
    """
    Upload a receipt image to extract expense details automatically.
    """
)

st.markdown("---")

uploaded_file = st.file_uploader(
    "Upload Receipt",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Uploaded Receipt",
        use_container_width=True
    )

    st.success("Receipt uploaded successfully ✅")

    st.info(
        "OCR integration will be added in the next phase."
    )

else:
    st.info("Please upload a receipt image.")