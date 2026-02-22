import tkinter as tk
from tkinter import font as tkfont
import time
import random
import json
import os

class Car:
    """Represents a car with extensive details, now with a futuristic twist."""
    def __init__(self, make, model, year, color, engine, horsepower, torque,
                 drivetrain, transmission, acceleration, top_speed, fuel_economy, price,
                 ai_level, holographic_color, description):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.engine = engine
        self.horsepower = horsepower
        self.torque = torque
        self.drivetrain = drivetrain
        self.transmission = transmission
        self.acceleration = acceleration  # 0-60 mph in seconds
        self.top_speed = top_speed        # mph
        self.fuel_economy = fuel_economy  # combined mpg (or MPGe for Tesla)
        self.price = price                 # USD
        self.ai_level = ai_level
        self.holographic_color = holographic_color
        self.description = description

    def display_name(self):
        return f"{self.year} {self.make} {self.model}"

    def to_dict(self):
        """Convert Car object to dictionary for JSON serialization."""
        return {
            "make": self.make,
            "model": self.model,
            "year": self.year,
            "color": self.color,
            "engine": self.engine,
            "horsepower": self.horsepower,
            "torque": self.torque,
            "drivetrain": self.drivetrain,
            "transmission": self.transmission,
            "acceleration": self.acceleration,
            "top_speed": self.top_speed,
            "fuel_economy": self.fuel_economy,
            "price": self.price,
            "ai_level": self.ai_level,
            "holographic_color": self.holographic_color,
            "description": self.description
        }

    @classmethod
    def from_dict(cls, data):
        """Create Car object from dictionary."""
        return cls(
            data["make"], data["model"], data["year"], data["color"],
            data["engine"], data["horsepower"], data["torque"],
            data["drivetrain"], data["transmission"], data["acceleration"],
            data["top_speed"], data["fuel_economy"], data["price"],
            data["ai_level"], data["holographic_color"], data["description"]
        )

