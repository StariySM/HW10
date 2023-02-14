from collections import UserDict


class AddressBook(UserDict):

    def add_record(self, record):
        self.data.update({record.name.value: record})


class Record:
    def __init__(self, name, phone=None):
        self.name = Name(name)
        self.r_phones = Phone(phone)

    def add(self, new_phone):
        self.r_phones.phone.append(new_phone)

    def change(self, old_phone, new_phone):
        for i, ph in enumerate(self.r_phones.phone):
            if ph == old_phone:
                self.r_phones.phone[i] = new_phone
                break

    def delete(self, old_phone):
        for i, ph in enumerate(self.r_phones.phone):
            if ph == old_phone:
                self.r_phones.phone.pop(i)
                break


class Field:
    pass


class Name(Field):

    def __init__(self, name):
        self.value = name


class Phone(Field):
    def __init__(self, phone=None):
        self.value = []
        self.value.append(phone)


# rec1 = Record("Vasya", "11111")
# rec2 = Record("Dima", ['22222', "333333"])
# rec3 = Record("Jeka")
# friends = AddressBook()
# friends.add_record(rec1)
# friends.add_record(rec2)
# friends.add_record(rec3)
