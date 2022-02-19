from collections import UserDict


class AddressBook(UserDict):

    def add_record(self, obj):
        if isinstance(obj, Record):
            self.data[obj.name] = obj

    def __str__(self) -> str:
        result = "\n".join([str(v) for v in self.data.values()])
        return result

    def del_record(self, obj):
        if isinstance(obj, Record):
            self.data[obj.name] = obj


class Record:

    def __init__(self, name, phone) -> None:
        self.name = name
        self.phones = []
        self.phones.append(phone)


class Field():
    pass


class Name():
    def __init__(self, name):
        self.value = name


class Phone():
    def __init__(self, phone):
        self.value = phone


if __name__ == '__main__':
    ab = AddressBook()
    record = Record('Bill', '23456777')
    ab.add_record(record)
    print(ab.data.keys(), ab.data.values())
    print(AddressBook())
