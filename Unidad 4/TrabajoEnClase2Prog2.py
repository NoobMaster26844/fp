Cap = int(input("Cantidad a invertir: $"))
Intereses = int(input("Interés anual: %"))
Años = int(input("Años a invertir: "))
I = Intereses/100
L = Cap*I
E = Cap*L
R = E*Años

print("Capital Final: $",R)
print("FIN")