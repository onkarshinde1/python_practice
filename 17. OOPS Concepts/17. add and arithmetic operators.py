class Distance:
    def __init__(self, km):
        self.km = km

    def __add__(self, other):
        return self.km + other.km

    def __sub__(self, other):
        return self.km - other.km

    def __mul__(self, times):
        return self.km * times

    def __str__(self):
        return f"{self.km} km"


d1 = Distance(10)
d2 = Distance(5)
print(d1 + d2)

print(d1 + d2)  # 15 km
print(d1 - d2)  # 5 km
print(d1 * 3)  # 30 km
