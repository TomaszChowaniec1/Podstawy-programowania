circumference = input('Enter circumference of the tree: ')
diameter = float(circumference) / 3.14
can_cut = diameter >= 50
print(f'Tree can be cut: {can_cut}')