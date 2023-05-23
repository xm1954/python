import sys

def example_func():
    a = [1, 2, 3]  # 리스트 객체 생성
    b = a  # b가 a를 참조

example_func()
# example_func 함수가 종료되면서 a와 b는 더 이상 참조되지 않음
# 가비지 컬렉션은 a와 b 객체를 회수함
#위의 예제에서 example_func 함수가 실행되면 리스트 객체 a가 생성되고, 
변수 b가 a를 참조합니다. 그러나 함수가 종료되면서 a와 b는 더 이상 
참조되지 않으므로 가비지 컬렉션에 의해 회수됩니다.


#2번째 예제

# import gc

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None

# # 순환 참조 생성
# node1 = Node(1)
# node2 = Node(2)
# node1.next = node2
# node2.next = node1

# # 순환 참조가 있는 객체는 가비지 컬렉션에 의해 회수됨
# del node1
# del node2

# # 명시적으로 가비지 컬렉션 실행
# gc.collect()


# Node 클래스는 다음 노드를 가리키는 next 속성을 가집니다. node1과 node2는 서로를 참조하여 순환 참조를 생성합니다. 그러나 del 키워드를 사용하여 node1과 node2를 삭제하면 순환 참조가 끊어지고, 가비지 컬렉션에 의해 회수됩니다. 마지막으로 gc.collect()를 호출하여 명시적으로 가비지 컬렉션을 실행합니다.