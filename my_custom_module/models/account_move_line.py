from odoo import models, fields, api

class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    balance_currency = fields.Monetary(
        string='Balance en Moneda',
        currency_field='company_currency_id',
        compute='_compute_balance_currency',
        store=True
    )

    @api.depends('debit', 'credit', 'amount_currency', 'currency_id')
    def _compute_balance_currency(self):
        for line in self:
            if not line.currency_id or line.currency_id == line.company_currency_id:
                line.balance_currency = line.debit - line.credit
            else:
                line.balance_currency = line.amount_currency
