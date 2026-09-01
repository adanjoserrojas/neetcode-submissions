class MinStack:

    def __init__(self):
        self.arr: list = []
        self.minu: list = []

    def push(self, val: int) -> None:

        if not self.minu:
            self.minu.append(val)
        else:
            if self.minu[-1] >= val:
                self.minu.append(val)

        self.arr.append(val)

    def pop(self) -> None:
        if self.arr[-1] == self.minu[-1]:
            self.minu.pop()
        self.arr.pop()
        

    def top(self) -> int:
        return self.arr[-1]
        
    def getMin(self) -> int:
        return self.minu[-1]


        
