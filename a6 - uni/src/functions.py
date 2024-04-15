#
# The program's functions are implemented here. There is no user interaction in this file, therefore no input/print statements. Functions here
# communicate via function parameters, the return statement and raising of exceptions. 
#

import random
from copy import deepcopy

def add_random_values():
    '''
    :return: a list with random values
    '''
    scores = []
    for i in range(10):
        scores.append((random.randint(0, 10), random.randint(0, 10), random.randint(0, 10)))
    return scores


def get_p1(score) -> int:
    return score[0]


def get_p2(score) -> int:
    return score[1]


def get_p3(score) -> int:
    return score[2]


def get_index(el):
    return el[3]


def get_average_score(score) -> int:
    return get_p1(score) + get_p2(score) + get_p3(score)


def set_p1(scores, pos, val):
    scores[pos] = (val, get_p2(scores[pos]), get_p3(scores[pos]))


def set_p2(scores, pos, val):
    scores[pos] = (get_p1(scores[pos]), val, get_p3(scores[pos]))


def set_p3(scores, pos, val):
    scores[pos] = (get_p1(scores[pos]), get_p2(scores[pos]), val)


def push_stack(scores_stack, scores):
    '''
    :param scores_stack: a list: stack for undo
    :param scores: list of scores
    :return: stack modified after an operation
    '''
    scores_stack.append(deepcopy(scores))
    return scores_stack


#A
def add_result(scores_stack, scores, p1, p2, p3):
    '''
    :param scores_stack: a list: stack for undo
    :param scores: list of scores
    :param p1: integer value of p1
    :param p2: integer value of p2
    :param p3: integer value of p3
    :return: list of scores modified with adding
    '''
    if 0 > p1 or 0 > p2 or 0 > p3 or 10 < p1 or 10 < p2 or 10 < p3 or p1 != int(p1) or p2 != int(p2) or p3 != int(p3):
        raise ValueError("Incorrect data")
    push_stack(scores_stack, scores)
    scores.append((p1, p2, p3))

    return scores


def insert_result(scores_stack, scores, p1, p2, p3, pos):
    '''
    :param scores_stack: stack for undo
    :param scores: list of scores
    :param p1: value of p1
    :param p2: value of p2
    :param p3: value of p3
    :param pos: position to inset
    :return: list of scores modified with insert
    '''
    if 0 > p1 or 0 > p2 or 0 > p3 or 10 < p1 or 10 < p2 or 10 < p3 or p1 != int(p1) or p2 != int(p2) or p3 != int(p3) or pos < 0 or pos != int(pos):
        raise ValueError("Incorrect data")
    push_stack(scores_stack, scores)
    scores[pos] = (p1, p2, p3)

    return scores


#B
def remove_score(scores_stack, scores, pos):
    '''
    :param scores_stack: stack for undo
    :param scores: list of scores
    :param pos: position to be modified
    :return: list of scores with modified scores from pos
    '''
    if pos >= len(scores) or pos < 0 or pos != int(pos):
        raise ValueError("Incorrect data")
    push_stack(scores_stack, scores)
    scores[pos] = (0, 0, 0)

    return scores


def remove_scores(scores_stack, scores, st, end):
    '''
    :param scores_stack: stack for undo
    :param scores: list of scores
    :param st: start position
    :param end: end position
    :return: list of scores with modified scores from st to end
    '''
    if st >= end or end >= len(scores) or st < 0 or st != int(st) or end != int(end):
        raise ValueError("Incorrect data")
    push_stack(scores_stack, scores)
    for i in range(st, end + 1):
        scores[i] = (0, 0, 0)
    return scores


def replace_score(scores_stack, scores, pos, p, val):
    '''
    :param scores_stack: stack for undo
    :param scores: list of scores
    :param pos: position in which modify the value
    :param p: the problem to modify value
    :param val: the new value
    :return: list of scores with new value
    '''
    if pos < 0 or pos >= len(scores) or val < 0 or val > 10 or pos != int(pos) or val != int(val):
        raise ValueError("Incorrect data")
    if p != "P1" and p != "P2" and p != "P3":
        raise ValueError("Incorrect data")
    push_stack(scores_stack, scores)
    if p == "P1":
        set_p1(scores, pos, val)
    elif p == "P2":
        set_p2(scores, pos, val)
    elif p == "P3":
        set_p3(scores, pos, val)
    return scores


#C
def get_list_by_average_score(scores, sign, score):
    '''
    :param scores: list of scores
    :param sign: string or > or < or =
    :param score: integer value of score tu be compared
    :return: list of participants who has the score in function of sign
    '''
    if sign != "=" and sign != ">" and sign != "<" or score != int(score):
        raise ValueError("Incorrect data")

    participants = []
    if sign == "=":
        for i in range(len(scores)):
            sc = scores[i]
            if get_average_score(sc) == score:
                participants.append(i)
    elif sign == ">":
        for i in range(len(scores)):
            sc = scores[i]
            if get_average_score(sc) > score:
                participants.append(i)
    elif sign == "<":
        for i in range(len(scores)):
            sc = scores[i]
            if get_average_score(sc) < score:
                participants.append(i)

    return participants


