from odoo import models, fields

class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    balance_currency = fields.Monetary(
        string='Balance in Currency',
        currency_field='currency_id',  # Usar la moneda del apunte contable
        help='Balance in the currency defined in the account.',
    )
