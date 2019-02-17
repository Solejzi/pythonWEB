with open("zadanie_4_triangle_big.txt", "r+") as file:
    nums = list()

    for line in file.readlines():
        trimmed_line = line.strip(" ")
        str_nums = trimmed_line.split()
        row = list()

        for str_num in str_nums:
            if str_num:
                row.append(int(str_num))
        nums.append(row)

    last_row = list()

    for row in nums:
        if len(last_row) > 0:  # pomijamy pierwszy wiersz
            for idx, num in enumerate(row):
                if idx == 0:
                    row[idx] += last_row[idx]
                elif idx == len(row) - 1:
                    row[idx] += last_row[idx - 1]
                else:
                    rsum = row[idx] + last_row[idx - 1]
                    lsum = row[idx] + last_row[idx]

                    row[idx] = max(rsum, lsum)

        last_row = row

    print(max(nums[-1]))