with open('rows.txt', 'r+') as file:
    file.seek(0)
    listing = []
    for row in file:
        for num in row:
            if num != ' ':
                listing.append(num)
            else:
                pass
    mini = 999999999999
    maxi = 0
    list_of_nums = []
    list_of_diff = []
    current_num = ''
    listing.append('\n')
    for i in listing:
        if i == '\n':
            maxi = max(list_of_nums)
            mini = min(list_of_nums)
            list_of_nums.clear()
            list_of_diff.append(maxi - mini)
        if i != '\t' and i != '\n':
            current_num += i
        else:
            integer = int(current_num)
            list_of_nums.append(integer)
            current_num=''
    sum = 0
    print(list_of_diff)
    for number in list_of_diff:
        sum += number
    print(sum)

