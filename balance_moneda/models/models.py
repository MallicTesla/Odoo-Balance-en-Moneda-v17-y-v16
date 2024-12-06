# -*- coding: utf-8 -*-

from odoo import models, fields

class AccountEntry(models.Model):
    _name = 'accounting_entries.account_entry'
    _description = 'Apunte Contable Personalizado'

    name = fields.Char(string='Descripción', required=True)
    date = fields.Date(string='Fecha', required=True, default=fields.Date.context_today)
    debit = fields.Float(string='Debe', default=0.0)
    credit = fields.Float(string='Haber', default=0.0)
    currency_id = fields.Many2one('res.currency', string='Divisa')
    amount_currency = fields.Monetary(string='Importe en Divisa', currency_field='currency_id')
    company_currency_id = fields.Many2one('res.currency', string='Moneda de la Compañía', required=True)
    balance_currency = fields.Monetary(
        string='Balance en Moneda',
        compute='_compute_balance_currency',
        store=True,
        currency_field='company_currency_id'
    )

    def _compute_balance_currency(self):
        for record in self:
            record.balance_currency = record.debit - record.credit
