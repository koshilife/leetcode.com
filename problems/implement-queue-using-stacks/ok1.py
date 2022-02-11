#!/usr/bin/env python3

'''
https://leetcode.com/problems/implement-queue-using-stacks/
'''

class MyQueue:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        return None if self.empty() else self.queue.pop(0)

    def peek(self) -> int:
        return None if self.empty() else self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0

if __name__ == "__main__":
    queue = MyQueue()
    print(queue.push(1) == None)
    print(queue.push(2) == None)
    print(queue.peek() == 1)
    print(queue.pop() == 1)
    print(queue.empty() == False)
