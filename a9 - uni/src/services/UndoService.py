from src.ui.errors import *
class FunctionCall:
    def __init__(self, fun_name, *fun_params):
        self.__fun_name = fun_name
        self.__fun_params = fun_params

    def call(self):
        return self.__fun_name(*self.__fun_params)

    def __call__(self, *args, **kwargs):
        # overload the function call operator -- ()
        return self.call()


class Operation:
    def __init__(self, fundo: FunctionCall, fredo: FunctionCall):
        self.__fundo = fundo
        self.__fredo = fredo

    def undo(self):
        return self.__fundo()  # <=> to self.__fundo.call()

    def redo(self):
        return self.__fredo()


class UndoError(Exception):
    pass


class UndoService:
    def __init__(self):
        # history of the program's operations
        self.__history = []
        self.__index = 0

    def record(self, oper: Operation):
        self.__history.append(oper)
        self.__index += 1

    def undo(self):
        if self.__index == 0:
            raise ValidationException("No more undos")
        self.__index -= 1
        self.__history[self.__index].undo()

    def redo(self):
        if self.__index >= len(self.__history):
            raise ValidationException("No more redos")
        self.__history[self.__index].redo()
        self.__index += 1

