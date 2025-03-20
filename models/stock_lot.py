from odoo import fields, models


class CustomProductionLot(models.Model):
    _inherit = 'stock.lot'

    x_active = fields.Boolean(
        default=True,
        string="Active",
        help="Set to true for archived lot numbers otherwise false",
    )
