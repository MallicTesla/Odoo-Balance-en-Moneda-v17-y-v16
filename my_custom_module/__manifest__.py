{
    'name': 'Balance en Moneda',
    'version': '1.0',
    'summary': 'Agregar campo de Balance en moneda para apuntes contables',
    'author': 'Mallic',

    'category': 'Accounting',

    'depends': ['account'],

    'data': [
        'views/account_move_line_views.xml',
        'security/ir.model.access.csv',
    ],

    'installable': True,
    'application': False,
}
