import gc

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# 순환 참조 생성
a = Node(1)
b = Node(2)
a.next = b
b.next = a

# 가비지 컬렉션 수행
gc.collect()

# 객체가 해제되지 않음
print(a.value)  # 출력: 1
print(b.value)  # 출력: 2

import gc

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# 순환 참조 끊기
a = Node(1)
b = Node(2)
a.next = b
b.next = None  # 순환 참조 끊기

# 가비지 컬렉션 수행
gc.collect()

# 객체가 해제됨
print(a.value)  # NameError: name 'a' is not defined
print(b.value)  # NameError: name 'b' is not defined