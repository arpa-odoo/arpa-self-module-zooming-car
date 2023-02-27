from odoo import models , fields

class ZoomingcarRentType(models.Model):
    _name="zoomingcar.rent.type"
    _description="this car store the car rental type information"


    name=fields.Char("Name",required=True)
    description=fields.Text("Description")