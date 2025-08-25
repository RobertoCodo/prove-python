#!/usr/bin/env python3
# Calcolatrice semplice - chiede operazione, poi due numeri, con controllo input alfabetico

def scegli_operazione():
    ops = {
        '+': 'add',
        'somma': 'add',
        '-': 'sub',
        'sottrazione': 'sub',
        '*': 'mul',
        'x': 'mul',
        'moltiplicazione': 'mul',
        '/': 'div',
        'divisione': 'div'
    }
    while True:
        scelta = input("Quale operazione vuoi eseguire? (+, -, *, / o 'somma', 'sottrazione', 'moltiplicazione', 'divisione'): ").strip().lower()
        if any(c.isalpha() for c in scelta) and scelta not in ops:
            # Se l'utente ha inserito lettere non riconosciute come nomi di operazioni
            print("Errore: input non valido. Inserisci una delle operazioni consentite.")
            continue
        if scelta in ops:
            return ops[scelta]
        print("Operazione non riconosciuta. Riprova.")

def leggi_numero(prompt):
    while True:
        s = input(prompt).strip()
        if any(c.isalpha() for c in s):
            print("Errore: inserire solo numeri (nessun carattere alfabetico). Riprova.")
            continue
        try:
            return float(s)
        except ValueError:
            print("Errore: input non valido. Assicurati di inserire un numero valido (es. 3.5).")

def calcola(op, a, b):
    if op == 'add':
        return a + b
    if op == 'sub':
        return a - b
    if op == 'mul':
        return a * b
    if op == 'div':
        if b == 0:
            raise ZeroDivisionError("Divisione per zero")
        return a / b
    raise ValueError("Operazione sconosciuta")

def main():
    op = scegli_operazione()
    a = leggi_numero("Inserisci il primo numero: ")
    b = leggi_numero("Inserisci il secondo numero: ")
    try:
        risultato = calcola(op, a, b)
    except ZeroDivisionError:
        print("Errore: divisione per zero non consentita.")
        return
    # Stampa risultato senza .0 se è intero
    if risultato == int(risultato):
        print("Risultato:", int(risultato))
    else:
        print("Risultato:", risultato)

if __name__ == "__main__":
    main()