

def return_keys(number_string: str) -> str | None:
    number_list = list(number_string)
    display_string = []
    _ = 0
    print(number_list)
    print(_)
    if len(number_list) != 4:
        print("Error in length of number_string")
        exit(0)

    for i in number_list:
        print(i)
        if i == "9":
            display_string.append(align_keys(position=_ ,keys=['W', 'X', 'Y', 'Z']))
        elif i == '8':
            display_string.append(align_keys(position=_ ,keys=['T', 'U', 'V']))
        elif i == '7':
            display_string.append(align_keys(position=_ ,keys=['P', 'Q', 'R', 'S']))
        elif i == '6':
            display_string.append(align_keys(position=_ ,keys=['M', 'N', 'O']))
        elif i == '5':
            display_string.append(align_keys(position=_ ,keys=['J', 'K', 'L']))
        elif i == '4':
            display_string.append(align_keys(position=_ ,keys=['G', 'H', 'I']))
        elif i == '3':
            display_string.append(align_keys(position=_ ,keys=['D', 'E', 'F']))
        elif i == '2':
            display_string.append(align_keys(position=_ ,keys=['A', 'B', 'C']))
        elif i == '0' or i == '1':
            return ""
        _ +=1
    print(display_string)
    display_string = str(display_string)
    return display_string


def align_keys(position: int, keys: list):
        print(f"align_keys: {position} {keys}")
        print(keys[position])
        return keys[position]

return_keys(number_string="4567")

