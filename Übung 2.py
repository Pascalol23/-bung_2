class Vector3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"({self.x},{self.y},{self.z})"
    
    def __add__(self, other):

        if type(other) == int or type(other) == float:
            return Vector3(self.x + other, self.y + other, self.z + other)
        else:
            return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other):
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            return Vector3(self.x * other, self.y * other, self.z * other)
        else:
            return Vector3(self.x * other.x, self.y * other.y, self.z * other.z)
    
    def __rmul__(self, other):
        return Vector3(self.x * other, self.y * other, self.z * other)
    
   

    def cross(self, other):
        return Vector3((self.y * other.z)-(self.z * other.y), (self.z * other.x)-(self.x * other.z), (self.x * other.y)-(self.y * other.x))

    def dot(self, other):
        return float((self.x * other.x) + (self.y * other.y) + (self.z * other.z))
    
    def normalize(self, other):
        return Vector3(round(self.x/(self.x*2+self.x+self.x)**0.5, 3), round(self.x/(self.x+self.x+self.x)**0.5, 3), round(self.x/(self.x+self.x+self.x)**0.5, 3))


a = Vector3(3,4,2)
b = Vector3(2,1,0)


v10 = a +b

print(v10)
v10 = a -b

print(v10)
v10 = a*b

print(v10)

v11 = a.cross(b)
print(v11)

v11 = a.dot(b)
print(v11)

v12 = a.normalize(a)
print(v12.x,v12.y,v12.z)