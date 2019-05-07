# -*- coding: utf-8 -*-
{
    'name': 'patient management',
    'author': 'deepak',
    'version': '1.1',
    'summary': 'patient app',
    'sequence': 30,
    'description': """
application
    """,
    'category': 'Managing',
    'depends': ['base'],
    'data': ['view/patient_info_view.xml',
             'view/doctor_info_view.xml',
             'view/disease_info_view.xml'],
    'installable': True,
    'application': False,
    'auto_install': False,
}