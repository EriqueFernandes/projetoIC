import yaml
from yaml import Loader

with open("../yaml/teste.yaml", encoding='utf8') as f:
    for ya in yaml.load_all(f,Loader=Loader):
        print(ya)