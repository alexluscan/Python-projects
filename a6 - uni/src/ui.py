#
# This is the program's UI module. The user interface and all interaction with the user (print and input statements) are found here
#

import functions


def add_ui(com, stack, scores):
    if len(com) != 4:
        print("Invalid add command!")
    else:
        try:
            scores = functions.add_result(stack, scores, int(com[1]), int(com[2]), int(com[3]))
        except ValueError as ve:
            print("ERROR!")
            print(str(ve))

    return scores, stack


def insert_ui(com, stack, scores):
    if len(com) != 6:
        print("Invalid insert command")
    else:
        try:
            scores = functions.insert_result(stack, scores, int(com[1]), int(com[2]), int(com[3]), int(com[5]))
        except ValueError as ve:
            print("ERROR!")
            print(str(ve))
    return scores, stack


def replace_ui(com, stack, scores):
    if len(com) != 5:
        print("Invalid replace command")
    else:
        try:
            scores = functions.replace_score(stack, scores, int(com[1]), com[2], int(com[4]))
        except ValueError as ve:
            print("ERROR!")
            print(str(ve))
    return scores, stack


def remove_ui(com, stack, scores):
    if len(com) != 2 and len(com) != 3 and len(com) != 4:
        print("Invalid remove command")
    elif len(com) == 2:
        try:
            scores = functions.remove_score(stack, scores, int(com[1]))
        except ValueError as ve:
            print("ERROR!")
            print(str(ve))
    elif len(com) == 4:
        try:
            scores = functions.remove_scores(stack, scores, int(com[1]), int(com[3]))
        except ValueError as ve:
            print("ERROR!")
            print(str(ve))
    elif len(com) == 3:
        try:
            scores = functions.remove_average_score(stack, scores, com[1], int(com[2]))
        except ValueError as ve:
            print("ERROR!")
            print(str(ve))
    return scores, stack


def list_scores(scores):
  print(*scores, sep = "\n")


def list_participants(lst):
  print(*lst, sep = " ")

def display_ui(com, scores):
    if len(com) != 1 and len(com) != 2 and len(com) != 3:
        print("Invalid list command")
    elif len(com) == 1:
        list_scores(scores)
    elif len(com) == 2:
        try:
            lst = functions.get_top(scores, len(scores))
            list_participants(lst)
        except ValueError as ve:
            print("ERROR!")
            print(str(ve))
    elif len(com) == 3:
        try:
            lst = functions.get_list_by_average_score(scores, com[1], int(com[2]))
            list_participants(lst)
        except ValueError as ve:
            print("ERROR!")
            print(str(ve))


def display_top_ui(com, scores):
    if len(com) != 2 and len(com) != 3:
        print("Invalid top command")
    elif len(com) == 2:
        try:
            lst = functions.get_top(scores, int(com[1]))
            list_participants(lst)
        except ValueError as ve:
            print("ERROR!")
            print(str(ve))
    elif len(com) == 3:
        try:
            if com[2] == "P1":
                lst = functions.get_top_p1(scores, int(com[1]))
            if com[2] == "P2":
                lst = functions.get_top_p2(scores, int(com[1]))
            if com[2] == "P3":
                lst = functions.get_top_p3(scores, int(com[1]))
            list_participants(lst)
        except ValueError as ve:
            print("ERROR!")
            print(str(ve))


def process_command(command, scores, stack):
    commands = ["add", "insert", "remove", "replace", "list", "top", "undo"]

    if command[0] not in commands:
        print("This is an invalid command. Please try again")
        return scores, stack

    if command[0] == "add":
        scores, stack = add_ui(command, stack, scores)

    elif command[0] == "insert":
        scores, stack = insert_ui(command, stack, scores)

    elif command[0] == "remove":
        scores, stack = remove_ui(command, stack, scores)

    elif command[0] == "replace":
        scores, stack = replace_ui(command, stack, scores)

    elif command[0] == "list":
        display_ui(command, scores)

    elif command[0] == "top":
        display_top_ui(command, scores)

    elif command[0] == "undo":
        scores = functions.undo_last_operation(scores, stack)

    return scores, stack


def print_menu():
    print("The following commands are available:\n")
    print("add <P1 score> <P2 score> <P3 score>")
    print("insert <P1 score> <P2 score> <P3 score> at <position>")
    print("remove <position>")
    print("remove <start position> to <end position>")
    print("replace <old score> <P1 | P2 | P3> with <new score>")
    print("list")
    print("list sorted")
    print("list [ < | = | > ] <score>")
    print("top <number>")
    print("top <number> <P1 | P2 | P3>")
    print("remove [ < | = | > ] <score>")
    print("undo")


def print_ui():
  scores = functions.add_random_values()
  stack = []
  print_menu()
  while True:
    print("Enter a command: ")
    command = input().split()
    scores, stack = process_command(command, scores, stack)