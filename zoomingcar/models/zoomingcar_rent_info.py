from odoo import models , fields
from datetime import date

class ZoomingcarRentInfo(models.Model):
    _name="zoomingcar.rent.info"
    _description="this is zooming car rental info model store the rental information"
    
    name=fields.Char("Name",required=True)
    license_plate=fields.Char('License Plate')
    postcode=fields.Char('Postcode')
    location_id=fields.Many2one('zoomingcar.rent.location',string="Location")
    states=fields.Selection(selection=[('available','Available'),('booked','Booked')], default='available')
    driver=fields.Boolean('Driver')
    driver_id=fields.Many2one('res.partner','Driver Name')
    deposit=fields.Integer(string="Deposit")
    last_odometer=fields.Float('Last Odometer', required=True)
    chassis_number=fields.Integer('Chassis Number')
    purchase_value=fields.Integer('Purchase Value')
    type_id=fields.Many2one('zoomingcar.rent.type',string='Car Type')
    seats_number=fields.Integer('Seats Number')
    colour=fields.Char('Colour')
    model_year=fields.Integer('Model Year')
    transmission_type=fields.Selection(selection=[('manual','Manual'),('automatic','Automatic')])
    horse_power=fields.Integer('Horse Power')
    fuel_type=fields.Selection(
        selection=[('diesel','Diesel'),('petrol','Petrol'),('cng','Cng')]
        )
    rent_per_km=fields.Float('Rent Per Km',default = 20.0)
    rent_per_hours=fields.Float('Rent Per Hours',default = 150.0)
    rent_per_day=fields.Float('Rent Per Day',default = 2000.0)
    state=fields.Selection(
        selection=[('new','New'),('booked','Booked') ],
        default='new'
        )
    booking_ids=fields.One2many("zoomingcar.rent.booking","info_id")
    car_image=fields.Image(string="Image")



    _sql_constraints=[
        ('check_deposit', 'CHECK(deposit>=0)', "Price must be Postive")
    ]
