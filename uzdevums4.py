"""
Programma pārbauda punktu atrašanās vietu aplī.
Izveidoja Kasandra Kornelija Snikere DP2-2

(0; 1) Punkts atrodas uz figuras robežas.
(1; 0) Punkts atrodas uz figuras robežas.
(0; -1) Punkts atrodas uz figuras robežas.
(-1; 0) Punkts atrodas uz figuras robežas.
(0.6; 0.8) Punkts atrodas uz figuras robežas.
(0.8; -0.6) Punkts atrodas uz figuras robežas.
(-0.6; -0.8) Punkts atrodas uz figuras robežas.

(0; 0) Punkts atrodas figūras iekšā.
(-0.5; 0.5) Punkts atrodas figūras iekšā.
(0.9; 0.2) Punkts atrodas figūras iekšā.
(0; 0;7) Punkts atrodas figūras iekšā.

(2; 2) Punkts atrodas ārpus figūras.
(0; 2) Punkts atrodas ārpus figūras.
(-2; -1) Punkts atrodas ārpus figūras.
(1; 1) Punkts atrodas ārpus figūras.

"""


from math import sqrt
point_x=float(input())
point_y=float(input())
C=round(point_x**2+point_y**2, 2)
if C<1:
    print("Punkts atrodas figūras iekšā.")
elif C==1:
    print("Punkts atrodas uz figuras robežas.")
else:
    print("Punkts atrodas ārpus figūras.")
