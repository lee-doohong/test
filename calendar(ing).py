import calendar

def days_diff(a, b):
    data = sorted([a, b], reverse=True)
    a = data[0]
    b = data[1]
    year_sub = (a[0] - b[0])*365
    day_sub = (a[2] - b[2])
    result = []
    # print(b[1], a[1])
    a_y = a[0]
    b_y = b[0]
    if a[0] == b[0] : b_y += 1
    for j in range(a_y, b_y):
        for i in range(b[1], a[1]) :
            # print(calendar.monthrange(a[0], i)[1])
            result.append(calendar.monthrange(j, i)[1])
    month_sub = sum(result)
    return year_sub + month_sub + day_sub





# print(days_diff((1982, 4, 19), (1982, 4, 22)))
# print(days_diff((2014, 1, 1), (2014, 8, 27)))


if __name__ == '__main__':
    print("Example:")
    print(days_diff((1982, 4, 19), (1982, 4, 22)))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
    assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
    assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238
    print("Coding complete? Click 'Check' to earn cool rewards!")
