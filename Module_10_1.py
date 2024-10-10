import time
from datetime import datetime
from threading import Thread


time_start = datetime.now()
# file_name='data.txt'
word_count=0
def write_words(word_count, file_name):
    with open (file_name, "w", encoding="utf-8") as file:
        for i in range(word_count):
            line="Какое-то слово "+str(i+1)+'\n'
            file.write(line)
            time.sleep(0.1)
    print(f'Завершена запись в файл: {file_name}')


write_words(10,'data1.txt')
write_words(30,'data2.txt')
write_words(200,'data3.txt')
write_words(100,'data4.txt')

time_end = datetime.now()

time_res=time_end-time_start
print(f'Работа функций: {time_res}')

time_start_2 = datetime.now()

thr_first=Thread(target=write_words,args=(10,'data5.txt'))
thr_second=Thread(target=write_words,args=(30,'data6.txt'))
thr_third=Thread(target=write_words,args=(200,'data7.txt'))
thr_four=Thread(target=write_words,args=(100,'data8.txt'))

thr_first.start()
thr_second.start()
thr_third.start()
thr_four.start()

thr_first.join()
thr_second.join()
thr_third.join()
thr_four.join()

time_end_2 = datetime.now()

time_res_2=time_end_2-time_start_2
print(f"Работа потоков: {time_res_2}")

