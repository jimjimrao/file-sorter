# asks user for folder file path
# sorts files into individual folders by year and then sorts into date
print('\n'+"sort_time_5.py") 
import os, time, datetime, platform , glob, shutil 
#pip install module

print(platform.system())
# path = '/Users/jimmyrao/Desktop/file_sorter/Favorites 2/'
path = input("Type in your folder's file path:") + "/"

if os.path.exists(path+'sort_log.txt'):
    print("ERROR: Already been sorted")
    exit()
    
filenames = glob.glob(path+'*')
dictionary = {}
#dicitonary = {filename: file_year, file_month}

def mac_file(file): 
    return datetime.datetime.fromtimestamp(os.stat(file).st_birthtime)

def win_file(file):
    return datetime.datetime.fromtimestamp(os.path.getctime(file))



#check operating system (windows or mac)
osys = platform.system()

if osys == 'Windows':
    operating_system = 'win'

elif osys == 'Darwin':
    operating_system = 'mac'

for file in filenames:

    if operating_system == 'win':
        file_time = win_file(file)

    elif operating_system == 'mac':
        file_time = mac_file(file)

    file_year = file_time.strftime("%Y")
    file_month = file_time.strftime("%m %b")
    dictionary[file] =  file_year,file_month

log = ''

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