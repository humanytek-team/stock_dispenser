# -*- coding: utf-8 -*-
# Copyright 2017 Humanytek - Manuel Marquez <manuel@humanytek.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

{
    'name': 'Stock Dispensers Manager',
    'description': """
    This module allows odoo users with rol stock manager to easily manage stock
    dispensers users.
    """,
    'author': "Humanytek",
    'website': "http://www.humanytek.com",
    'category': 'Stock',
    'version': '1.1.0',
    'depends': ['stock', 'stock_is_stock_user'],
    'data': [
        'views/stock_dispenser_view.xml',
        'views/stock_picking_view.xml',
    ],
    'demo': [
    ],
}
