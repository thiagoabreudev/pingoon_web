#!/usr/bin/python
# -*- encoding: utf-8 -*-
import xmlrpclib


class Persistencia(object):
    def __init__(self):
        self.url = 'http://localhost:8069'
        self.db = 'odoo_teste'
        self.username = 'admin'
        self.password = 'admin'
        self.common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(self.url))
        self.uid = self.common.authenticate(self.db, self.username, self.password, {})
        self.models = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(self.url))

    def search(self, **kwargs):
        objeto = kwargs.get('objeto')
        fields = kwargs.get('fields') #TODO: fields deve vir no formato de domain, tuplas de listas
        ids = self.models.excute_kw(self.db, self.uid, self.password, objeto, 'search',
                                    [[[fields]]])
        return ids

    def create(self, **kwargs):
        objeto = kwargs.get('objeto')
        vals = kwargs.get('vals')
        res_id = self.models.execute_kw(self.db, self.uid, self.password, objeto, 'create', [vals])
        return res_id

