import os

def crypt(dir):
    import pyAesCrypt
    question = input('Шифровать или расшифровать файл? -- ')
    if question == 'Шифровать':
        dir = input('Введите название файла для шифрования: ')
        password = input('Введите ключ: ')
        bufferSize = 512 * 1024
        pyAesCrypt.encryptFile(str(dir), str(dir) + '.aes', password, bufferSize)
        print('Шифрование завершено ' + str(dir) + '.aes')
    else:
        file = input('Введите название файла для расшифровки: ')
        password = input('Введите ключ: ')
        bufferSize = 512 * 1024
        pyAesCrypt.decryptFile(str(file), str(os.path.splitext(file)[0]), password, bufferSize)
        print(str(os.path.splitext(file)[0]))
        os.remove(file)

crypt(dir)


