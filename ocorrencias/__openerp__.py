#!/usr/bin/python
# -*- encoding: utf-8 -*-

# -*- encoding: utf-8 -*-
{
    "name": "ocorrencia",
    'version': '1.0',
    "author": "SGO",
    "website": "",
    "category": "Ocorrencia",
    "description": "Modulo para gestao de ocorrencias",
    "license": "Other proprietary",
    "depends": [
        'base_setup',
        'board',
        ],
    "demo": [],
    "data": [
        'views/ocorrencia_view.xml',
        'views/ocorrencia_dashboard.xml',
        'wizard/wizard_mapeamento_ocorrencias_view.xml',
        'views/action.xml',
        'views/menu.xml',
    ],
    "js": [
      'static/src/js/teste.js',
    ],
    "installable": True,
    "application": True,
    "active": False,
}
