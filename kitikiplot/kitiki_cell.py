"""
File Name: kitiki_cell.py
Description: This file defines the 'KitikiCell' class for each rectangular cell in kitiki plot
Author: Boddu Sri Pavan
Date Created: 21-10-2024
Last Modified: 20-11-2024
"""

from .kitiki_color_config import ColorConfig
from matplotlib.patches import Rectangle

class KitikiCell(ColorConfig):
    """
    Represents a cell in the KitikiPlot visualization.

    This class extends the ColorConfig class to add functionality for creating 
    individual cells in a grid-based visualization.

    Parameters
    ----------
    data : pd.DataFrame or list
        - The input data which can be either a 'pd.DataFrame' or a 'list'.
        - If a list is provided, it will be converted into a DataFrame using specified stride and window length.
    stride : int (optional)
        - The number of elements to move the window after each iteration when converting a list to a DataFrame. 
        - Default is 1.
    window_length : int (optional)
        - The length of each window when converting a list to a DataFrame. 
        - Default is 10.
    """
    
    def __init__(self, data, stride= 1, window_length= 10):
        """
        Initialize the KitikiCell object by inheriting from ColorConfig.

        Parameters
        ----------
        data : pd.DataFrame or list
            - The input data to be processed.
        stride : int (optional)
            - The number of elements to move the window after each iteration when converting a list to a DataFrame. 
            - Default is 1.
        window_length : int (optional)
            - The length of each window when converting a list to a DataFrame. 
            - Default is 10.
        """

        super().__init__(data=data, stride= stride, window_length= window_length)


    def create( self,
                x,
                y,
                each_sample,
                cell_width,
                cell_height,
                window_gap,
                cmap,
                edge_color,
                fallback_color,
                hmap,
                fallback_hatch,
                display_hatch,
                transpose,
                **kitiki_cell_kwargs):
        
        """
        Create a rectangular cell for the KitikiPlot visualization.

        Parameters
        ----------
        x : int
            - The x-coordinate of the cell in the grid.
        y : int
            - The y-coordinate of the cell in the grid.
        each_sample : list
            - A list containing each data record used for determining color and hatch patterns to plot KitikiPlot.
        cell_width : float
            - The width of each cell in the grid.
            - Default is 0.5.
        cell_height : float
            - The height of each cell in the grid.
            - Default is 2.0.
        window_gap : float
            - The gap between cells in the grid.
            - Default is 1.0.
        cmap : str or dict
            - If a string, it should be a colormap name to generate colors.
            - If a dictionary, it should map unique values to specific colors.
            - Default is 'rainbow'.
        edge_color : str
            - The color to use for the edges of the rectangle.
            - Default is '#000000'.
        fallback_color : str
            - The color to use as fallback if no specific color is assigned.
            - Default is '#FAFAFA'.
        hmap : dict
            - A dictionary mapping unique values to their corresponding hatch patterns.
            - Default is '{}'.
        fallback_hatch : str
            - The hatch pattern to use as fallback if no specific hatch is assigned.
            - Default is '" "' (string with single space).
        display_hatch : bool
            - A flag indicating whether to display hatch patterns on cells.
            - Default is False.
        transpose : bool
            - A flag indicating whether to transpose the dimensions of the cells.
            - Default is False.
        kitiki_cell_kwargs : keyword arguments
            - Additional keyword arguments passed to customize the Rectangle object.
            - Default is {}.

        Returns
        -------
        matplotlib.patches.Rectangle: A Rectangle object representing the configured cell for KitikiPlot visualization.
        """

        # Calculate dimensions for the rectangle based on grid position and size parameters
        rect_dim= (window_gap*(x+1)+ cell_width*(x+1) , cell_height*(y+1))

        # Adjust dimensions if transposing is set to 'True'
        if transpose== True:
            rect_dim= (cell_height*(y+1), window_gap*(x+1)+ cell_width*(x+1))

        # Return a Rectangle object with specified dimensions and styles based on input parameters
        return Rectangle( rect_dim,
           width= cell_width, 
           height= cell_height,
           facecolor= cmap[0][ each_sample[y] ],
           edgecolor= cmap[1],
           hatch= hmap[each_sample[y]],
           **kitiki_cell_kwargs
           )