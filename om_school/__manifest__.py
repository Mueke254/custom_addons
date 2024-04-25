# -*- coding: utf-8 -*-

{
    'name': 'School Management',
    'version': '1.0.0',
    'category': 'School',
    'sequence': -100,
    'summary': 'School Management System',
    'description': """School Management System""",
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/student_view.xml',
        'views/registration_view.xml',
        'views/certificate_view.xml',
        'views/diploma_view.xml',
        'views/degree_view.xml',
    ],
    'demo': [],
    'application': True,
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
