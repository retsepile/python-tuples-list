# Exercise 2
def common_member(ages, ages1):
    for x in ages:
        for y in ages1:
            if x == y:
                result = True
                return result


print(common_member([2, 12, 12, 14, 15, 16, 16, 17, 18, 14, 20, 20], [2, 4, 12, 14, 15, 16, 16, 17, 18, 14, 20, 20]))
