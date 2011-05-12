#!/usr/bin/python
#-*-coding:utf-8-*-
#######################
# av-avcı problemi    #
#       sayz          #
# sayz@bil.omu.edu.tr #
#######################


def grid_ciz(gr_size, hunter, prey):
    print "   ",
    grid, gr_raw = [], []
    for i in range(gr_size[0]):
        if((i + 1) < 10):
            print "%s " % (i + 1),
        else:
            print "%s" % (i + 1),
        gr_raw.append(". ")
    print ""
    for i in range(gr_size[1]):
        grid.append(gr_raw)
    for i in range(gr_size[1]):
        if((i + 1) < 10):
            print str(i + 1) + "  ",
        else:
            print str(i + 1) + " ",
        for j in range(gr_size[0]):
            if ((hunter == prey) and ((j + 1, i + 1) == hunter)):
                print "# ",
            elif ((j + 1, i + 1) == hunter):
                print "H ",
            elif ((j + 1, i + 1) == prey):
                print "P ",
            else:
                print grid[i][j],
        print ""


def uzaklik(hunter, prey):
    return ((hunter[0] - prey[0]) ** 2 + (hunter[1] - prey[1]) ** 2) ** 0.5


def movement_H(hunter):
    hareketH = []
    if((hunter[0] - 1 != 0) and (hunter[1] - 1 != 0)):
        hareketH.append((hunter[0] - 1, hunter[1] - 1))
    if(hunter[0] - 1 != 0):
        hareketH.append((hunter[0] - 1, hunter[1]))
        hareketH.append((hunter[0] - 1, hunter[1] + 1))
    if(hunter[1] - 1 != 0):
        hareketH.append((hunter[0], hunter[1] - 1))
        hareketH.append((hunter[0] + 1, hunter[1] - 1))
    hareketH.append((hunter[0], hunter[1] + 1))
    hareketH.append((hunter[0] + 1, hunter[1]))
    hareketH.append((hunter[0] + 1, hunter[1] + 1))
    return hareketH


def movement_P(prey):
    hareketP = []
    if(prey[0] - 1 != 0):
        hareketP.append((prey[0] - 1, prey[1]))
    if(prey[1] - 1 != 0):
        hareketP.append((prey[0], prey[1] - 1))
    hareketP.append((prey[0], prey[1] + 1))
    hareketP.append((prey[0] + 1, prey[1]))
    return hareketP


def tasani_at(gr_size, hareket):
    silinecekler = []
    for konum in hareket:
        if (konum[0] > gr_size[0]) or (konum[1] > gr_size[1]):
            silinecekler.append(konum)
    for silinecek in silinecekler:
        hareket.remove(silinecek)
    return hareket


def av_gorme(hunter, prey):
    return uzaklik(hunter, prey) < 1.5


def yeni_konum(gr_size, hunter, prey):
    tempu = uzaklik(hunter, prey)
    moveH = tasani_at(gr_size, movement_H(hunter))
    moveP = tasani_at(gr_size, movement_P(prey))
    if (av_gorme(hunter, prey)):
        for p in range(len(moveP)):
            yu = uzaklik(hunter, moveP[p])
            if yu > tempu:
                tempu = yu
                prey = moveP[p]
        for h in range(len(moveH)):
            yu = uzaklik(moveH[h], prey)
            if yu < tempu:
                tempu = yu
                hunter = moveH[h]
    else:
        for h in range(len(moveH)):
                yu = uzaklik(moveH[h], prey)
                if yu < tempu:
                    tempu = yu
                    hunter = moveH[h]
    return hunter, prey


def iskelet():
    gr_size = input("lutfen gridin boyutlarını giriniz(x,y)-->")
    prey = input("av'ın koordindatlarını giriniz(x,y)----->")
    hunter = input("avcı'nın koordindatlarını giriniz(x,y)-->")
    print """
    (i) interaktif mod
    (s) similasyon mod
    """
    isc = raw_input("hangi mod(i/s):")
    grid_ciz(gr_size, hunter, prey)
    k = 0
    if isc == "i":
        while True:
            yk = yeni_konum(gr_size, hunter, prey)
            hunter, prey = yk[0], yk[1]
            ehc = raw_input("devam mı?:")
            if ehc == "e":
                grid_ciz(gr_size, hunter, prey)
                if hunter == prey:
                    print "av " + str(k + 1) + " adımda yakalandı"
                    exit(1)
            else:
                break
            k += 1
    elif isc == "s":
        while hunter != prey:
            yk = yeni_konum(gr_size, hunter, prey)
            hunter, prey = yk[0], yk[1]
            k += 1
    grid_ciz(gr_size, hunter, prey)
    print "av " + str(k) + " adımda yakalandı"
    exit(1)


if __name__ == '__main__':
    iskelet()
