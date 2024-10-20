import multiprocessing
import datetime

def read_info(name):
    all_data=[]
    with open (name, 'r') as file:
         for line in file:
             line=line.strip()
             if line:
                 all_data.append(line)
    return all_data

file_list=[]  #формируем список файлов
for file in range(1,5):
    file_list.append(f"./Files/file {file}.txt")

# Способ #1:
start=datetime.datetime.now()

for i in file_list:
    name=i
    read_info(name)

end=datetime.datetime.now()
print("Способ #1 \nЗатраченное время: ", end-start)


print('-'*35)
# Способ #2:
import multiprocessing

start=datetime.datetime.now()

if __name__=="__main":
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, file_list)

end=datetime.datetime.now()
print("Способ #2 \nЗатраченное время: ", end-start)



# print(file_list)


