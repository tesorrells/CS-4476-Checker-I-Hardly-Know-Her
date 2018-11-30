
def pixelToCheckerboard(red, black):
    red_out_x = list()
    red_out_y = list()
    black_out_x = list()
    black_out_y = list()
    delineation = [0, 500/8.0, 2*500/8.0, 3*500/8.0, 4*500/8.0, 5*500/8.0, 6*500/8.0, 7*500/8.0, 500]

    # Red X
    for i in range(len(red)):
        for d in range(len(delineation)):
            if (red[i][0] > delineation[d]) and (red[i][0] < delineation[d+1]):
                red_out_x.append(d)
    # Red Y
    for i in range(len(red)):
        for d in range(len(delineation)):
            if (red[i][1] > delineation[d]) and (red[i][1] < delineation[d+1]):
                red_out_y.append(d)
    # Black X
    for i in range(len(black)):
        for d in range(len(delineation)):
            if (black[i][0] > delineation[d]) and (black[i][0] < delineation[d + 1]):
                black_out_x.append(d)
    # Black Y
    for i in range(len(black)):
        for d in range(len(delineation)):
            if (black[i][1] > delineation[d]) and (black[i][1] < delineation[d + 1]):
                black_out_y.append(d)

    print("")

