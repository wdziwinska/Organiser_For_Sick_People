from matplotlib import pyplot as plt


class Plots:

    def drawPlot(self, plotTitle, x, y, color):
        fig, ax = plt.subplots(1, 1, figsize=(15, 5))
        ax.plot(x, y, color=color, linestyle='--', marker='.')
        ax.set_title(plotTitle)
        fig.patch.set_facecolor('xkcd:grey')
        ax.set_facecolor('xkcd:dark grey')
        # ax.set(xlabel='Data', ylabel='Puls')
        xticks = ax.get_xticks()
        if len(xticks) >= 10:
            ax.set_xticks(xticks[::len(xticks) // 5])  # set new tick positions
        ax.tick_params(axis='x', rotation=12, labelsize=7)  # set tick rotation