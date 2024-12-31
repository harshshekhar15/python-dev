

class KeyValueStore:
    def __init__(self):
        self.stack = [{}]
    
    def set(self, key, value):
        self.stack[-1][key] = value
    
    def get(self, key):
        for index in range(len(self.stack)-1, -1, -1):
            if key in self.stack[index].keys():
                return self.stack[index][key]
        return None
    
    def delete(self, key):
        if self.get(key) != None:
            self.stack[-1][key] = None
    
    def begin(self):
        self.stack.append({})
    
    def commit(self):
        if len(self.stack) > 1:
            last_dict = self.stack.pop()
            for key, value in last_dict.items():
                if value is None:
                    del self.stack[-1][key]
                else:
                    self.stack[-1][key] = value
    
    def rollback(self):
        if len(self.stack) > 1:
            self.stack.pop()


new_store = KeyValueStore()
# print(new_store.rollback())
# print(new_store.rollback())
new_store.begin()
print(new_store.stack)
new_store.set(1, "abc")
new_store.set(2, "def")
new_store.set(3, "ghi")
print(new_store.stack)
print(new_store.commit())
print("********")
print(new_store.stack)
print("********")
new_store.begin()
new_store.set(1, "xyz")
print(new_store.delete(3))
print(f"Value of 3: {new_store.get(3)}")
print(new_store.stack)
# new_store.commit()
new_store.rollback()
print("********")
print(new_store.stack)
print(new_store.rollback())
print(new_store.rollback())
print("********Stack after multiple false commits********")
print(new_store.stack)