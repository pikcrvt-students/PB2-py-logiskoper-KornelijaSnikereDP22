point_x=float(input())
point_y=float(input())
if point_x<-1 or point_x>3 and point_y>1 or point_y<-2:
    print("Punkts ir ārpus robežas")
elif point_x==-1 or point_x==3 or point_y==1 or point_y==-2:
    print("Punkts atrodas uz robežas")
else:
    print("Punkts atrodas figuras iekšā")
