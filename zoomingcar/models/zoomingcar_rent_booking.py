from odoo import models , fields,api
from odoo.exceptions import ValidationError
from datetime import *


class ZoomingcarRentBooking(models.Model):
    _name="zoomingcar.rent.booking"
    _description="This is booking model used to store booking details"



    from_date=fields.Date('From Date',copy=False,default=date.today())
    to_date=fields.Date('To Date',copy=False,default=date.today())
    name=fields.Char()
    buyer_id = fields.Many2one('res.partner', string='Customer Name')
    rent_type=fields.Selection(
        selection=[('kilometers','Kilometers'),('hours','Hours'),('days','Days')],
        default='kilometers'
        )
    info_id=fields.Many2one("zoomingcar.rent.info")
    hours_days=fields.Integer(required=True,string="Hours/Km")
    total_rent=fields.Float(compute="_rent_calculation",default=0.0)
    status=fields.Selection(string="status", selection=[('accepted','Accepted'),('refused','Refused')])
    date=fields.Date(default=date.today(),required=True)



    @api.depends('hours_days','from_date','to_date')
    def _rent_calculation(self):
        for record in self:
            if record.rent_type=='kilometers':
                record.total_rent=record.info_id.rent_per_km * record.hours_days
            
            elif record.rent_type=='hours':
                record.total_rent=record.info_id.rent_per_hours * record.hours_days
            
            else:
                a=(record.to_date-record.from_date).days
                record.total_rent=record.info_id.rent_per_day*a

     
    def action_accepted(self):
        for record in self:
            record.status='accepted'
            record.info_id.state='booked'

    def action_refused(self):
        for record in self:
            record.status='refused'

