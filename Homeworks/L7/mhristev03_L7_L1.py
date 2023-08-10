""" 
Създайте клас Fibs за редицата на Фибоначи, реализиращ протокола за итериране. 
Следният код  трябва да може да се изпълнява върху него

fbs = Fibs()
for f in fbs:
    if f > 1000:
    print(f)
    break
"""
class Fibs:
    def __init__(self):
        self.prev = 0
        self.curr = 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        fib = self.prev
        self.prev, self.curr = self.curr, self.prev + self.curr
        return fib
