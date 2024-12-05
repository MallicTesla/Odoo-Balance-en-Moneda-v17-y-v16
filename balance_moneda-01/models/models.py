from odoo import api, fields, models

class AccountMoveLine(models.Model):
    _name = "account.move.line"
    _inherit = "analytic.mixin"
    _description = "Journal Item"
    _order = "date desc, move_name desc, id"
    _check_company_auto = True
    _rec_names_search = ['name', 'move_id', 'product_id']

    # Parent fields
    move_id = fields.Many2one(
        comodel_name='account.move',
        string='Journal Entry',
        required=True,
        readonly=True,
        index=True,
        auto_join=True,
        ondelete="cascade",
        check_company=True,
    )
    journal_id = fields.Many2one(
        related='move_id.journal_id', store=True, precompute=True,
        index=True,
        copy=False,
    )
    company_id = fields.Many2one(
        related='move_id.company_id', store=True, readonly=True, precompute=True,
        index=True,
    )
    company_currency_id = fields.Many2one(
        string='Company Currency',
        related='move_id.company_currency_id', readonly=True, store=True, precompute=True,
    )
    move_name = fields.Char(
        string='Number',
        related='move_id.name', store=True,
        index='btree',
    )

    # Nuevos campos
    amount_currency = fields.Monetary(
        string='Amount in Currency',
        currency_field='currency_id',
        compute='_compute_amount_currency',
        readonly=True,
    )

    currency_id = fields.Many2one(
        'res.currency', string='Currency', required=True, readonly=True,
    )

    balance_in_currency = fields.Monetary(
        string='Balance in Company Currency',
        currency_field='company_currency_id',
        compute='_compute_balance_in_currency',
        store=True,
    )

    @api.depends('amount_currency', 'currency_id', 'company_currency_id')
    def _compute_balance_in_currency(self):
        for record in self:
            if record.currency_id == record.company_currency_id:
                record.balance_in_currency = record.amount_currency
            else:
                # Si es necesario usar el tipo de cambio de la moneda de la transacción
                record.balance_in_currency = record.amount_currency * record.currency_id.rate

    @api.depends('currency_id', 'amount_currency')
    def _compute_amount_currency(self):
        # Este método dependerá de cómo desees calcular el monto en la moneda de la transacción
        for record in self:
            if record.currency_id:
                # Calcula el valor de 'amount_currency' de acuerdo a la moneda de la transacción
                record.amount_currency = record.amount_currency * record.currency_id.rate

