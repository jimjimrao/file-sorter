import os, time, datetime, platform , glob, shutil 
#pip install module

path = input("Type in your folder's file path:")

#check operating system (windows or mac)
osys = platform.system()

if osys == 'Windows':
    operating_system = 'win'
    path = path + '\\'

elif osys == 'Darwin':
    operating_system = 'mac'
    path = path + '/'

#keeps program from sorting again if it has already been done 
if os.path.exists(path+'sort_log.txt'):        
    print("ERROR: Already been sorted")
    exit()
    
filenames = glob.glob(path+'*')
dictionary = {}
#dicitonary = {filename: file_year, file_month}

def mac_file(file): 
    return datetime.datetime.fromtimestamp(os.stat(file).st_birthtime)

def win_file(file):
    return datetime.datetime.fromtimestamp(os.path.getmtime(file))


for file in filenames:

    if operating_system == 'win':
        file_time = win_file(file)
        breaker = '\\'

    elif operating_system == 'mac':
        file_time = mac_file(file)
        breaker ='/'

    file_year = file_time.strftime("%Y")
    file_month = file_time.strftime("%m %b")
    dictionary[file] =  file_year,file_month

log = ''
counter = 0
for key, value in dictionary.items():

    if not os.path.exists(path+value[0]):              # if the directory for the specific date DNE,
        os.makedirs(path+value[0])                      # make a new folder for that directory

    if not os.path.exists(path+value[0]+breaker+value[1]):
        os.makedirs(path+value[0]+breaker+value[1])

    filename = key.split(breaker)
    filename = filename[-1]

    if not os.path.exists(path+value[0]+breaker+value[1]+breaker+filename):
        print(filename + '   was moved to   ' + path+value[0]+breaker+value[1])

        if os.path.isfile(key):
            shutil.move(key,path+value[0]+breaker+value[1]+breaker+filename)
           

        elif os.path.isdir(key):
            shutil.copytree(key, path+value[0]+breaker+value[1]+breaker+ filename)
            shutil.rmtree(key)
    
    log = log + '<<'+ key + '>>  moved to:  <<'+ path+value[0]+breaker+value[1]+breaker+filename + '>>'+  '\n' + '\n'
    counter += 1 
counter = str(counter)
log = log + 'Sorting complete.'+  '\n' + counter + ' files were organized. '
with open(path+'sort_log.txt','w') as f:
    f.write(log)
    