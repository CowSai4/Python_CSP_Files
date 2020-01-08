with open('inputs/day2.txt','r') as infile:
    data = infile.readlines()



all = []

for line in data:
    l, w, h = map(int, line.split('x'))
    lw = l*w
    lh = l*h
    wh = w*h 

    surflw = lw*2
    surflh = lh*2
    surfwh = wh*2
    surface = surflw + surflh + surfwh

    bow = l * w * h

    rib2l = l*2
    rib2h = h*2
    rib2w = w*2

    rib_list = [rib2l, rib2h, rib2w]

    rib_list.sort()

    rib_all = rib_list[0] + rib_list[1]

    #print(rib_all)
    #print(bow)

    bow_rib = (rib_all + bow)

    fin_bow_rib = []
    #print(bow_rib)
    
    fin_bow_rib.append(bow_rib)

    #print(min([lw, lh, wh]))
    #print(surface)

    print(sum(fin_bow_rib))

    total = surface + min([lw, lh, wh])
    all.append(total)
#print(sum(all))

