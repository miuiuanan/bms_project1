# -*- encoding: utf-8 -*-
{
    'name': 'BMS CA',
    'summary': 'The product of BMSGroup Global',
    'version': '10.0.1.0',
    'category': 'tools',
    'summary': """
The new configurable Odoo Web Login Screen
""",
    'author': "BMSGroup Global",
    'website': 'bmsgroupglobal.com',
    'depends': [
    ],
    'data': [
        'data/ir_config_parameter.xml',
        'data/email_template.xml',
        'templates/webclient_templates.xml',
        'templates/website_templates.xml',
    ],
    'qweb': [
    ],
    'installable': True,
    'application': True,
}
