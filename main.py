#sorts files into individual folders by year and then sorts into date
print('\n'+"sort_time_4.py") 
import os, time, datetime, platform , glob, shutil 
#pip install module

path = '/Users/jimmyrao/Desktop/file_sorter/Favorites 2/'
if os.path.exists(path+'sort_log.txt'):
    print("ERROR: Already been sorted")
    exit()
filenames = glob.glob(path+'*')
print(filenames)
dictionary = {}
#dicitonary = {filename: creation_time}

def mac_file(file): 
    return datetime.datetime.fromtimestamp(os.stat(file).st_birthtime)

def win_file(file):
    return datetime.datetime.fromtimestamp(os.path.getctime(file))

#testing
# file = '/Users/jimmyrao/Desktop/jimmy_kang.jpg'
# file_time = mac_file(file)
# file_date = file_time.strftime("%m %Y")
# file_year = file_time.strftime("%Y")
# # print(file_date)
# # print(file_year)

#check operating system (windows or mac)
osys = platform.system()
# print(osys)
if osys == 'Windows':
    operating_system = 'win'
elif osys == 'Darwin':
    operating_system = 'mac'

for file in filenames:
    if operating_system == 'win':
        file_time = win_file(file)
    elif operating_system == 'mac':
        file_time = mac_file(file)
    # file_date = file_time.strftime("%m %Y")
    file_year = file_time.strftime("%Y")
    file_month = file_time.strftime("%m_%b")
    dictionary[file] =  file_year,file_month


# x = dictionary['/Users/jimmyrao/Desktop/file_sorter/Favorites/IMG_3015.JPG']
# print(x)
log = ''
print(dictionary)

for key, value in dictionary.items():
    if not os.path.exists(path+value[0]):              # if the directory for the specific date DNE,
        os.makedirs(path+value[0])                      # make a new folder for that directory
        print(path+value[0]+'/'+value[1])
    if not os.path.exists(path+value[0]+'/'+value[1]):
        os.makedirs(path+value[0]+'/'+value[1])
    filename = key.split('/')
    filename = filename[-1]
    if not os.path.exists(path+value[0]+'/'+value[1]+'/'+filename):
        print(path+value[0]+'/'+value[1]+'/'+filename)
        if os.path.isfile(key):
            shutil.move(key,path+value[0]+'/'+value[1]+'/'+filename)
            log = log + key + ' moved to ' + path+value[0]+'/'+value[1]+'/'+filename + '\n' + '\n'
        elif os.path.isdir(key):
            shutil.copytree(key, path+value[0]+'/'+value[1]+'/'+ filename)
            shutil.rmtree(key)
            log = log + key + ' moved to ' + path+value[0]+'/'+value[1]+'/'+filename + '\n' + '\n'
    
with open(path+'sort_log.txt','w') as f:
    f.write(log)