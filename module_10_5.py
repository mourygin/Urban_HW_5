import datetime
import multiprocessing
def read_info(name):
    all_data = []
    with open('./Files/' + name, "r") as file:
        while True:
            line = file.readline()
            if line != '':
                all_data.append(file.readline())
            else:
                break
    return

if __name__ == '__main__':
    files = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']
    start = datetime.datetime.now()

    # ******    Multithreading    ******
    # for filename in files:
    #     read_info(filename)

    # ******    Multiprocessing    ******
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, files)

    finish = datetime.datetime.now()
    print(finish - start)
    
    # Multithreading 0:00:03.688711
    # Multiprocessing 0:00:01.693246