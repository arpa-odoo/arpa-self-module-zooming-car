from odoo import models , fields

class ResUsers(models.Model):
    _inherit="res.users" 
    # _here name is not necessary bcoz we manipulate in the same model

    car_ids=fields.One2many("zoomingcar.rent.info","driver_id" )
    