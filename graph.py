import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

def main():
    input = np.loadtxt("testFile.csv", dtype='i', delimiter=',')
    #print(input)
    explored = 0
    arena = np.zeros([10,10])
    for i in range(10):
        for j in range(10):
            arena[i][j] = input[(i*10)+j][2]
            if (arena[i][j] >0):
                explored +=1
    print(arena)

    updateGrid(arena)
    print(explored)


def updateGrid(grid):
    plt.imshow(grid, cmap='PuBu', interpolation='nearest')
    #cmap = mpl.colors.ListedColormap(['white','red'])
    # axes = plt.gca()
    # axes.set_xlim([0,9])
    # axes.set_ylim([0,9])
    #img = plt.imshow(grid, cmap='winter')
    #grd = plt.grid(True)
    plt.show()

if __name__ == '__main__':
    main()
