# -*- coding: utf-8 -*-
# from odoo import http


# class ThemeHaqueSilver(http.Controller):
#     @http.route('/theme_haque_silver/theme_haque_silver/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/theme_haque_silver/theme_haque_silver/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('theme_haque_silver.listing', {
#             'root': '/theme_haque_silver/theme_haque_silver',
#             'objects': http.request.env['theme_haque_silver.theme_haque_silver'].search([]),
#         })

#     @http.route('/theme_haque_silver/theme_haque_silver/objects/<model("theme_haque_silver.theme_haque_silver"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('theme_haque_silver.object', {
#             'object': obj
#         })
