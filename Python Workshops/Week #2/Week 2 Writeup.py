grade_lists = [73, 92, 89, 90]
add = input("Add your final grade: ")
v = int(add)
grade_lists.append(v)

def calc():
    total = sum(grade_lists) / 5
    return total

b = calc()
print(b)