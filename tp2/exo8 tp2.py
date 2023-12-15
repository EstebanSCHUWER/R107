x = float(input("Entrez un réel : "))

appartient_a_I = (x >= 2 and x < 3) or (x > 0 and x <= 1) or (x >= -10 and x <= -2)

if appartient_a_I:
    print(f"{x} appartient à I.")
else:
    print(f"{x} n'appartient pas à I.")
