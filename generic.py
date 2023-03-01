from typing import TypeVar, Generic
T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(Generic[T]):
        self.array: list[T] = []
        self.top: int = -1

    def push(self, value: T):
        self.array.append(value)
        self.top += 1

    def pop(self) -> T:
        self.array.append(value)
        self.top += 1

    def pop(self) -> T:
        if -1 is self.top:
            raise Exception("Stack underflow")
        pop_value = self.array[self.top]
        self.top -= 1
        return pop_value
    
st = Stack[int]()
st.push(5)
st.push(1)
st.push(7)

print(st.pop())
print(st.pop())
print(st.pop())