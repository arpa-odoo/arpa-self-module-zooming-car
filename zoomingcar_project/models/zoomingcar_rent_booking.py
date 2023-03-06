from odoo import models,fields,Command

class ZoomingcarRentBooking(models.Model):
    _inherit ="zoomingcar.rent.booking"

    def action_accepted(self):
        self.env['project.project'].create(
            {
            "name":self.buyer_id.name,
            'partner_id':self.buyer_id.id,
            'task_ids':[
            Command.create(
            {
            'name':'Rent',
            }
            )
            ]
            }
        )
        return super().action_accepted()