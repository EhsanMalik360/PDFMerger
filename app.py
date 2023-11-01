import streamlit as st
from PyPDF2 import PdfWriter
from io import BytesIO


# Show the Streamlit app in the browser
st.set_page_config(layout="wide")

st.title('PDF Merger')

uploaded_files = st.file_uploader("Choose PDF files", accept_multiple_files=True, type=['pdf'])

if uploaded_files:
    if st.button('Merge PDFs'):
        merger = PdfWriter()

        for pdf in uploaded_files:
            merger.append(pdf)

        with st.spinner('Merging PDFs...'):
            pdf_bytes = BytesIO()
            merger.write(pdf_bytes)
            pdf_bytes.seek(0)  # reset the cursor to the beginning of the file

        st.success('Merge Complete!')
        st.download_button(
            label="Download Merged PDF",
            data=pdf_bytes,
            file_name='merged.pdf',
            mime='application/pdf'
        )
