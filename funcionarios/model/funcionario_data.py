#!/usr/bin/python
# -*- encoding: utf-8 -*-

from openerp.osv import osv, fields

TIPO_FUNCIONARIO = [('1', 'Tecnico'), ('2', 'Analista de suporte')]


class Funcionario(osv.Model):

    _name = 'funcionario'
    _rec_name = 'funcionario_nome'
    _columns = {
        'active': fields.boolean('Ativo'),
        'funcionario_nome': fields.char('Nome', size=100),
        'funcionario_tipo': fields.selection(TIPO_FUNCIONARIO, 'Tipo')
    }