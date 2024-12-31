"""
Implement (code) a Key value store with transactions.

Write a Fully funcitonal code in 25-30 min in interview with test cases

Set
Get
Delete are methods in Key value store

for transactions
Begin
Commit
Rollback

"""


class KeyValueStore:
    def __init__(self):
        self.stack = [{}]
    
    def set(self, key, value):
        self.stack[-1][key] = value
    
    def get(self, key):
        for index in range(self.stack[-1], -1, -1):
            if key in self.stack[index]:
                return self.stack[index][key]
        return Exception(f"Key not found")
            
        # if key in self.store.keys():
        #     return self.store[key]
        # else:
        #     return Exception(f"Key not found")
    
    def delete(self, key):
        for index in range(len(self.stack)-1, -1, -1):
            if key in self.stack[index]:
                # del self.stack[index][key]
                self.stack[-1][key] = None
        return Exception(f"Key not found")
        # self.stack[-1][key] = None
        # if key in self.store.keys():
        #     del self.store[key]
        # else:
        #     return Exception(f"Key not found")
    
    def begin(self):
        self.stack.append({})
    
    def commit(self):
        if len(self.stack) > 1:
            last_dict = self.stack.pop()
            for key, value in last_dict.items():
                # if value is None and key in self.stack[-1].keys():
                if value is None:
                    del self.stack[-1][key]
                # elif value is None and key not in self.stack[-1].keys():
                #     continue
                else:
                    self.stack[-1][key] = value
    
    def rollback(self):
        self.stack.pop()
            

new_store = KeyValueStore()
# print(new_store.commit())
# print(new_store.commit())
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
print(new_store.delete(4))
print(new_store.stack)
new_store.commit()
# new_store.rollback()
print("********")
print(new_store.stack)
print(new_store.commit())
print(new_store.commit())
print("********Stack after multiple false commits********")
print(new_store.stack)