point_x=float(input())
point_y=float(input())
if point_y>0 and point_x>0 and round(point_y*1000)/1000<round((-1.5*point_x+3)*1000)/1000:
    print("Punkts atrodas figūras iekšā.")
elif point_y==0 or point_y==3 or point_x==0 or point_x==2 or round(point_y*1000)/1000==round((-1.5*point_x+3)*1000)/1000:
    print("Punkts atrodas uz figuras robežas.")
else:
    print("Punkts atrodas ārpus figūras.")
