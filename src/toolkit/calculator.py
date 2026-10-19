def tokenize(s):
    tokens = []
    now = ""
    need_num = True
    number_and = [str(i) for i in range(10)] + ["."]
    i = 0
    while i < len(s):
        c = s[i]
        if c == " ":
            i += 1
            continue
        if c == "/" and i + 1 < len(s) and s[i + 1] == "/":
            if now != "":
                tokens.append(now)
                now = ""
            tokens.append("//")
            need_num = True
            i += 2
            continue
        if c in number_and:
            now += c
            need_num = False
        elif c in "+-*/%":
            if c == "-" and need_num:
                now += c
                i += 1
                continue
            if now != "":
                tokens.append(now)
                now = ""
            tokens.append(c)
            need_num = True
        else:
            raise ValueError(f"Недопустимый символ: {c}")
        i += 1

    if now != "":
        tokens.append(now)

    return tokens


def calculate(tokens):
    if not tokens:
        raise ValueError("Пустое выражение")
    nums = []
    op = []
    for t in tokens:
        if t in "+-*/%//":
            op.append(t)
        else:
            nums.append(float(t))

    if len(nums) != len(op) + 1:
        raise ValueError("Пропущен операнд")

    i = 0
    while i < len(op):
        if op[i] in "*/%//":
            if op[i] == "*":
                nums[i] = nums[i] * nums[i + 1]
            elif op[i] == "/":
                if nums[i + 1] == 0:
                    raise ValueError("Деление на ноль")
                nums[i] = nums[i] / nums[i + 1]
            elif op[i] == "//":
                if nums[i + 1] == 0:
                    raise ValueError("Деление на ноль")
                nums[i] = float(int(nums[i]) // int(nums[i + 1]))
            elif op[i] == "%":
                if nums[i + 1] == 0:
                    raise ValueError("Деление на ноль")
                nums[i] = nums[i] % nums[i + 1]
            del nums[i + 1]
            del op[i]
        else:
            i += 1

    res = nums[0]
    for i in range(len(op)):
        if op[i] == "+":
            res += nums[i + 1]
        else:
            res -= nums[i + 1]
    return res