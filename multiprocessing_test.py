import multiprocessing as mp
import time

def name_time(name):
    print(f'Hello {name}, now itme is {time.time()}')
    print(f'sleeping for 2 secondes.....')
    time.sleep(2)
    print('After sleeping...')
    
if __name__ == '__main__':
    process_list = []
    
    # 10 forks process
    for i in range(10):
        # args is tuple
        # args = ('Anred',) => with comma
        process = mp.Process(target=name_time, args=('Andrew',))
        process_list.append(process)
        
    for p in process_list:
        p.start()
    
    # wait for forks    
    # for p in process_list:
    #     p.join()
        
    # print first, it doesn't wait processing end
    print('Other instructions')
    print('End')