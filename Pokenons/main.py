import requests

token = '8c5edf82a90afed894c270368f7e01f8'
host = 'https://pokemonbattle.me:9104'

answer_t = requests.post(f'{host}/trainers/reg', json = 
                       { 'trainer_token': token, 
                        'email': 'ind-anastasija-golovacheva@qa.studio', 
                        'password': 'P3A3I0KoJD-ujd23HNJI'
                        }, headers = {'Content-Type': 'application/json'})
print (answer_t.text) 


answer_reg = requests.post(f'{host}/trainers/confirm_email', json = {    
                          'trainer_token': token
                        },headers = {'Content-Type': 'application/json'} )
print (answer_reg.text)

pokemon_new = requests.post(f'{host}/pokemons', json = {
                            'name': 'Dixy',
                            'photo': 'https://dolnikov.ru/pokemons/albums/001.png',                            
                            },headers = {'Content-Type': 'application/json', 'trainer_token': token})

print (pokemon_new.text)

pokemon_name = requests.put(f'{host}/pokemons', json = {
    'pokemon_id': '12725',
    'name': 'Qwery',
    'photo': 'https://dolnikov.ru/pokemons/albums/001.png'
}, headers = {'Content-Type': 'application/json', 'trainer_token': token}) 

print (pokemon_name.text)

pokemon_pokeball = requests.post(f'{host}/trainers/add_pokeball', json = {"pokemon_id": "12725"}, 
                                 headers = {'Content-Type': 'application/json', 'trainer_token': token} )
print (pokemon_pokeball.text)

answer = requests.get(f'{host}/trainers', json = {'trainer_token': token}, params= {'trainer_id' : '4635'})
print (answer.text, answer.status_code)
