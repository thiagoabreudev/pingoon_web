#!/usr/bin/python
# -*- encoding: utf-8 -*-

from openerp.osv import osv
import requests
import json


class Ocorrencia(osv.Model):
    _name = 'ocorrencia'
    _inherit = 'ocorrencia'

    def create(self, cr, uid, vals):
        endereco_aproximado = self.get_endereco_aproximado(vals.get('ocorrencia_longitude'),
                                                           vals.get('ocorrencia_latitude'))
        mapa = self.get_mapa(vals.get('ocorrencia_longitude'), vals.get('ocorrencia_latitude'))
        vals['ocorrencia_endereco_aproximado'] = endereco_aproximado
        vals['ocorrencia_mapa'] = mapa
        res = super(Ocorrencia, self).create(cr, uid, vals)
        return res

    def button_mapa(self, cr, uid, ids, context):
        dados_ocorrencia = self.read(cr, uid, ids, ['ocorrencia_longitude', 'ocorrencia_latitude'])
        longitude = latitude = 0

        for dado in dados_ocorrencia:
            longitude = dado.get('ocorrencia_longitude')
            latitude = dado.get('ocorrencia_latitude')

        url = "https://maps.googleapis.com/maps/api/staticmap?center=" + latitude + "," + longitude+\
              "&markers="+latitude+"," + longitude + "&zoom=16&size=640x640"
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

    @staticmethod
    def get_endereco_aproximado(longitude, latitude):
        endereco = "Nao foi possivel encontrar endereco aproximado"
        try:
            url = 'http://maps.google.com/maps/api/geocode/json?address={lat},{long}&sensor=false'
            url = url.format(long=longitude, lat=latitude)
            requisicao = requests.get(url)
            if requisicao.status_code == 200:
                dados = json.loads(requisicao.content)
                if dados.get('results'):
                    endereco = dados.get('results')[0].get('formatted_address').encode('utf-8')
        except:
            pass
        return endereco

    @staticmethod
    def get_mapa(longitude, latitude):
        mapa = False
        try:
            url = "https://maps.googleapis.com/maps/api/staticmap?center=" + latitude + "," +longitude +\
                  "&markers="+latitude+"," + longitude + "&zoom=17&size=640x640"
            requisicao = requests.get(url)
            mapa = False
            if requisicao.status_code == 200:
                mapa = requisicao.content
                mapa = mapa.encode('base64')
        except:
            pass
        return mapa