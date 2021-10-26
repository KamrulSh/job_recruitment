# -*- coding: utf-8 -*-
{
    'name': "eJob Recruitment",
    'sequence': 1,
    'summary': """
        A job recruitment module.""",

    'description': """
        A job recruitment module
    """,

    'author': "Kamrul",
    'website': "http://www.yourcompany.com",
    'category': 'Services',
    'version': '0.1',
    'license': 'LGPL-3',
    'website': "http://www.yourcompany.com",
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'data/application_sequence.xml',
        'views/all_munu_items.xml',
        'views/job_position_views.xml',
        'views/job_applicant_views.xml',
        'views/recruit_stage_views.xml',
    ],
    'demo': [
        # 'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
