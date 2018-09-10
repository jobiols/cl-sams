# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------------
#
#    Copyright (C) 2016  jeo Software  (http://www.jeosoft.com.ar)
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
    'name': 'sams',
    'version': '11.0.0.0',
    'license': 'Other OSI approved licence',
    'category': 'Tools',
    'summary': 'Customización Sams',
    'author': 'jeo Software',
    'depends': [

        # para la localizacion argentina
        'l10n_ar_account',
        'l10n_ar_afipws_fe',        # Factura Electrónica Argentina
        'l10n_ar_aeroo_einvoice',   # impresion de factura electronica aeroo
        'l10n_ar_account_vat_ledger_citi',
        'account_debt_management',  #
        'l10n_ar_aeroo_payment_group',  #

        'sale_management',
        'account_invoicing',
        'purchase',
        'project',

        # aplicaciones instaladas
#        'sale', 'l10n_ar_aeroo_sale',  # ventas
#        'purchase', 'l10n_ar_aeroo_purchase',  # compras
#        'account_accountant',  # permisos para contabilidad
#        'stock', 'stock_account', 'l10n_ar_aeroo_stock','sale_stock',
#        'product_unique',
#        'account_reconciliation_menu',  # agrega boton en partner
#        'base_state_active',  # Deactivate US States
#        'account_fix',  # Account Fixes
#        'account_invoice_tax_wizard',  # add manual taxes on invoices
#        'web_export_view',  # exportar vistas en excel
#        'account_clean_cancelled_invoice_number',  # borrar facturas canceladas

#        'account_document',
#        'account_withholding',
#        'barcodes',
#        'procurement_jit',
#        'report_extended_purchase',
#        'report_extended_sale',
#        'web_kanban', 'web_kanban_gauge', 'web_planner', 'web_settings_dashboard',
#        'web_tip', 'web_view_editor', 'base_import'
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
        {'usr': 'jobiols', 'repo': 'cl-vhing', 'branch': '11.0'},
        {'usr': 'ingadhoc', 'repo': 'odoo-argentina', 'branch': '11.0'},
        {'usr': 'ingadhoc', 'repo': 'account-financial-tools', 'branch': '11.0'},
        {'usr': 'ingadhoc', 'repo': 'account-payment', 'branch': '11.0'},
        {'usr': 'ingadhoc', 'repo': 'miscellaneous', 'branch': '11.0'},
        {'usr': 'ingadhoc', 'repo': 'argentina-reporting', 'branch': '11.0'},
        {'usr': 'ingadhoc', 'repo': 'reporting-engine', 'branch': '11.0'},
        {'usr': 'ingadhoc', 'repo': 'aeroo_reports', 'branch': '11.0'},
        {'usr': 'OCA', 'repo': 'partner-contact', 'branch': '11.0'},
        {'usr': 'OCA', 'repo': 'web', 'branch': '11.0'},
    ],
    'docker': [
        {'name': 'odoo', 'usr': 'jobiols', 'img': 'odoo-jeo', 'ver': '11.0'},
        {'name': 'postgres', 'usr': 'postgres', 'ver': '9.6'},
        {'name': 'nginx', 'usr': 'nginx', 'ver': 'latest'},
        {'name': 'aeroo', 'usr': 'adhoc', 'img': 'aeroo-docs'},
    ]
}
