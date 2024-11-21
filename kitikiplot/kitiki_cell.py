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
    Represents a cell in the Kitikiplot visualization.

    This class extends the ColorConfig class to add functionality for creating 
    individual cells in a grid-based visualization. Each cell can be customized 
    with colors, hatches, and dimensions based on the provided parameters.

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
            - The number of elements to move the window after each iteration when converting 
              a list to a DataFrame. 
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
        Create a rectangular cell for the Kitikiplot visualization.

        Parameters
        ----------
        x : int
            - The x-coordinate (column index) of the cell in the grid.
        y : int
            - The y-coordinate (row index) of the cell in the grid.
        each_sample : list
            - A list containing sample values used for determining color and hatch patterns.
        cell_width : float
            - The width of each cell in the grid.
            - Default is 0.5
        cell_height : float
            - The height of each cell in the grid.
            - Default is 2
        cmap : list
            - A list containing color mappings for filling and edge colors.
            - Default is 'rainbow'


        fallback_color : str
            - The color to use as fallback if no specific color is assigned.
            - Default is '#FAFAFA'
        edge_color : str
            - The color to use for the edges of the rectangle.
            - Default is '#000000'
        window_gap : float
            - The gap between cells in the grid.
            - Default is 1
        hmap : dict
            A dictionary mapping unique values to their corresponding hatch patterns.
        fallback_hatch : str
            - The hatch pattern to use as fallback if no specific hatch is assigned.
            - Default is '" "' (string with single space)
        display_hatch : bool
            A flag indicating whether to display hatch patterns on cells.
            - Default is False
        transpose : bool
            A flag indicating whether to transpose the dimensions of the cells.
        kitiki_cell_kwargs : keyword arguments
            Additional keyword arguments passed to customize the Rectangle object.

        Returns
        -------
        Rectangle: A Rectangle object representing the configured cell for visualization.
        """

        # Calculate dimensions for the rectangle based on grid position and size parameters
        rect_dim= (window_gap*(x+1)+ cell_width*(x+1) , cell_height*(y+1))

        # Adjust dimensions if transposing is enabled
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