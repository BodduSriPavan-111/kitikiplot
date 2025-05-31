"""
File Name: linear.py
Description: This file defines linear concentration plot
Author: Boddu Sri Pavan
Date Created: 25-05-2025
Last Modified: 25-05-2025
"""

from kitikiplot.core import KitikiPlot

def plot( 
            data, focus, focus_alpha, xlabel, ylabel, xticks_values, ytick_prefix, 
            stride= 1,
            figsize= (20,1), 
            cell_width= 2, 
            transpose= True, 
            display_xticks= True, 
            xticks_rotation= 90,
            display_legend= True, 
            title= "Linear Plot: Ecology Data Visualization", 
            return_figure= True, 
            legend_kwargs= {"bbox_to_anchor": (1.01, 1), "loc":'upper left', "borderaxespad": 0.},
            cmap= {} 
        ):

    ktk= KitikiPlot( data= data, stride= stride, window_length= len(data) )

    ktk.plot(
            figsize= figsize,
            cell_width= cell_width,
            cmap= cmap,
            focus= focus,
            focus_alpha= focus_alpha,
            transpose= transpose,
            xlabel= xlabel,
            ylabel= ylabel,
            display_xticks= display_xticks,
            xticks_values= xticks_values,
            ytick_prefix= ytick_prefix,
            xticks_rotation= xticks_rotation, 
            display_legend= display_legend,
            title= title,
            return_figure= return_figure,
            legend_kwargs= legend_kwargs)