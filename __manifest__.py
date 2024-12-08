# -*- coding: utf-8 -*-
{
    'name': "digicare HRMS",

    'summary': "Digital Care  - Healthcare Records Management System  ",

    'description': """
    DidiCare - HRMS is a solution for digital healthcare records maangement system. 
    It aims manage all process related to medical insurance operations and provide 
    a lot of reports and optimized management records for patients, medical centers, 
    praticians, drugs tracking records and powerful decision making. 
    """,

    'author': "SIGEM - Coopernit",
    'website': "https://www.coopernit.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Services',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

