import matplotlib.pyplot as plt
import seaborn as sns

class DataVisualization:
    @staticmethod
    def plot_data(df, x, y):
        sns.lineplot(data=df, x=x, y=y)
        plt.show()
