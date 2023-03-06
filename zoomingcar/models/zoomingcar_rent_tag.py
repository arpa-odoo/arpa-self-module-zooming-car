from odoo import models, fields


class ZoomingcarRentTag(models.Model):
    _name="zoomingcar.rent.tag"
    _description="This is zoomingcar tag model for giving tags to the cars "
    _order="name"



    name = fields.Char(string="Tag Name",required=True)
    color = fields.Integer()

    _sql_constraints = [
        ('check_tag_name', 'UNIQUE(name)', 'The name must be unique')
    ]