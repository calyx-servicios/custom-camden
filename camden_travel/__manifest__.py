# -*- coding: utf-8 -*-
{
    'name': "Camden Travel",

    'summary': """
        Modificaciones y adaptaciones sobre modelos de CRM, Sales y Accounts para administracion de una agencia de viajes""",

    'description': """
        
    """,

    'author': "Calyx",
    'website': "http://www.calyxservicios.com.ar",

    'category': 'Tools',
    'version': '0.1',


    'depends': ['crm', 'account', 'sale_crm', 'sale', 'project', 'sale_timesheet'],


    'data': [
        'data.xml',
        'security/ir.model.access.csv',
        'views/destination_view.xml',
        'views/crm_lead_view.xml',
        'views/sale_order_view.xml',
    ],

    'demo': [
    ],
}