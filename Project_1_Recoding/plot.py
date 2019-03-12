
import matplotlib.pyplot as plt
import globals as g


def plot_plg():    # generate and plot the playground

    # plot the lines of the table
    v0 = [(0, 0), (0, 12)]
    v1 = [(4, 4), (0, 12)]
    v2 = [(8, 8), (0, 12)]
    v3 = [(12, 12), (0, 12)]
    h0 = [(0, 12), (0, 0)]
    h1 = [(0, 12), (4, 4)]
    h2 = [(0, 12), (8, 8)]
    h3 = [(0, 12), (12, 12)]
    plt.plot(v0[0], v0[1], v1[0], v1[1], v2[0], v2[1], v3[0], v3[1])
    plt.plot(h0[0], h0[1], h1[0], h1[1], h2[0], h2[1], h3[0], h3[1])

    # plot the elements (crosses and circles)
    for j in range(3):

        for k in range(3):
            yc = 10 - j * 4  # changing reference (from PLG indexes to PLOT coordinates) --> DEFINING CENTER OF FIGURES
            xc = 2 + k * 4

            if g.plg[j][k] == 1:      # plot a 'cross' by a vert. and a horit. line from a given center (xc,yc)
                vl = [(xc, xc, xc), (yc - 1, yc, yc + 1)]
                hl = [(xc - 1, xc, xc + 1), (yc, yc, yc)]
                plt.plot(vl[0], vl[1], hl[0], hl[1])

            elif g.plg[j][k] == -1:       # plot a 'circle' by 4 lines from a given center (xc,yc)
                se = [(xc, xc + 1), (yc - 1, yc)]
                ne = [(xc, xc + 1), (yc + 1, yc)]
                no = [(xc, xc - 1), (yc + 1, yc)]
                so = [(xc, xc - 1), (yc - 1, yc)]
                plt.plot(se[0], se[1], ne[0], ne[1], no[0], no[1], so[0], so[1])

    # visualization
    plt.xlabel('X:  1                2                 3', fontsize=16)
    plt.ylabel('Y:  1           2           3', fontsize=16)
    plt.xticks([])
    plt.yticks([])
    plt.box(on=None)
    print("PRESENT TABLETOP:")
    plt.show()
