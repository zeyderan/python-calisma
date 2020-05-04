with open('newfile.txt','r',encoding='utf-8') as file:
    content = file.read()
    print(content)
    file.seek(40)# cursor göndermek istediğimiz konum
    content = file.read()
    print(file.tell())#cursor konumunu verir
    print(content)