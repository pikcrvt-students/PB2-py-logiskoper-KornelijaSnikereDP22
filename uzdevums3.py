point_x=float(input())
point_y=float(input())
if point_y<0 or point_x<0 or round(point_y*1000)/1000 > round((-1.5*point_x+3)*1000)/1000:
    print("Punkts atrodas ārpus figūras.")
elif point_y==0 or point_x==0 or round(point_y*1000)/1000==round((-1.5*point_x+3)*1000)/1000:
    print("Punkts atrodas uz figuras robežas.")
else:
    print("Punkts atrodas figūras iekšā.")
