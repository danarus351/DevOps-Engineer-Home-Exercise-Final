import requests as re
import pandas as pd

def filter_chars():
    filtered_chars = []
    data = re.get('https://rickandmortyapi.com/api/character').json()['results']
    for char in data:
        if char['species'] == 'Human' and char['status'] == 'Alive' and 'Earth' in  char['origin']['name']:
            char = {
                'Name' : char['name'],
                'Location' : char['location']['name'],
                'Image': char['image']
            }
            filtered_chars.append(char)
    return filtered_chars

def export_to_csv(filtered_chars):
    pd.DataFrame(filtered_chars).to_csv('chars.csv', index=False)
    print('Chars exported')


if __name__ == '__main__':
    chars  =filter_chars()
    export_to_csv(chars)
