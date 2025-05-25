# import sys
# import os
# import io
# from io import StringIO

# from Bio import SeqIO

# sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '..')))

# from kitikiplot.genomics import grid
# import streamlit as st

# st.title( body= ":blue[Genome Visualization]")

# # data= st.text_input( label= "Genome", key= "data", placeholder= "Ex: AATTTTCGT")
# uploaded_file= st.file_uploader("Upload a file (Format: .fasta)")

# if uploaded_file is not None:
#     data= str(list( SeqIO.parse(StringIO(uploaded_file.getvalue().decode("utf-8")), "fasta") )[0].seq)

# window_length= st.number_input( key= "window_length", label= "Window/ Chunk Length", min_value= 0, max_value= 200, value= 50)

# submit= st.button( key= "submit", label= "Submit" )

# global figure 

# figure= None

# if submit:

#     figure= grid.plot( nucleotide_sequence= data, window_length= window_length )
    
#     print("Figure: ", figure)

#     st.pyplot( figure )


# if figure!= None:
#     img_bytes = io.BytesIO()
#     figure.savefig(img_bytes, format="png")
#     img_bytes.seek(0)

#     st.download_button(
#     label="Download Plot as PNG",
#     data=img_bytes,
#     file_name= uploaded_file.name+"GridPlot.png",
#     mime="image/png"
#         )

import streamlit as st

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '..')))

from io import StringIO, BytesIO

from Bio import SeqIO

from kitikiplot.genomics import grid

st.set_page_config(layout="wide")

# --- Column Layout ---
col1, _, col2 = st.columns([18, 2, 80])  # 20% : 80%


# --- Column 1: Sidebar Area ---
with col1:

    data= "" 

    # Some Text + File Upload (top 30% area)
    st.markdown("### Upload your Genome File")
    uploaded_file= st.file_uploader("Upload a file (Format: .fasta)")

    if uploaded_file is not None:

        data= str(list( SeqIO.parse(StringIO(uploaded_file.getvalue().decode("utf-8")), "fasta") )[0].seq)

    # Input: Chunk/window length
    window_length= st.number_input( key= "window_length", label= "Window/ Chunk Length", min_value= 0, max_value= 200, value= 50)

    # Spacer to push button to bottom 20%
    # st.markdown("<div style='height:px;'></div>", unsafe_allow_html=True)
    submit = st.button("Submit", type="primary")

    st.markdown("<div style='margin-top: 30px;'></div>", unsafe_allow_html=True)

    # Banner Image (top 5–10%)
    st.image("banner.png", use_container_width =True)

    figure= grid.plot( nucleotide_sequence= data, window_length= window_length )

    st.markdown("</div>", unsafe_allow_html=True)

# --- Column 2: Output Area ---
with col2:
    st.markdown("## Genome Grid Plot")

    # Only show output if submit is clicked
    if submit and uploaded_file is not None:

        st.pyplot( figure )

        if figure!= None:
            img_bytes = BytesIO()
            figure.savefig(img_bytes, format="png")
            img_bytes.seek(0)

            st.download_button(
            label="Download Plot as PNG",
            data=img_bytes,
            file_name= uploaded_file.name+"GridPlot.png",
            mime="image/png"
                )
