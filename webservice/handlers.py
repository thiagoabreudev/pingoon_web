#!/usr/bin/python
# -*- encoding: utf-8 -*-

import time
from orm import Persistencia
import json


def search(environ, start_response):
    pass


def read(environ, start_response):
    orm = Persistencia()
    start_response('200 OK', [('Content-type', 'application/json')])
    params = environ['params']
    ocorrencia_ids = params.get('ocorrencia_ids', [])
    if ocorrencia_ids and isinstance(ocorrencia_ids, str):
        ocorrencia_ids = ocorrencia_ids.split(',')
    ocorrencia_ids = map(lambda i: int(i), ocorrencia_ids)
    dados = orm.read(ocorrencia_ids, fields='state', objeto='ocorrencia')
    res = json.dumps({'dados': dados})
    return res


def create_ocorrencia(environ, start_response):
    orm = Persistencia()
    start_response('200 OK', [('Content-type', 'application/json')])
    params = environ['params']
    foto = params.get('ocorrencia_foto')
    if foto:
        foto = foto.replace(' ', '+')
    else:
        foto = ""

    vals = {
        'ocorrencia_titulo': params.get('ocorrencia_titulo', "SEM TITULO"),
        'ocorrencia_descricao': params.get('ocorrencia_descricao', 'SEM DESCRICAO'),
        'ocorrencia_foto': foto,
        'ocorrencia_latitude': params.get('ocorrencia_latitude', 'SEM LATITUDE'),
        'ocorrencia_longitude': params.get('ocorrencia_longitude', 'SEM LONGITUDE'),
    }
    ocorrencia_id = orm.create(objeto='ocorrencia', vals=vals)
    if ocorrencia_id:
        resp = {'id': ocorrencia_id}
    else:
        resp = {'erro': "Erro ao criar registro"}
    yield json.dumps(resp)

if __name__ == '__main__':
    from rest import PathDispatcher
    from wsgiref.simple_server import make_server

    dispatcher = PathDispatcher()
    dispatcher.register('GET', '/pesquisa', read)
    dispatcher.register('POST', '/criaocorrencia', create_ocorrencia)
    httpd = make_server('', 8081, dispatcher)
    print ('Servindo na porta 8081...')
    httpd.serve_forever()