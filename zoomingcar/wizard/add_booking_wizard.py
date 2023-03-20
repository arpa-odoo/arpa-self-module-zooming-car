from odoo import models , fields,Command,api

class AddBookingWizard(models.TransientModel):
    _name="add.booking.wizard"
    _description="this is a wizard used for adding bookings directly in the selected cars"

    from_date=fields.Date('From Date',copy=False,default=fields.Date.today())
    to_date=fields.Date('To Date',copy=False,default=fields.Date.today())
    buyer_id = fields.Many2one('res.partner', string='Customer Name')
    rent_type=fields.Selection(
        selection=[('kilometers','Kilometers'),('hours','Hours'),('days','Days')],
        default='kilometers'
        )
    hours_km_days=fields.Integer(required=True,string="Hours/Km/days")
    total_rent=fields.Float(compute="_rent_calculation",default=0.0)
    info_id=fields.Many2one("zoomingcar.rent.info")




    @api.depends('hours_km_days','from_date','to_date')
    def _rent_calculation(self):
        for record in self:
            if record.rent_type=='kilometers':
                record.total_rent=record.info_id.rent_per_km * record.hours_km_days
            
            elif record.rent_type=='hours':
                record.total_rent=record.info_id.rent_per_hours * record.hours_km_days
            
            else:
                total_days=(record.to_date-record.from_date).days
                record.total_rent=record.info_id.rent_per_day*total_days


    def add_booking_function(self):
        result = self.env['zoomingcar.rent.info'].browse(self.env.context.get('active_ids'))
        for record in result:
                record.write({
                    'booking_ids':[
                        Command.create({
                            'from_date':self.from_date,
                            'to_date':self.to_date,
                            'buyer_id':self.buyer_id.id,
                            'rent_type':self.rent_type,
                            'hours_km_days':self.hours_km_days,
                            'total_rent':self.total_rent,
                        })
                    ]
                })