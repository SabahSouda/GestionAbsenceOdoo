
{
    'name': 'Gestion des Absences des Professeurs',
    'version': '1.0',
    'summary': 'Module simple pour gérer les absences des professeurs',
    'category': 'Education',
    'author': 'EMSI',
    'depends': ['base'],
    'application': True,
    'data': [
        'security/ir.model.access.csv',
        'views/professeur_views.xml',
        'views/absence_views.xml',
        'views/dashboard_view.xml',
        'views/menu.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'absences_professeurs/static/src/css/dashboard.css',
        ],
    },

    'installable': True,
    
}
