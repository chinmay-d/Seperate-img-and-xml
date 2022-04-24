import os, shutil

mix_path = input("enter path of folder which contains xml and its corresponding img: ")
root_path = input("enter a path to save imgs and xml file differently: ")
img_path = "image_folder/"
xml_path = "xml_folder/"

imageFullPath = os.path.join(root_path, img_path)
xmlFullPath = os.path.join(root_path, xml_path)

if not os.path.exists(xmlFullPath) and not os.path.exists(imageFullPath):
    os.makedirs(xmlFullPath)
    os.makedirs(imageFullPath)
    
imgs = 0
xmls = 0

for folders, subfoldersk, files in os.walk(mix_path):
    for file in files:
        # print(file)
        lst = file.split('.')
        if lst[-1] == "xml":
            #move to xml folder
            shutil.copy2(os.path.join(folders, file), xmlFullPath)
            xmls += 1

        else :
            #move to imgs folder
            shutil.copy2(os.path.join(folders, file), imageFullPath)
            imgs += 1
        # print(lst[-1])
        lst.clear()
print("copied {} xml files into xml_folder and {} image files to images_folder".format(xmls,imgs))