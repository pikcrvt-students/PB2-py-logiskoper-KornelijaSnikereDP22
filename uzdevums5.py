'''
Programma pārbauda punktu atrašanas vietu apgrieztā aplī.
Izveidoja Kasandra Kornelija Snikere DP2-2


(-1; 2) Punkts atrodas uz robežlīnijas.
(-3; 2) Punkts atrodas uz robežlīnijas.
(-2; 1) Punkts atrodas uz robežlīnijas.
(-2; 3) Punkts atrodas uz robežlīnijas.
(-2.5; 2.5) Punkts atrodas uz robežlīnijas.
(-1.2; 2.6) Punkts atrodas uz robežlīnijas.
(-1.04; 1.72) Punkts atrodas uz robežlīnijas.
(-2.8; 1.4) Punkts atrodas uz robežlīnijas.
(-2.8; 2.2) Punkts atrodas uz robežlīnijas.

(-2; 2) Punkts atrodas figūras iekšā.
(-1.5; 1.5) Punkts atrodas figūras iekšā.
(-2.5; 2) Punkts atrodas figūras iekšā.
(-2; 2.6) Punkts atrodas figūras iekšā.
(-2.6; 2.3) Punkts atrodas figūras iekšā.

(-3; 1) Punkts atrodas ārpus figūras.
(0; 2) Punkts atrodas ārpus figūras.
(-1; 0) Punkts atrodas ārpus figūras.
(-2.6; 2.6) Punkts atrodas ārpus figūras.
(-1.8; 3.2) Punkts atrodas ārpus figūras.
'''

from math import sqrt
x=float(input())
y=float(input())
C=round((x+2)**2+(y-2)**2,2)
s=x+5
if C>1 or y>s:
    print("Punkts atrodas ārpus figūras.")
elif C==1 or y==s:
    print("Punkts atrodas uz robežlīnijas.")
else:
    print("Punkts atrodas figūras iekšā.")
