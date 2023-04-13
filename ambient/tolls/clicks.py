from . import gui
import pyautogui


def alertImageNotFound(imgName):
    raise Exception(f"{imgName} não foi encontrado")


def doNothing(x=1, y=2):
    pass


def find(
    self,
    imgName,
    waiting_time=500,
    afterAction=lambda: pyautogui.press("enter"),
    notFoundAction=alertImageNotFound,
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


def tryToClick(self, btnName):
    if not self.find(btnName, matching=0.93, waiting_time=2000):
        try:
            self.find(f"{btnName}_r", matching=0.93, waiting_time=2000)
            self.click()
        except Exception:
            raise Exception(f'o botão "{btnName}" não foi encontrado')
    else:
        self.click()


def click(self, btnName, error=False):
    if error:
        self.tab()
    btn = btnName
    try:
        tryToClick(self, btn)
    except Exception as e:
        if gui.wrong(text=f"({btn})[{e}]")["tryAgain"]:
            click(self, btnName, error=not error)


def clickIfPossible(self, btn):
    find(
        self,
        btn,
        waiting_time=1000,
        afterAction=lambda: click(self, btn),
        notFoundAction=lambda imgName: print(imgName, "não achado mas segue o fluxo"),
    )


def remove_self_nescessity(self, func):
    def wrapper(*args, **kwargs):
        return func(self, *args, **kwargs)

    return wrapper
