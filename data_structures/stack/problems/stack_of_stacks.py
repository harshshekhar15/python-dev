"""
Imagine a (literal) stack of plates. If the stack gets too high, it might topple. Therefore,
in real life we would likely start a new stack when the previous stack exceeds some threshold.
Implement a data structure SetofStacks that mimics this. SetOfStacks should be composed of 
several stacks and should create a new stack once the previous exceeds capacity. SetofStacks.push()
and SetOfStacks.pop() should behave identically to a single stack(that is pop() should return the
same values as it would if there were just a single stack).

Follow up:
Implement a function popAt(int index) which performs a pop operation on a specific sub - stack. 
"""

class SetofStacks:
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.stacks = []
    
    def __str__(self)-> str:
        return str(self.stacks)
    
    def push(self, item):
        """
        There can be two situations:
        - Stack is empty: Append the item to the stack.
        - Stack is non-empty: This too will have two situations -
            - Last stack is full - Append the item to the stack as a new stack.
            - Last stack is not full - Append the item to the last stack.
        """
        if len(self.stacks) > 0 and len(self.stacks[-1]) < self.capacity:
            self.stacks[-1].append(item)
        else:
            self.stacks.append([item])
    
    def pop(self):
        # Delete all the empty stacks first from the end
        while len(self.stacks) and len(self.stacks[-1]) == 0:
            self.stacks.pop()
        if len(self.stacks) > 0:
            return self.stacks[-1].pop()
        else:
            return None
    
    def popAt(self, index):
        if len(self.stacks[index]) > 0:
            return self.stacks[index].pop()
        else:
            return None

new_stack = SetofStacks(2)
print(new_stack)
new_stack.push(1)
new_stack.push(2)
new_stack.push(3)
print(new_stack)
new_stack.push(4)
print(new_stack)
print(new_stack.pop())
print(new_stack)
print(new_stack.pop())
print(new_stack)
print(new_stack.pop())
print(new_stack)
# print(new_stack.popAt(2))
# print(new_stack)