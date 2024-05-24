def enumerate_list(list):
    new_list = []
    new_new_list = []
    for element in list:
        if len(element) != 0 :
            new_list.append(element)
    for index, element2 in enumerate(new_list):
        espacio = f"{int(index)}. {element2.title()}"
        new_new_list.append(espacio)
    return new_new_list


def enumerate_backwards(list):
    new_listback = []
    new_new_listback = []
    for element in list:
        if len(element) != 0 :
            new_listback.append(element)
    for index, element2 in enumerate(new_listback):
        espacio = f"{int(index)}. {element2.title()[::-1]}"
        new_new_listback.append(espacio)
    return new_new_listback
