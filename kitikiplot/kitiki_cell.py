from .kitiki_color_config import ColorConfig
from matplotlib.patches import Rectangle

class KitikiCell:

    def __init__(self, data, line_width= 1):

        self.data= data
        self.line_width= line_width
        self.color_config= ColorConfig( data= self.data )



    def create( self, x, y, each_sample, cell_width, cell_height, cmap, edge_color, window_gap ):

        color_map= self.color_config.config( cmap= cmap, edge_color= edge_color )

        return Rectangle((window_gap*(x+1)+ cell_width*(x+1) , y*2+1),
           width= cell_width, 
           height= cell_height,
           facecolor= color_map[0][ each_sample[y] ],
           edgecolor= color_map[1],
           linewidth= self.line_width)