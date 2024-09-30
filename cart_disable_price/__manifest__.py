# -*- coding: utf-8 -*-
{
    'name': "cart_disable_price",
    'summary': "Meant to disable add to cart button when price is 0 and disables products with the price 0 from being listed",
    'description': """
        This module hides the 'Add to Cart' button for products with a price of 0.
    """,
    'author': "My Company",
    'website': "http://www.yourcompany.com",
    'category': 'Website',
    'version': '0.1',
    'depends': ['base', 'website_sale'],
    'data': [
        'views/product_template_views.xml',
        'views/views.xml',
    ],
}