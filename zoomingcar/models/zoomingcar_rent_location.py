from odoo import models , fields

class ZoomingcarRentLocation(models.Model):
    _name="zoomingcar.rent.location"
    _description="this model store the location of the car"

    name=fields.Char("Name",required=True)
    location_ids=fields.One2many('zoomingcar.rent.info','location_id')
