print("Inserire due numeri da sommare")
print("Inserire 'q' per terminare")

while True:
    primo_numero = input("\nInserisci primo numero: ")
    if primo_numero == 'q':
        break
    secondo_numero = input("\nInserisci secondo numero: ")
    if secondo_numero == 'q':
        break
    try:
        risultato = int(primo_numero) + int(secondo_numero)
    except ValueError:
        print("Attenzione, si possono sommare SOLO numeri!")
    else:
        print(f"Il risultato della somma è: {risultato}")