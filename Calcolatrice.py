def scegli_operazione():
    mappa = {
        'somma': '+', 'addizione': '+', '+': '+',
        'sottrazione': '-', 'meno': '-', '-': '-',
        'moltiplicazione': '*', 'per': '*', '*': '*',
        'divisione': '/', 'dividi': '/', '/': '/'
    }
    prompt = "Scegli l'operazione (+, -, *, /) o scrivi 'somma', 'sottrazione', 'moltiplicazione', 'divisione': "
    while True:
        scelta = input(prompt).strip().lower()
        if scelta in mappa:
            return mappa[scelta]
        print("Operazione non valida. Riprova.")


def leggi_numero(prompt):
    while True:
        s = input(prompt).strip().replace(',', '.')
        if any(ch.isalpha() for ch in s):
            print("Errore: non inserire lettere. Inserisci un numero.")
            continue
        try:
            return float(s)
        except ValueError:
            print("Input non valido. Inserisci un numero (es. 3.14).")


def main():
    op = scegli_operazione()
    a = leggi_numero("Inserisci il primo numero: ")
    while True:
        b = leggi_numero("Inserisci il secondo numero: ")
        if op == '/' and b == 0:
            print("Errore: divisione per zero. Inserisci un secondo numero diverso da zero.")
            continue
        break

    if op == '+':
        risultato = a + b
    elif op == '-':
        risultato = a - b
    elif op == '*':
        risultato = a * b
    elif op == '/':
        risultato = a / b

    # mostra risultato; se è intero lo mostriamo senza decimali
    if risultato.is_integer():
        print(f"Risultato: {int(risultato)}")
    else:
        print(f"Risultato: {risultato}")


if __name__ == "__main__":
    main()