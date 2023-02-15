from collections import UserDict


class AddressBook(UserDict):

    def add_record(self, record):
        self.data.update({record.name.value: record})


class Record:
    def __init__(self, name, phone=None):
        self.name = name
        self.phones = [phone]

    def add(self, new_phone):
        self.phones.append(new_phone)

    def change(self, old_phone, new_phone):
        for i, ph in enumerate(self.phones):
            if ph == old_phone:
                self.phones[i] = new_phone
                break

    def delete(self, old_phone):
        for i, ph in enumerate(self.phones):
            if ph == old_phone:
                self.phones.pop(i)
                break


class Field:
    pass


class Name(Field):

    def __init__(self, value):
        self.value = value


class Phone(Field):
    def __init__(self, value):
        self.value = value


if __name__ == '__main__':
    name = Name('Bill')
    phone = Phone('1234567890')
    rec = Record(name, phone)
    ab = AddressBook()
    ab.add_record(rec)

    name = Name('Bill')
    phone = Phone('1234567890')
    rec = Record(name, phone)
    ab = AddressBook()
    ab.add_record(rec)

    assert isinstance(ab['Bill'], Record)
    assert isinstance(ab['Bill'].name, Name)
    assert isinstance(ab['Bill'].phones, list)
    assert isinstance(ab['Bill'].phones[0], Phone)
    assert ab['Bill'].phones[0].value == '1234567890'

    print('All Ok)')
