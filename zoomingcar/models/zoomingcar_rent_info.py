from odoo import models , fields , api
from datetime import date

class ZoomingcarRentInfo(models.Model):
    _name="zoomingcar.rent.info"
    _description="this is zooming car rental info model store the rental information"
    _inherit = ['mail.thread','mail.activity.mixin']
    _rec_name="name"
    # it is by default but just for reference
    
    name=fields.Char(string='Name',required=True)
    license_plate=fields.Char('License Plate')
    postcode=fields.Integer('Postcode')
    location_id=fields.Many2one('zoomingcar.rent.location',string="Location")
    tag_ids=fields.Many2many('zoomingcar.rent.tag',string="Tags",relation="zoomingcar_rent_tag_rel")
    # states=fields.Selection(selection=[('available','Available'),('booked','Booked')], default='available',tracking=True)
    driver=fields.Boolean(string='Driver')
    driver_id=fields.Many2one('res.users','Driver Name')
    deposit=fields.Integer(string="Deposit",tracking=True)
    last_odometer=fields.Float('Last Odometer', required=True)
    chassis_number=fields.Char(string='Chassis Number')
    purchase_value=fields.Integer(string='Purchase Value')
    type_id=fields.Many2one('zoomingcar.rent.type',string='Car Type',tracking=True)
    seats_number=fields.Integer(string='Seats Number')
    color=fields.Char(string='Color',tracking=True)
    model_year=fields.Integer(string='Model Year')
    transmission_type=fields.Selection(selection=[('manual','Manual'),('automatic','Automatic')],tracking=True)
    horse_power=fields.Char(string='Horse Power')
    fuel_type=fields.Selection(
        selection=[('diesel','Diesel'),('petrol','Petrol'),('cng','Cng')]
        )
    rent_per_km=fields.Float(string='Rent Per Km',default = 20.0)
    rent_per_hours=fields.Float(string='Rent Per Hours',default = 150.0)
    rent_per_day=fields.Float(string='Rent Per Day',default = 2000.0)
    state=fields.Selection(
        selection=[('new','New'),('booked','Booked') ],
        default='new',
        tracking =True
        )
    booking_ids=fields.One2many("zoomingcar.rent.booking","info_id")
    car_image=fields.Image(string="Image",tracking=True)
    favorite=fields.Boolean()
    seq_name = fields.Char(string='Car Reference', required=True,readonly=True, default=lambda self: ('New'))
    kanban_state = fields.Selection([
        ('normal','Grey'),
        ('done','Green'),
        ('blocked','Red')], string='Kanban State')

    @api.model
    def create(self,vals):
        vals['seq_name'] = self.env['ir.sequence'].next_by_code('zoomingcar.rent.info')
        return super(ZoomingcarRentInfo,self).create(vals)

    _sql_constraints=[
        ('check_deposit','CHECK(deposit>=0)', "Deposit must be Postive")
    ]   