# -*- coding: utf-8 -*-
# from odoo import http


# class BalanceMoneda(http.Controller):
#     @http.route('/balance_moneda/balance_moneda', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/balance_moneda/balance_moneda/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('balance_moneda.listing', {
#             'root': '/balance_moneda/balance_moneda',
#             'objects': http.request.env['balance_moneda.balance_moneda'].search([]),
#         })

#     @http.route('/balance_moneda/balance_moneda/objects/<model("balance_moneda.balance_moneda"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('balance_moneda.object', {
#             'object': obj
#         })

