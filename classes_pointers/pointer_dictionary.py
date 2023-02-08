d1 = {"A": 1}
d2 = d1

print("Before updating :")
print(f"d1 : {d1}")
print(f"d2 : {d2}")

print(f"d1 points to : {id(d1)}")
print(f"d2 points to : {id(d2)}")

d2["A"] = 5
print("After updating :")
print(f"d1 : {d1}")
print(f"d2 : {d2}")

print(f"d1 points to : {id(d1)}")
print(f"d2 points to : {id(d2)}")

d3 = {"A": 8}
d2 = d3
print("After second update :")
print(f"d1 : {d1}")
print(f"d2 : {d2}")
print(f"d3 : {d3}")

print(f"d1 points to : {id(d1)}")
print(f"d2 points to : {id(d2)}")
print(f"d3 points to : {id(d3)}")

