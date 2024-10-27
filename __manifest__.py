{
    'name': 'POS Kitchen Display',
    'version': '1.0',
    'category': 'Point of Sale',
    'summary': 'Kitchen Display System for POS orders',
    'description': """
        This module adds a kitchen display system for managing POS orders in the kitchen.
    """,
    'depends': ['point_of_sale', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'views/pos_kitchen_display_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'pos_kitchen_display/static/src/js/KitchenDisplay.js',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
