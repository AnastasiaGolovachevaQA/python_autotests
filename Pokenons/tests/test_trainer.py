import requests
import pytest
token = '8c5edf82a90afed894c270368f7e01f8'
host = 'https://pokemonbattle.me:9104'

def test_trainer_status_code():
    answer_trainer = requests.get(f'{host}/trainers', json = {'trainer_token': token})
    assert answer_trainer.status_code == 200  

def test_name_trainer(): 
    answer_name = requests.get(f'{host}/trainers', json = {'trainer_token': token}, params= {'trainer_id' : '4635'})
    assert answer_name.json()['trainer_name']== 'Misty'