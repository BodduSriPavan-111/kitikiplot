from .kitiki_color_config import ColorConfig
from matplotlib.patches import Rectangle

class KitikiCell:

    def __init__(self, data, cell_width= 0.5, cell_height= 2, line_width= 1):

        self.data= data
        self.cell_width= cell_width
        self.cell_height= cell_height
        self.line_width= line_width
        self.color_config= ColorConfig( data= self.data )



    def create( self, x, y, each_sample, cmap= "rainbow", edge_color= "#000000" ):

        color_map= self.color_config.config( cmap= cmap, edge_color= edge_color )

        return Rectangle((x+1, y*2+1),
           width= self.cell_width, 
           height= self.cell_height,
           facecolor= color_map[0][ each_sample[y] ],
           edgecolor= color_map[1],
           linewidth= self.line_width)