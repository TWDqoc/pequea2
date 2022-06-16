# -*- coding: utf-8 -*-
{
    'name': "Pequea Sales",

    'summary': "",

    'description': """
    """,

    'author': "QOC Innovations",
    'website': "http://www.qocinnovations.com",

    'category': 'Customizations',
    'version': '15.0.1',
    'license': 'LGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['sale_management', 'purchase', 'sale_stock'],

    # always loaded
    'data': [
        'views/sale_views.xml',
        'views/account_move_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}
