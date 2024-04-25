import requests
from django.shortcuts import render

def consulta_cep(request):
    data = {}
    if 'cep' in request.GET:
        cep = request.GET['cep']
        response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
        data = response.json()
        if 'erro' not in data:
            data.update({
                'cep': cep,
                'rua': data['logradouro'],
                'bairro': data['bairro'],
                'cidade': data['localidade'],
                'uf': data['uf'],
                'ibge': data['ibge'],
            })
        else:
            data['error'] = 'CEP não encontrado.'
    return render(request, 'consulta_cep.html', data)