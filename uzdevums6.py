""" 
Programma pārbauda punktu atrašanās vietu četrstūrī (25.variants).
Izveidoja Kasandra Kornelija Snikere

(0.7; -1.2) Punkts atrodas uz figūras robežlīnijas.
(1; -2.3) Punkts atrodas uz figūras robežlīnijas.
(-1.33; -0.5) Punkts atrodas uz figūras robežlīnijas.
(0.4; -0.9) Punkts atrodas uz figūras robežlīnijas.
(1.5; -2) Punkts atrodas uz figūras robežlīnijas.
(-1; -2) Punkts atrodas uz figūras robežlīnijas.
(0; -3) Punkts atrodas uz figūras robežlīnijas.
(-2.5; -0.5) Punkts atrodas uz figūras robežlīnijas.
(0; -0.5) Punkts atrodas uz figūras robežlīnijas.
(1; -2.34) Punkts atrodas uz figūras robežlīnijas.
(-1.3; -1.7) Punkts atrodas uz figūras robežlīnijas.

(2; -0.5) Punkts atrodas ārpus figūras.
(2.5; -1.35) Punkts atrodas ārpus figūras.
(2.5; -3) Punkts atrodas ārpus figūras.
(1; -4) Punkts atrodas ārpus figūras.
(-2; -4) Punkts atrodas ārpus figūras.
(-4; -0.5) Punkts atrodas ārpus figūras.
(-3; 0) Punkts atrodas ārpus figūras.
(-2; 1) Punkts atrodas ārpus figūras.
(-4; 0) Punkts atrodas ārpus figūras.
(0; 5) Punkts atrodas ārpus figūras.

(0.5; -2) Punkts atrodas figūras iekšā.
(-1; -1.5) Punkts atrodas figūras iekšā.
(0.2; -2.8) Punkts atrodas figūras iekšā.
(-0.8; -2) Punkts atrodas figūras iekšā.
(-2; -1.9) Punkts atrodas figūras iekšā.
"""
x=float(input())
y=float(input())
if x<-2.5 or y<-3 or y>-0.5 or x>1.5:
    print("Punkts atrodas ārpus figūras.")
elif y==-1*x-0.5 or y==-0.5 or y==round(0.66*x-3,2) or y==-1*x-3:
    print("Punkts atrodas uz figūras robežlīnijas.")
else:
    print("Punkts atrodas figūras iekšā.")