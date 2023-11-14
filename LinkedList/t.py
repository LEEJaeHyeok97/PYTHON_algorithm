# Linked List는 메모리상에서 연속성을 유지하지 않아도 되기 때문에 메모리 사용이 좀 더 자유롭다.
# 다만, next node의 address도 추가적으로 저장해야 하기 때문에 데이터 하나당 차지하는 메모리가 더 커지게 된다.

#Node 구현
class Node:
    def __init__(self, value = 0, next = None):
        self.value = value
        self.next = next

first = Node(1)
second = Node(2)
third = Node(3)

first.next = second
second.next = third

