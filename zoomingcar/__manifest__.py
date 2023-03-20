{
    'name':'Zooming Car',
    'depends':['mail'],
    'summary':'This is a zooming car module used for handling the car rental bussiness',
    'author':'Arjun Panchal',
    'version':'1.0',
    'installable':True,
    'application':True,
    'auto_install':True,
    'license':'LGPL-3',
    'image':['icons.png'],
    'data':[
    'security/ir.model.access.csv',
    'wizard/add_booking_wizard_view.xml',
    'views/zoomingcar_rent_tag_views.xml',
    'views/zoomingcar_rent_booking_views.xml',
    'views/zoomingcar_rent_info_views.xml',
    'views/zoomingcar_rent_location_views.xml',
    'views/zoomingcar_rent_type_views.xml',
    'views/zoomingcar_menu.xml',
    'views/res_users_views.xml',
    ],
    'demo':[
    'demo/zoomingcar_demo.xml'
    ]

}