def sort_list_by_average(scores):
    '''
    :param scores: list of scores
    :return: sorted list of scores by average score
    '''
    n = len(scores)
    lst = []
    for i in range(n):
        lst.append((get_p1(scores[i]), get_p2(scores[i]), get_p3(scores[i]), i))
    for i in range(n - 1):
        for j in range(i + 1, n):
            if get_average_score(lst[i]) < get_average_score(lst[j]):
                lst[i], lst[j] = lst[j], lst[i]

    return lst


def sort_list_by_p1(scores):
    '''
    :param scores: list of scores
    :return: sorted list of scores by p1
    '''
    n = len(scores)
    lst = []
    for i in range(n):
        lst.append((get_p1(scores[i]), get_p2(scores[i]), get_p3(scores[i]), i))
    for i in range(n - 1):
        for j in range(i + 1, n):
            if get_p1(lst[i]) < get_p1(lst[j]):
                lst[i], lst[j] = lst[j], lst[i]

    return lst


def sort_list_by_p2(scores):
    '''
    :param scores: list of scores
    :return: sorted list of scores by p2
    '''
    n = len(scores)
    lst = []
    for i in range(n):
        lst.append((get_p1(scores[i]), get_p2(scores[i]), get_p3(scores[i]), i))
    for i in range(n - 1):
        for j in range(i + 1, n):
            if get_p2(lst[i]) < get_p2(lst[j]):
                lst[i], lst[j] = lst[j], lst[i]

    return lst


def sort_list_by_p3(scores):
    '''
    :param scores: list of scores
    :return: sorted list of scores by p3
    '''
    n = len(scores)
    lst = []
    for i in range(n):
        lst.append((get_p1(scores[i]), get_p2(scores[i]), get_p3(scores[i]), i))
    for i in range(n - 1):
        for j in range(i + 1, n):
            if get_p3(lst[i]) < get_p3(lst[j]):
                lst[i], lst[j] = lst[j], lst[i]

    return lst


#D
def get_top(scores, number):
    if number != int(number) or number > len(scores):
        raise ValueError("Incorrect data")

    lst = sort_list_by_average(scores)
    new_lst = []
    for i in range(number):
        new_lst.append(get_index(lst[i]))

    return new_lst


def get_top_p1(scores, number):
    if number != int(number) or number > len(scores):
        raise ValueError("Incorrect data")
    lst = sort_list_by_p1(scores)
    new_lst = []
    for i in range(number):
        new_lst.append(get_index(lst[i]))

    return new_lst


def get_top_p2(scores, number):
    if number != int(number) or number > len(scores):
        raise ValueError("Incorrect data")
    lst = sort_list_by_p2(scores)
    new_lst = []
    for i in range(number):
        new_lst.append(get_index(lst[i]))

    return new_lst


def get_top_p3(scores, number):
    if number != int(number) or number > len(scores):
        raise ValueError("Incorrect data")
    lst = sort_list_by_p3(scores)
    new_lst = []
    for i in range(number):
        new_lst.append(get_index(lst[i]))

    return new_lst


def remove_average_score(scores_stack, scores, sign, score):
    '''

    :param sign:
    :param score:
    :return:
    '''
    if sign != "=" and sign != ">" and sign != "<" or score != int(score):
        raise ValueError("Incorrect data")
    push_stack(scores_stack, scores)
    if sign == "=":
        for i in range(len(scores)):
            sc = scores[i]
            if get_average_score(sc) == score:
                set_p1(scores, i, 0)
                set_p2(scores, i, 0)
                set_p3(scores, i, 0)
    elif sign == ">":
        for i in range(len(scores)):
            sc = scores[i]
            if get_average_score(sc) > score:
                set_p1(scores, i, 0)
                set_p2(scores, i, 0)
                set_p3(scores, i, 0)
    elif sign == "<":
        for i in range(len(scores)):
            sc = scores[i]
            if get_average_score(sc) < score:
                set_p1(scores, i, 0)
                set_p2(scores, i, 0)
                set_p3(scores, i, 0)

    return scores


def undo_last_operation(scores, scores_stack):
    """
    Undo the last operation.

    :param scores: The list of scores.
    :param scores_stack: The scores history stack.
    :return: The list of scores with the last operation undone.
    """
    if len(scores_stack) == 0:
        raise ValueError("No more transactions to undo.")

    last_state = scores_stack.pop()
    scores.clear()
    scores.extend(last_state)

    return scores