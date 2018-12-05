def convert_from_base_10(num,base):
    remainder_list = []
    #symbols = "0123456789ABCDEF"
    while num!= 0:
        whole = num // base
        remainder = num % base
        remainder_list.append(str(remainder))
        #symbol = symbol[remainder]
        #remainder_list.append(symbol)
        print(whole, remainder)
        num = whole

    remainder_list.reverse()
    remainder_list = "".join(remainder_list)
    return remainder_list


new_number = convert_from_base_10(235,16)
print(new_number)