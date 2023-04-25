from . import gui
import pyautogui
from typing import Callable, Self, TypeVar

gui = gui.gui


C = TypeVar("C")


def alertImageNotFound(imgName):
    raise Exception(f"{imgName} não foi encontrado")


def doNothing(x=1, y=2):
    pass


def find(
    self: Self,
    imgName: str,
    waiting_time: int = 500,
    afterAction: Callable = lambda: pyautogui.press("enter"),
    notFoundAction: alertImageNotFound = alertImageNotFound,
):
    try:
        if not self.find(imgName, matching=0.93, waiting_time=waiting_time):
            notFoundAction(imgName)
        else:
            afterAction()
        return True
    except Exception as e:
        if gui.wrong(text=e)["tryAgain"]:
            return find(
                self,
                imgName,
                waiting_time=waiting_time,
                afterAction=afterAction,
                notFoundAction=notFoundAction,
            )


def tryToClick(self: Self, btnName: str, waiting_time: int = 2000):
    if not self.find(btnName, matching=0.93, waiting_time=waiting_time):
        try:
            self.find(f"{btnName}_r", matching=0.93, waiting_time=waiting_time)
            self.click()
        except Exception:
            raise Exception(f'o botão "{btnName}" não foi encontrado')
    else:
        self.click()


def click(self: Self, btnName: str, waiting_time: int = 2000, error=False):
    if error:
        self.tab()
    btn = btnName
    try:
        tryToClick(self, btn, waiting_time=waiting_time)
    except Exception as e:
        if gui.wrong(text=f"({btn})[{e}]")["tryAgain"]:
            click(self, btnName, waiting_time=waiting_time, error=not error)


def clickIfPossible(self, btn: str):
    find(
        self,
        btn,
        waiting_time=1000,
        afterAction=lambda: click(self, btn),
        notFoundAction=lambda imgName: print(imgName, "não achado mas segue o fluxo"),
    )


def remove_self_necessity(
    self: Self,
    func: C,
) -> C:
    def wrapper(*args, **kwargs):
        return func(self, *args, **kwargs)

    return wrapper


def with_types(thing):
    S = TypeVar("S")

    TIPO_CERTO = (find, click, clickIfPossible)

    def take_type(thing, type: S) -> S:
        return thing

    return take_type(thing, TIPO_CERTO)
