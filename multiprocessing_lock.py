import multiprocessing as mp
import time

def deposit(balance, lock):
    for i in range(100):
        time.sleep(0.01)
        # locked
        lock.acquire()
        balance.value += 1
        # release
        lock.release()
        
def withdraw(balance, lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        balance.value -= 1
        lock.release()
            
if __name__ == '__main__':
    balance = mp.Value('i', 500)
    
    # if we don't use lock, the depoist and withdraw would go a thte same time with different termination time, 
    # #the results will be not 500 and fluntuated
    lock = mp.Lock()
    
    
    p1 = mp.Process(target=deposit, args=(balance, lock))
    p2 = mp.Process(target=withdraw, args=(balance, lock))
                    
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    
    print(f'Balance: {balance.value}')
    # test