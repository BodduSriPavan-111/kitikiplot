import sys
import os
import io
from io import StringIO

from Bio import SeqIO

sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '..')))

from kitikiplot.core import KitikiPlot
import streamlit as st

# m = st.markdown("""
# <style>
# div.stButton > button:first-child {
#     background: rgb(93,224,230);
#     background: linear-gradient(90deg, rgba(93,224,230,1) 0%, rgba(0,74,173,1) 100%);
#     color:#ffffff;
#     width:100%;
# }
# div.stButton > button:hover {
#     background-color: #38b6ff;
#     color:#ffffff;
#     }
# </style>""", unsafe_allow_html=True)

st.title( body= ":blue[Streamlit]")

# data= st.text_input( label= "Genome", key= "data", placeholder= "Ex: AATTTTCGT")
uploaded_file= st.file_uploader("Upload a file (Format: .fasta)")

if uploaded_file is not None:
    data= str(list( SeqIO.parse(StringIO(uploaded_file.getvalue().decode("utf-8")), "fasta") )[0].seq)
    st.write( data )

col1, col2= st.columns(2)

flag= 0

with col1:
    
    window_length= st.number_input( key= "window_length", label= "Window Length", min_value= 0, max_value= 20, value= 0)

with col2:
    stride= st.number_input(key= "stride", label= "Stride", min_value= 0, max_value= 10, value= 1)


#   figsize: tuple = (25, 5),
#   window_range: str | tuple = "all",  
#   fallback_color: str = "#FAFAFA",
#   hmap: dict = {},
#   fallback_hatch: str = " ",
#   xticks_values: list = [],
#   yticks_values: list = [],
#   legend_hatch: bool = False,
#   legend_kwargs: dict = {},
#   kitiki_cell_kwargs: dict = {}
    
with st.expander("Additional Settings"):
    
    col3, col4, col5= st.columns( 3 )

    with col3:

        title= st.text_input( key= "title", label= "Title", placeholder= "Genome Visualization using KitikiPlot", value= "Genome Visualization using KitikiPlot" )
        cmap= st.text_input( key= "cmap", label= "CMAP", placeholder= "Ex: rainbow, viridis, plasma, terrain, jet")
        cell_width= st.number_input( key= "cell_width", label= "Cell Width", min_value= 0.5, max_value= 5.0, value= 0.5 )
        cell_height= st.number_input( key= "cell_height", label= "Cell Height", min_value= 0.5, max_value= 5.0, value= 2.0 )
        window_gap= st.number_input( key= "window_gap", label= "Window Gap", min_value= 0.5, max_value= 5.0, value= 1.0 )
        window_range= st.text_input( key= "window_range", label= "Window Range", placeholder= "Ex: all, 1, 2, ...", value= "all")

    with col4:

        xticks_rotation= st.number_input( key= "xticks_rotation", label= "X-Ticks Rotation", min_value= 0, max_value= 360, value= 0)
        yticks_rotation= st.number_input( key= "yticks_rotation", label= "Y-Ticks Roatation", min_value= 0, max_value= 360, value= 0)
        
        xlabel= st.text_input( key= "xlabel", label= "X-Label", placeholder= "Ex: Nucleotide", value= "Nucleotide_n")
        ylabel= st.text_input( key= "ylabel", label= "Y-Label", placeholder= "Ex: Sequence", value= "Sequence")

        xtick_prefix= st.text_input( key= "xtick_prefix", label= "X-Tick Prefix", placeholder= "Ex: Nucleotide", value= "Nucleotide")
        ytick_prefix= st.text_input( key= "ytick_prefix", label= "Y-Tick Prefix", placeholder= "Ex: Seq", value= "Sequence")

    with col5:

        transpose= st.checkbox( key= "transpose", label= "Transpose" )
        align= st.checkbox( key= "align", label= "Align", value= True )
        display_xticks= st.checkbox( key= "display_xticks", label= "Display X-Ticks", value= True )
        display_yticks= st.checkbox( key= "display_yticks", label= "Display Y-Ticks" )
        display_grid= st.checkbox( key= "display_grid", label= "Display Grid")
        display_legend= st.checkbox( key= "display_legend", label= "Display Legend" )
        display_hatch= st.checkbox( key= "display_hatch", label= "Display Hatch")

        edge_color= st.color_picker( key= "edge_color", label= "Edge Color" )


import streamlit.components.v1 as components
def ChangeButtonColour(widget_label, font_color, background_color='transparent'):
    htmlstr = f"""
        <script>
            var elements = window.parent.document.querySelectorAll('button');
            for (var i = 0; i < elements.length; ++i) {{ 
                if (elements[i].innerText == '{widget_label}') {{ 
                    elements[i].style.color ='{font_color}';
                    elements[i].style.background = '{background_color}';
                    elements[i].style.width= '100%'a
                }}
            }}
        </script>
        """
    components.html(f"{htmlstr}", height=0, width=0)


col6, col7= st.columns(2)

with col6:
    submit= st.button( key= "submit", label= "Submit" )


ChangeButtonColour('Submit', 'red', 'linear-gradient(90deg, rgba(93,224,230,1) 0%, rgba(0,74,173,1) 100%)') # button txt to find, colour to assign
ChangeButtonColour('Download', '#c19af5', '#354b75') # button txt to find, colour to assign

global figure 

figure= None

if submit:

    if data!=None and window_length!=None and stride!=None:

        data= [i for i in data]
        window_length= len(data)

        ktk= KitikiPlot( data= data, window_length= window_length, stride= stride)

        figure= ktk.plot(
                    figsize= (20, 3),
                    cell_width= 2,
                    cmap= {'A': '#007FFF', 'T': "#fffc00", "G": "#00ff00", "C": "#960018"},
                    transpose= transpose,
                    xlabel= xlabel,
                    ylabel= ylabel,
                    display_yticks= display_yticks,
                    xtick_prefix= xtick_prefix,
                    xticks_rotation= xticks_rotation,
                    title= title,
                    display_legend= display_legend,
                    return_figure= True,
                    legend_kwargs= {"bbox_to_anchor": (1.01, 1), "loc":'upper left', "borderaxespad": 0.}
                )
        
        st.pyplot( figure )
        st.write("Everything is ok !")

    else:
        st.error("Please check all inputs are provided !")

with col7:
    
    if figure!= None:
        img_bytes = io.BytesIO()
        figure.savefig(img_bytes, format="png")
        img_bytes.seek(0)

        st.download_button(
        label="Download Plot as PNG",
        data=img_bytes,
        file_name="plot.png",
        mime="image/png"
         )