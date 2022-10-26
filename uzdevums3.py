""" 
Programma pārbauda punktu atrašanās vietu trijstūrī.
Izveidoja Kasandra Kornelija Snikere DP2-2

(0;0) Punkts atrodas uz figuras robežas.
(0; 3) Punkts atrodas uz figuras robežas.
(1.2; 1.2) Punkts atrodas uz figuras robežas.
(0.1; 2.85) Punkts atrodas uz figuras robežas.
(1.5; 0.75) Punkts atrodas uz figuras robežas.

(1; 1) Punkts atrodas figūras iekšā.
(0.4; 1.6) Punkts atrodas figūras iekšā.
(1.2; 0.2) Punkts atrodas figūras iekšā.

(2; 2) Punkts atrodas ārpus figūras.
(2; -1) Punkts atrodas ārpus figūras.
(-1; 1) Punkts atrodas ārpus figūras.
"""

point_x=float(input())
point_y=float(input())
if point_y<0 or point_x<0 or round(point_y*1000)/1000 > round((-1.5*point_x+3)*1000)/1000:
    print("Punkts atrodas ārpus figūras.")
elif point_y==0 or point_x==0 or round(point_y*1000)/1000==round((-1.5*point_x+3)*1000)/1000:
    print("Punkts atrodas uz figuras robežas.")
else:
    print("Punkts atrodas figūras iekšā.")
