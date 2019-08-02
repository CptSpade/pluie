import requests
import json

code_postal = input("Code postal, ville... : ")

try:
    r = requests.get('http://www.meteofrance.com/mf3-rpc-portlet/rest/lieu/facet/pluie/search/' + code_postal)
    id_ville = json.loads(r.text)[0]['id']
    r = requests.get('http://www.meteofrance.com/mf3-rpc-portlet/rest/pluie/'+id_ville)

    for i in json.loads(r.text)["niveauPluieText"]:
        print(i)
    input()
except:
    print("T'es sûr que t'as bien écrit ?")
