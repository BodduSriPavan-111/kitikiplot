"""
File Name: linear.py
Description: This file defines linear genomic plot
Author: Boddu Sri Pavan
Date Created: 21-05-2025
Last Modified: 24-05-2025
"""

from kitikiplot.core import KitikiPlot

def plot( nucleotide_sequence: str )->  bool:
    """
    Generates linear genomic plot for short genome sequences.

    Parameters
    ----------
    nucleotide_sequence : str
        - Sequence of 'A', 'T', 'G', and 'C'.
    """

    # Preprocess input genomic sequence
    nucleotide_sequence=nucleotide_sequence.upper()

    ktk= KitikiPlot( data= nucleotide_sequence, stride= 1, window_length= len(nucleotide_sequence) )

    ktk.plot(
                figsize= (20, 1),
                cell_width= 2,
                cmap= {'A': '#007FFF', 'T': "#fffc00", "G": "#00ff00", "C": "#960018"},
                transpose= True,
                xlabel= "Nucleotides",
                ylabel= "Window",
                display_yticks= False,
                xtick_prefix= "Nucleotide",
                xticks_rotation= 90,
                title= "Linear Plot: Nucleotide Sequence Visualization",
                display_legend= True,
                legend_kwargs= {"bbox_to_anchor": (1.01, 1), "loc":'upper left', "borderaxespad": 0.}
            )