num_list = (123, 333, 443)
last_digit = []

for num in num_list:
    num = str(num)
    last_digit.append(num[-1])

    product = last_digit[-1] * last_digit[0]
    if product[-1] == last_digit[-1]:
        True
    else:
        False
