#!/usr/bin/python
# -*- encoding: utf-8 -*-


url = 'http://localhost:8069'
db = 'odoo_teste'
username = 'admin'
password = 'admin'

import xmlrpclib
common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(url))
print common.version()
uid = common.authenticate(db, username, password, {})

#Search
args = ['id', '=', 1]
models = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(url))
ids = models.execute_kw(db, uid, password, 'ocorrencia', 'search', [[['id', '!=', 1]]])
print ids

#read
read_funcionario = models.execute_kw(db, uid, password, 'ocorrencia', 'read', [ids],
                                     {'fields': []})

#create
funcionario_id = models.execute_kw(db, uid, password, 'funcionario', 'create', [{
    'funcionario_nome': 'Thiago',
    'active': True,
}])