def generate_additional_cars(target_count=10000):
    """Generate a massive list of cars using randomized realistic data."""
    additional = []

    # Extensive list of makes and their typical models with base specs
    makes_db = {
        "Ford": [
            ("Fiesta", "1.6L I4", 120, 112, "FWD", "5-speed manual", 8.5, 115, 32, 16000),
            ("Focus", "2.0L I4", 160, 146, "FWD", "6-speed auto", 7.5, 130, 28, 22000),
            ("Mustang", "5.0L V8", 450, 410, "RWD", "6-speed manual", 4.2, 155, 18, 45000),
            ("F-150", "3.5L V6 EcoBoost", 400, 500, "4WD", "10-speed auto", 5.5, 120, 20, 55000),
            ("Explorer", "2.3L EcoBoost", 300, 310, "AWD", "10-speed auto", 6.5, 130, 22, 48000),
            ("Escape", "1.5L EcoBoost", 180, 190, "FWD", "8-speed auto", 8.0, 120, 28, 28000),
            ("Bronco", "2.7L V6", 330, 415, "4WD", "7-speed manual", 6.0, 140, 17, 38000),
        ],
        "Chevrolet": [
            ("Spark", "1.4L I4", 98, 94, "FWD", "CVT", 9.5, 105, 33, 14000),
            ("Cruze", "1.4L Turbo", 153, 177, "FWD", "6-speed auto", 7.8, 125, 30, 21000),
            ("Camaro", "6.2L V8", 455, 455, "RWD", "6-speed manual", 4.0, 165, 16, 42000),
            ("Corvette", "6.2L V8", 490, 465, "RWD", "8-speed dual-clutch", 2.9, 194, 19, 62000),
            ("Silverado", "5.3L V8", 355, 383, "4WD", "8-speed auto", 6.5, 120, 18, 50000),
            ("Equinox", "1.5L Turbo", 170, 203, "FWD", "6-speed auto", 8.5, 115, 28, 26000),
            ("Tahoe", "5.3L V8", 355, 383, "4WD", "10-speed auto", 7.0, 115, 17, 55000),
        ],
        "Honda": [
            ("Civic", "2.0L I4", 158, 138, "FWD", "CVT", 7.2, 125, 33, 22000),
            ("Accord", "2.0L Turbo", 252, 273, "FWD", "10-speed auto", 5.5, 145, 26, 32000),
            ("CR-V", "1.5L Turbo", 190, 179, "AWD", "CVT", 7.5, 120, 30, 30000),
            ("Pilot", "3.5L V6", 280, 262, "AWD", "9-speed auto", 6.5, 115, 22, 40000),
            ("Odyssey", "3.5L V6", 280, 262, "FWD", "10-speed auto", 6.8, 115, 22, 37000),
            ("Ridgeline", "3.5L V6", 280, 262, "AWD", "9-speed auto", 6.5, 115, 21, 42000),
        ],
        "Nissan": [
            ("Versa", "1.6L I4", 122, 114, "FWD", "CVT", 9.0, 115, 35, 16000),
            ("Sentra", "2.0L I4", 149, 146, "FWD", "CVT", 8.0, 125, 33, 21000),
            ("Altima", "2.5L I4", 188, 180, "FWD", "CVT", 6.8, 130, 32, 26000),
            ("Maxima", "3.5L V6", 300, 261, "FWD", "CVT", 5.8, 140, 24, 38000),
            ("GT-R", "3.8L Twin-Turbo V6", 565, 467, "AWD", "6-speed dual-clutch", 2.9, 196, 16, 115000),
            ("Z", "3.0L Twin-Turbo V6", 400, 350, "RWD", "6-speed manual", 4.3, 155, 19, 50000),
            ("Rogue", "1.5L Turbo", 201, 225, "AWD", "CVT", 7.2, 120, 30, 29000),
            ("Pathfinder", "3.5L V6", 284, 259, "4WD", "9-speed auto", 7.0, 115, 23, 38000),
        ],
        "BMW": [
            ("2 Series", "2.0L Turbo", 228, 258, "RWD", "8-speed auto", 5.5, 130, 27, 38000),
            ("3 Series", "2.0L Turbo", 255, 294, "RWD", "8-speed auto", 5.4, 155, 30, 43000),
            ("5 Series", "3.0L Turbo", 335, 331, "RWD", "8-speed auto", 5.0, 155, 26, 56000),
            ("X3", "2.0L Turbo", 248, 258, "AWD", "8-speed auto", 6.0, 130, 24, 47000),
            ("X5", "3.0L Turbo", 335, 330, "AWD", "8-speed auto", 5.3, 155, 24, 61000),
            ("M3", "3.0L Twin-Turbo", 473, 406, "RWD", "6-speed manual", 3.8, 155, 19, 72000),
            ("M4", "3.0L Twin-Turbo", 473, 406, "RWD", "6-speed manual", 3.8, 155, 19, 75000),
            ("M5", "4.4L Twin-Turbo", 600, 553, "AWD", "8-speed auto", 3.2, 190, 16, 105000),
        ],
        "Mercedes-Benz": [
            ("A-Class", "2.0L Turbo", 188, 221, "FWD", "7-speed dual-clutch", 6.3, 130, 26, 34000),
            ("C-Class", "2.0L Turbo", 255, 295, "RWD", "9-speed auto", 5.5, 130, 25, 45000),
            ("E-Class", "3.0L Turbo", 362, 369, "AWD", "9-speed auto", 4.8, 130, 23, 60000),
            ("S-Class", "4.0L V8", 496, 516, "AWD", "9-speed auto", 4.1, 155, 20, 115000),
            ("GLC", "2.0L Turbo", 255, 273, "AWD", "9-speed auto", 5.9, 130, 22, 50000),
            ("GLE", "3.0L Turbo", 362, 369, "AWD", "9-speed auto", 5.3, 130, 20, 63000),
            ("GLS", "4.0L V8", 483, 516, "AWD", "9-speed auto", 4.9, 130, 18, 80000),
        ],
        "Audi": [
            ("A3", "2.0L Turbo", 184, 221, "FWD", "7-speed dual-clutch", 6.8, 130, 28, 35000),
            ("A4", "2.0L Turbo", 201, 236, "Quattro", "7-speed dual-clutch", 6.3, 130, 28, 40000),
            ("A6", "3.0L Turbo", 335, 369, "Quattro", "7-speed dual-clutch", 5.1, 130, 23, 57000),
            ("A8", "3.0L Turbo", 335, 369, "Quattro", "8-speed auto", 5.3, 130, 21, 87000),
            ("Q3", "2.0L Turbo", 184, 221, "Quattro", "7-speed dual-clutch", 7.2, 130, 24, 36000),
            ("Q5", "2.0L Turbo", 261, 273, "Quattro", "7-speed dual-clutch", 5.6, 135, 25, 45000),
            ("Q7", "3.0L Turbo", 335, 369, "Quattro", "8-speed auto", 5.5, 130, 20, 58000),
            ("R8", "5.2L V10", 562, 406, "Quattro", "7-speed dual-clutch", 3.2, 201, 14, 170000),
        ],
        "Porsche": [
            ("718 Boxster", "2.0L Turbo", 300, 280, "RWD", "6-speed manual", 4.5, 170, 22, 62000),
            ("911 Carrera", "3.0L Twin-Turbo", 379, 331, "RWD", "8-speed dual-clutch", 3.8, 182, 20, 115000),
            ("Cayenne", "3.0L Turbo", 335, 332, "AWD", "8-speed auto", 5.6, 155, 18, 70000),
            ("Macan", "2.9L Twin-Turbo", 375, 383, "AWD", "7-speed dual-clutch", 4.7, 155, 18, 60000),
            ("Panamera", "2.9L Twin-Turbo", 440, 405, "AWD", "8-speed dual-clutch", 4.0, 175, 20, 95000),
            ("Taycan", "Electric", 402, 254, "AWD", "2-speed auto", 3.8, 150, 79, 85000),
        ],
        "Tesla": [
            ("Model 3", "Electric", 283, 307, "RWD", "1-speed", 5.3, 140, 138, 45000),
            ("Model Y", "Electric", 384, 376, "AWD", "1-speed", 3.5, 155, 131, 55000),
            ("Model S", "Electric", 670, 687, "AWD", "1-speed", 2.3, 200, 120, 95000),
            ("Model X", "Electric", 670, 687, "AWD", "1-speed", 2.5, 163, 102, 110000),
            ("Cybertruck", "Electric", 600, 700, "AWD", "1-speed", 3.0, 130, 80, 70000),
        ],
        "Lamborghini": [
            ("Huracán", "5.2L V10", 602, 413, "AWD", "7-speed dual-clutch", 2.9, 202, 13, 250000),
            ("Aventador", "6.5L V12", 769, 531, "AWD", "7-speed ISR", 2.9, 217, 11, 500000),
            ("Urus", "4.0L Twin-Turbo V8", 641, 627, "AWD", "8-speed auto", 3.2, 190, 15, 230000),
            ("Countach", "6.5L V12", 769, 531, "AWD", "7-speed ISR", 2.9, 217, 11, 2500000),
        ],
        "Ferrari": [
            ("Roma", "3.9L Twin-Turbo V8", 612, 561, "RWD", "8-speed dual-clutch", 3.2, 199, 18, 250000),
            ("F8 Tributo", "3.9L Twin-Turbo V8", 710, 568, "RWD", "7-speed dual-clutch", 2.9, 211, 16, 300000),
            ("SF90 Stradale", "4.0L Twin-Turbo V8 + Hybrid", 986, 590, "AWD", "8-speed dual-clutch", 2.5, 211, 17, 600000),
            ("488 Pista", "3.9L Twin-Turbo V8", 711, 568, "RWD", "7-speed dual-clutch", 2.8, 211, 16, 350000),
        ],
        "Toyota": [
            ("Corolla", "1.8L I4", 139, 126, "FWD", "CVT", 8.5, 120, 35, 21000),
            ("Camry", "2.5L I4", 203, 184, "FWD", "8-speed auto", 7.2, 135, 32, 26000),
            ("Prius", "1.8L Hybrid", 121, 105, "FWD", "CVT", 9.8, 115, 56, 25000),
            ("RAV4", "2.5L I4", 203, 184, "AWD", "8-speed auto", 7.5, 125, 28, 28000),
            ("Highlander", "3.5L V6", 295, 263, "AWD", "8-speed auto", 6.5, 115, 23, 38000),
            ("Tacoma", "3.5L V6", 278, 265, "4WD", "6-speed manual", 7.0, 115, 18, 33000),
            ("Supra", "3.0L Turbo", 382, 368, "RWD", "8-speed auto", 3.9, 155, 22, 53000),
        ],
        "Dodge": [
            ("Charger", "5.7L V8", 370, 395, "RWD", "8-speed auto", 5.1, 155, 18, 35000),
            ("Challenger", "5.7L V8", 375, 410, "RWD", "6-speed manual", 5.0, 155, 18, 34000),
            ("Durango", "5.7L V8", 360, 390, "AWD", "8-speed auto", 6.2, 145, 19, 52000),
            ("Journey", "2.4L I4", 172, 165, "FWD", "4-speed auto", 9.0, 115, 21, 25000),
        ],
        "Jeep": [
            ("Wrangler", "3.6L V6", 285, 260, "4WD", "6-speed manual", 6.5, 115, 18, 33000),
            ("Grand Cherokee", "3.6L V6", 295, 260, "4WD", "8-speed auto", 7.0, 115, 20, 40000),
            ("Cherokee", "2.4L I4", 180, 170, "FWD", "9-speed auto", 8.5, 115, 24, 28000),
            ("Compass", "2.4L I4", 180, 175, "FWD", "6-speed auto", 8.5, 115, 24, 25000),
        ],
        "Subaru": [
            ("Impreza", "2.0L", 152, 145, "AWD", "CVT", 8.5, 120, 28, 20000),
            ("WRX", "2.4L Turbo", 271, 258, "AWD", "6-speed manual", 5.5, 155, 21, 31000),
            ("Outback", "2.5L", 182, 176, "AWD", "CVT", 8.5, 120, 26, 28000),
            ("Forester", "2.5L", 182, 176, "AWD", "CVT", 8.5, 115, 29, 27000),
            ("Ascent", "2.4L Turbo", 260, 277, "AWD", "CVT", 7.0, 115, 22, 34000),
        ],
        "Mazda": [
            ("MX-5 Miata", "2.0L", 181, 151, "RWD", "6-speed manual", 5.7, 135, 29, 28000),
            ("Mazda3", "2.5L", 186, 186, "FWD", "6-speed auto", 6.5, 130, 28, 24000),
            ("Mazda6", "2.5L Turbo", 250, 320, "FWD", "6-speed auto", 5.8, 130, 24, 30000),
            ("CX-5", "2.5L Turbo", 250, 320, "AWD", "6-speed auto", 6.2, 130, 24, 32000),
            ("CX-9", "2.5L Turbo", 250, 320, "AWD", "6-speed auto", 6.5, 130, 22, 38000),
        ],
        "Volkswagen": [
            ("Golf", "1.4L Turbo", 147, 184, "FWD", "6-speed manual", 7.3, 130, 30, 23000),
            ("Golf GTI", "2.0L Turbo", 241, 273, "FWD", "7-speed dual-clutch", 5.5, 155, 27, 31000),
            ("Jetta", "1.5L Turbo", 158, 184, "FWD", "8-speed auto", 7.5, 125, 32, 22000),
            ("Passat", "2.0L Turbo", 174, 206, "FWD", "6-speed auto", 7.5, 130, 26, 26000),
            ("Tiguan", "2.0L Turbo", 184, 221, "AWD", "8-speed auto", 8.0, 120, 24, 29000),
            ("Atlas", "3.6L V6", 276, 266, "AWD", "8-speed auto", 7.5, 115, 20, 35000),
        ],
        "Hyundai": [
            ("Elantra", "2.0L", 147, 132, "FWD", "CVT", 7.5, 125, 33, 20000),
            ("Elantra N", "2.0L Turbo", 276, 289, "FWD", "6-speed manual", 5.0, 155, 23, 34000),
            ("Sonata", "1.6L Turbo", 180, 195, "FWD", "8-speed auto", 7.2, 130, 32, 26000),
            ("Kona", "2.0L", 147, 132, "FWD", "CVT", 8.0, 120, 30, 22000),
            ("Santa Fe", "2.5L Turbo", 277, 311, "AWD", "8-speed dual-clutch", 6.2, 130, 22, 36000),
            ("Palisade", "3.8L V6", 291, 262, "AWD", "8-speed auto", 6.5, 115, 19, 35000),
        ],
        "Kia": [
            ("Forte", "2.0L", 147, 132, "FWD", "CVT", 7.5, 125, 33, 19000),
            ("K5", "1.6L Turbo", 180, 195, "FWD", "8-speed auto", 7.0, 130, 31, 25000),
            ("Stinger", "3.3L Twin-Turbo", 368, 376, "RWD", "8-speed auto", 4.6, 167, 20, 44000),
            ("Soul", "2.0L", 147, 132, "FWD", "CVT", 8.0, 120, 29, 19000),
            ("Sportage", "2.5L", 187, 178, "AWD", "8-speed auto", 7.5, 120, 25, 26000),
            ("Telluride", "3.8L V6", 291, 262, "AWD", "8-speed auto", 6.5, 120, 19, 42000),
        ],
    }

    colors = ["Red", "Blue", "Black", "White", "Silver", "Gray", "Green", "Yellow", "Orange", "Purple", "Brown", "Gold", "Cyan", "Magenta", "Lime", "Teal", "Maroon", "Navy"]
    drivetrains = ["FWD", "RWD", "AWD", "4WD"]
    transmissions = ["5-speed manual", "6-speed manual", "7-speed manual", "4-speed auto", "5-speed auto", "6-speed auto", "8-speed auto", "10-speed auto", "CVT", "7-speed dual-clutch", "8-speed dual-clutch"]
    ai_levels = ["Level 1 Assist", "Level 2 Autopilot", "Level 2+ Highway", "Level 3 Autonomy", "Level 1 Park Assist", "Level 2 Traffic Jam", "Level 2+ Nav Assist"]
    holographic_colors = ["Neon Red", "Electric Blue", "Neon Green", "Plasma Purple", "Inferno Orange", "Arctic White", "Cyber Yellow", "Quantum Pink", "Laser Violet", "Photon Cyan"]

    # Generate cars until we reach target_count
    while len(additional) < target_count:
        # Randomly pick a make and one of its models
        make = random.choice(list(makes_db.keys()))
        model_entry = random.choice(makes_db[make])
        model, engine_base, base_hp, base_torque, drv_base, trans_base, acc_base, top_speed_base, mpg_base, price_base = model_entry

        # Random year (1990-2025) to add variety
        year = random.randint(1990, 2025)

        # Slight variations in specs based on year and randomness
        hp = int(base_hp * (0.9 + 0.2 * random.random()))
        torque = int(base_torque * (0.9 + 0.2 * random.random()))
        acc = round(acc_base * (0.85 + 0.3 * random.random()), 1)
        top_speed = int(top_speed_base * (0.95 + 0.1 * random.random()))
        mpg = int(mpg_base * (0.9 + 0.2 * random.random()))
        price = int(price_base * (0.8 + 0.4 * random.random()))

        # Randomly pick other attributes
        color = random.choice(colors)
        drivetrain = random.choice(drivetrains)  # could also use drv_base but we'll randomize
        transmission = random.choice(transmissions)
        ai = random.choice(ai_levels)
        holo = random.choice(holographic_colors)

        # Create description
        description = f"The {year} {make} {model} is a {color.lower()} vehicle featuring a {engine_base} engine producing {hp} hp. It offers a blend of performance and comfort, typical of {make}."

        car = Car(make, model, year, color, engine_base, hp, torque, drivetrain, transmission,
                  acc, top_speed, mpg, price, ai, holo, description)
        additional.append(car)

    return additional

