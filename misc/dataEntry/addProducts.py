
from ProductManagement import models


category1 = models.CatalogCategory()
category1.name = 'Dremel'
category1.save()


category2 = models.CatalogCategory()
category2.name = 'Benchtop'
category2.parent_id = 1
category2.save()


category3 = models.CatalogCategory()
category3.name = 'Compact'
category3.parent_id = 1
category3.save()


category4 = models.CatalogCategory()
category4.name = 'Multitools'
category4.parent_id = 1
category4.save()





product1 = models.Product()
product1.name = '9100 Fortiflex with Foot Switch'
product1.category_id = 2
product1.description = """
The Dremel Fortiflex is a high quality precision tool, consisting of a powerful hanging motor (300W), a patented heavy duty flexible shaft, an exchangeable precision hand piece and a foot pedal for variable speed control (0-20.000rpm). Variable shank diameter (0.3 - 4.0mm), suitable for all high quality Dremel accessories.

The ideal tool for stationary projects, like woodworking, jewellery making, stone working, car restoration, or any project where a combination of power and precision is required. The Dremel Fortiflex: power meets precision.

Contents:
* Dremel Fortiflex motor
* Heavy Duty flexshaft
* Hand piece
* Foot pedal
* 21 High quality Dremel accessories
* Hanging hook
* Inspiring welcome poster
* Instruction manual

UK plug 230 Volt.

Accessories included: 431, 438, 430, 408, 432, 407, 117, 9910, 7103, 403, 84922, 953 and 628.
"""

product1.manufacturer = "Dremel"
product1.price = 247
product1.save()




product2 = models.Product()
product2.name = 'MotoSaw MS20'
product2.category_id = 2
product2.description = """
The Dremel Moto-Saw is a compact and easy-to-use scroll saw for making detailed cuts in different materials. With its range of different saw blades, the Dremel Moto-Saw can handle many different materials easily. Thanks to its detachable fretsaw, it can be used not only stationary but in-hand anywhere. This user-friendly scroll saw is not only easy to store and set-up, but also easy to operate.

Features and Benefits
Easy to use: quick accessory change combined with effortless set-up and storage due to its compact size.
Dual functioning: stationary mode for precision work and handheld mode for larger work pieces.
Reduced vibration: hold down foot.
Precise straight cuts: guide rails and parallel guide to assist cutting up to 18 mm.
Match speed to project at hand: Full variable speed control (1.500-2.250 RPM).

Contents
Dremel Moto-Saw
2x General Purpose Wood Cutting Saw Blade (MS51)
2x Fine Wood Cutting Saw Blade (MS52)
1 x Metal Cutting Saw Blade (MS53)
Parallel Guide attachment
Instruction manual
Sturdy and spacious storage case

Technical specifications
Rated power input: 70 W
Voltage: 220 - 240 V
Weight: 1.10 kg
No load speed: 1.500 - 2.250 1/min
"""

product2.manufacturer = "Dremel"
product2.price = 97

product2.save()





product3 = models.Product()
product3.name = 'DSM20 Saw Max Kit'
product3.category_id = 3
product3.description = """
The Dremel DSM20 is the ultimate compact saw with an excellent line of sight and powerful 710 Watt motor.

The saw easily performs precise straight, plunge and flush cuts into materials up to 20mm thick including wood, metal, tiles and bricks.

Features and Benefits
•Excellent line of sight: for accurate cutting.
•Abrasive wheel technology: for straight cuts, plunge cuts and flush cuts in wood, metal, tile, plastic and masonry.
•Worm drive gearing: for durability and power.
•Powerful 710W motor: for tough applications.
•Adjustable depth guide: for precision and control.
•Dust extraction port: for clean working environment.

Contents
•Dremel DSM20 tool
•1x DSM500 Multipurpose Carbide Cutting Wheel
•3x DSM510 Metal and Plastic Cutting Wheel
•Vacuum Cleaner Attachment
•Straight Edge Guide
•Cutting Guide
•Inspiring welcome DVD
•Sturdy and spacious storage case

Technical specifications
Rated power input: 710 W
Voltage: 220 - 240 V UK 3 pin plug
Weight: 1,70 kg
No load speed: 17.000 1/min
"""

product3.manufacturer = "Dremel"
product3.price = 117

product3.save()




product4 = models.Product()
product4.name = '6800 Trio Tool'
product4.category_id = 3
product4.description = """
The Dremel TRIO has a 3 in 1 Spiral System which enables you to cut, sand and rout with 1 and the same tool. The Dremel TRIO has superior ergonomics, a 2 position handle and variable speed which ensures the most optimal rate of working in different materials. With its 360° spiral cutting technology and plunge-cut ability, the tool makes quick and freehand cuts in wood, plastic, drywall, metal, and wall tile.

• Cuts, Sands and Routs: one tool, multiple applications.
• Soft start: smooth start without jerk effect.
• Electronic feedback: maintains speed under load for better finish of workpiece.
• Adjustable RPM: for precise working in different materials and applications.
• Pivoting handle: easier work orientation (horizontal & vertical). • Pistol grip: comfortable handling.
• Adjustable working depth: for working in various material thickness.
• Non marking foot: won't scratch delicate surfaces.
• Second Hand Grip zone: for maximum control.
• Vacuum Attachment: for cleaner working environment.

Contents:
• Dremel Trio™
• 1x TR407 Sanding Mandrel
• 3x TR408 Sanding Band P60
• 3x TR432 Sanding Band P120
• 1x TR563 Multipurpose Carbide Cutting Bit
• 1x TR654 Straight Router Bit
• Vacuum Cleaner Attachment
• Line and Circle Cutter Attachment
• Inspiring welcome poster
• Instruction manual
• Sturdy and spacious storage case

Technical specification:
Rated power input: 200 W
Voltage: 230-240 V
Weight: 1,20 kg
No load speed: 10.000 - 20.000 1/min

** Please note: this Trio tool only accepts bits with 4.8mm shank. Compaitble item part numbers begin with TR.

"""

product4.manufacturer = "Dremel"
product4.price = 67

product4.save()


product5 = models.Product()
product5.name = '4200-4/75 EZ Change Kit'
product5.category_id = 4
product5.description = """The powerful Dremel 4200 is the first multitool with an integrated accessory quick change mechanism: EZ Change. This innovative feature ensures keyless accessory change within seconds.

Thanks to it's electronic feedback and powerful motor the tool always delivers maximum force when the job gets tougher. Together with the soft grip and precise speed setting you are in perfect control of every situation.

The Dremel 4200: top technology and maximum performance.

Features:
EZ Change: easy pull levers for the fastest, keyless accessory change
175W motor for high performance
Electronic feedback for enhanced torque and performance
Full variable speed control (5.000 - 33.000 RPM) for maximum precision
Soft grip in all gripping areas for excellent handling
Separate on/off switch for easy handling
Not compatible with the 628, 4485 and 4486 accessories

Contents:
Dremel 4200 tool
75 high quality Dremel accessories
Cutting Guide attachment
Line & Circle Cutter
Shaping Platform attachment
Comfort Guard attachment
Inspiring information DVD
"""

product5.manufacturer = "Dremel"
product5.price = 137

product5.save()
