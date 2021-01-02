#sorts files into individual folders in the form: month_year 
import os, time, datetime, platform , glob, shutil 
#pip install module

path = '/Users/jimmyrao/Desktop/screenshots/'
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
# print(file_date)

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
    file_date = file_time.strftime("%m %Y")
    dictionary[file] = file_date

# print(dictionary)
log = ''

for key, value in dictionary.items():
    if not os.path.exists(path+value):              # if the directory for the specific date DNE,
        os.makedirs(path+value)                      # make a new folder for that directory
    filename = key.split('/')
    filename = filename[-1]
    if not os.path.exists(path+value+'/'+filename):
        print(path+value+'/'+filename)
        if os.path.isfile(key):
            shutil.move(key,path+value+'/'+filename)
            log = log + key + ' moved to ' + path+value+'/'+filename + '\n' + '\n'
        elif os.path.isdir(key):
            shutil.copytree(key, path+value+'/'+ filename)
            shutil.rmtree(key)
            log = log + key + ' moved to ' + path+value+'/'+filename + '\n' + '\n'
 
with open(path+'log.txt','w') as f:
    f.write(log)