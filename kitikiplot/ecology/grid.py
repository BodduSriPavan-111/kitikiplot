"""
File Name: linear.py
Description: This file defines grid concentration plot for ecological data visualization
Author: Boddu Sri Pavan
Date Created: 31-05-2025
Last Modified: 31-05-2025
"""

from kitikiplot.core import KitikiPlot

def plot( data, stride, window_length, focus, focus_alpha, xlabel, ylabel, xticks_values, ytick_prefix, cmap= {} ):

    ktk= KitikiPlot( data= data, stride= stride, window_length= window_length )

    ktk.plot(
        figsize= (20, 5),
        cell_width= 2,
        cmap= {-200: "#00db3e", 1: "#00b7db", 2: "#4400d8", 3: "#ff7070", 4: "#b0009b"},
        focus= True,
        focus_alpha= 0.2,
        transpose= True,
        align= False,
        xlabel= "Time",
        ylabel= "Sliding Windows of CO(GT) values (in mg/m^3)",
        display_xticks= True,
        xticks_values= time_period,
        ytick_prefix= "Window",
        xticks_rotation= 90, 
        display_legend= True,
        title= "CO(GT) Trend in Air",
        legend_kwargs= {"bbox_to_anchor": (1.01, 1), "loc":'upper left', "borderaxespad": 0.})