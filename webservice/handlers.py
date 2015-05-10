#!/usr/bin/python
# -*- encoding: utf-8 -*-

import time
from orm import Persistencia

_hello_resp = """
<html>
    <body >
        <script>alert({msg})</script>
    </body>
<html>
"""

_resp = """
<html>
    <head>
    </head>
    <body>
        <script>alert({msg})</script>
    </body>
</html>
"""
# _hello_resp = "OK"


def hello_word(environ, start_response):
    start_response('200 OK', [('Content-type', 'text/html')])
    params = environ['params']
    resp = _hello_resp.format(name=params.get('name'))
    print resp
    yield resp


def search(environ, start_response):
    pass


def create_ocorrencia(environ, start_response):
    # http://localhost:8081/criaocorrencia?ocorrencia_titulo=diego;ocorrencia_descricao=teste
    orm = Persistencia()
    start_response('200 OK', [('Content-type', 'text/html')])
    params = environ['params']
    vals = {
        'ocorrencia_titulo': params.get('ocorrencia_titulo'),
        'ocorrencia_descricao': params.get('ocorrencia_descricao', ''),
        'ocorrencia_foto': params.get('ocorrencia_foto_text', '')
    }
    ocorrencia_id = orm.create(objeto='ocorrencia', vals=vals)
    if ocorrencia_id:
        return 'index.html'
    else:
        return "alert('Nao foi possivel criar ocorrencia);"

if __name__ == '__main__':
    from rest import PathDispatcher
    from wsgiref.simple_server import make_server

    dispatcher = PathDispatcher()
    dispatcher.register('GET', '/hello', hello_word)
    dispatcher.register('GET', '/search', search)
    dispatcher.register('POST', '/criaocorrencia', create_ocorrencia)
    httpd = make_server('', 8081, dispatcher)
    print ('Servindo na porta 8080...')
    httpd.serve_forever()