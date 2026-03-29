lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
def   print_filtred_list(l):
    for n in l:
        if n < 30 and n %3 == 0:
            print(n)

print_filtred_list(lst)