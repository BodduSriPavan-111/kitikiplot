"""
File Name: linear.py
Description: This file defines grid concentration plot for ecological data visualization
Author: Boddu Sri Pavan
Date Created: 31-05-2025
Last Modified: 31-05-2025
"""

from kitikiplot.core import KitikiPlot

def plot( data, stride, window_length,
            cmap= {},
            figsize= (20, 5),
            focus= True,
            focus_alpha= 0.2,
            transpose= True,
            align= False,
            xlabel= "Time",
            ylabel= "Sliding Windows of CO(GT) values (in mg/m^3)",
            display_xticks= True,
            xticks_values= [],
            yticks_values= [],
            ytick_prefix= "Window",
            xticks_rotation= 90, 
            display_legend= True,
            title= "CO(GT) Trend in Air",
            legend_kwargs= {"bbox_to_anchor": (1.01, 1), "loc":'upper left', "borderaxespad": 0.}
        ):
    """
    Grid Plot for ecological data.
    Focus can be set to highlight particular time-interval of sliding window.
    """

    ktk= KitikiPlot( data= data, stride= stride, window_length= window_length )

    ktk.plot(
        figsize= (20, 5),
        cell_width= 2,
        cmap= cmap,
        focus= focus,
        focus_alpha= focus_alpha,
        transpose= transpose,
        align= align,
        xlabel= xlabel,
        ylabel= ylabel,
        display_xticks= display_xticks,
        xticks_values= xticks_values,
        yticks_values= yticks_values,
        ytick_prefix= ytick_prefix,
        xticks_rotation= xticks_rotation, 
        display_legend= display_legend,
        title= title,
        legend_kwargs= legend_kwargs
    )