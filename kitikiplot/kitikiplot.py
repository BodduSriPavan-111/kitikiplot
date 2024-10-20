from .kitiki_cell import KitikiCell
import matplotlib.pyplot as plt

class kitikiplot:

    def __init__(self, data):

        self.data= data
        self.cell= KitikiCell( data= self.data )
        self.rows= self.data.shape[0]
        self.cols= self.data.shape[1]

    def plot( self, figsize= (25, 5), title= "KitikiPlot: Intuitive Visualization for Sliding Window", xlabel= "Sliding Windows", ylabel= "Frames", xticks_rotation= 0, yticks_rotation= 0 ):

        fig, ax = plt.subplots( figsize= figsize)

        patches= [] 

        data= self.data.values

        for index in range(self.rows):

            each_sample= data[ index ]

            for time_frame in range(self.cols):

                patches.append(  self.cell.create(index, time_frame, each_sample))

        for each_patch in patches:
            ax.add_patch( each_patch )

        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)

        plt.xticks( [i+1.25 for i in range(self.rows)], ['Window_'+str(i+1) for i in range(self.rows)], rotation= xticks_rotation)
        plt.yticks( [i*2+1.5 for i in range(self.cols)], ["Frame_"+str(i) for i in range(self.cols)], rotation= yticks_rotation)
        # automatically scale the plot
        ax.relim()
        ax.autoscale_view() 
        plt.show()