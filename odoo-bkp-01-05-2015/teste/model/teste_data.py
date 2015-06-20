#!/usr/bin/python
# -*- encoding: utf-8 -*-

from openerp.osv import osv, fields

class teste(osv.Model):
    _name = 'teste'
    _columns = {
        'nome': fields.char('Nome da pessoa'),
        'sobrenome': fields.char('Sobre nome', )
    }
