import os




if __name__ == "__main__":


    for (root,dirs,files) in os.walk('.', topdown=True):
        print (root)
        print(files)
        for file in files:
            if file.endswith('.jpg'):
                oldname = os.path.join(root,file)
                newname = os.path.join(root, os.path.basename(root)+'.jpg' )
                os.rename(oldname, newname)

