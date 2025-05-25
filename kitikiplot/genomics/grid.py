"""
File Name: linear.py
Description: This file defines linear genomic plot
Author: Boddu Sri Pavan
Date Created: 21-05-2025
Last Modified: 24-05-2025
"""

from kitikiplot.core import KitikiPlot

import pandas as pd

def plot( nucleotide_sequence: str, window_length= 30, cell_width= 2 ):
    """
    Generates linear genomic plot for short genome sequences.

    Parameters
    ----------
    nucleotide_sequence : str
        - Sequence of 'A', 'T', 'G', and 'C'.
    """

    # Preprocess input genomic sequence
    nucleotide_sequence=nucleotide_sequence.upper()

    residual= len(nucleotide_sequence)%window_length

    l= []
    for index in range( len(nucleotide_sequence)// window_length):

        l.append( list(nucleotide_sequence[index*window_length: (index+1)*window_length]) )

    if residual > 0:
        l.append( list(nucleotide_sequence[(-1)*residual:]) + ["No_Data"]* (window_length- residual) )

    grid_df= pd.DataFrame(l)

    ktk= KitikiPlot( data= grid_df, stride= 0 )

    fig= ktk.plot(
                figsize= (grid_df.shape[1]//3, grid_df.shape[0]//3),
                cell_width= cell_width,
                cmap= {'A': '#007FFF', 'T': "#fffc00", "G": "#00ff00", "C": "#960018"},
                transpose= True,
                window_gap= 0,
                xlabel= "Nucleotides",
                ylabel= "Nucleotide Chunk",
                display_xticks= False,
                display_yticks= False,
                title= "Grid Plot: Nucleotide Sequence Visualization",
                display_legend= True,
                legend_kwargs= {"bbox_to_anchor": (1.01, 1), "loc":'upper left', "borderaxespad": 0.},
                return_figure= True,
                kitiki_cell_kwargs= {"linewidth": 0.5}
            )
    
    return fig