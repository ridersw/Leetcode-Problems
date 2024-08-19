class MyQueue:

    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []
        self.top_element = None

    def push(self, x: int) -> None:
        self.stack_1.append(x)

        if not self.top_element:
            self.top_element = x
        
        print(f'stack_1: {self.stack_1}')

    def pop(self) -> int:
        while self.stack_1:
            res = self.stack_1.pop()
            self.stack_2.append(res)

        self.stack_2.pop()
        while self.stack_2:
            ele = self.stack_2.pop()
            self.stack_1.append(ele)
        print(f'stack_1: {self.stack_1}')
        return res

    def peek(self) -> int:
        return self.stack_1[0]
        

    def empty(self) -> bool:
        # print(f'stack_1: {self.stack_1}')
        # print(f'stack_2: {self.stack_2}')
        # print(f'curr_stack: {self.curr_stack}')
        return len(self.stack_1) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

# Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

# Implement the MyQueue class:

# void push(int x) Pushes element x to the back of the queue.
# int pop() Removes the element from the front of the queue and returns it.
# int peek() Returns the element at the front of the queue.
# boolean empty() Returns true if the queue is empty, false otherwise.
# Notes:

# You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
# Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.
 

# Example 1:

# Input
# ["MyQueue", "push", "push", "peek", "pop", "empty"]
# [[], [1], [2], [], [], []]
# Output
# [null, null, null, 1, 1, false]

# Explanation
# MyQueue myQueue = new MyQueue();
# myQueue.push(1); // queue is: [1]
# myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
# myQueue.peek(); // return 1
# myQueue.pop(); // return 1, queue is [2]
# myQueue.empty(); // return false
 

# Constraints:

# 1 <= x <= 9
# At most 100 calls will be made to push, pop, peek, and empty.
# All the calls to pop and peek are valid.