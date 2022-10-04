point_x=float(input())
point_y=float(input())
if point_x<-5 or point_x>2 and point_y>3 or point_y<-1:
    print("Punkts ir ārpus robežas")
elif point_x==-5 or point_x==2 or point_y==3 or point_y==-1:
    print("Punkts atrodas uz robežas")
else:
    print("Punkts atrodas figuras iekšā")