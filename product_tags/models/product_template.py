# Copyright <YEAR(S)> <AUTHOR(S)>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, tools, SUPERUSER_ID, _


class Product(models.Model):
    _inherit = "product.template"

    tag_id = fields.Many2many(
        'product.tag',
        column1='product_id',
        column2='tag_id',
        string='Etiquetas')


