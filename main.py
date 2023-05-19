from typing import List

import subprocess
import os

def words() -> List[List[str]]:
    with open('palavras.txt', 'r') as file:
        data = file.read().split('\n')
        return list(map(lambda x: x.split(' '), data))

def try_password(filename: str, word: str) -> bool:
    command = ['openssl', 'enc', '-d', '-aes-256-cbc', '-pbkdf2', '-salt', '-in', 
               f'./enc/{filename}', '-out', f'./dec/{filename}.dec', '-pass', f'pass:{word}']

    process = subprocess.run(command, capture_output=True)
    if process.returncode == 0:
        print(f'Senha: {word}, arquivo: {filename}')
        return True

    return False

words_list = words()
found = False
for file in os.listdir('./enc'):
    for line in words_list:
        for word in line:
            if try_password(file, word):
                found = True
                break
        if found:
            found = False
            break