import os

def crypt(dir):
    import pyAesCrypt
    question = input('Шифровать или расшифровать файл? -- ')
    if question == 'Шифровать':
        dir = 'C:\\Users\\38096\\studying\\1.txt'
        password = input('Введите ключ: ')
        bufferSize = 512 * 1024
        pyAesCrypt.encryptFile(str(dir), str(dir) + '.aes', password, bufferSize)
        print('Шифрование завершено ' + str(dir) + '.aes')
    else:
        file = 'C:\\Users\\38096\\studying\\1.txt.aes'
        password = input('Введите ключ: ')
        bufferSize = 512 * 1024
        pyAesCrypt.decryptFile(str(file), str(os.path.splitext(file)[0]), password, bufferSize)
        print(str(os.path.splitext(file)[0]))
        os.remove(file)

crypt(dir)


