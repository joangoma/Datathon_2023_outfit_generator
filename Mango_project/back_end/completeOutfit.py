## INCOMPLETO

class clothe:
    Type: list[bool]    # which type of clothe is

    def __init__(self):
        self.Type = [False for _ in range(5)]

    def getType(self) -> list[bool]:
        return self.Type


class outfit:


def init() -> 


def complete_outfit(clothes: list[str]) -> list[str]:
    init()
    
    current_outfit: list[bool] = [False for _ in range(5)]

    # Update current outfit with the input data outfit
    for i in range(len(clothes)):     
        Type = findClothe(clothes[i]).getType()
        for j in range(len(Type)):
            current_outfit[j] = current_outfit[j] or Type[j]

