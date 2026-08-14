#เขียน function name convert currency ที่ทำหน้าที่ในการเเปลงสกุล


EXCHANGE_RATE = 33 

def main():
    print("Currency Converter")
    print("1. THB to USD")
    print("2. USD to THB")

    choice = input("Choose conversion direction (1 or 2): ")

    if choice == "1":
        amount = float(input("Enter amount in THB: "))
        result = amount / EXCHANGE_RATE
        print(f"\nFormula used: USD = THB / {EXCHANGE_RATE}")
        print(f"{amount:.2f} THB = {result:.2f} USD")

    elif choice == "2":
        amount = float(input("Enter amount in USD: "))
        result = amount * EXCHANGE_RATE
        print(f"\nFormula used: THB = USD * {EXCHANGE_RATE}")
        print(f"{amount:.2f} USD = {result:.2f} THB")

if __name__ == "__main__":
    main()