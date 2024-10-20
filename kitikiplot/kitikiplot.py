from .kitiki_cell import KitikiCell
import matplotlib.pyplot as plt

class kitikiplot:

    def __init__(self, data):

        self.data= data
        self.cell= KitikiCell( data= self.data )
        self.rows= self.data.shape[0]
        self.cols= self.data.shape[1]

    def plot( self, figsize= (25, 5) ):

        fig, ax = plt.subplots( figsize= figsize)

        patches= [] 

        data= self.data.values

        for index in range(self.rows):

            each_sample= data[ index ]

            for time_frame in range(self.cols):

                patches.append(  self.cell.create(index, time_frame, each_sample))

        for each_patch in patches:
            ax.add_patch( each_patch )

        # automatically scale the plot
        ax.relim()
        ax.autoscale_view() 
        plt.show()