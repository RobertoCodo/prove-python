def controlla_input_numerico(messaggio):
    # Funzione per controllare che l'input sia numerico
    # Restituisce il numero se valido, altrimenti chiede nuovamente l'input
    while True:
        try:
            numero = float(input(messaggio))
            return numero
        except ValueError:
            print("Errore: Inserisci solo numeri! Le lettere non sono valide.")
            print("Riprova...")

def calcolatrice():
    # Funzione principale della calcolatrice
    # Mostra il titolo della calcolatrice
    print()
    print("=== CALCOLATRICE PYTHON ===")
    print()
    
    # Menu delle operazioni disponibili
    print("Operazioni disponibili:")
    print("1. Addizione (+)")
    print("2. Sottrazione (-)")
    print("3. Moltiplicazione (*)")
    print("4. Divisione (/)")
    print("5. Potenza (**)")
    print("6. Radice quadrata (√)")
    print()
    
    # Controllo input per l'operazione
    while True:
        try:
            scelta = input("Quale operazione vuoi eseguire? (1-6): ")
            if scelta in ['1', '2', '3', '4', '5', '6']:
                break
            else:
                print("Errore: Inserisci un numero da 1 a 6!")
        except:
            print("Errore: Input non valido! Inserisci un numero da 1 a 6.")
    
    # Chiedi il primo numero
    primo_numero = controlla_input_numerico("Inserisci il primo numero: ")
    
    # Chiedi il secondo numero (non necessario per la radice quadrata)
    if scelta != '6':
        secondo_numero = controlla_input_numerico("Inserisci il secondo numero: ")
    
    # Esegui l'operazione scelta
    risultato = 0
    operazione = ""
    
    if scelta == '1':
        risultato = primo_numero + secondo_numero
        operazione = f"{primo_numero} + {secondo_numero}"
    elif scelta == '2':
        risultato = primo_numero - secondo_numero
        operazione = f"{primo_numero} - {secondo_numero}"
    elif scelta == '3':
        risultato = primo_numero * secondo_numero
        operazione = f"{primo_numero} * {secondo_numero}"
    elif scelta == '4':
        if secondo_numero == 0:
            print("Errore: Non puoi dividere per zero!")
            return
        risultato = primo_numero / secondo_numero
        operazione = f"{primo_numero} / {secondo_numero}"
    elif scelta == '5':
        risultato = primo_numero ** secondo_numero
        operazione = f"{primo_numero} ** {secondo_numero}"
    elif scelta == '6':
        if primo_numero < 0:
            print("Errore: Non puoi calcolare la radice quadrata di un numero negativo!")
            return
        risultato = primo_numero ** 0.5
        operazione = f"√{primo_numero}"
    
    # Mostra il risultato
    print()
    print(f"Risultato: {operazione} = {risultato}")
    
    # Chiedi se vuole continuare
    while True:
        continua = input("\nVuoi fare un'altra operazione? (sì/no): ").lower()
        if continua in ['sì', 'si', 's', 'yes', 'y']:
            print("\n" + "="*50 + "\n")
            calcolatrice()
            return
        elif continua in ['no', 'n']:
            print("Grazie per aver usato la calcolatrice! Arrivederci!")
            print()
            return
        else:
            print("Risposta non valida. Inserisci 'sì' o 'no'.")

# Avvia la calcolatrice
if __name__ == "__main__":
    calcolatrice()
