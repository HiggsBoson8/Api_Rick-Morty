import requests

# api - application protocol interface - fastapi, restapi
# rest - 
# json формат api 2 - dictionary


# url = 'https://rickandmortyapi.com/api/character'
# r = requests.get(url)
# data = r.json()
# with open('character.json', 'r') os f:
#     a = f.read()
    
# url = 'https://yandex.kz'
# response = requests.get(url)
# print(response.status_code)


# def get_character(id):
#     url = f'https://rickandmortyapi.com/api/character/{id}'
#     response = requests.get(url)
#     data = response.json() 
#     return data 
# print(get_character(361))

# def get_character_info(id):
#     data = get_character(id)
#     information = f'''
#     Идентификатор персонажа: {data['name']}
#     Имя персонажа: {data['name']}
#     Пол персонажа: {data['gender']}
#     Статус персонажа: {data['status']}
#     Личность персонажа: {data['type']}
#     Вид(раса) персонажа: {data['species']}
#     Местоположение персонажа: {data['location']['name']}
#     Дата создания: {data['created']}
#     '''
#     return information
# print(get_character_info(19))
    
    
def get_info(gets):
    url = f'https://rickandmortyapi.com/api/{gets}'
    response = requests.get(url)
    data = response.json()
    return data

def get_episode(gets):
    get_id_episodes = get_info(f'character/{gets}')
    for i in get_id_episodes['episode']:
        response = requests.get(i)
        episode = response.json()
        information_episode = f'''
    Эпизод где участвует персонаж:
        Название эпизода: {episode['name']}
        Дата релиза: {episode['air_date']}
        Эпизод: {episode['episode']}
        Дата создания: {episode['created']}
        '''
        return information_episode

def get_location(gets):
    get_id = get_info(f'character/{gets}')
    for i in get_id.keys():
        if i == 'location':
            name_location = get_id['location']['name']
            url_location = get_id['location']['url']
            if url_location not in '':
                id_url = url_location.split('/')[-1]
                location = get_info(f'location/{id_url}')
                name_dimension = location['dimension']
                type_location = location['type']
                information_location = f'''
        Название локации: {name_location}
        Тип локации: {type_location}
        Измерение локации: {name_dimension}
        '''
                return information_location
            else:
                information_location = f"""
        Название локации: {name_location}
        Тип локации: Unknown
        Измерение локации: Unknown"""
                return information_location

def get_character_info(gets):
    if gets <= 826:
        character = get_info(f'character/{gets}')
        information = f"""
        Идентификатор персонажа: {character['id']}
        Имя персонажа: {character['name']}
        Пол персонажа: {character['gender']}
        Жизненное положение: {character['status']}
        Какой расе относится: {character['species']}
        Личность: {character['type']}
        Дата создания: {character['created']}
        Эпизоды где есть персонаж: {' ' .join(character['episode']) .center(10)}
        {get_location(gets)}
        """
        return information
    return 'Не правильный id персонажа'
character = int(input('Введите id персонажа: '))
print(get_character_info(character))
    

    
    
    
    
    