def create_car_list():
    """Create the full list of cars (special + generated)."""
    # Original hand-crafted cars (the special ones)
    cars = [
        Car("Dodge", "Charger", 2020, "Red",
            "6.2L Supercharged HEMI V8", 707, 650,
            "RWD", "8-speed automatic", 3.6, 196, 15, 72000,
            "Level 2 Autopilot", "Neon Red",
            "The Dodge Charger SRT Hellcat is a high-performance muscle car with aggressive styling and blistering speed. It combines modern technology with classic American muscle."),
        Car("Dodge", "Durango", 2022, "Black",
            "5.7L HEMI V8", 360, 390,
            "AWD", "8-speed automatic", 6.2, 145, 19, 52000,
            "Level 1 Driver Assist", "Shadow Black",
            "The Durango is a versatile SUV that offers three rows of seating and powerful engine options. It blends utility with Dodge's signature performance attitude."),
        Car("Toyota", "Camry", 2021, "Silver",
            "2.5L 4-Cylinder", 203, 184,
            "FWD", "8-speed automatic", 7.2, 135, 32, 26000,
            "Level 2 Safety Sense", "Arctic Silver",
            "The Toyota Camry is a reliable and fuel-efficient midsize sedan known for its comfort, safety features, and long-lasting quality. It's one of the best-selling cars in America."),
        Car("Toyota", "Corolla", 2023, "White",
            "1.8L 4-Cylinder", 139, 126,
            "FWD", "CVT", 8.5, 120, 35, 21000,
            "Level 1 Safety", "Pearl White",
            "The Corolla is a compact car that delivers excellent fuel economy and a reputation for durability. It's practical, affordable, and comes with Toyota Safety Sense."),
        Car("BMW", "3 Series", 2022, "Blue",
            "2.0L TwinPower Turbo Inline-4", 255, 294,
            "RWD", "8-speed automatic", 5.4, 155, 30, 43000,
            "Level 3 Highway Autopilot", "Electric Blue",
            "The BMW 3 Series is the benchmark for luxury sport sedans. It offers precise handling, a refined interior, and advanced technology, all while being fun to drive."),
        Car("BMW", "X5", 2021, "Gray",
            "3.0L BMW TwinPower Turbo Inline-6", 335, 330,
            "AWD", "8-speed automatic", 5.3, 155, 24, 61000,
            "Level 3 Autonomy", "Titanium Gray",
            "The X5 is a midsize luxury SUV that combines on-road comfort with off-road capability. It features a plush cabin, powerful engines, and the latest iDrive system."),
        Car("Audi", "A4", 2023, "Black",
            "2.0L TFSI 4-Cylinder", 201, 236,
            "Quattro AWD", "7-speed S tronic", 6.3, 130, 28, 40000,
            "Level 2 Adaptive Cruise", "Mythos Black",
            "The Audi A4 is a sophisticated compact executive sedan. It offers a quiet, high-tech interior, Quattro all-wheel drive, and a balance of performance and efficiency."),
        Car("Audi", "Q5", 2022, "White",
            "2.0L TFSI 4-Cylinder with mild hybrid", 261, 273,
            "Quattro AWD", "7-speed S tronic", 5.6, 135, 25, 45000,
            "Level 2+ Autonomy", "Glacier White",
            "The Q5 is a popular luxury SUV that excels in comfort and technology. It provides a smooth ride, upscale interior, and available plug-in hybrid variant."),
        Car("Lamborghini", "Aventador", 2021, "Yellow",
            "6.5L V12", 769, 531,
            "AWD", "7-speed ISR", 2.9, 217, 11, 500000,
            "Level 1 Track Assist", "Giallo Orion",
            "The Aventador is Lamborghini's flagship V12 supercar. With its sharp design, scissor doors, and exhilarating performance, it represents the pinnacle of Italian exotic engineering."),
        Car("Lamborghini", "Urus", 2023, "Orange",
            "4.0L Twin-Turbo V8", 641, 627,
            "AWD", "8-speed automatic", 3.2, 190, 15, 230000,
            "Level 2 Terrain Assist", "Arancio Borealis",
            "The Urus is the world's first Super Sport Utility Vehicle. It combines the soul of a supercar with the practicality of an SUV, offering breathtaking performance and luxury."),
        Car("BMW", "M3 Competition", 2023, "Brooklyn Grey",
            "3.0L Twin-Turbo Inline-6", 503, 479,
            "RWD", "8-speed automatic", 3.8, 155, 19, 76000,
            "Level 2 Driving Assistant", "Neon Grey",
            "The BMW M3 Competition is a high-performance sports sedan that combines track-focused capability with everyday usability. Its powerful engine, precise handling, and aggressive styling make it a standout in its class."),
        Car("Tesla", "Model X Plaid", 2023, "Midnight Silver",
            "Tri-Motor All-Wheel Drive", 1020, 1050,
            "AWD", "Single-speed automatic", 2.5, 163, 102, 110000,
            "Full Self-Driving (Level 2+)", "Electric Blue",
            "The Tesla Model X Plaid is an all-electric luxury SUV with breathtaking performance and cutting-edge technology. Its falcon-wing doors, spacious interior, and industry-leading range make it a futuristic family hauler."),
        Car("Dodge", "Challenger SRT Demon 170", 2023, "Plum Crazy Purple",
            "6.2L Supercharged HEMI V8 (E85)", 1025, 945,
            "RWD", "8-speed automatic", 1.66, 140, 13, 100000,
            "Level 1 Drag Assist", "Inferno Red",
            "The Dodge Challenger SRT Demon 170 is the ultimate factory drag car, designed to dominate the quarter mile. With up to 1,025 horsepower on E85, it features a trans brake, drag radial tires, and a host of performance upgrades, making it the most powerful muscle car ever produced."),
    ]

    # Generate and add 10000+ additional cars
    additional_cars = generate_additional_cars(10000)
    cars.extend(additional_cars)
    return cars

