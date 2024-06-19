class OnlineSalesRegisterCollector:
    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}

    @property
    def name_items(self):
        return self.__name_items

    @property
    def number_items(self):
        return self.__number_items

    def add_item_to_cheque(self, name):
        if len(name) == 0 or len(name) > 40:
            raise ValueError('Нельзя добавить товар, если в его названии нет символов или их больше 40')
        elif name not in self.__item_price:
            raise NameError('Позиция отсутствует в товарном справочнике')
        else:
            self.__name_items.append(name)
            self.__number_items += 1

    def delete_item_from_check(self, name):
        if name not in self.__name_items:
            raise NameError('Позиция отсутствует в чеке')
        else:
            self.__name_items.remove(name)
            self.__number_items -= 1

    def check_amount(self):
        total = []
        for value in self.__item_price.values():
            if value in self.__name_items:
                total.append(value)
        if len(total) > 10:
            return sum(total) * 0.9
        return total

    def twenty_percent_tax_calculation(self):
        twenty_percent_tax = []
        total = []
        for key, value in self.__tax_rate.items():
            if key in self.__name_items:
                if value == 20:
                    twenty_percent_tax.append(key)
                    total.append(value)
        if len(total) > 10:
            return sum(total) * 0.2 * 0.9
        else:
            return sum(total) * 0.2

    def ten_percent_tax_calculation(self):
        ten_percent_tax = []
        total = []
        for key, value in self.__tax_rate.items():
            if key in self.__name_items:
                if value == 20:
                    ten_percent_tax.append(key)
                    total.append(value)
        if len(total) > 10:
            return sum(total) * 0.1 * 0.9
        else:
            return sum(total) * 0.1

    def total_tax(self):
        return self.ten_percent_tax_calculation() + self.twenty_percent_tax_calculation()

    @staticmethod
    def get_telephone_number(telephone_number):
        if type(telephone_number) not in [int, str]:
            raise ValueError('Необходимо ввести цифры')

        if type(telephone_number) == int:
            telephone_number = str(telephone_number)

        if not telephone_number.isdigit():
            raise ValueError('Необходимо ввести цифры')

        if len(telephone_number) != 10:
            raise ValueError('Необходимо ввести 10 цифр после "+7"')

        return f'+7{telephone_number}'


new_cheque = OnlineSalesRegisterCollector()
new_cheque.add_item_to_cheque('чипсы')
new_cheque.add_item_to_cheque('кола')
new_cheque.add_item_to_cheque('печенье')
new_cheque.add_item_to_cheque('молоко')
new_cheque.add_item_to_cheque('кефир')
print(new_cheque.name_items)
print(new_cheque.number_items)
print(new_cheque.check_amount())
print(new_cheque.ten_percent_tax_calculation())
print(new_cheque.twenty_percent_tax_calculation())
print(new_cheque.total_tax())
print(new_cheque.get_telephone_number('1234567890'))
new_cheque.delete_item_from_check('чипсы')
print(new_cheque.name_items)
print(new_cheque.number_items)
