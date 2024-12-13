from odoo import models, fields, api

class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    balance_currency = fields.Monetary(
        string='Balance en Moneda',
        currency_field='account_currency_id',  # Cambio: moneda de la cuenta
        compute='_compute_balance_currency',
        store=True
    )

    account_currency_id = fields.Many2one(
        'res.currency',
        related='account_id.currency_id',
        string='Moneda de la Cuenta',
        readonly=True
    )

    @api.depends('debit', 'credit', 'amount_currency', 'currency_id', 'account_currency_id')
    def _compute_balance_currency(self):
        for line in self:
            if line.account_currency_id:
                if line.currency_id == line.account_currency_id:
                    line.balance_currency = line.amount_currency
                elif not line.currency_id or line.currency_id == line.company_currency_id:
                    line.balance_currency = line.debit - line.credit
                else:
                    # Convertir el balance a la moneda de la cuenta contable
                    balance = line.debit - line.credit
                    line.balance_currency = line.currency_id._convert(
                        balance,
                        line.account_currency_id,
                        line.company_id,
                        line.date
                    )
            else:
                line.balance_currency = line.debit - line.credit
