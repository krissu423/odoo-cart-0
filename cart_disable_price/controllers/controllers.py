# -*- coding: utf-8 -*-
# from odoo import http


# class CartDisablePrice(http.Controller):
#     @http.route('/cart_disable_price/cart_disable_price/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cart_disable_price/cart_disable_price/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('cart_disable_price.listing', {
#             'root': '/cart_disable_price/cart_disable_price',
#             'objects': http.request.env['cart_disable_price.cart_disable_price'].search([]),
#         })

#     @http.route('/cart_disable_price/cart_disable_price/objects/<model("cart_disable_price.cart_disable_price"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cart_disable_price.object', {
#             'object': obj
#         })
