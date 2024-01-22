#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    try:
        for i in range(list_length):
            result_list = my_list_1[i] / my_list_2[i]

            elem_1 = my_list_1[i] if i < len(my_list_1) else 0
            elem_2 = float(my_list_2[i]) if i < len(my_list_2) and my_list_2[i] != 0 else 0

            try:
                result = elem_1 / elem_2
                result_list.append(result)
            except ZeroDivisionError:
                print("division by 0")
                result_list.append(0)

    except (TypeError, ValueError, IndexError):
        print("out of range")
        result_list.append(0)

    finally:
        return result_list
