import os, glob, random, string

base_dir, dirs, loading = os.path.dirname(os.path.realpath(__file__)), [], 0

def listdirs(rootdir):
    for file in os.listdir(rootdir):
        d = os.path.join(rootdir, file)
        if os.path.isdir(d):
            dirs.append(d)
            listdirs(d) 
listdirs(base_dir)
print(f"diretórios selecionados: {len(dirs)} \n")
input("Iniciar Programa? ")

for d in dirs:
    l1,l2,l3 = [], [], []

    os.chdir(d)

    for file in os.listdir(d):
        if file in glob.glob("*.png") and file not in l1:
            l1.append(file)

    for file in os.listdir(d):
        if file in glob.glob("*.png") and file in l1:
            raname = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10)) + ".png"
            os.rename(file,raname)
            l2.append(raname)

    for file in os.listdir(d):
        if file in glob.glob("*.png") and file in l2 and file not in l1:
            temp = random.choice(l1)
            while temp in l3:
                temp = random.choice(l1)
            l3.append(temp)
            os.rename(file,temp)

    loading += 1
    print(f"Carregando: {loading}/{len(dirs)}")