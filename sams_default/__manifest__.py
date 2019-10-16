# -----------------------------------------------------------------------------------
#
#    Copyright (C) 2019  jeo Software  (http://www.jeosoft.com.ar)
#    All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# -----------------------------------------------------------------------------------
{
    'name': 'samse',
    'version': '11.0e.2.0.0',
    'license': 'Other OSI approved licence',
    'category': 'Tools',
    'summary': 'Customización Sams',
    'author': 'jeo Software',
    'depends': [

        # para la localizacion argentina
        'standard_depends_ee',

        # aplicaciones instaladas
        'crm',
        'project',
        'stock',
        'mrp',
        'sale_management',
        'hr_timesheet',
        'account_invoicing',
        'website',
        'purchase',
        'hr',
        'fleet',
        'l10n_ar_stock', # remito electronico argentino

        # utilitarios
        'l10n_ar_stock',
    ],

    'data': [
    ],
    'test': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'images': [],

    'port': '8069',
    'repos': [
        {'usr': 'jobiols', 'repo': 'cl-sams', 'branch': '11.0e'},
        {'usr': 'oca', 'repo': 'stock-logistics-workflow', 'branch': '11.0'},

        {'usr': 'jobiols', 'repo': 'odoo-addons', 'branch': '11.0'},
        {'usr': 'ingadhoc', 'repo': 'odoo-argentina', 'branch': '11.0'},
        {'usr': 'ingadhoc', 'repo': 'product', 'branch': '11.0'},
        {'usr': 'ingadhoc', 'repo': 'argentina-sale', 'branch': '11.0'},
        {'usr': 'ingadhoc', 'repo': 'account-financial-tools',         'branch': '11.0'},
        {'usr': 'ingadhoc', 'repo': 'account-payment', 'branch': '11.0'},
        {'usr': 'ingadhoc', 'repo': 'odoo-support', 'branch': '11.0'},
        {'usr': 'ingadhoc', 'repo': 'miscellaneous', 'branch': '11.0'},
        {'usr': 'ingadhoc', 'repo': 'argentina-reporting',         'branch': '11.0'},
        {'usr': 'ingadhoc', 'repo': 'stock', 'branch': '11.0'},
        {'usr': 'ingadhoc', 'repo': 'website', 'branch': '11.0'},
        {'usr': 'ingadhoc', 'repo': 'sale', 'branch': '11.0'},
        {'usr': 'ingadhoc', 'repo': 'product', 'branch': '11.0'},
        {'usr': 'ingadhoc', 'repo': 'partner', 'branch': '11.0'},
        {'usr': 'ingadhoc', 'repo': 'account-invoicing', 'branch': '11.0'},
        {'usr': 'ingadhoc', 'repo': 'reporting-engine', 'branch': '11.0'},
        {'usr': 'ingadhoc', 'repo': 'aeroo_reports', 'branch': '11.0'},
        {'usr': 'ingadhoc', 'repo': 'account-financial-tools', 'branch': '11.0'},
        {'usr': 'ingadhoc', 'repo': 'sale', 'branch': '11.0'},

        {'usr': 'oca', 'repo': 'partner-contact', 'branch': '11.0'},
        {'usr': 'oca', 'repo': 'web', 'branch': '11.0'},
        {'usr': 'oca', 'repo': 'server-tools', 'branch': '11.0'},
        {'usr': 'oca', 'repo': 'server-brand', 'branch': '11.0'},
        {'usr': 'oca', 'repo': 'social', 'branch': '11.0'},
        {'usr': 'oca', 'repo': 'knowledge', 'branch': '11.0'},
        {'usr': 'oca', 'repo': 'sale-workflow', 'branch': '11.0'},
    ],
    'docker': [
        {'name': 'odoo', 'usr': 'jobiols', 'img': 'odoo-ent', 'ver': '11.0e'},
        {'name': 'postgres', 'usr': 'postgres', 'ver': '11.1-alpine'},
        {'name': 'nginx', 'usr': 'nginx', 'ver': 'latest'},
        {'name': 'aeroo', 'usr': 'adhoc', 'img': 'aeroo-docs'},
    ]
}
