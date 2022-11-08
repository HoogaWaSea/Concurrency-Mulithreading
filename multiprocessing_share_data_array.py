# To share sequence of value among processes

import multiprocessing as mp
import time

def squares(numbers, square_list):
    for n in numbers:
        square_list.append(n**2)
    
    print(f'square_list inside process {square_list}')

def cubes(numbers, res):
    idx  = 0
    for num in numbers:
        res[idx] = num ** 3
        idx += 1
    print(f'res Array inside process.function:{res[::]}')
    
if __name__ == '__main__':
    numbers = [1, 2, 3]
    square_list = []
    
    p = mp.Process(target=squares, args=(numbers, square_list))
    p.start()
    p.join()
    
    print(f'squares_list outside process {square_list}')
    
    # share value in an array by process
    res = mp.Array('i', len(numbers))
    p1 = mp.Process(target=cubes, args=(numbers, res))
    p1.start()
    p1.join()
    
    print(f'res Array outside process {res[::]}')
    
    # test