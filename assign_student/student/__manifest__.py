# -*- coding: utf-8 -*-
{
    'name': 'student management',
    'author': 'deepak',
    'version': '1.1',
    'summary': 'student app',
    'sequence': 30,
    'description': """
application
    """,
    'category': 'Managing',
    'depends': ['base'],
    'data': ['view/student_info_view.xml',
             'view/course_info_view.xml',
             'view/faculty_info_view.xml'],
    'installable': True,
    'application': False,
    'auto_install': False,
}