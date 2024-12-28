# -----------------------------------------------------------------------------------
#
#    Copyright (C) 2022 jeo Software  (http://www.jeosoft.com.ar)
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
    "name": "sams17e",
    "version": "17.0.1.0.0",
    "license": "Other OSI approved licence",
    "category": "Tools",
    "summary": "Customización Sams",
    "author": "jeo Software",
    "depends": [
    ],
    "data": [],
    "test": [],
    "installable": True,
    "application": True,
    "config": [],
    # Here begins odoo-env manifest configuration
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # manifest version, if omitted it is backward compatible
    "env-ver": "2",
    # if Enterprise it installs in a different directory than community
    "odoo-license": "EE",
    # port where odoo starts serving pages
    "port": "8069",
    # list of url repos to install in the form 'repo-url directory'
    "git-repos": [
        "https://github.com/jobiols/cl-sams.git -b 17.0e",
#        "git@github.com:jobiols/jeo-enterprise.git",
        # OCA
        # "https://github.com/OCA/server-tools oca-server-tools",
        # "https://github.com/OCA/stock-logistics-workflow oca-stock-logistics-workflow",
        # "https://github.com/OCA/sale-workflow oca-sale-workflow",
        # "https://github.com/OCA/field-service oca-field-service",
        # "https://github.com/OCA/hr oca-hr",
        # "https://github.com/OCA/social oca-social",
        # "https://github.com/OCA/partner-contact oca-partner-contact",
        # "https://github.com/OCA/pos oca-pos",
        # "https://github.com/OCA/reporting-engine oca-reporting-engine",
        # "https://github.com/OCA/hr-expense oca-hr-expense",
        # "https://github.com/OCA/edi oca-edi",
        # "https://github.com/OCA/manufacture oca-manufacture",
        # "https://github.com/OCA/crm oca-crm",
        # "https://github.com/OCA/purchase-workflow oca-purchase-workflow",
        # "https://github.com/OCA/project oca-project",
        # "https://github.com/OCA/search-engine oca-search-engine",
        # "https://github.com/OCA/maintenance oca-maintenance",
        # "https://github.com/OCA/stock-logistics-warehouse oca-stock-logistics-warehouse",
        # "https://github.com/OCA/account-payment oca-account-payment",
        # "https://github.com/OCA/multi-company oca-multi-company",
        # "https://github.com/OCA/rma oca-rma",
        # "https://github.com/OCA/delivery-carrier oca-delivery-carrier",
        # "https://github.com/OCA/operating-unit oca-operating-unit",
        # "https://github.com/OCA/knowledge oca-knowledge",
        # "https://github.com/OCA/wms oca-wms",
        # "https://github.com/OCA/mis-builder oca-mis-builder",
        # "https://github.com/OCA/bank-payment oca-bank-payment",
        # "https://github.com/OCA/account-invoice-reporting oca-account-invoice-reporting",
        # "https://github.com/OCA/timesheet oca-timesheet",
        # "https://github.com/OCA/web oca-web",
        # "https://github.com/OCA/account-financial-tools oca-account-financial-tools",
        # "https://github.com/OCA/sale-reporting oca-sale-reporting",
        # "https://github.com/OCA/account-financial-reporting oca-account-financial-reporting",
        # "https://github.com/OCA/e-commerce oca-e-commerce",
        # "https://github.com/OCA/contract oca-contract",
        # "https://github.com/OCA/helpdesk oca-helpdesk",
        # "https://github.com/OCA/product-attribute oca-product-attribute",
        # "https://github.com/OCA/account-analytic",
        # "https://github.com/OCA/server-ux oca-server-ux",
        # "https://github.com/OCA/website oca-website",
        # "https://github.com/OCA/ddmrp oca-ddmrp",
        # "https://github.com/OCA/account-fiscal-rule oca-account-fiscal-rule",
        # "https://github.com/OCA/storage oca-storage",
        # "https://github.com/OCA/stock-logistics-reporting oca-stock-logistics-reporting",
        # "https://github.com/OCA/geospatial oca-geospatial",
        # "https://github.com/OCA/vertical-hotel oca-vertical-hotel",
        # "https://github.com/OCA/server-auth oca-server-auth",
        # "https://github.com/OCA/account-reconcile oca-account-reconcile",
        # "https://github.com/OCA/server-backend oca-server-backend",
        # "https://github.com/OCA/vertical-association oca-vertical-association",
        # "https://github.com/OCA/account-invoicing oca-account-invoicing",
        # "https://github.com/OCA/product-variant oca-product-variant",
        # "https://github.com/OCA/queue oca-queue",
        # "https://github.com/OCA/account-closing oca-account-closing",
        # "https://github.com/OCA/iot oca-iot",
        # "https://github.com/OCA/dms oca-dms",
        # "https://github.com/OCA/margin-analysis oca-margin-analysis",
        # "https://github.com/OCA/payroll oca-payroll",
        # "https://github.com/OCA/hr-holidays oca-hr-holidays",
        # "https://github.com/OCA/role-policy oca-role-policy",
        # "https://github.com/OCA/apps-store oca-apps-store",
        # "https://github.com/OCA/rest-framework rest-framework",
        # "https://github.com/OCA/brand rest-brand",
        # "https://github.com/OCA/report-print-send oca-report-print-send",
        # "https://github.com/OCA/server-brand oca-server-brand",
        # "https://github.com/OCA/business-requirement oca-business-requirement",
        # "https://github.com/OCA/commission oca-commission",
        # "https://github.com/OCA/product-pack oca-product-pack",
        # "https://github.com/OCA/currency oca-currency",
        # "https://github.com/OCA/credit-control oca-credit-control",
        # "https://github.com/OCA/stock-logistics-barcode oca-stock-logistics-barcode",
        # "https://github.com/OCA/event oca-event",
        # "https://github.com/OCA/hr-attendance oca-hr-attendance",
        # "https://github.com/OCA/website-cms oca-website-cms",
        # "https://github.com/OCA/survey oca-survey",
        # "https://github.com/OCA/stock-logistics-transport oca-stock-logistics-transport",
        # "https://github.com/OCA/manufacture-reporting oca-manufacture-reporting",
        # "https://github.com/OCA/management-system oca-management-system",
        # "https://github.com/OCA/fleet oca-fleet",
        # "https://github.com/OCA/project-reporting oca-project-reporting",
        # "https://github.com/OCA/stock-logistics-reporting oca-stock-logistics-reporting",
        # ingadhoc
        # Para el caso de la 17 y 18 adhoc tiene modificaciones que todavia no se pudieron mezclar en oca
        "https://github.com/ingadhoc/account-financial-tools.git sub_l10n-ar/account-financial-tools",
        "https://github.com/ingadhoc/account-payment.git sub_l10n-ar/account-payment",
        "https://github.com/ingadhoc/odoo-argentina.git sub_l10n-ar/odoo-argentina",
        "https://github.com/ingadhoc/argentina-sale.git sub_l10n-ar/argentina-sale",
        "https://github.com/ingadhoc/account-invoicing.git sub_l10n-ar/account-invoicing",
        "https://github.com/ingadhoc/odoo-argentina-ee.git sub_l10n-ar/odoo-argentina-ee",
        "https://github.com/ingadhoc/stock.git sub_l10n-ar/stock",
        "https://github.com/ingadhoc/aeroo_reports.git sub_l10n-ar/aeroo_reports",

        "https://github.com/adhoc-cicd/oca-server-tools sub_l10n-ar/oca-server-tools",
        "https://github.com/adhoc-cicd/oca-stock-logistics-workflow.git sub_l10n-ar/oca-stock-logistics-workflow",
        "https://github.com/adhoc-cicd/oca-web.git sub_l10n-ar/oca-web",

        # Odoomates
        # "https://github.com/odoomates/odooapps odoomates-odooapps",
    ],
    # list of images to use in the form 'name image-url'
    "docker-images": [
        "odoo jobiols/odoo-ent:17.0e",
        "postgres postgres:14.15-alpine",
    ],
}
