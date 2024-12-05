# -*- coding: utf-8 -*-
{
    'name': "Balance en Moneda",
    'summary': "Módulo para calcular y mostrar balance en la moneda definida en las cuentas contables",
    'description': """
        Agrega un campo para mostrar el balance en la moneda de la cuenta contable, 
        completa los campos de importe en divisa y divisa si están vacíos, y permite mostrar estos datos en la vista Pivot.
    """,

    'author': "Mallic corp",
    'website': "https://www.yourcompany.com",

    'category': 'Accounting',
    'version': '0.1',

    'depends': ['base', 'account'],  # Dependencia del módulo "account"

    'data': [
        'views/account_move_line_views.xml',  # Vistas de cuenta
        'security/ir.model.access.csv',       # Archivo de acceso
        # Aquí puedes añadir más archivos si tienes otros elementos como reportes, plantillas de datos, etc.
    ],

    'installable': True,
    'application': False,
    'auto_install': False,
}


