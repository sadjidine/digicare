# -*- coding: utf-8 -*-
# from odoo import http


# class Digicare(http.Controller):
#     @http.route('/digicare/digicare', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/digicare/digicare/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('digicare.listing', {
#             'root': '/digicare/digicare',
#             'objects': http.request.env['digicare.digicare'].search([]),
#         })

#     @http.route('/digicare/digicare/objects/<model("digicare.digicare"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('digicare.object', {
#             'object': obj
#         })

