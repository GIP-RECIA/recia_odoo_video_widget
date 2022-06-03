# -*- coding: utf-8 -*-
{
    'name': "recia_odoo_video_widget",

    'summary': """
        Replace the original media JS widget.
    """,

    'description': """
        Replace the original media JS widget.
        Add GIP Recia's PODs compatibility.
    """,

    'author': "Grégory Brousse<pro@gregory-brousse.fr>",
    'website': "https://www.recia.fr",

    'category': 'Technical',
    'version': '0.1',

    'depends': ['web_editor'],
    'data': [],
    'demo': [],
    'assets': {
        'web_editor.assets_wysiwyg': [
            ('replace', '/web_editor/static/src/js/wysiwyg/widgets/media.js', '/recia_odoo_video_widget/static/src/js/media.js'),
        ],
    }
}