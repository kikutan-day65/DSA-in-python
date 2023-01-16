class Cookie:
    def __init__(self, color):
        self.color = color
    
    def get_color(self):
        return self.color
    
    def set_color(self, color):
        self.color = color

cookie1 = Cookie("green")
cookie2 = Cookie("bule")

print("cookie1 is", cookie1.get_color())
print("cookie2 is", cookie2.get_color())

cookie1.set_color("yellow")
print("cookie1 is", cookie1.get_color())
print("cookie2 is", cookie2.get_color())