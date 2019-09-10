import sys, json

currency_list = ['USD', 'EUR', 'GBP']
if len(sys.argv) != 2:
    print("usage: my_file.py argument, only one argument")
    exit(1)
else:
    carname = sys.argv[1].upper()
    with open('cars.json', 'r') as file:
        cars = json.load(file)
        try:
            print(cars['cars'][carname])
        except:
            price = input("Enter price for this car:")
            while not price.isdigit():
                price = input("Enter price for this car:")
            currency = input("Enter currency(USD, EUR, GBP):")
            while currency.upper() not in currency_list:
                currency = input("Enter currency(USD, EUR, GBP):")
            if currency.upper() == "EUR":
                price = float(price) * 1.11
                price = str(round(price))
            elif currency.upper() == "GBP":
                price = float(price) * 1.24
                price = str(round(price))
            print(price, " USD")
            data = {carname: price + " " + "USD"}
            cars['cars'].update(data)
            with open('cars.json', 'w') as file_car:
                json.dump(cars, file_car)
