import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

def main():
    input = np.loadtxt("csv/simplerw_10_300.csv", dtype='i', delimiter=',')
    #print(input)

    arena = np.zeros([10,10])
    for i in range(10):
        for j in range(10):
            arena[i][j] = input[(i*10)+j][2]

    print(arena)

    updateGrid(arena)

def updateGrid(grid):
    plt.imshow(grid, cmap='PuBu', interpolation='nearest')
    #cmap = mpl.colors.ListedColormap(['white','red'])
    # axes = plt.gca()
    # axes.set_xlim([0,9])
    # axes.set_ylim([0,9])
    #img = plt.imshow(grid, cmap='winter')
    #grd = plt.grid(True)
    plt.savefig("figures/simplerw_10_300.png")
    plt.show()

if __name__ == '__main__':
    main()
