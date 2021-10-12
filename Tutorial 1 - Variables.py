tree_height = int(input('height :' ))
space = tree_height-1
pine = 1


while tree_height != 0:
    for i in range(0,space):
        print(' ' , end=(''))
    for j in range(0,pine ):
        print('#' , end=(''))
    print()
    space -= 1
    pine += 2
    tree_height -= 1




