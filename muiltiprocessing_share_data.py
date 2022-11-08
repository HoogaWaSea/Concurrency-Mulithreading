# Share data between processes using value

import multiprocessing as mp
import time

def increment(counter):
    # global counter => wrong
    # counter += 1 => wrong
    counter.value += 1
    


if __name__ == '__main__':
    # counter = 1 => wrong
    
    # all the processes worked for counter
    counter = mp.Value('i', 1)
    
    for i in range(10):
        process = mp.Process(target=increment, args=(counter,))
        process.start()
        process.join()
        
    print(f'counter:{counter.value}')
    
# test222