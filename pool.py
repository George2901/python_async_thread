import requests
import time
from threading import Thread




def fetch(id):
    url = 'https://www.google.com'
    response = requests.get(url)
    print( f'{id} {response.status_code}')

def main():
    max_threads = 100
    ids = 0
    ct = 0
    threads = [Thread(target=fetch, args=[ids]) for _ in range(max_threads)]
    [thread.start() for thread in threads]

    while True:
        if ct >= max_threads:ct = max_threads%ct
        if not threads[ct].is_alive():
            threads[ct] = Thread(target=fetch, args=[ids])
            threads[ct].start()
            ids+=1
            ct +=1
        time.sleep(0.01)
    

if __name__ == '__main__':
    main()




