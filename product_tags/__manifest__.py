# Copyright 2019 jeo Software
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Product Tags",
    "summary": "Agrega etiquetas a los productos",
    "version": "12.0.0.0.0",
    "development_status": "Production/Stable",  #  "Alpha|Beta|Production/Stable|Mature",
    "category": "Tools",
    "website": "http://jeosoft.com.ar",
    "author": "jeo Software",
    "maintainers": ["jobiols"],
    "license": "AGPL-3",
    "application": False,
    "installable": False,
    "preloadable": False,
    "external_dependencies": {
        "python": [],
        "bin": [],
    },
    "excludes": [],
    "depends": [
        "base",
        'product'
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/product_view.xml",
    ],
    "demo": [
        "demo/product_tags.xml",
    ],
    "qweb": [
    ]
}
