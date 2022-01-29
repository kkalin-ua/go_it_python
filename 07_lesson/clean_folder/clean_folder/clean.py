import os, shutil, re, sys
from itertools import groupby
from unicodedata import name

#path = r'C:\Users\Konstantin\Desktop\Хлам'
new_dir = ["images", "documents", "audio", "video", "archives"]
files_info = {'images': [], 'archives': [], 'documents': [], 'audio': [], 'video': [], 'unknown': [], 'known': []}

def сreating_new_dir(new_dir):
    for dirr in new_dir:
        if not os.path.exists(path + '\\' + dirr):
            os.mkdir(path + '\\' + dirr)
        else:
            continue


def del_empty_dirs(path):
    for d in os.listdir(path):
        a = os.path.join(path, d)
        if os.path.isdir(a):
            del_empty_dirs(a)
            if not os.listdir(a):
                os.rmdir(a)


def moving_files(path, all_files):
    CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
    TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u", 
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "u", "ja", "je", "ji", "g") 
    TRANS = {} 
     
    for c, t in zip(CYRILLIC_SYMBOLS, TRANSLATION): 
        TRANS[ord(c)] = t 
        TRANS[ord(c.upper())] = t.upper()

    for files in all_files:
            filesssss = files[files.rindex("."):].lower()
            name_file = (files[files.rindex("\\"):]).translate(TRANS)
            name_file_tran = name_file[0] + (re.sub("[^A-Za-z0-9]", "_", name_file[1:name_file.rindex(".")])) + name_file[name_file.rindex("."):]
            
            try:
                if "\\images\\" in files and "\\documents\\" in files and "\\audio\\" in files and "\\video\\" in files and "rchives\\" in files:
                    continue
                
                elif filesssss in (".jpg", ".png", ".jpeg", ".svg", ".jfif"):
                    sss = path + "\\images" + name_file_tran
                    shutil.move(os.path.join(files), os.path.join(sss))
                    files_info['images'].append(name_file_tran[1:])
                    files_info['known'].append(filesssss)
                    
                elif filesssss in (".avi", ".mp4", ".mov", ".mkv"):
                    sss = path + "\\video" + name_file_tran
                    shutil.move(os.path.join(files), os.path.join(sss))
                    files_info['video'].append(name_file_tran[1:])
                    files_info['known'].append(filesssss)
                
                elif filesssss in (".doc", ".docx", ".txt", ".pdf", ".xlsx", ".pptx"):
                    sss = path + "\\documents" + name_file_tran
                    shutil.move(os.path.join(files), os.path.join(sss))
                    files_info['documents'].append(name_file_tran[1:])
                    files_info['known'].append(filesssss)
                
                elif filesssss in (".mp3", ".ogg", ".wav", ".amr"):
                    sss = path + "\\audio" + name_file_tran
                    shutil.move(os.path.join(files), os.path.join(sss))
                    files_info['audio'].append(name_file_tran[1:])
                    files_info['known'].append(filesssss)

                if filesssss in (".zip", ".gz", ".tar"):
                    sss = path + "\\archives" + name_file_tran
                    name_dir = path + '\\archives\\' + (re.sub("[^A-Za-z0-9]", "_", name_file[1:name_file.rindex(".")]))
                    files_info['archives'].append(name_file_tran)
                    files_info['known'].append(filesssss)
                    try:
                        os.mkdir(name_dir)
                    except FileExistsError:
                        pass
                    shutil.unpack_archive(files, name_dir, filesssss[1:])
                    shutil.move(os.path.join(files), os.path.join(sss))

                else:
                    files_info['unknown'].append(filesssss)
                    continue

            except FileNotFoundError:
                continue


def list_file_dir(path):
    all_files = []
    all_dirs = []

    for address, dirs, files in os.walk(path):
        
        for file in files:
            all_files.append(address+'\\'+file)

        for dirss in dirs:
            all_dirs.append(dirss)
        
    return all_files


def normalize(path): #___________________MAIN___________________

    сreating_new_dir(new_dir)
    all_files = list_file_dir(path)
    all_files = all_files
    moving_files(path, all_files)
    del_empty_dirs(path)
    
    files_info['known'] = [el for el, _ in groupby(files_info['known'])]
    files_info['unknown'] = [el for el, _ in groupby(files_info['unknown'])]

    print(files_info)


# normalize(path)

def main():
    path = sys.argv[1:]

    if path:
        normalize(path)
        
    else:
        print("Сорян, Вы не указали путь к папке. Всего хорошего!)")
    

if name == "__main__":
    main()
