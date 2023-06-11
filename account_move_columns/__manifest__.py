{
    'name': 'Add columns to invoices',
    'version': '13.0.1.0.0',
    'category': 'Tecnical',
    'sequence': 1,
    'author': 'Jeo Software',
    'description': """ Agregar columna Fecha Contable en vista de tree facturas """,
    'depends': [
        'account',
    ],
    'data': [
        'views/account_move_view.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
