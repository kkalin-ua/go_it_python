users = [{
    "Bob": {"phones": ["30674567676"]},
    "Peter":{"phones": ['6751852326']},
    "Olga":{"phones": ['050 1525452']},
    "Mike":{"phones": ['0661234567']},
    "Anna":{"phones": ['044 2441856']},
    "Nick":{"phones": ['']},
    "lia":{"phones": ['']},
    "":{"phones": ['067 155545455']}
}]


def input_error(function):
    def inner(string):
        try:
            return function(string)
        except KeyError:
            return "Enter user name"
        except ValueError:
            return "Give me name and phone, please"
        except IndexError:
            return "Give me name and phone, please"
    return inner


@input_error
def add_new_contact(command):
    global users
    new_name = command.lower().split()[1]
    new_nubber = command.lower().split()[2]

    for user in users:
        cont = [x.strip() for x in new_nubber.split(',')]
        user[new_name] = {"phones": cont}


@input_error
def change_contact(command):
    new_name = command.lower().split()[1]
    new_number = command.lower().split()[2]

    for i in users:
        for nam, val in i.items():
            if new_name == nam.lower():
                new_number = [x.strip() for x in new_number.split(',')]
                val["phones"] = new_number


def exit_command():
    print("Good bye!")


def greeting_command():
    print("How can I help you?")


def show_all_command():
    for i in users:
        for nam, val in i.items():
            print(nam + ": " + (", ".join(val["phones"])))


@input_error
def show_phone(command):
    name = command.lower().split()[1]
    for i in users:
        for nam, val in i.items():
            if name == nam.lower():
                print(nam + ": " + (", ".join(val["phones"])))


# **************************
EXIT_COMMANDS = ("good bye", "close", "exit", "bye")
ADD_COMMANDS = ("add", "+")  # ++++++++++++++++++++
GREETING_COMMANDS = ("hello", "alloha",)
SHOW_PHONE_COMMANDS = ("phone",)
SHOW_ALL_COMMANDS = ("show all",)  # **************************
CHANGE_COMMANDS = ("change",)


COMMANDS = {
    ADD_COMMANDS: add_new_contact,
    GREETING_COMMANDS: greeting_command,
    SHOW_PHONE_COMMANDS: show_phone,
    SHOW_ALL_COMMANDS: show_all_command,
    EXIT_COMMANDS: exit_command,
    CHANGE_COMMANDS: change_contact}


def get_handler(operator):
    return COMMANDS[operator]


def main():

    command = input('For start program, print Hello: ')
    if command.lower() in GREETING_COMMANDS:
        greeting_command()

        while True:
            command = input('Imput command: ')
            comma = command.lower().split()[0]
            command_len = len(command.split())

            if comma in ADD_COMMANDS and command_len >= 3:
                get_handler(ADD_COMMANDS)(command)
#                print(users)

            elif comma in SHOW_PHONE_COMMANDS and command_len >= 2:
                get_handler(SHOW_PHONE_COMMANDS)(command)

            elif comma in CHANGE_COMMANDS and command_len >= 3:
                get_handler(CHANGE_COMMANDS)(command)
#                print(users)

            elif command.lower() in SHOW_ALL_COMMANDS:
                get_handler(SHOW_ALL_COMMANDS)()

            elif command.lower() in EXIT_COMMANDS:
                exit_command()
                break


# if __name__ == "__main__":
#     main()


main()
