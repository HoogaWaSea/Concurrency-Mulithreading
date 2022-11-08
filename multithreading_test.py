import threading as ms
import time

def name_time(name):
    print(f'Hello {name}, now itme is {time.time()}')
    print(f'sleeping for 2 secondes.....')
    time.sleep(2)
    print('After sleeping...')
    
if __name__ == '__main__':
    thread_list = []
    
    # 10 forks process
    for i in range(10):
        # args is tuple
        # args = ('Anred',) => with comma
        thread = ms.Thread(target=name_time, args=('Andrew',))
        thread_list.append(thread)
        
    for t in thread_list:
        t.start()
    
    # wait for forks    
    # for p in process_list:
    #     p.join()
        
    # print first, it doesn't wait processing end
    print('Other instructions')
    print('End')
    
    # test