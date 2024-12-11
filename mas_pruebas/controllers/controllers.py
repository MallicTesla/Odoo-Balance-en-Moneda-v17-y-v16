# -*- coding: utf-8 -*-
# from odoo import http


# class MasPruebas(http.Controller):
#     @http.route('/mas_pruebas/mas_pruebas', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mas_pruebas/mas_pruebas/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('mas_pruebas.listing', {
#             'root': '/mas_pruebas/mas_pruebas',
#             'objects': http.request.env['mas_pruebas.mas_pruebas'].search([]),
#         })

#     @http.route('/mas_pruebas/mas_pruebas/objects/<model("mas_pruebas.mas_pruebas"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mas_pruebas.object', {
#             'object': obj
#         })

