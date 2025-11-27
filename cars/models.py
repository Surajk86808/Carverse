from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField 
from multiselectfield import MultiSelectField


class Car(models.Model):

    # ---------- INDIA STATE CHOICES ----------
    state_choices = (
        ('AP', 'Andhra Pradesh'),
        ('AR', 'Arunachal Pradesh'),
        ('AS', 'Assam'),
        ('BR', 'Bihar'),
        ('CT', 'Chhattisgarh'),
        ('GA', 'Goa'),
        ('GJ', 'Gujarat'),
        ('HR', 'Haryana'),
        ('HP', 'Himachal Pradesh'),
        ('JH', 'Jharkhand'),
        ('KA', 'Karnataka'),
        ('KL', 'Kerala'),
        ('MP', 'Madhya Pradesh'),
        ('MH', 'Maharashtra'),
        ('MN', 'Manipur'),
        ('ML', 'Meghalaya'),
        ('MZ', 'Mizoram'),
        ('NL', 'Nagaland'),
        ('OD', 'Odisha'),
        ('PB', 'Punjab'),
        ('RJ', 'Rajasthan'),
        ('SK', 'Sikkim'),
        ('TN', 'Tamil Nadu'),
        ('TS', 'Telangana'),
        ('TR', 'Tripura'),
        ('UP', 'Uttar Pradesh'),
        ('UK', 'Uttarakhand'),
        ('WB', 'West Bengal'),
        ('DL', 'Delhi'),
        ('JK', 'Jammu & Kashmir'),
        ('LD', 'Lakshadweep'),
        ('PY', 'Puducherry'),
    )
    
    features_choices = (
        ('Air Conditioning', 'Air Conditioning'),
        ('Anti-Lock Braking System (ABS)', 'Anti-Lock Braking System (ABS)'),       
        ('Navigation System', 'Navigation System'),
        ('Power Steering', 'Power Steering'),
        ('Leather Seats', 'Leather Seats'),
        ('Bluetooth Connectivity', 'Bluetooth Connectivity'),
        ('Backup Camera', 'Backup Camera'),
        ('Cruise Control', 'Cruise Control'),
        ('Sunroof/Moonroof', 'Sunroof/Moonroof'),
        ('Alloy Wheels', 'Alloy Wheels'),
        ('Heated Seats', 'Heated Seats'),
        ('Automatic Windows', 'Automatic Windows'),
        ('Keyless Entry', 'Keyless Entry'),
        ('GPS Navigation', 'GPS Navigation'),
        ('Parking Sensors', 'Parking Sensors'), 
        ('Electric Mirrors', 'Electric Mirrors'),
        ('Remote Start', 'Remote Start'),
        ('Blind Spot Detection', 'Blind Spot Detection'),
        ('Lane Departure Warning', 'Lane Departure Warning'),
        ('LED Headlights', 'LED Headlights'),
        ('Rain Sensing Wipers', 'Rain Sensing Wipers'),
        ('Multi-Function Steering Wheel', 'Multi-Function Steering Wheel'),
        ('Onboard Computer', 'Onboard Computer'),
        ('Traction Control', 'Traction Control'),
        ('Tire Pressure Monitoring System (TPMS)', 'Tire Pressure Monitoring System (TPMS)'),
        ('Auto-Dimming Rearview Mirror', 'Auto-Dimming Rearview Mirror'),
        ('Heated Steering Wheel', 'Heated Steering Wheel'),
        ('Seat Memory', 'Seat Memory'),
        ('Front Fog Lights', 'Front Fog Lights'),
        ('Other', 'Other'),
    )

    # ---------- YEAR CHOICES ----------
    year_choice = [(r, r) for r in range(2000, datetime.now().year + 1)]

    # ---------- DOORS ----------
    door_choices = (
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    )

    # ---------- MODEL FIELDS ----------
    car_title = models.CharField(max_length=255)
    state = models.CharField(max_length=50, choices=state_choices)
    color = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField(choices=year_choice)
    features = MultiSelectField(choices=features_choices,blank=True)

    condition = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    description = RichTextField()

    body_style = models.CharField(max_length=100)

    # ---------- IMAGES ----------
    car_photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    car_photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    # ---------- CAR DETAILS ----------
    engine = models.CharField(max_length=100)
    transmission = models.CharField(max_length=100)
    interior = models.CharField(max_length=100)

    miles = models.IntegerField()
    doors = models.CharField(max_length=10, choices=door_choices)
    passengers = models.IntegerField()
    vin_no = models.CharField(max_length=100)
    mileage = models.IntegerField()

    fuel_type = models.CharField(max_length=100)
    no_of_owners = models.IntegerField()

    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.car_title
