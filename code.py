1 class Stack:
    2     def __init__(self):
    3         self.items = []
    4
    5     def push(self, item):
    6         """
    7         스택의 맨 위에 항목을 추가합니다.
    8         """
    9         self.items.append(item)
   10
   11     def pop(self):
   12         """
   13         스택의 맨 위 항목을 제거하고 반환합니다.
   14         스택이 비어 있으면 IndexError를 발생시킵니다.
   15         """
   16         if self.is_empty():
   17             raise IndexError("pop from empty stack")
   18         return self.items.pop()
   19
   20     def peek(self):
   21         """
   22         스택의 맨 위 항목을 반환하지만 제거하지는 않습니다.
   23         스택이 비어 있으면 IndexError를 발생시킵니다.
   24         """
   25         if self.is_empty():
   26             raise IndexError("peek from empty stack")
   27         return self.items[-1]
   28
   29     def is_empty(self):
   30         """
   31         스택이 비어 있으면 True를, 그렇지 않으면 False를 반환합니다.
   32         """
   33         return len(self.items) == 0
   34
   35     def size(self):
   36         """
   37         스택에 있는 항목의 수를 반환합니다.
   38         """
   39         return len(self.items)
   40
   41     def __str__(self):
   42         """
   43         스택의 문자열 표현을 반환합니다.
   44         """
   45         return str(self.items)