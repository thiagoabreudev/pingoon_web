#!/usr/bin/python
# -*- encoding: utf-8 -*-

from openerp.osv import osv


class Ocorrencia(osv.Model):
    _name = 'ocorrencia'
    _inherit = 'ocorrencia'

    def button_mapa(self, cr, uid, ids, context):
        dados_ocorrencia = self.read(cr, uid, ids, ['ocorrencia_longitude', 'ocorrencia_latitude'])
        longitude = latitude = 0

        for dado in dados_ocorrencia:
            longitude = dado.get('ocorrencia_longitude')
            latitude = dado.get('ocorrencia_latitude')
        url = "http://www.google.com.br/maps/@%s,%s" % (longitude, latitude)
        return {
            'type': 'ir.actions.act_url',
            'url': url,
            'target': 'new'
        }

    def button_visualizar(self, cr, uid, ids, context):
        res = self.write(cr, uid, ids, vals={'state': '2'})
        return res

    def button_atender(self, cr, uid, ids, context):
        res = self.write(cr, uid, ids, vals={'state': '3'})
        return res

    def button_fehcar(self, cr, uid, ids, context):
        res = self.write(cr, uid, ids, vals={'state': '4'})
        return res

    def button_cancelar(self, cr, uid, ids, context):
        res = self.write(cr, uid, ids, vals={'state': '5'})
        return res
    