from math import sqrt
point_x=float(input())
point_y=float(input())
C=sqrt(point_x**2+point_y**2)
if C<1:
    print("Punkts atrodas figūras iekšā.")
elif C==1:
    print("Punkts atrodas uz figuras robežas.")
else:
    print("Punkts atrodas ārpus figūras.")