# Crea una calcolatrice che chiede all'utente di inserire due numeri e un'operazione
# e poi esegue l'operazione tra i due numeri
from math import sqrt

hello_message = """

Ciao! Sono una calcolatrice semplice.
Inserisci due numeri e un'operazione, e ti mostrerò il risultato.

Operazioni disponibili:
- addizione (+)
- sottrazione (-)
- moltiplicazione (*)
- divisione (/)
- potenza (**)
- radice quadrata (√)

"""

while True:
    print(hello_message)
    
    action = input("Inserisci l'operazione: ")

    if action == "addizione" or action == "+":
        numero1 = float(input("Inserisci il primo numero: "))
        numero2 = float(input("Inserisci il secondo numero: "))
        risultato = numero1 + numero2
        print(f"Il risultato dell'addizione è: {risultato}")
    elif action == "sottrazione" or action == "-":
        numero1 = float(input("Inserisci il primo numero: "))
        numero2 = float(input("Inserisci il secondo numero: "))
        risultato = numero1 - numero2
        print(f"Il risultato della sottrazione è: {risultato}")
    elif action == "moltiplicazione" or action == "*":
        numero1 = float(input("Inserisci il primo numero: "))
        numero2 = float(input("Inserisci il secondo numero: "))
        risultato = numero1 * numero2
        print(f"Il risultato della moltiplicazione è: {risultato}")
    elif action == "divisione" or action == "/":
        numero1 = float(input("Inserisci il primo numero: "))
        numero2 = float(input("Inserisci il secondo numero: "))
        if numero2 == 0:
            print("Errore: divisione per zero. Inserisci un secondo numero diverso da zero.")
            continue
        risultato = numero1 / numero2
        print(f"Il risultato della divisione è: {risultato}")
    elif action == "potenza" or action == "**":
        numero1 = float(input("Inserisci il primo numero: "))
        numero2 = float(input("Inserisci il secondo numero: "))
        risultato = numero1 ** numero2
        print(f"Il risultato della potenza è: {risultato}")
    elif action == "radice quadrata" or action == "√":
        numero1 = float(input("Inserisci il numero: "))
        risultato = numero1 ** 0.5
        print(f"Il risultato della radice quadrata è: {sqrt(numero1)}")
    else:
        print("Operazione non valida. Riprova.")

    continue_message = "Vuoi continuare? (s/n): "
    continue_answer = input(continue_message).strip().lower()
    if continue_answer == "n":
        break
    elif continue_answer == "s":
        continue
    else:
        print("Risposta non valida. Riprova.")
        continue
    