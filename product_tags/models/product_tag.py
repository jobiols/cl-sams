# For copyright and license notices, see __manifest__.py file in module root

from odoo import api, fields, models, tools, SUPERUSER_ID, _
from odoo.exceptions import UserError, ValidationError


class ProductTag(models.Model):
    _description = 'Product Tags'
    _name = 'product.tag'
    _order = 'parent_left, name'
    _parent_store = True
    _parent_order = 'name'

    name = fields.Char(
        string='Nombre de la etiqueta',
        required=True)
    color = fields.Integer(
        string='Color Index'
    )
    parent_id = fields.Many2one(
        'product.tag',
        string='Categoria padre',
        index=True,
        ondelete='cascade'
    )
    child_ids = fields.One2many(
        'product.tag',
        'parent_id',
        string='Categorias Hijas'
    )
    active = fields.Boolean(
        default=True,
        help="El campo activo permite esconder la categoria sin elimnarla."
    )
    parent_left = fields.Integer(
        string='Left parent',
        index=True
    )
    parent_right = fields.Integer(
        string='Right parent',
        index=True
    )
    product_ids = fields.Many2many(
        'product.template',
        column1='tag_id',
        column2='product_id',
        string='Products'
    )

    @api.constrains('parent_id')
    def _check_parent_id(self):
        if not self._check_recursion():
            raise ValidationError(_('Error ! No se pueden crear etiquetas '
                                    'recursivas'))

    @api.multi
    def name_get(self):
        """ Return the categories' display name, including their direct
            parent by default.

            If ``context['partner_category_display']`` is ``'short'``, the short
            version of the category name (without the direct parent) is used.
            The default is the long version.
        """
        if self._context.get('partner_category_display') == 'short':
            return super().name_get()

        res = []
        for category in self:
            names = []
            current = category
            while current:
                names.append(current.name)
                current = current.parent_id
            res.append((category.id, ' / '.join(reversed(names))))
        return res

    @api.model
    def name_search(self, name, args=None, operator='ilike', limit=100):
        args = args or []
        if name:
            # Be sure name_search is symetric to name_get
            name = name.split(' / ')[-1]
            args = [('name', operator, name)] + args
        return self.search(args, limit=limit).name_get()
