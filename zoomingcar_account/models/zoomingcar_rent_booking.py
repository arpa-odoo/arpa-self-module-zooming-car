from odoo import models ,fields,Command

class ZoomingcarRentBooking(models.Model):
    _inherit = "zoomingcar.rent.booking"


    def action_accepted(self):
        self.env['account.move'].create(
            {
            'name':self.buyer_id.name,
            'partner_id':self.buyer_id.id,
            'move_type':'out_invoice',
            'invoice_line_ids':[
            Command.create({
                'name':'Rent',
                'price_unit':self.total_rent
            }),
            Command.create({
                'name':'Booking Charge',
                'price_unit':100.0
            })]
            }
        )
        return super().action_accepted()