def save_cars_to_json(filename="car_database.json"):
    """Generate the full car list and save it to a JSON file."""
    print("Generating car database (this may take a few seconds)...")
    cars = create_car_list()
    data = [car.to_dict() for car in cars]
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Saved {len(cars)} cars to {filename}")
    return cars

def load_cars_from_json(filename="car_database.json"):
    """Load car list from a JSON file."""
    if not os.path.exists(filename):
        print(f"{filename} not found. Generating a new database...")
        return save_cars_to_json(filename)
    with open(filename, "r") as f:
        data = json.load(f)
    cars = [Car.from_dict(item) for item in data]
    print(f"Loaded {len(cars)} cars from {filename}")
    return cars

class NeonCarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("NEON CAR DATABASE 3000")
        self.root.geometry("1200x750")
        self.root.configure(bg="#0a0f0f")

        # Futuristic fonts
        self.title_font = tkfont.Font(family="Courier New", size=22, weight="bold")
        self.header_font = tkfont.Font(family="Courier New", size=14, weight="bold")
        self.label_font = tkfont.Font(family="Consolas", size=11)
        self.value_font = tkfont.Font(family="Consolas", size=11, weight="normal")

        # Neon color palette
        self.bg_dark = "#0a0f0f"
        self.neon_green = "#00ff9d"
        self.neon_pink = "#ff00c1"
        self.neon_cyan = "#00f3ff"
        self.neon_yellow = "#f0e68c"
        self.text_light = "#e0e0e0"
        self.panel_bg = "#1a1f1f"
        self.entry_bg = "#252b2b"

        # Load car data from JSON
        self.cars = load_cars_from_json()

        # Build UI
        self.create_header()
        self.create_main_panels()
        self.create_status_bar()
        self.populate_listbox()

        # Start pulsing animation
        self.pulse_header()

    # ... (rest of the UI methods remain exactly the same as before) ...
    def create_header(self):
        header_frame = tk.Frame(self.root, bg=self.bg_dark, height=90)
        header_frame.pack(fill=tk.X, side=tk.TOP)
        header_frame.pack_propagate(False)

        shadow_label = tk.Label(
            header_frame,
            text="⚡ NEON CAR DATABASE 3000 ⚡",
            font=self.title_font,
            bg=self.bg_dark,
            fg="#222222"
        )
        shadow_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER, x=3, y=3)

        self.title_label = tk.Label(
            header_frame,
            text="⚡ NEON CAR DATABASE 3000 ⚡",
            font=self.title_font,
            bg=self.bg_dark,
            fg=self.neon_green
        )
        self.title_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        canvas = tk.Canvas(header_frame, bg=self.bg_dark, height=4, highlightthickness=0)
        canvas.pack(fill=tk.X, side=tk.BOTTOM)
        canvas.create_line(0, 2, 1200, 2, fill=self.neon_cyan, width=4)

    def create_main_panels(self):
        main_container = tk.Frame(self.root, bg=self.bg_dark)
        main_container.pack(fill=tk.BOTH, expand=True, padx=15, pady=10)

        # Left panel (car list)
        left_panel = tk.Frame(main_container, bg=self.panel_bg, width=350)
        left_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=False, padx=(0,15))
        left_panel.pack_propagate(False)
        left_panel.config(highlightbackground=self.neon_green, highlightcolor=self.neon_green,
                          highlightthickness=2, bd=0)

        list_title = tk.Label(
            left_panel,
            text="[ CAR ARCHIVE ]",
            font=self.header_font,
            bg=self.panel_bg,
            fg=self.neon_green
        )
        list_title.pack(anchor=tk.W, pady=(10,5), padx=10)

        scrollbar = tk.Scrollbar(left_panel, bg=self.panel_bg, troughcolor=self.entry_bg,
                                 activebackground=self.neon_green, elementborderwidth=0)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y, padx=(0,5), pady=10)

        self.listbox = tk.Listbox(
            left_panel,
            yscrollcommand=scrollbar.set,
            font=self.label_font,
            bg=self.entry_bg,
            fg=self.neon_cyan,
            selectbackground=self.neon_green,
            selectforeground=self.bg_dark,
            bd=0,
            highlightthickness=0,
            relief=tk.FLAT
        )
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(10,0), pady=10)
        scrollbar.config(command=self.listbox.yview)
        self.listbox.bind('<<ListboxSelect>>', self.on_select)

        # Right panel (details)
        right_panel = tk.Frame(main_container, bg=self.panel_bg)
        right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        right_panel.config(highlightbackground=self.neon_pink, highlightcolor=self.neon_pink,
                           highlightthickness=2, bd=0)

        details_title = tk.Label(
            right_panel,
            text="[ VEHICLE SPECIFICATIONS ]",
            font=self.header_font,
            bg=self.panel_bg,
            fg=self.neon_pink
        )
        details_title.pack(anchor=tk.W, pady=(10,5), padx=15)

        # Scrollable canvas for details
        canvas_frame = tk.Frame(right_panel, bg=self.panel_bg)
        canvas_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=(0,10))

        self.canvas = tk.Canvas(canvas_frame, bg=self.panel_bg, highlightthickness=0)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        v_scrollbar = tk.Scrollbar(canvas_frame, orient=tk.VERTICAL, command=self.canvas.yview,
                                   bg=self.panel_bg, troughcolor=self.entry_bg,
                                   activebackground=self.neon_pink, elementborderwidth=0)
        v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvas.configure(yscrollcommand=v_scrollbar.set)

        self.details_frame = tk.Frame(self.canvas, bg=self.panel_bg)
        self.canvas.create_window((0, 0), window=self.details_frame, anchor=tk.NW)

        self.details_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        self.create_details_widgets()

    def create_details_widgets(self):
        self.detail_widgets = {}

        attributes = [
            ("MAKE", "make", "", self.neon_cyan),
            ("MODEL", "model", "", self.neon_cyan),
            ("YEAR", "year", "", self.neon_cyan),
            ("COLOR", "color", "", self.neon_cyan),
            ("ENGINE", "engine", "", self.neon_cyan),
            ("HORSEPOWER", "horsepower", " hp", self.neon_cyan),
            ("TORQUE", "torque", " lb-ft", self.neon_cyan),
            ("DRIVETRAIN", "drivetrain", "", self.neon_cyan),
            ("TRANSMISSION", "transmission", "", self.neon_cyan),
            ("0-60 MPH", "acceleration", " sec", self.neon_cyan),
            ("TOP SPEED", "top_speed", " mph", self.neon_cyan),
            ("FUEL ECONOMY", "fuel_economy", " mpg", self.neon_cyan),
            ("BASE PRICE", "price", " USD", self.neon_cyan),
            ("AI LEVEL", "ai_level", "", self.neon_pink),
            ("HOLO COLOR", "holographic_color", "", self.neon_pink),
        ]

        row = 0
        for label_text, attr, unit, color in attributes:
            lbl = tk.Label(
                self.details_frame,
                text=label_text,
                font=self.label_font,
                bg=self.panel_bg,
                fg=color,
                anchor=tk.W
            )
            lbl.grid(row=row, column=0, sticky=tk.W, pady=3, padx=(0,10))

            val = tk.Label(
                self.details_frame,
                text="",
                font=self.value_font,
                bg=self.panel_bg,
                fg=self.text_light,
                anchor=tk.W,
                wraplength=400,
                justify=tk.LEFT
            )
            val.grid(row=row, column=1, sticky=tk.W, pady=3)
            self.detail_widgets[attr] = (val, unit)
            row += 1

        # Description field
        desc_label = tk.Label(
            self.details_frame,
            text="DESCRIPTION",
            font=self.header_font,
            bg=self.panel_bg,
            fg=self.neon_yellow,
            anchor=tk.W
        )
        desc_label.grid(row=row, column=0, columnspan=2, sticky=tk.W, pady=(15,5))

        desc_frame = tk.Frame(self.details_frame, bg=self.panel_bg)
        desc_frame.grid(row=row+1, column=0, columnspan=2, sticky=tk.W+tk.E, pady=(0,15))

        self.description_text = tk.Text(
            desc_frame,
            height=6,
            wrap=tk.WORD,
            font=self.value_font,
            bg=self.entry_bg,
            fg=self.text_light,
            bd=0,
            highlightthickness=1,
            highlightbackground=self.neon_yellow,
            highlightcolor=self.neon_yellow,
            relief=tk.FLAT
        )
        self.description_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        desc_scroll = tk.Scrollbar(desc_frame, orient=tk.VERTICAL, command=self.description_text.yview,
                                   bg=self.panel_bg, troughcolor=self.entry_bg,
                                   activebackground=self.neon_yellow, elementborderwidth=0)
        desc_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.description_text.config(yscrollcommand=desc_scroll.set)
        self.description_text.config(state=tk.DISABLED)

        self.details_frame.columnconfigure(1, weight=1)

    def create_status_bar(self):
        status_frame = tk.Frame(self.root, bg=self.bg_dark, height=30)
        status_frame.pack(fill=tk.X, side=tk.BOTTOM)
        status_frame.pack_propagate(False)

        self.status_label = tk.Label(
            status_frame,
            text="",
            font=("Consolas", 9),
            bg=self.bg_dark,
            fg=self.neon_green
        )
        self.status_label.pack(side=tk.LEFT, padx=10)

        self.update_status()

    def update_status(self):
        current_time = time.strftime("%H:%M:%S")
        car_count = len(self.cars)
        self.status_label.config(
            text=f"[ SYSTEM ONLINE ]   ⚡   {car_count} VEHICLES IN DATABASE   ⚡   {current_time}"
        )
        self.root.after(1000, self.update_status)

    def pulse_header(self):
        colors = [self.neon_green, self.neon_cyan, self.neon_pink, self.neon_yellow]
        current_fg = self.title_label.cget("fg")
        try:
            idx = colors.index(current_fg)
            next_color = colors[(idx + 1) % len(colors)]
        except ValueError:
            next_color = colors[0]
        self.title_label.config(fg=next_color)
        self.root.after(500, self.pulse_header)

    def populate_listbox(self):
        for car in self.cars:
            self.listbox.insert(tk.END, car.display_name())

    def on_select(self, event):
        selection = self.listbox.curselection()
        if not selection:
            return
        index = selection[0]
        car = self.cars[index]

        self.detail_widgets["make"][0].config(text=car.make)
        self.detail_widgets["model"][0].config(text=car.model)
        self.detail_widgets["year"][0].config(text=str(car.year))
        self.detail_widgets["color"][0].config(text=car.color)
        self.detail_widgets["engine"][0].config(text=car.engine)
        self.detail_widgets["horsepower"][0].config(text=f"{car.horsepower}{self.detail_widgets['horsepower'][1]}")
        self.detail_widgets["torque"][0].config(text=f"{car.torque}{self.detail_widgets['torque'][1]}")
        self.detail_widgets["drivetrain"][0].config(text=car.drivetrain)
        self.detail_widgets["transmission"][0].config(text=car.transmission)
        self.detail_widgets["acceleration"][0].config(text=f"{car.acceleration}{self.detail_widgets['acceleration'][1]}")
        self.detail_widgets["top_speed"][0].config(text=f"{car.top_speed}{self.detail_widgets['top_speed'][1]}")
        self.detail_widgets["fuel_economy"][0].config(text=f"{car.fuel_economy}{self.detail_widgets['fuel_economy'][1]}")
        self.detail_widgets["price"][0].config(text=f"${car.price:,}{self.detail_widgets['price'][1]}")
        self.detail_widgets["ai_level"][0].config(text=car.ai_level)
        self.detail_widgets["holographic_color"][0].config(text=car.holographic_color)

        self.description_text.config(state=tk.NORMAL)
        self.description_text.delete(1.0, tk.END)
        self.description_text.insert(tk.END, car.description)
        self.description_text.config(state=tk.DISABLED)

def main():
    root = tk.Tk()
    app = NeonCarApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()