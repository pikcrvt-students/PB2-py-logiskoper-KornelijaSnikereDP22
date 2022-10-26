x=float(input())
y=float(input())
C=round(sqrt((x+2)**2+(y-2)**2), 2)
s=x-5
if C<2 and y<s:
    print("Punkts atrodas figūras iekšā.")
elif C==2 or y==s:
    print("Punkts atrodas uz robežlīnijas.")
else:
    print("Punkts atrodas ārpus figūras.")