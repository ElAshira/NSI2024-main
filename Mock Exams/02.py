def indices_maxi(tab):
    if tab == []:
        raise ValueError("Your array is empty, please  do check the datas")
    max_value = max(tab)
    index_of_value = tab.index(max_value)
    return (max_value, index_of_value)

def positif(pile):
    pile_1 = list(pile)
    pile_2 = []

    while pile_1 != []:
        x = pile_1.pop()
        if x >= 0:
            pile_2.append(x)

    pile.clear()
    while pile_2 != []:
        x = pile_2.pop()
        pile.append(x)

    return pile

input_pile = [-1, 2, -3, 4, -5, 6]
result = positif(input_pile)
print(result)
