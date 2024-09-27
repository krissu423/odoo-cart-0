{
    'name': 'Disable Add to Cart for 0€ Products',
    'version': '13.0.1.0.0',
    'summary': 'Disables the add to cart button for products with a price of 0€.',
    'category': 'Website',
    'author': 'Kristjan',
    'website': 'https://teval.ee',
    'license': 'AGPL-3',
    'depends': ['website_sale'],
    'data': [
        'views/product_template_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}