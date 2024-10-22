from .kitiki_color_config import ColorConfig
from matplotlib.patches import Rectangle

class KitikiCell(ColorConfig):

    def __init__(self, data, line_width= 1):

        super().__init__(data=data)
        self.line_width= line_width



    def create( self, x, y, each_sample, cell_width, cell_height, cmap, fallback_color, edge_color, window_gap ):

        color_map= self.color_config( cmap= cmap, edge_color= edge_color, fallback_color= fallback_color )
        # hatch_map= self.hatch_config( hmap= hmap, fallback_hatch= fallback_hatch)

        return Rectangle( (window_gap*(x+1)+ cell_width*(x+1) , cell_height*(y+1)),
           width= cell_width, 
           height= cell_height,
           linewidth= self.line_width,
           facecolor= color_map[0][ each_sample[y] ],
           edgecolor= color_map[1],
        #    hatch= hatch_map
           )