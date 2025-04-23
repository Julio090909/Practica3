def exchange_money(budget, exchange_rate):
    return budget * exchange_rate


def main():
    print("=== Calculadora de Divisas ===")

    try:
        budget = float(input("Ingrese el monto en su moneda original (por ejemplo, USD): "))
        exchange_rate = float(input("Ingrese la tasa de cambio (1 USD equivale a cuánta moneda local): "))

        resultado = exchange_money(budget, exchange_rate)

        print(f"\nCon un presupuesto de {budget} y una tasa de cambio de {exchange_rate},")
        print(f"el equivalente en la moneda local es: {round(resultado, 2)}\n")

    except ValueError:
        print("❌ Por favor, ingrese valores numéricos válidos.")


if __name__ == "__main__":
    main()