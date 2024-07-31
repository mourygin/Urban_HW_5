from random import randint
from datetime import datetime
import time
from threading import Thread
def wite_words(word_count, file_name):
    words_list =['zero', 'one', 'two', 'three','four', 'five', 'six', 'seven', 'eight', 'nine']
    file = open(file_name, 'w')
    file.write('-----------------------------------------------\n')
    for i in range(word_count):
        inx = randint(0, 9)
        file.write(f'The word #{i+1} - {chr(39)}{words_list[inx]}{chr(39)}\n')
        time.sleep(0.1)
    file.close()
    print(f'Writing to file {file_name} is complite')

# wite_words(5, 'test.txt')
time_beg = datetime.now()
wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')
time_end = datetime.now()
print(f'It takes {time_end - time_beg} seconds')

time_beg = datetime.now()
thr_1 = Thread(target=wite_words, args=(10, 'example5.txt'))
thr_2 = Thread(target=wite_words, args=(30, 'example6.txt'))
thr_3 = Thread(target=wite_words, args=(200, 'example7.txt'))
thr_4 = Thread(target=wite_words, args=(100, 'example8.txt'))

thr_1.start()
thr_2.start()
thr_3.start()
thr_4.start()

thr_1.join()
thr_2.join()
thr_3.join()
thr_4.join()
time_end = datetime.now()
print(f'It takes {time_end - time_beg} seconds')

