import subprocess
import os

def words():
    with open('palavras.txt', 'r') as file:
        return file.read().split('\n')


words_list = words()
for file in os.listdir('./enc'):
    for word in words_list:
        command = ['openssl', 'enc', '-d', '-aes-256-cbc', '-pbkdf2', '-salt', '-in', f'./enc/{file}', '-out', f'./dec/{file}.dec', '-pass', f'pass:{word}']
        process = subprocess.run(command)
        if process.returncode == 0:
            print(f'Senha: {word}')
            break
