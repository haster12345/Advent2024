def day_one():
    with open(r'inputs/day1.txt') as f:
        txt = f.read()
        lines = txt.split('\n')
        left_list = []
        right_list = []
        out = 0

        for row in lines:
            if not row:
                continue

            num_left = row[:5].strip()
            num_right = row[-5:].strip()
            left_list.append(num_left)
            right_list.append(num_right)

        left_list.sort()
        right_list.sort()

        for lnum, rnum in zip(left_list, right_list):
            out += abs(int(lnum) - int(rnum))

        return out

def day_two():
    with open(r'inputs/day2.txt') as f:
        txt = f.read()
        lines = txt.split('\n')
        print(lines)


if __name__ == "__main__":
    print(day_two())
