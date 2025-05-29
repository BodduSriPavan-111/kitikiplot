"""
File Name: linear.py
Description: This file defines linear concentration plot
Author: Boddu Sri Pavan
Date Created: 25-05-2025
Last Modified: 25-05-2025
"""

from kitikiplot.core import KitikiPlot

def plot( data, focus, focus_alpha, xlabel, ylabel, xticks_values, ytick_prefix, cmap= {} ):

    ktk= KitikiPlot( data= data, stride= 1, window_length= len(data) )

    ktk.plot(
            figsize= (20, 1),
            cell_width= 2,
            cmap= cmap,
            focus= focus,
            focus_alpha= focus_alpha,
            transpose= True,
            xlabel= xlabel,
            ylabel= ylabel,
            display_xticks= True,
            xticks_values= xticks_values,
            ytick_prefix= ytick_prefix,
            xticks_rotation= 90, 
            display_legend= True,
            title= "Linear Plot: Ecology Data Visualization",
            legend_kwargs= {"bbox_to_anchor": (1.01, 1), "loc":'upper left', "borderaxespad": 0.})