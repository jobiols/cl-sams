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
    'name': 'sams13e',
    'version': '13.0.0.0.0',
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
        'l10n_ar_stock',  # remito electronico argentino

        # utilitarios
        'l10n_ar_stock',
        'product_tags',
    ],

    'data': [
    ],
    'test': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'images': [],


    'limit_request': '8196',
    'limit_memory_soft': '640000000',
    'limit_memory_hard': '760000000',
    'limit_time_cpu': '60',
    'limit_time_real': '120',

    # Here begins odoo-env manifest configuration
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # manifest version, if omitted it is backward compatible
    'env-ver': '2',

    # if Enterprise it installs in a different directory than community
    'odoo-license': 'EE',

    # port where odoo starts serving pages
    'port': '8069',

    # list of url repos to install in the form 'repo-url directory'
    'git-repos': [

        'https://github.com/jobiols/cl-sams.git -b 13.0e',
        'https://github.com/oca/stock-logistics-workflow.git',

        'https://github.com/jobiols/odoo-addons.git',

        'https://github.com/ingadhoc/odoo-argentina.git',
        'https://github.com/ingadhoc/product.git',

        'https://github.com/ingadhoc/argentina-sale',
        'https://github.com/ingadhoc/account-financial-tools',
        'https://github.com/ingadhoc/account-payment',
        'https://github.com/ingadhoc/miscellaneous',
        'https://github.com/ingadhoc/argentina-reporting',
        'https://github.com/ingadhoc/stock',
        'https://github.com/ingadhoc/website',
        'https://github.com/ingadhoc/sale',
        'https://github.com/ingadhoc/product',
        'https://github.com/ingadhoc/partner',
        'https://github.com/ingadhoc/account-invoicing',
        'https://github.com/ingadhoc/reporting-engine',
        'https://github.com/ingadhoc/account-financial-tools',
        'https://github.com/ingadhoc/sale',
        'https://github.com/ingadhoc/account-invoicing',

        'https://github.com/oca/partner-contact',
        'https://github.com/oca/web',
        'https://github.com/oca/server-tools',
        'https://github.com/oca/social',
        'https://github.com/oca/sale-workflow',
        'https://github.com/oca/server-ux',
        'https://github.com/oca/contract',
    ],

    # list of images to use in the form 'name image-url'
    'docker-images': [
        'odoo jobiols/odoo-ent:13.0e',
        'postgres postgres:10.1-alpine',
        'nginx nginx'
    ]
}
