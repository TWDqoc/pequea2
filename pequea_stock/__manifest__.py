# -*- coding: utf-8 -*-
{
    'name': "Pequea Stock",

    'summary': "",

    'description': """
    """,

    'author': "QOC Innovations",
    'website': "http://www.qocinnovations.com",

    'category': 'Customizations',
    'version': '15.0.1',
    'license': 'LGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['stock', 'pequea_sales'],

    # always loaded
    'data': [
        'views/stock_picking_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}
