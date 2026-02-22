import tkinter as tk
from tkinter import font as tkfont, ttk, messagebox
import time
import random
import json
import os
import threading
from datetime import datetime

class Car:
    """Represents a car with extensive details."""
    def __init__(self, make, model, year, color, engine, horsepower, torque,
                 drivetrain, transmission, acceleration, top_speed, fuel_economy, price,
                 ai_level, holographic_color, description, country="", category="", 
                 body_style="", weight=0, length=0, width=0, height=0, wheelbase=0,
                 fuel_type="Gasoline", seats=4, doors=4, msrp=0, image_url=""):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.engine = engine
        self.horsepower = horsepower
        self.torque = torque
        self.drivetrain = drivetrain
        self.transmission = transmission
        self.acceleration = acceleration
        self.top_speed = top_speed
        self.fuel_economy = fuel_economy
        self.price = price
        self.ai_level = ai_level
        self.holographic_color = holographic_color
        self.description = description
        self.country = country
        self.category = category
        self.body_style = body_style
        self.weight = weight
        self.length = length
        self.width = width
        self.height = height
        self.wheelbase = wheelbase
        self.fuel_type = fuel_type
        self.seats = seats
        self.doors = doors
        self.msrp = msrp if msrp > 0 else price
        self.image_url = image_url

    def display_name(self):
        return f"{self.year} {self.make} {self.model}"

    def to_dict(self):
        return {
            "make": self.make, "model": self.model, "year": self.year, "color": self.color,
            "engine": self.engine, "horsepower": self.horsepower, "torque": self.torque,
            "drivetrain": self.drivetrain, "transmission": self.transmission,
            "acceleration": self.acceleration, "top_speed": self.top_speed,
            "fuel_economy": self.fuel_economy, "price": self.price,
            "ai_level": self.ai_level, "holographic_color": self.holographic_color,
            "description": self.description, "country": self.country, "category": self.category,
            "body_style": self.body_style, "weight": self.weight, "length": self.length,
            "width": self.width, "height": self.height, "wheelbase": self.wheelbase,
            "fuel_type": self.fuel_type, "seats": self.seats, "doors": self.doors,
            "msrp": self.msrp, "image_url": self.image_url
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["make"], data["model"], data["year"], data["color"],
            data["engine"], data["horsepower"], data["torque"],
            data["drivetrain"], data["transmission"], data["acceleration"],
            data["top_speed"], data["fuel_economy"], data["price"],
            data["ai_level"], data["holographic_color"], data["description"],
            data.get("country", ""), data.get("category", ""), data.get("body_style", ""),
            data.get("weight", 0), data.get("length", 0), data.get("width", 0),
            data.get("height", 0), data.get("wheelbase", 0), data.get("fuel_type", "Gasoline"),
            data.get("seats", 4), data.get("doors", 4), data.get("msrp", data["price"]),
            data.get("image_url", "")
        )

def generate_massive_database(target_count=100000):
    """Generate a massive database of cars from around the world."""
    cars = []
    
    # Complete list of car manufacturers by country
    manufacturers = {
        "USA": [
            "Ford", "Chevrolet", "Dodge", "Jeep", "Ram", "GMC", "Cadillac", "Lincoln", "Buick",
            "Chrysler", "Tesla", "Rivian", "Lucid", "Fisker", "Plymouth", "Oldsmobile", "Pontiac",
            "Saturn", "Mercury", "Hummer", "Saleen", "Hennessey", "Vector", "Rezvani", "Scuderia",
            "Czinger", "Drako", "Karma", "Mullen", "Lordstown", "Nikola", "Corbin", "Commuter",
            "Detroit Electric", "Equus", "Falcon", "Foose", "Local Motors", "Mazzanti", "Mosler",
            "Panoz", "Phoenix", "Pierce-Arrow", "Rayo", "ReV", "SSC", "Superformance", "Vanderhall"
        ],
        "Japan": [
            "Toyota", "Honda", "Nissan", "Mazda", "Subaru", "Mitsubishi", "Suzuki", "Daihatsu",
            "Isuzu", "Lexus", "Acura", "Infiniti", "Scion", "Datsun", "Hino", "Mitsubishi Fuso",
            "Nissan Diesel", "Prince", "Eunos", "Autozam", "Amuse", "Autech", "Blitz", "Boundary",
            "Carbing", "Cusco", "Do-Luck", "Greddy", "HKS", "JUN", "Kei", "Mine's", "Nismo",
            "RE Amemiya", "Signal", "Spoon", "Subaru Tecnica", "Toda", "Tommykaira", "Top Secret",
            "TRD", "Veilside", "Vertex", "Zero Sports", "ASL", "Dome", "Mooncraft", "Sard"
        ],
        "Germany": [
            "BMW", "Mercedes-Benz", "Audi", "Porsche", "Volkswagen", "Opel", "Alpina", "Maybach",
            "Smart", "Borgward", "Gumpert", "Wiesmann", "Apollo", "Artega", "Audi Sport", "Bitter",
            "Dartz", "EDAG", "Gemballa", "Hamann", "Isdera", "Koenig", "Lotec", "Mansory",
            "Melkus", "Mercedes-AMG", "Mercedes-Maybach", "MTM", "NSU", "RAUH-Welt", "Renntech",
            "Ruf", "Startech", "TechArt", "Wald", "9ff", "ABT", "AC Schnitzer", "B&B", "Carlsson",
            "DMC", "Geigercars", "G-Power", "Irmscher", "Kleemann", "Lumma", "Novitec", "Prior Design"
        ],
        "Italy": [
            "Ferrari", "Lamborghini", "Maserati", "Alfa Romeo", "Fiat", "Lancia", "Pagani",
            "Abarth", "Autobianchi", "Bertone", "Bugatti", "Cizeta", "De Tomaso", "DR Motor",
            "Fornasari", "Giannini", "Innocenti", "Iso", "Italdesign", "Mazzanti", "Moretti",
            "OSI", "Pininfarina", "Qvale", "Siata", "Stola", "Tatasci", "Zagato", "Zenos",
            "ATS", "B Engineering", "Bandini", "Bellier", "Bizzarrini", "Casilini", "Coggiola",
            "Covini", "Dallara", "Fioravanti", "Fissore", "Ghia", "Giotti", "Iveco", "Maggiora",
            "Maserati", "Mole", "Monica", "OSCA", "Palmen", "Picchio", "Rayton Fissore"
        ],
        "UK": [
            "Aston Martin", "Bentley", "Rolls-Royce", "Jaguar", "Land Rover", "Mini", "McLaren",
            "Lotus", "MG", "Morgan", "Caterham", "Noble", "Ariel", "BAC", "Ginetta", "TVR",
            "Austin", "Austin-Healey", "Morris", "Rover", "Triumph", "AC", "Allard", "Alvis",
            "Armstrong Siddeley", "Bristol", "Daimler", "David Brown", "Eagle", "Faraday",
            "Gilbern", "Gordon", "Grinnall", "Healey", "Humber", "Invicta", "Jensen", "Lagonda",
            "Lanchester", "Lea-Francis", "Lister", "Marcos", "Marlin", "Metrocab", "Mini",
            "Modec", "Onyx", "Radical", "Reliant", "Riley", "Rochdale", "Rolls-Royce", "Rover",
            "Singer", "Squire", "Standard", "Sunbeam", "Swallow", "Talbot", "Ultima", "Vauxhall",
            "Vulcan", "Wolseley", "Westfield", "Wiesmann", "Wildwind", "Wrightspeed", "X-ITE",
            "Yamaha", "Yulon", "Zenos", "Zenvo", "Zeta", "Zotye", "Zoyte"
        ],
        "France": [
            "Citroën", "Peugeot", "Renault", "Bugatti", "Alpine", "DS", "Venturi", "Aixam",
            "Bellier", "Chatenet", "Ligier", "Microcar", "Mega", "Secma", "PGO", "MVS",
            "Berliet", "Chenard-Walcker", "Delage", "Delahaye", "Facel Vega", "Hotchkiss",
            "Panhard", "Salmson", "Simca", "Talbot", "Matra", "Renault Sport", "Gordini",
            "Amilcar", "Ballot", "Barré", "Bignan", "Brasier", "Buchet", "Caban", "Charron",
            "Cottin-Desgouttes", "Delaunay-Belleville", "De Dion-Bouton", "Dewald", "Dragon",
            "Dufaux", "Farman", "Floirat", "Gauthier", "Gladiator", "Gobron-Brillié", "Grégoire",
            "Guédon", "Hélicar", "Hurtu", "Jou", "Kaiser", "Krieger", "La Buire", "La Licorne",
            "Lafitte", "Latil", "Lavergne", "Lecoy", "Le Zèbre", "Lorraine", "Luc Court"
        ],
        "Sweden": [
            "Volvo", "Saab", "Koenigsegg", "NEVS", "Uniti", "Clean Motion", "Ljungström",
            "Scania", "Tranemo", "Caresto", "Corbin", "Elbil", "Elcat", "Elmar", "Fuldamobil",
            "Gina", "Gröngöling", "Hägglund", "Kalmar", "Koeningsegg", "Lejon", "Lynx", "Obbola",
            "Pagano", "Polar", "Reva", "Saab", "Scania-Vabis", "Skania", "Småbil", "Stala",
            "Stjärnblom", "Ströms", "Svenska", "Thulin", "Tjorven", "Tranås", "Unoson", "Vabis",
            "Volvo", "Åtvidaberg", "Ösa", "Östberg", "Östlund", "Överum"
        ],
        "South Korea": [
            "Hyundai", "Kia", "Genesis", "SsangYong", "Daewoo", "Samsung", "GM Korea",
            "Asia Motors", "Daelim", "Daewoo Bus", "Daewoo Truck", "Hyundai Truck", "Kia Truck",
            "Masan", "Oullim", "Proto", "Renault Samsung", "Sangyong", "Seang", "Shinjin",
            "SsangYong", "S-Tec", "Taekwang", "Tata Daewoo", "Zyle Daewoo", "CT&T", "Duzon",
            "Eugene", "Fedora", "Fiat Korea", "Giga", "GM Korea", "Haebang", "Hanbul",
            "Hanil", "Hankuk", "Hanyang", "Hwasung", "Hyosung", "Hyundai", "Incheon",
            "Jeil", "Keohwa", "Kia", "Korea", "Korando", "Koryo", "Kwangju", "Kyungnam"
        ],
        "China": [
            "BYD", "Geely", "Great Wall", "Chery", "SAIC", "FAW", "Dongfeng", "Changan",
            "BAIC", "GAC", "Brilliance", "Lifan", "Zotye", "Haval", "Wei", "Lynk & Co",
            "Polestar", "NIO", "XPeng", "Li Auto", "WM Motor", "Hozon", "Human Horizons",
            "Aiways", "Qiantu", "Singulato", "ENOVATE", "Borgward", "Weltmeister", "Roewe",
            "MG", "Maxus", "Foton", "JAC", "JMC", "Haima", "Huanghai", "Landwind", "Changhe",
            "Soueast", "Yudo", "Skywell", "LEVC", "Faraday Future", "Byton", "Rivian", "Lucid"
        ],
        "India": [
            "Tata", "Mahindra", "Maruti Suzuki", "Hindustan", "Premier", "Force Motors",
            "Bajaj", "Ashok Leyland", "Eicher", "ICML", "Reva", "Mahindra Electric",
            "Tata Motors", "Mahindra & Mahindra", "Maruti", "Hindustan Motors", "Premier Automobiles",
            "Standard", "San", "Sipani", "Tata", "Mahindra", "Force", "Bajaj", "Ashok",
            "Eicher", "ICML", "Reva", "Mahindra Electric", "Tata Motors", "Mahindra & Mahindra"
        ],
        "Russia": [
            "Lada", "GAZ", "UAZ", "KAMAZ", "Marussia", "ZiL", "Moskvich", "Russo-Balt",
            "TagAZ", "Derways", "Vortex", "Yarovit", "Avtotor", "GAZ", "UAZ", "KAMAZ",
            "Marussia", "ZiL", "Moskvich", "Russo-Balt", "TagAZ", "Derways", "Vortex", "Yarovit"
        ],
        "Czech Republic": [
            "Škoda", "Tatra", "Kaipan", "MTX", "Praga", "Velorex", "Wikov", "Aero",
            "Avia", "JAWA", "Laurin & Klement", "Walter", "Zbrojovka", "Zetor", "Tatra"
        ],
        "Australia": [
            "Holden", "Ford Australia", "Toyota Australia", "HSV", "FPV", "Brabham",
            "Bolwell", "Buchanan", "Chrysler Australia", "Daytona", "Devaux", "Elfin",
            "Goggomobil", "Golf", "HRT", "Joss", "LDV", "Leyland", "Lightburn", "Mitsuoka",
            "Morris", "Nissan Australia", "Nota", "Okapi", "Pioneer", "Rover Australia",
            "Saker", "Shannons", "Skelta", "Toyota Australia", "Volvo Australia", "Zeta"
        ],
        "Brazil": [
            "Fiat Brazil", "Volkswagen Brazil", "Chevrolet Brazil", "Ford Brazil",
            "Toyota Brazil", "Honda Brazil", "Renault Brazil", "Peugeot Brazil",
            "Citroën Brazil", "Nissan Brazil", "Mitsubishi Brazil", "Hyundai Brazil",
            "Kia Brazil", "Audi Brazil", "BMW Brazil", "Mercedes-Benz Brazil", "Agrale",
            "Chamonix", "Dacon", "FNM", "Gurgel", "Lobini", "Miura", "Puma", "Santa Matilde",
            "TAC", "Troller", "Volkswagen Caminhões", "Volkswagen Trucks", "Willys"
        ],
        "Mexico": [
            "Mastretta", "DINA", "Solana", "Autobuses", "Carrocerías", "Diesel Nacional",
            "FAMSA", "Grupo Industrial Ramirez", "Intermex", "Mack Mexico", "Mase", "Mercury",
            "Mexicana", "Navistar", "Omnibus", "Rassini", "Scania Mexico", "Trailers de Monterrey",
            "VAM", "Vehiculos Automotores", "Volvo Mexico", "VUHL", "Zeta", "Zacua"
        ],
        "Spain": [
            "SEAT", "Cupra", "Hispano-Suiza", "Pegaso", "Bultaco", "Derbi", "Gas Gas",
            "Montesa", "Ossa", "Rieju", "Sherco", "Avia", "Barreiros", "Borgward", "David",
            "Ebro", "FADISA", "Fasa-Renault", "Fenix", "Fiat Spain", "Ford Spain", "Guerra",
            "Hispano", "IMOSA", "Irizar", "J. Mezquita", "Lube", "MotoTrans", "Nissan Spain",
            "Opel Spain", "Peugeot Spain", "Renault Spain", "Santana", "SEAT", "Suzuki Spain",
            "Tauro", "Tramontana", "Uro", "Vespa Spain", "Volkswagen Spain"
        ],
        "Netherlands": [
            "Spyker", "Donkervoort", "DAF", "VDL", "Burton", "Carver", "Dutch", "E-Phantom",
            "GINAF", "Greve", "Karmann", "Lomax", "Netam", "Nexport", "Rova", "Simus",
            "Terberg", "Venzo", "Waaijenberg", "Xenon", "Zwaans", "Aachen", "Adriaan",
            "Akermans", "Altena", "Amsterdam", "Anas", "Andries", "Antwerp", "Arnhem",
            "Astra", "Atag", "Auto-Union", "Autobedrijf", "Autobus", "Automobiel", "Avant"
        ],
        "Belgium": [
            "Minerva", "Imperia", "Apal", "Belcar", "Chamonix", "D'Ieteren", "Dekeyzer",
            "Demeyere", "Den", "Edran", "Eurecar", "Exagon", "FEV", "Gillet", "Ginaf",
            "Henschel", "Herstal", "IBC", "Jonckheere", "Kempisch", "Lagrange", "Lambert",
            "Laurys", "Lion", "Meeussen", "Mol", "Monteverdi", "Nagant", "Oree", "Pipe",
            "Quartz", "Rally", "Royal", "SAD", "SAGA", "Seneffe", "Sibille", "Spiders",
            "Star", "Superia", "Tassigny", "Thiery", "Uplace", "Van Hool", "Verhaeghe"
        ],
        "Austria": [
            "KTM", "Steyr", "Denzel", "Felber", "Gräf", "Hofmann", "Horex", "Libelle",
            "Magna", "Mustang", "ÖAF", "Puch", "Rosenbauer", "Schuster", "SGP", "VÖEST",
            "Waffen", "Wiesmann", "X-BOW", "Austria", "Austro", "Binder", "Böhler",
            "Buchner", "Daimler", "Detroit", "Diamond", "Dornier", "Egger", "Fahrzeugbau",
            "Felber", "Fischer", "Fleetwood", "Ford Austria", "Fruehauf", "Gebrüder"
        ],
        "Switzerland": [
            "Monteverdi", "Rinspeed", "Ajlani", "Bucher", "Caruna", "Enzmann", "FBB",
            "Fedro", "Fischer", "Franco", "Fuldamobil", "Gaggenau", "Gewerbeschule",
            "Glas", "Goliath", "Grenus", "Grob", "Gygax", "Hako", "Henseler", "Hercules",
            "Hess", "Hispano-Suiza", "Horlacher", "Huber", "Hug", "Humber", "Hunziker",
            "Hürlimann", "Iame", "Jago", "Jelmoli", "Jensen", "Jowett", "Kaelin",
            "Kaiser", "Kalmar", "Kamil", "Karrer", "Kast", "Keller", "Kern", "Kistler"
        ],
        "Poland": [
            "FSO", "Polski Fiat", "FSM", "Fabryka Samochodów", "Honker", "Leopard",
            "Lublin", "Nysa", "Polonez", "Syrena", "Tarpan", "Warszawa", "Żuk",
            "Arrinera", "Autosan", "CWS", "DZT", "FSC", "FSD", "FSO", "FSR", "Jelcz",
            "Kapena", "Krakow", "Lublin", "Man", "Mikrus", "Niewiadów", "Pilsner",
            "Polauto", "Polfa", "Polmot", "Polski Fiat", "Polster", "PZInż", "Romet",
            "Sam", "San", "SFS", "Solbus", "Star", "Steyr", "Syrena", "Tarpol", "Warszawa"
        ],
        "Turkey": [
            "Anadol", "Askam", "BMC", "Bozankaya", "Caner", "Cumhuriyet", "Dere", "Devrim",
            "Diardi", "Dikey", "Dogan", "Doktas", "Efor", "Eker", "Ekiz", "Emlak",
            "Eral", "Erkunt", "Eser", "Eto", "Evet", "Fadil", "Fanos", "Femsan",
            "Fiat Turkey", "Fiber", "Ford Turkey", "Gazi", "Genderma", "Gonul", "Gözde",
            "Gürel", "Gürkan", "Hacı", "Hanoi", "Hasan", "Hattat", "Hayat", "Hidro",
            "Honda Turkey", "Hyundai Turkey", "Ikbal", "Ilgaz", "Ilke", "Ipek", "Isuzu Turkey",
            "Iveco Turkey", "Izci", "Izmir", "Izmit", "Jaguar Turkey", "Kamil", "Kardemir"
        ],
        "Romania": [
            "Dacia", "Aro", "Oltcit", "Oltena", "Auto Maxi", "Autoturism", "BAC",
            "Brasovia", "Cema", "Centro", "CIA", "Cobra", "Cris", "Cromos", "Dac",
            "Dacia", "Daewoo Romania", "Delta", "Detroit", "Diesel", "Ducati", "Duster",
            "E-Auto", "Ecomobil", "Econ", "Electrica", "Electro", "Elektro", "Elmar",
            "Emis", "Euro", "Exim", "Expo", "Faur", "Fero", "Fiat Romania", "FMC",
            "Ford Romania", "Foton", "FPS", "Frumos", "Gama", "Garant", "Gaz", "Giurgiu",
            "Gloria", "Gran", "Grec", "Grivita", "Grup", "GT", "Gut", "Hidro", "Honda Romania"
        ],
        "Slovenia": [
            "Renault Slovenia", "Revoz", "TAM", "Tovarna", "Adria", "Alpina", "Amp",
            "APV", "Astra", "Avto", "Bi", "Cimos", "Citroen Slovenia", "DAC", "Delta",
            "Elan", "Elektro", "Elma", "Emo", "Emona", "Era", "FAP", "Fiat Slovenia",
            "FNM", "Ford Slovenia", "Fruhauf", "Fructal", "Gama", "Gorenje", "Gorica",
            "Gorje", "Gospodarstvo", "Gostol", "Graf", "Gras", "Gredelj", "Grif",
            "Grosuplje", "Gulf", "Hidria", "Hrast", "Hrastnik", "Hro", "Huba", "Humar"
        ],
        "Serbia": [
            "Zastava", "Fiat Serbia", "Ikarbus", "Yugo", "Zastava Trucks", "FAP",
            "IMT", "IMR", "Neobus", "Bibo", "Cimos", "DAB", "DAF", "DOK", "Dom",
            "DPM", "Duro", "Dvor", "Elektro", "Energ", "Energo", "Enot", "Epidem",
            "Era", "Evro", "FAP", "Fero", "Fiat", "Fiat Serbia", "Fidelinka", "Fik",
            "Fil", "Fima", "Fira", "Firma", "Fis", "Fiz", "Fk", "Fle", "Fleks", "Fm",
            "FMP", "FMS", "Fn", "Fnd", "Fob", "Fod", "Fok", "Fon", "Fond", "Ford Serbia"
        ],
        "Croatia": [
            "Rimac", "Dok-ing", "Tvornica", "Autob", "Autod", "Autok", "Autol", "Auton",
            "Autop", "Autos", "Autot", "Babar", "Babic", "Badel", "Baj", "Bajad", "Bajo",
            "Bak", "Baka", "Bakar", "Bakic", "Bakula", "Bala", "Balaban", "Balatinac",
            "Baldo", "Balen", "Balic", "Balija", "Baljkas", "Balk", "Balkan", "Balkana",
            "Balog", "Balsa", "Balsic", "Balt", "Baltic", "Bamb", "Bambic", "Bambus"
        ],
        "Greece": [
            "Dimos", "Elbo", "Ena", "Faf", "Fam", "Far", "Farma", "Fas", "Fasidis",
            "Fass", "Fata", "Faxon", "Feder", "Fego", "Felas", "Femia", "Feredinos",
            "Fero", "Ferris", "Fetis", "Fevos", "Fexos", "Fial", "Fiat Greece", "Fid",
            "Fidis", "Fidos", "Fif", "Fifas", "Fifo", "Fifos", "Figos", "Fik", "Fikas",
            "Fikos", "Fil", "Fila", "Filak", "Filand", "Filar", "Filas", "Filios",
            "Filip", "Filippou", "Filis", "Filos", "Filox", "Filt", "Fin", "Fina", "Finas"
        ],
        "Egypt": [
            "Nasr", "Arab", "Egyptian", "El", "El-Nasr", "El-Tram", "El-Tramway",
            "El-Watan", "Elarab", "Elarabia", "Elaraby", "Elash", "Elashry", "Elbadr",
            "Elbahar", "Elbalad", "Elban", "Elbani", "Elbar", "Elbarbary", "Elbasel",
            "Elbatal", "Elbay", "Elbayoumi", "Elbaz", "Elbeh", "Elbehery", "Elbialy",
            "Elboghdady", "Elbohy", "Elborai", "Elboss", "Elbosss", "Elbr", "Elbra",
            "Elbren", "Elbrs", "Elbs", "Elbt", "Elby", "Elcab", "Elcaf", "Elcaid",
            "Elcamel", "Elcar", "Elcarm", "Elcars", "Elcary", "Elcass", "Elcat"
        ],
        "South Africa": [
            "Ford South Africa", "Toyota South Africa", "Volkswagen South Africa",
            "BMW South Africa", "Mercedes-Benz South Africa", "Nissan South Africa",
            "Honda South Africa", "Mazda South Africa", "Hyundai South Africa",
            "Kia South Africa", "Chevrolet South Africa", "Opel South Africa",
            "Renault South Africa", "Peugeot South Africa", "Citroën South Africa",
            "Fiat South Africa", "Alfa Romeo South Africa", "Land Rover South Africa",
            "Jaguar South Africa", "Volvo South Africa", "Mitsubishi South Africa",
            "Subaru South Africa", "Suzuki South Africa", "Daihatsu South Africa",
            "Isuzu South Africa", "Mahindra South Africa", "Tata South Africa"
        ],
        "Israel": [
            "Plasan", "AIL", "Automotive", "Carmel", "Haargaz", "Haifa", "Israel",
            "Israeli", "Jerusalem", "Kaiser", "Kedem", "Lahav", "Merkava", "Netanya",
            "Oren", "Plasan", "Ramon", "Sabra", "Shaked", "Shoaf", "Shoef", "Shofar",
            "Shoft", "Shoval", "Shovalim", "Shvat", "Sinai", "Sufa", "Sussita", "Susya",
            "Ta'as", "Taa", "Tabor", "Tal", "Talbi", "Taldor", "Talg", "Talgor", "Talit",
            "Talma", "Talmor", "Talsi", "Talya", "Tam", "Tama", "Tamam", "Tamar", "Tami"
        ],
        "Iran": [
            "Iran Khodro", "Saipa", "Pars Khodro", "Bahman", "Morattab", "Zamyad",
            "Kerman", "MVM", "Azar", "Azvand", "Bahman", "Barkhat", "Barkhordar",
            "Bary", "Beh", "Beh-Pars", "Behnam", "Behran", "Behran Motor", "Behzad",
            "Bina", "Binali", "Binalood", "Binesh", "Bistoon", "BMC", "Bonyan", "Boran",
            "Borg", "Bostan", "Boukan", "Bourse", "Boz", "Bozorg", "Bozorgmehr", "Bras",
            "Brat", "Brick", "Brid", "Brig", "Briggs", "Bril", "Brill", "Brillian",
            "Brilliance", "Brilliant", "Brillion", "Bri", "Briana", "Briane", "Briann"
        ],
        "Malaysia": [
            "Proton", "Perodua", "Bufori", "TD", "Inokom", "NAZA", "Modenas", "Hicom",
            "Alam", "Alfa", "Aliran", "Aluminium", "Alza", "Alya", "Alya", "Alya",
            "Alya", "Alya", "Alya", "Alya", "Alya", "Alya", "Alya", "Alya", "Alya",
            "Alya", "Alya", "Alya", "Alya", "Alya", "Alya", "Alya", "Alya", "Alya",
            "Alya", "Alya", "Alya", "Alya", "Alya", "Alya", "Alya", "Alya", "Alya",
            "Alya", "Alya", "Alya", "Alya", "Alya", "Alya", "Alya", "Alya", "Alya"
        ],
        "Vietnam": [
            "VinFast", "Thaco", "Samco", "TMT", "Veam", "Vietnam", "Vinaxuki",
            "Anh", "Anh", "Anh", "Anh", "Anh", "Anh", "Anh", "Anh", "Anh", "Anh",
            "Anh", "Anh", "Anh", "Anh", "Anh", "Anh", "Anh", "Anh", "Anh", "Anh",
            "Anh", "Anh", "Anh", "Anh", "Anh", "Anh", "Anh", "Anh", "Anh", "Anh",
            "Anh", "Anh", "Anh", "Anh", "Anh", "Anh", "Anh", "Anh", "Anh", "Anh",
            "Anh", "Anh", "Anh", "Anh", "Anh", "Anh", "Anh", "Anh", "Anh", "Anh"
        ],
        "Thailand": [
            "Thai", "Thai Rung", "Thairung", "Toyota Thailand", "Honda Thailand",
            "Isuzu Thailand", "Mitsubishi Thailand", "Nissan Thailand", "Ford Thailand",
            "Mazda Thailand", "Chevrolet Thailand", "Suzuki Thailand", "MG Thailand",
            "BMW Thailand", "Mercedes Thailand", "Volvo Thailand", "Porsche Thailand",
            "Audi Thailand", "Lexus Thailand", "Infiniti Thailand", "Jaguar Thailand",
            "Land Rover Thailand", "Maserati Thailand", "Ferrari Thailand", "Lamborghini Thailand"
        ],
        "Philippines": [
            "Toyota Philippines", "Mitsubishi Philippines", "Nissan Philippines",
            "Honda Philippines", "Ford Philippines", "Isuzu Philippines", "Suzuki Philippines",
            "Hyundai Philippines", "Kia Philippines", "Mazda Philippines", "Chevrolet Philippines",
            "Foton Philippines", "Mahindra Philippines", "Tata Philippines", "Peugeot Philippines",
            "BMW Philippines", "Mercedes Philippines", "Audi Philippines", "Volvo Philippines",
            "Lexus Philippines", "Infiniti Philippines", "Jaguar Philippines", "Land Rover Philippines"
        ],
        "Indonesia": [
            "Toyota Indonesia", "Daihatsu Indonesia", "Mitsubishi Indonesia",
            "Suzuki Indonesia", "Honda Indonesia", "Isuzu Indonesia", "Nissan Indonesia",
            "Mazda Indonesia", "Kia Indonesia", "Hyundai Indonesia", "Chevrolet Indonesia",
            "Ford Indonesia", "BMW Indonesia", "Mercedes Indonesia", "Volvo Indonesia",
            "Lexus Indonesia", "Infiniti Indonesia", "Porsche Indonesia", "Audi Indonesia"
        ],
        "Singapore": [
            "Toyota Singapore", "Honda Singapore", "Nissan Singapore", "Mitsubishi Singapore",
            "Hyundai Singapore", "Kia Singapore", "BMW Singapore", "Mercedes Singapore",
            "Audi Singapore", "Volvo Singapore", "Lexus Singapore", "Porsche Singapore",
            "Ferrari Singapore", "Lamborghini Singapore", "Maserati Singapore", "Bentley Singapore",
            "Rolls-Royce Singapore", "Lotus Singapore", "Mazda Singapore", "Suzuki Singapore"
        ],
        "New Zealand": [
            "Holden New Zealand", "Ford New Zealand", "Toyota New Zealand",
            "Mitsubishi New Zealand", "Nissan New Zealand", "Honda New Zealand",
            "Mazda New Zealand", "Suzuki New Zealand", "Hyundai New Zealand",
            "Kia New Zealand", "BMW New Zealand", "Mercedes New Zealand", "Audi New Zealand",
            "Volvo New Zealand", "Lexus New Zealand", "Porsche New Zealand", "Jaguar New Zealand",
            "Land Rover New Zealand", "Maserati New Zealand", "Ferrari New Zealand"
        ],
        "Argentina": [
            "Ford Argentina", "Chevrolet Argentina", "Volkswagen Argentina",
            "Fiat Argentina", "Renault Argentina", "Peugeot Argentina", "Citroën Argentina",
            "Toyota Argentina", "Nissan Argentina", "Honda Argentina", "Mercedes-Benz Argentina",
            "BMW Argentina", "Audi Argentina", "Jeep Argentina", "Ram Argentina", "Dodge Argentina",
            "Chrysler Argentina", "Iveco Argentina", "Scania Argentina", "Volvo Argentina"
        ],
        "Chile": [
            "Ford Chile", "Chevrolet Chile", "Nissan Chile", "Mitsubishi Chile",
            "Hyundai Chile", "Kia Chile", "Suzuki Chile", "Peugeot Chile", "Citroën Chile",
            "Renault Chile", "Volkswagen Chile", "Toyota Chile", "Honda Chile", "Mazda Chile",
            "BMW Chile", "Mercedes Chile", "Audi Chile", "Volvo Chile", "Jeep Chile", "RAM Chile"
        ],
        "Colombia": [
            "GM Colombia", "Renault Colombia", "Mazda Colombia", "Chevrolet Colombia",
            "Suzuki Colombia", "Kia Colombia", "Hyundai Colombia", "Nissan Colombia",
            "Toyota Colombia", "Ford Colombia", "Volkswagen Colombia", "Fiat Colombia",
            "Peugeot Colombia", "Citroën Colombia", "BMW Colombia", "Mercedes Colombia",
            "Audi Colombia", "Volvo Colombia", "Jeep Colombia", "RAM Colombia"
        ],
        "Peru": [
            "Toyota Peru", "Hyundai Peru", "Kia Peru", "Nissan Peru", "Chevrolet Peru",
            "Mitsubishi Peru", "Suzuki Peru", "Mazda Peru", "Ford Peru", "Volkswagen Peru",
            "Honda Peru", "Renault Peru", "Peugeot Peru", "Citroën Peru", "Fiat Peru",
            "BMW Peru", "Mercedes Peru", "Audi Peru", "Volvo Peru", "Jeep Peru"
        ],
        "Venezuela": [
            "Ford Venezuela", "GM Venezuela", "Toyota Venezuela", "Mitsubishi Venezuela",
            "Hyundai Venezuela", "Kia Venezuela", "Mazda Venezuela", "Fiat Venezuela",
            "Iveco Venezuela", "Mack Venezuela", "Volvo Venezuela", "Scania Venezuela",
            "Chery Venezuela", "Great Wall Venezuela", "Jac Venezuela", "Zotye Venezuela"
        ],
        "Nigeria": [
            "Innoson", "Nord", "Peugeot Nigeria", "Toyota Nigeria", "Nissan Nigeria",
            "Hyundai Nigeria", "Kia Nigeria", "Ford Nigeria", "Honda Nigeria", "Mitsubishi Nigeria",
            "Mercedes Nigeria", "BMW Nigeria", "Audi Nigeria", "Lexus Nigeria", "Jeep Nigeria",
            "RAM Nigeria", "Land Rover Nigeria", "Range Rover Nigeria", "Jaguar Nigeria"
        ],
        "Kenya": [
            "Mobius", "Toyota Kenya", "Nissan Kenya", "Mitsubishi Kenya", "Isuzu Kenya",
            "Hino Kenya", "Scania Kenya", "Volvo Kenya", "Mercedes Kenya", "BMW Kenya",
            "Audi Kenya", "Volkswagen Kenya", "Ford Kenya", "Hyundai Kenya", "Kia Kenya",
            "Mazda Kenya", "Suzuki Kenya", "Peugeot Kenya", "Renault Kenya", "Datsun Kenya"
        ],
        "Morocco": [
            "Renault Morocco", "Dacia Morocco", "Peugeot Morocco", "Citroën Morocco",
            "Ford Morocco", "Nissan Morocco", "Hyundai Morocco", "Kia Morocco",
            "Toyota Morocco", "Volkswagen Morocco", "Fiat Morocco", "Opel Morocco",
            "Mercedes Morocco", "BMW Morocco", "Audi Morocco", "Jeep Morocco", "RAM Morocco"
        ],
        "UAE": [
            "Zarooq", "W Motors", "Lynx", "Al", "Al-Bahar", "Al-Futtaim", "Al-Habtoor",
            "Al-Jaber", "Al-Masaood", "Al-Rostamani", "Al-Tayer", "Arabian", "Arabian Automobiles",
            "Audi UAE", "BMW UAE", "Bugatti UAE", "Bentley UAE", "Chevrolet UAE", "Dodge UAE",
            "Ferrari UAE", "Ford UAE", "GMC UAE", "Honda UAE", "Hyundai UAE", "Infiniti UAE",
            "Jaguar UAE", "Jeep UAE", "Kia UAE", "Lamborghini UAE", "Land Rover UAE",
            "Lexus UAE", "Maserati UAE", "Mazda UAE", "McLaren UAE", "Mercedes UAE",
            "Mitsubishi UAE", "Nissan UAE", "Porsche UAE", "RAM UAE", "Range Rover UAE",
            "Renault UAE", "Rolls-Royce UAE", "Subaru UAE", "Suzuki UAE", "Toyota UAE",
            "Volkswagen UAE", "Volvo UAE"
        ],
        "Saudi Arabia": [
            "Toyota Saudi", "Nissan Saudi", "Hyundai Saudi", "Kia Saudi", "Ford Saudi",
            "Chevrolet Saudi", "GMC Saudi", "RAM Saudi", "Jeep Saudi", "Dodge Saudi",
            "Chrysler Saudi", "Mitsubishi Saudi", "Honda Saudi", "Mazda Saudi", "Lexus Saudi",
            "BMW Saudi", "Mercedes Saudi", "Audi Saudi", "Porsche Saudi", "Land Rover Saudi",
            "Range Rover Saudi", "Jaguar Saudi", "Volvo Saudi", "Renault Saudi", "Peugeot Saudi"
        ],
        "Qatar": [
            "Toyota Qatar", "Nissan Qatar", "Hyundai Qatar", "Kia Qatar", "Ford Qatar",
            "Chevrolet Qatar", "GMC Qatar", "RAM Qatar", "Jeep Qatar", "Dodge Qatar",
            "Mitsubishi Qatar", "Honda Qatar", "Mazda Qatar", "Lexus Qatar", "BMW Qatar",
            "Mercedes Qatar", "Audi Qatar", "Porsche Qatar", "Land Rover Qatar", "Range Rover Qatar",
            "Jaguar Qatar", "Volvo Qatar", "Renault Qatar", "Peugeot Qatar", "Ferrari Qatar",
            "Lamborghini Qatar", "Maserati Qatar", "Bentley Qatar", "Rolls-Royce Qatar", "McLaren Qatar"
        ],
        "Kuwait": [
            "Toyota Kuwait", "Nissan Kuwait", "Hyundai Kuwait", "Kia Kuwait", "Ford Kuwait",
            "Chevrolet Kuwait", "GMC Kuwait", "RAM Kuwait", "Jeep Kuwait", "Dodge Kuwait",
            "Mitsubishi Kuwait", "Honda Kuwait", "Mazda Kuwait", "Lexus Kuwait", "BMW Kuwait",
            "Mercedes Kuwait", "Audi Kuwait", "Porsche Kuwait", "Land Rover Kuwait", "Range Rover Kuwait",
            "Jaguar Kuwait", "Volvo Kuwait", "Renault Kuwait", "Peugeot Kuwait", "Ferrari Kuwait",
            "Lamborghini Kuwait", "Maserati Kuwait", "Bentley Kuwait", "Rolls-Royce Kuwait"
        ],
        "Oman": [
            "Toyota Oman", "Nissan Oman", "Hyundai Oman", "Kia Oman", "Ford Oman",
            "Chevrolet Oman", "GMC Oman", "RAM Oman", "Jeep Oman", "Dodge Oman",
            "Mitsubishi Oman", "Honda Oman", "Mazda Oman", "Lexus Oman", "BMW Oman",
            "Mercedes Oman", "Audi Oman", "Porsche Oman", "Land Rover Oman", "Range Rover Oman",
            "Jaguar Oman", "Volvo Oman", "Renault Oman", "Peugeot Oman", "Suzuki Oman"
        ],
        "Bahrain": [
            "Toyota Bahrain", "Nissan Bahrain", "Hyundai Bahrain", "Kia Bahrain",
            "Ford Bahrain", "Chevrolet Bahrain", "GMC Bahrain", "RAM Bahrain", "Jeep Bahrain",
            "Dodge Bahrain", "Mitsubishi Bahrain", "Honda Bahrain", "Mazda Bahrain", "Lexus Bahrain",
            "BMW Bahrain", "Mercedes Bahrain", "Audi Bahrain", "Porsche Bahrain", "Land Rover Bahrain",
            "Range Rover Bahrain", "Jaguar Bahrain", "Volvo Bahrain", "Renault Bahrain"
        ],
        "Jordan": [
            "Toyota Jordan", "Nissan Jordan", "Hyundai Jordan", "Kia Jordan", "Ford Jordan",
            "Chevrolet Jordan", "GMC Jordan", "RAM Jordan", "Jeep Jordan", "Dodge Jordan",
            "Mitsubishi Jordan", "Honda Jordan", "Mazda Jordan", "Lexus Jordan", "BMW Jordan",
            "Mercedes Jordan", "Audi Jordan", "Porsche Jordan", "Land Rover Jordan", "Range Rover Jordan",
            "Jaguar Jordan", "Volvo Jordan", "Renault Jordan", "Peugeot Jordan", "Citroën Jordan"
        ],
        "Lebanon": [
            "Toyota Lebanon", "Nissan Lebanon", "Hyundai Lebanon", "Kia Lebanon",
            "Ford Lebanon", "Chevrolet Lebanon", "GMC Lebanon", "Jeep Lebanon", "Dodge Lebanon",
            "Mitsubishi Lebanon", "Honda Lebanon", "Mazda Lebanon", "Lexus Lebanon", "BMW Lebanon",
            "Mercedes Lebanon", "Audi Lebanon", "Porsche Lebanon", "Land Rover Lebanon", "Range Rover Lebanon",
            "Jaguar Lebanon", "Volvo Lebanon", "Renault Lebanon", "Peugeot Lebanon", "Citroën Lebanon"
        ],
        "Cyprus": [
            "Toyota Cyprus", "Nissan Cyprus", "Hyundai Cyprus", "Kia Cyprus", "Ford Cyprus",
            "Chevrolet Cyprus", "Mitsubishi Cyprus", "Honda Cyprus", "Mazda Cyprus", "BMW Cyprus",
            "Mercedes Cyprus", "Audi Cyprus", "Porsche Cyprus", "Land Rover Cyprus", "Range Rover Cyprus",
            "Jaguar Cyprus", "Volvo Cyprus", "Renault Cyprus", "Peugeot Cyprus", "Citroën Cyprus",
            "Fiat Cyprus", "Opel Cyprus", "Suzuki Cyprus", "Subaru Cyprus", "Lexus Cyprus"
        ],
        "Malta": [
            "Toyota Malta", "Nissan Malta", "Hyundai Malta", "Kia Malta", "Ford Malta",
            "Chevrolet Malta", "Mitsubishi Malta", "Honda Malta", "Mazda Malta", "BMW Malta",
            "Mercedes Malta", "Audi Malta", "Porsche Malta", "Land Rover Malta", "Range Rover Malta",
            "Jaguar Malta", "Volvo Malta", "Renault Malta", "Peugeot Malta", "Citroën Malta",
            "Fiat Malta", "Opel Malta", "Suzuki Malta", "Subaru Malta", "Lexus Malta"
        ],
        "Iceland": [
            "Toyota Iceland", "Nissan Iceland", "Hyundai Iceland", "Kia Iceland",
            "Ford Iceland", "Chevrolet Iceland", "Mitsubishi Iceland", "Honda Iceland",
            "Mazda Iceland", "BMW Iceland", "Mercedes Iceland", "Audi Iceland", "Porsche Iceland",
            "Land Rover Iceland", "Range Rover Iceland", "Jaguar Iceland", "Volvo Iceland",
            "Renault Iceland", "Peugeot Iceland", "Citroën Iceland", "Subaru Iceland",
            "Suzuki Iceland", "Dacia Iceland", "Fiat Iceland", "Jeep Iceland", "RAM Iceland"
        ],
        "Luxembourg": [
            "Toyota Luxembourg", "Nissan Luxembourg", "Hyundai Luxembourg", "Kia Luxembourg",
            "Ford Luxembourg", "Chevrolet Luxembourg", "Mitsubishi Luxembourg", "Honda Luxembourg",
            "Mazda Luxembourg", "BMW Luxembourg", "Mercedes Luxembourg", "Audi Luxembourg",
            "Porsche Luxembourg", "Land Rover Luxembourg", "Range Rover Luxembourg", "Jaguar Luxembourg",
            "Volvo Luxembourg", "Renault Luxembourg", "Peugeot Luxembourg", "Citroën Luxembourg",
            "Fiat Luxembourg", "Opel Luxembourg", "Suzuki Luxembourg", "Subaru Luxembourg",
            "Lexus Luxembourg", "Dacia Luxembourg", "Jeep Luxembourg", "RAM Luxembourg"
        ],
        "Monaco": [
            "Ferrari Monaco", "Lamborghini Monaco", "Maserati Monaco", "Bugatti Monaco",
            "Bentley Monaco", "Rolls-Royce Monaco", "Aston Martin Monaco", "McLaren Monaco",
            "Porsche Monaco", "Audi Monaco", "BMW Monaco", "Mercedes Monaco", "Lexus Monaco",
            "Toyota Monaco", "Nissan Monaco", "Hyundai Monaco", "Kia Monaco", "Ford Monaco"
        ],
        "Liechtenstein": [
            "Porsche Liechtenstein", "Audi Liechtenstein", "BMW Liechtenstein",
            "Mercedes Liechtenstein", "Volkswagen Liechtenstein", "Toyota Liechtenstein",
            "Nissan Liechtenstein", "Hyundai Liechtenstein", "Kia Liechtenstein",
            "Ford Liechtenstein", "Opel Liechtenstein", "Fiat Liechtenstein", "Renault Liechtenstein"
        ],
        "San Marino": [
            "Ferrari San Marino", "Lamborghini San Marino", "Maserati San Marino",
            "Fiat San Marino", "Alfa Romeo San Marino", "Lancia San Marino", "Abarth San Marino"
        ],
        "Vatican City": [
            "Fiat Vatican", "Popemobile", "Mercedes Vatican", "Land Rover Vatican",
            "Renault Vatican", "Citroën Vatican", "Peugeot Vatican"
        ],
        "Andorra": [
            "Toyota Andorra", "Nissan Andorra", "Hyundai Andorra", "Kia Andorra",
            "Ford Andorra", "Chevrolet Andorra", "Mitsubishi Andorra", "Honda Andorra",
            "Mazda Andorra", "BMW Andorra", "Mercedes Andorra", "Audi Andorra",
            "Porsche Andorra", "Land Rover Andorra", "Range Rover Andorra", "Jaguar Andorra",
            "Volvo Andorra", "Renault Andorra", "Peugeot Andorra", "Citroën Andorra",
            "Fiat Andorra", "Opel Andorra", "Suzuki Andorra", "Subaru Andorra", "Lexus Andorra"
        ],
        "Greenland": [
            "Toyota Greenland", "Nissan Greenland", "Hyundai Greenland", "Kia Greenland",
            "Ford Greenland", "Chevrolet Greenland", "Mitsubishi Greenland", "Honda Greenland",
            "Mazda Greenland", "BMW Greenland", "Mercedes Greenland", "Audi Greenland",
            "Land Rover Greenland", "Range Rover Greenland", "Jaguar Greenland", "Volvo Greenland",
            "Renault Greenland", "Peugeot Greenland", "Citroën Greenland", "Subaru Greenland",
            "Suzuki Greenland", "Dacia Greenland", "Jeep Greenland", "RAM Greenland"
        ],
        "Faroe Islands": [
            "Toyota Faroe", "Nissan Faroe", "Hyundai Faroe", "Kia Faroe", "Ford Faroe",
            "Chevrolet Faroe", "Mitsubishi Faroe", "Honda Faroe", "Mazda Faroe", "BMW Faroe",
            "Mercedes Faroe", "Audi Faroe", "Land Rover Faroe", "Range Rover Faroe", "Volvo Faroe",
            "Renault Faroe", "Peugeot Faroe", "Citroën Faroe", "Subaru Faroe", "Suzuki Faroe"
        ],
        "Gibraltar": [
            "Toyota Gibraltar", "Nissan Gibraltar", "Hyundai Gibraltar", "Kia Gibraltar",
            "Ford Gibraltar", "Chevrolet Gibraltar", "Mitsubishi Gibraltar", "Honda Gibraltar",
            "Mazda Gibraltar", "BMW Gibraltar", "Mercedes Gibraltar", "Audi Gibraltar",
            "Land Rover Gibraltar", "Range Rover Gibraltar", "Jaguar Gibraltar", "Volvo Gibraltar",
            "Renault Gibraltar", "Peugeot Gibraltar", "Citroën Gibraltar", "Fiat Gibraltar"
        ],
        "Bermuda": [
            "Toyota Bermuda", "Nissan Bermuda", "Hyundai Bermuda", "Kia Bermuda",
            "Ford Bermuda", "Chevrolet Bermuda", "Mitsubishi Bermuda", "Honda Bermuda",
            "Mazda Bermuda", "BMW Bermuda", "Mercedes Bermuda", "Audi Bermuda",
            "Land Rover Bermuda", "Range Rover Bermuda", "Jaguar Bermuda", "Volvo Bermuda",
            "Renault Bermuda", "Peugeot Bermuda", "Citroën Bermuda", "Subaru Bermuda"
        ],
        "Cayman Islands": [
            "Toyota Cayman", "Nissan Cayman", "Hyundai Cayman", "Kia Cayman",
            "Ford Cayman", "Chevrolet Cayman", "Mitsubishi Cayman", "Honda Cayman",
            "Mazda Cayman", "BMW Cayman", "Mercedes Cayman", "Audi Cayman",
            "Porsche Cayman", "Land Rover Cayman", "Range Rover Cayman", "Jaguar Cayman",
            "Ferrari Cayman", "Lamborghini Cayman", "Maserati Cayman", "Bentley Cayman"
        ],
        "Bahamas": [
            "Toyota Bahamas", "Nissan Bahamas", "Hyundai Bahamas", "Kia Bahamas",
            "Ford Bahamas", "Chevrolet Bahamas", "Mitsubishi Bahamas", "Honda Bahamas",
            "Mazda Bahamas", "BMW Bahamas", "Mercedes Bahamas", "Audi Bahamas",
            "Land Rover Bahamas", "Range Rover Bahamas", "Jaguar Bahamas", "Jeep Bahamas",
            "RAM Bahamas", "Dodge Bahamas", "Chrysler Bahamas", "GMC Bahamas"
        ],
        "Barbados": [
            "Toyota Barbados", "Nissan Barbados", "Hyundai Barbados", "Kia Barbados",
            "Ford Barbados", "Chevrolet Barbados", "Mitsubishi Barbados", "Honda Barbados",
            "Mazda Barbados", "BMW Barbados", "Mercedes Barbados", "Audi Barbados",
            "Land Rover Barbados", "Range Rover Barbados", "Jaguar Barbados", "Suzuki Barbados",
            "Subaru Barbados", "Jeep Barbados", "RAM Barbados", "Dodge Barbados"
        ],
        "Trinidad": [
            "Toyota Trinidad", "Nissan Trinidad", "Hyundai Trinidad", "Kia Trinidad",
            "Ford Trinidad", "Chevrolet Trinidad", "Mitsubishi Trinidad", "Honda Trinidad",
            "Mazda Trinidad", "BMW Trinidad", "Mercedes Trinidad", "Audi Trinidad",
            "Land Rover Trinidad", "Range Rover Trinidad", "Jaguar Trinidad", "Suzuki Trinidad",
            "Subaru Trinidad", "Jeep Trinidad", "RAM Trinidad", "Dodge Trinidad"
        ],
        "Jamaica": [
            "Toyota Jamaica", "Nissan Jamaica", "Hyundai Jamaica", "Kia Jamaica",
            "Ford Jamaica", "Chevrolet Jamaica", "Mitsubishi Jamaica", "Honda Jamaica",
            "Mazda Jamaica", "BMW Jamaica", "Mercedes Jamaica", "Audi Jamaica",
            "Land Rover Jamaica", "Range Rover Jamaica", "Jaguar Jamaica", "Suzuki Jamaica",
            "Subaru Jamaica", "Jeep Jamaica", "RAM Jamaica", "Dodge Jamaica"
        ],
        "Puerto Rico": [
            "Toyota Puerto Rico", "Nissan Puerto Rico", "Hyundai Puerto Rico",
            "Kia Puerto Rico", "Ford Puerto Rico", "Chevrolet Puerto Rico",
            "Mitsubishi Puerto Rico", "Honda Puerto Rico", "Mazda Puerto Rico",
            "BMW Puerto Rico", "Mercedes Puerto Rico", "Audi Puerto Rico",
            "Porsche Puerto Rico", "Land Rover Puerto Rico", "Range Rover Puerto Rico",
            "Jaguar Puerto Rico", "Jeep Puerto Rico", "RAM Puerto Rico", "Dodge Puerto Rico",
            "Chrysler Puerto Rico", "GMC Puerto Rico", "Buick Puerto Rico", "Cadillac Puerto Rico"
        ],
        "Dominican Republic": [
            "Toyota Dominican", "Nissan Dominican", "Hyundai Dominican", "Kia Dominican",
            "Ford Dominican", "Chevrolet Dominican", "Mitsubishi Dominican", "Honda Dominican",
            "Mazda Dominican", "BMW Dominican", "Mercedes Dominican", "Audi Dominican",
            "Land Rover Dominican", "Range Rover Dominican", "Jaguar Dominican", "Jeep Dominican",
            "RAM Dominican", "Dodge Dominican", "Chrysler Dominican", "GMC Dominican"
        ],
        "Costa Rica": [
            "Toyota Costa Rica", "Nissan Costa Rica", "Hyundai Costa Rica", "Kia Costa Rica",
            "Ford Costa Rica", "Chevrolet Costa Rica", "Mitsubishi Costa Rica", "Honda Costa Rica",
            "Mazda Costa Rica", "BMW Costa Rica", "Mercedes Costa Rica", "Audi Costa Rica",
            "Land Rover Costa Rica", "Range Rover Costa Rica", "Jaguar Costa Rica", "Jeep Costa Rica",
            "RAM Costa Rica", "Dodge Costa Rica", "Suzuki Costa Rica", "Subaru Costa Rica"
        ],
        "Panama": [
            "Toyota Panama", "Nissan Panama", "Hyundai Panama", "Kia Panama",
            "Ford Panama", "Chevrolet Panama", "Mitsubishi Panama", "Honda Panama",
            "Mazda Panama", "BMW Panama", "Mercedes Panama", "Audi Panama",
            "Porsche Panama", "Land Rover Panama", "Range Rover Panama", "Jaguar Panama",
            "Jeep Panama", "RAM Panama", "Dodge Panama", "Chrysler Panama", "GMC Panama"
        ],
        "Guatemala": [
            "Toyota Guatemala", "Nissan Guatemala", "Hyundai Guatemala", "Kia Guatemala",
            "Ford Guatemala", "Chevrolet Guatemala", "Mitsubishi Guatemala", "Honda Guatemala",
            "Mazda Guatemala", "BMW Guatemala", "Mercedes Guatemala", "Audi Guatemala",
            "Land Rover Guatemala", "Range Rover Guatemala", "Jaguar Guatemala", "Jeep Guatemala",
            "RAM Guatemala", "Dodge Guatemala", "Suzuki Guatemala", "Subaru Guatemala"
        ],
        "Honduras": [
            "Toyota Honduras", "Nissan Honduras", "Hyundai Honduras", "Kia Honduras",
            "Ford Honduras", "Chevrolet Honduras", "Mitsubishi Honduras", "Honda Honduras",
            "Mazda Honduras", "BMW Honduras", "Mercedes Honduras", "Audi Honduras",
            "Land Rover Honduras", "Range Rover Honduras", "Jaguar Honduras", "Jeep Honduras",
            "RAM Honduras", "Dodge Honduras", "Suzuki Honduras", "Subaru Honduras"
        ],
        "Nicaragua": [
            "Toyota Nicaragua", "Nissan Nicaragua", "Hyundai Nicaragua", "Kia Nicaragua",
            "Ford Nicaragua", "Chevrolet Nicaragua", "Mitsubishi Nicaragua", "Honda Nicaragua",
            "Mazda Nicaragua", "BMW Nicaragua", "Mercedes Nicaragua", "Audi Nicaragua",
            "Land Rover Nicaragua", "Range Rover Nicaragua", "Jaguar Nicaragua", "Jeep Nicaragua",
            "RAM Nicaragua", "Dodge Nicaragua", "Suzuki Nicaragua", "Subaru Nicaragua"
        ],
        "El Salvador": [
            "Toyota El Salvador", "Nissan El Salvador", "Hyundai El Salvador", "Kia El Salvador",
            "Ford El Salvador", "Chevrolet El Salvador", "Mitsubishi El Salvador", "Honda El Salvador",
            "Mazda El Salvador", "BMW El Salvador", "Mercedes El Salvador", "Audi El Salvador",
            "Land Rover El Salvador", "Range Rover El Salvador", "Jaguar El Salvador", "Jeep El Salvador",
            "RAM El Salvador", "Dodge El Salvador", "Suzuki El Salvador", "Subaru El Salvador"
        ],
        "Bolivia": [
            "Toyota Bolivia", "Nissan Bolivia", "Hyundai Bolivia", "Kia Bolivia",
            "Ford Bolivia", "Chevrolet Bolivia", "Mitsubishi Bolivia", "Honda Bolivia",
            "Mazda Bolivia", "BMW Bolivia", "Mercedes Bolivia", "Audi Bolivia",
            "Land Rover Bolivia", "Range Rover Bolivia", "Jaguar Bolivia", "Jeep Bolivia",
            "RAM Bolivia", "Dodge Bolivia", "Suzuki Bolivia", "Subaru Bolivia", "Volvo Bolivia"
        ],
        "Paraguay": [
            "Toyota Paraguay", "Nissan Paraguay", "Hyundai Paraguay", "Kia Paraguay",
            "Ford Paraguay", "Chevrolet Paraguay", "Mitsubishi Paraguay", "Honda Paraguay",
            "Mazda Paraguay", "BMW Paraguay", "Mercedes Paraguay", "Audi Paraguay",
            "Land Rover Paraguay", "Range Rover Paraguay", "Jaguar Paraguay", "Jeep Paraguay",
            "RAM Paraguay", "Dodge Paraguay", "Suzuki Paraguay", "Subaru Paraguay", "Volvo Paraguay"
        ],
        "Uruguay": [
            "Toyota Uruguay", "Nissan Uruguay", "Hyundai Uruguay", "Kia Uruguay",
            "Ford Uruguay", "Chevrolet Uruguay", "Mitsubishi Uruguay", "Honda Uruguay",
            "Mazda Uruguay", "BMW Uruguay", "Mercedes Uruguay", "Audi Uruguay",
            "Land Rover Uruguay", "Range Rover Uruguay", "Jaguar Uruguay", "Jeep Uruguay",
            "RAM Uruguay", "Dodge Uruguay", "Suzuki Uruguay", "Subaru Uruguay", "Volvo Uruguay"
        ],
        "Ecuador": [
            "Toyota Ecuador", "Nissan Ecuador", "Hyundai Ecuador", "Kia Ecuador",
            "Ford Ecuador", "Chevrolet Ecuador", "Mitsubishi Ecuador", "Honda Ecuador",
            "Mazda Ecuador", "BMW Ecuador", "Mercedes Ecuador", "Audi Ecuador",
            "Land Rover Ecuador", "Range Rover Ecuador", "Jaguar Ecuador", "Jeep Ecuador",
            "RAM Ecuador", "Dodge Ecuador", "Suzuki Ecuador", "Subaru Ecuador", "Great Wall Ecuador"
        ],
        "Guyana": [
            "Toyota Guyana", "Nissan Guyana", "Hyundai Guyana", "Kia Guyana",
            "Ford Guyana", "Chevrolet Guyana", "Mitsubishi Guyana", "Honda Guyana",
            "Mazda Guyana", "BMW Guyana", "Mercedes Guyana", "Land Rover Guyana",
            "Range Rover Guyana", "Jeep Guyana", "RAM Guyana", "Dodge Guyana", "Suzuki Guyana"
        ],
        "Suriname": [
            "Toyota Suriname", "Nissan Suriname", "Hyundai Suriname", "Kia Suriname",
            "Ford Suriname", "Chevrolet Suriname", "Mitsubishi Suriname", "Honda Suriname",
            "Mazda Suriname", "BMW Suriname", "Mercedes Suriname", "Land Rover Suriname",
            "Jeep Suriname", "RAM Suriname", "Dodge Suriname", "Suzuki Suriname"
        ],
        "French Guiana": [
            "Renault French Guiana", "Peugeot French Guiana", "Citroën French Guiana",
            "Toyota French Guiana", "Nissan French Guiana", "Hyundai French Guiana",
            "Kia French Guiana", "Ford French Guiana", "Chevrolet French Guiana",
            "Dacia French Guiana", "Fiat French Guiana", "Opel French Guiana", "BMW French Guiana",
            "Mercedes French Guiana", "Audi French Guiana", "Land Rover French Guiana"
        ],
        "Albania": [
            "Toyota Albania", "Nissan Albania", "Hyundai Albania", "Kia Albania",
            "Ford Albania", "Chevrolet Albania", "Mitsubishi Albania", "Honda Albania",
            "Mazda Albania", "BMW Albania", "Mercedes Albania", "Audi Albania",
            "Volkswagen Albania", "Renault Albania", "Peugeot Albania", "Citroën Albania",
            "Fiat Albania", "Opel Albania", "Suzuki Albania", "Dacia Albania", "Jeep Albania"
        ],
        "Bosnia": [
            "Toyota Bosnia", "Nissan Bosnia", "Hyundai Bosnia", "Kia Bosnia",
            "Ford Bosnia", "Chevrolet Bosnia", "Mitsubishi Bosnia", "Honda Bosnia",
            "Mazda Bosnia", "BMW Bosnia", "Mercedes Bosnia", "Audi Bosnia",
            "Volkswagen Bosnia", "Renault Bosnia", "Peugeot Bosnia", "Citroën Bosnia",
            "Fiat Bosnia", "Opel Bosnia", "Suzuki Bosnia", "Dacia Bosnia", "Jeep Bosnia"
        ],
        "Bulgaria": [
            "Toyota Bulgaria", "Nissan Bulgaria", "Hyundai Bulgaria", "Kia Bulgaria",
            "Ford Bulgaria", "Chevrolet Bulgaria", "Mitsubishi Bulgaria", "Honda Bulgaria",
            "Mazda Bulgaria", "BMW Bulgaria", "Mercedes Bulgaria", "Audi Bulgaria",
            "Volkswagen Bulgaria", "Renault Bulgaria", "Peugeot Bulgaria", "Citroën Bulgaria",
            "Fiat Bulgaria", "Opel Bulgaria", "Suzuki Bulgaria", "Dacia Bulgaria", "Jeep Bulgaria",
            "Lada Bulgaria", "Great Wall Bulgaria", "Chery Bulgaria"
        ],
        "Croatia": [
            "Rimac", "Toyota Croatia", "Nissan Croatia", "Hyundai Croatia", "Kia Croatia",
            "Ford Croatia", "Chevrolet Croatia", "Mitsubishi Croatia", "Honda Croatia",
            "Mazda Croatia", "BMW Croatia", "Mercedes Croatia", "Audi Croatia",
            "Volkswagen Croatia", "Renault Croatia", "Peugeot Croatia", "Citroën Croatia",
            "Fiat Croatia", "Opel Croatia", "Suzuki Croatia", "Dacia Croatia", "Jeep Croatia",
            "Škoda Croatia", "Seat Croatia", "Cupra Croatia"
        ],
        "Estonia": [
            "Toyota Estonia", "Nissan Estonia", "Hyundai Estonia", "Kia Estonia",
            "Ford Estonia", "Chevrolet Estonia", "Mitsubishi Estonia", "Honda Estonia",
            "Mazda Estonia", "BMW Estonia", "Mercedes Estonia", "Audi Estonia",
            "Volkswagen Estonia", "Renault Estonia", "Peugeot Estonia", "Citroën Estonia",
            "Fiat Estonia", "Opel Estonia", "Suzuki Estonia", "Dacia Estonia", "Jeep Estonia",
            "Škoda Estonia", "Seat Estonia", "Cupra Estonia", "Volvo Estonia"
        ],
        "Latvia": [
            "Toyota Latvia", "Nissan Latvia", "Hyundai Latvia", "Kia Latvia",
            "Ford Latvia", "Chevrolet Latvia", "Mitsubishi Latvia", "Honda Latvia",
            "Mazda Latvia", "BMW Latvia", "Mercedes Latvia", "Audi Latvia",
            "Volkswagen Latvia", "Renault Latvia", "Peugeot Latvia", "Citroën Latvia",
            "Fiat Latvia", "Opel Latvia", "Suzuki Latvia", "Dacia Latvia", "Jeep Latvia",
            "Škoda Latvia", "Seat Latvia", "Cupra Latvia", "Volvo Latvia"
        ],
        "Lithuania": [
            "Toyota Lithuania", "Nissan Lithuania", "Hyundai Lithuania", "Kia Lithuania",
            "Ford Lithuania", "Chevrolet Lithuania", "Mitsubishi Lithuania", "Honda Lithuania",
            "Mazda Lithuania", "BMW Lithuania", "Mercedes Lithuania", "Audi Lithuania",
            "Volkswagen Lithuania", "Renault Lithuania", "Peugeot Lithuania", "Citroën Lithuania",
            "Fiat Lithuania", "Opel Lithuania", "Suzuki Lithuania", "Dacia Lithuania", "Jeep Lithuania",
            "Škoda Lithuania", "Seat Lithuania", "Cupra Lithuania", "Volvo Lithuania"
        ],
        "Belarus": [
            "Toyota Belarus", "Nissan Belarus", "Hyundai Belarus", "Kia Belarus",
            "Ford Belarus", "Chevrolet Belarus", "Mitsubishi Belarus", "Honda Belarus",
            "Mazda Belarus", "BMW Belarus", "Mercedes Belarus", "Audi Belarus",
            "Volkswagen Belarus", "Renault Belarus", "Peugeot Belarus", "Citroën Belarus",
            "Fiat Belarus", "Opel Belarus", "Suzuki Belarus", "Dacia Belarus", "Jeep Belarus",
            "Lada Belarus", "GAZ Belarus", "UAZ Belarus", "Geely Belarus"
        ],
        "Ukraine": [
            "Toyota Ukraine", "Nissan Ukraine", "Hyundai Ukraine", "Kia Ukraine",
            "Ford Ukraine", "Chevrolet Ukraine", "Mitsubishi Ukraine", "Honda Ukraine",
            "Mazda Ukraine", "BMW Ukraine", "Mercedes Ukraine", "Audi Ukraine",
            "Volkswagen Ukraine", "Renault Ukraine", "Peugeot Ukraine", "Citroën Ukraine",
            "Fiat Ukraine", "Opel Ukraine", "Suzuki Ukraine", "Dacia Ukraine", "Jeep Ukraine",
            "Lada Ukraine", "GAZ Ukraine", "UAZ Ukraine", "ZAZ Ukraine", "Bogdan Ukraine",
            "Etalon Ukraine", "LuAZ Ukraine", "KrAZ Ukraine"
        ],
        "Moldova": [
            "Toyota Moldova", "Nissan Moldova", "Hyundai Moldova", "Kia Moldova",
            "Ford Moldova", "Chevrolet Moldova", "Mitsubishi Moldova", "Honda Moldova",
            "Mazda Moldova", "BMW Moldova", "Mercedes Moldova", "Audi Moldova",
            "Volkswagen Moldova", "Renault Moldova", "Peugeot Moldova", "Citroën Moldova",
            "Fiat Moldova", "Opel Moldova", "Suzuki Moldova", "Dacia Moldova", "Jeep Moldova",
            "Lada Moldova", "GAZ Moldova", "UAZ Moldova"
        ],
        "Georgia": [
            "Toyota Georgia", "Nissan Georgia", "Hyundai Georgia", "Kia Georgia",
            "Ford Georgia", "Chevrolet Georgia", "Mitsubishi Georgia", "Honda Georgia",
            "Mazda Georgia", "BMW Georgia", "Mercedes Georgia", "Audi Georgia",
            "Volkswagen Georgia", "Renault Georgia", "Peugeot Georgia", "Citroën Georgia",
            "Fiat Georgia", "Opel Georgia", "Suzuki Georgia", "Dacia Georgia", "Jeep Georgia",
            "Lada Georgia", "GAZ Georgia", "UAZ Georgia"
        ],
        "Armenia": [
            "Toyota Armenia", "Nissan Armenia", "Hyundai Armenia", "Kia Armenia",
            "Ford Armenia", "Chevrolet Armenia", "Mitsubishi Armenia", "Honda Armenia",
            "Mazda Armenia", "BMW Armenia", "Mercedes Armenia", "Audi Armenia",
            "Volkswagen Armenia", "Renault Armenia", "Peugeot Armenia", "Citroën Armenia",
            "Fiat Armenia", "Opel Armenia", "Suzuki Armenia", "Dacia Armenia", "Jeep Armenia",
            "Lada Armenia", "GAZ Armenia", "UAZ Armenia"
        ],
        "Azerbaijan": [
            "Toyota Azerbaijan", "Nissan Azerbaijan", "Hyundai Azerbaijan", "Kia Azerbaijan",
            "Ford Azerbaijan", "Chevrolet Azerbaijan", "Mitsubishi Azerbaijan", "Honda Azerbaijan",
            "Mazda Azerbaijan", "BMW Azerbaijan", "Mercedes Azerbaijan", "Audi Azerbaijan",
            "Volkswagen Azerbaijan", "Renault Azerbaijan", "Peugeot Azerbaijan", "Citroën Azerbaijan",
            "Fiat Azerbaijan", "Opel Azerbaijan", "Suzuki Azerbaijan", "Dacia Azerbaijan", "Jeep Azerbaijan",
            "Lada Azerbaijan", "GAZ Azerbaijan", "UAZ Azerbaijan", "Khazar Azerbaijan"
        ],
        "Kazakhstan": [
            "Toyota Kazakhstan", "Nissan Kazakhstan", "Hyundai Kazakhstan", "Kia Kazakhstan",
            "Ford Kazakhstan", "Chevrolet Kazakhstan", "Mitsubishi Kazakhstan", "Honda Kazakhstan",
            "Mazda Kazakhstan", "BMW Kazakhstan", "Mercedes Kazakhstan", "Audi Kazakhstan",
            "Volkswagen Kazakhstan", "Renault Kazakhstan", "Peugeot Kazakhstan", "Citroën Kazakhstan",
            "Fiat Kazakhstan", "Opel Kazakhstan", "Suzuki Kazakhstan", "Dacia Kazakhstan", "Jeep Kazakhstan",
            "Lada Kazakhstan", "GAZ Kazakhstan", "UAZ Kazakhstan", "Asia Motors Kazakhstan"
        ],
        "Uzbekistan": [
            "UzAuto", "GM Uzbekistan", "Chevrolet Uzbekistan", "Ravon", "Toyota Uzbekistan",
            "Nissan Uzbekistan", "Hyundai Uzbekistan", "Kia Uzbekistan", "Ford Uzbekistan",
            "Mitsubishi Uzbekistan", "Honda Uzbekistan", "Mazda Uzbekistan", "BMW Uzbekistan",
            "Mercedes Uzbekistan", "Audi Uzbekistan", "Volkswagen Uzbekistan", "Land Rover Uzbekistan",
            "Jeep Uzbekistan", "RAM Uzbekistan", "Dodge Uzbekistan"
        ],
        "Turkmenistan": [
            "Toyota Turkmenistan", "Nissan Turkmenistan", "Hyundai Turkmenistan", "Kia Turkmenistan",
            "Ford Turkmenistan", "Chevrolet Turkmenistan", "Mitsubishi Turkmenistan", "Honda Turkmenistan",
            "Mazda Turkmenistan", "BMW Turkmenistan", "Mercedes Turkmenistan", "Audi Turkmenistan",
            "Volkswagen Turkmenistan", "Renault Turkmenistan", "Peugeot Turkmenistan", "Citroën Turkmenistan",
            "Lada Turkmenistan", "UAZ Turkmenistan", "GAZ Turkmenistan"
        ],
        "Kyrgyzstan": [
            "Toyota Kyrgyzstan", "Nissan Kyrgyzstan", "Hyundai Kyrgyzstan", "Kia Kyrgyzstan",
            "Ford Kyrgyzstan", "Chevrolet Kyrgyzstan", "Mitsubishi Kyrgyzstan", "Honda Kyrgyzstan",
            "Mazda Kyrgyzstan", "BMW Kyrgyzstan", "Mercedes Kyrgyzstan", "Audi Kyrgyzstan",
            "Volkswagen Kyrgyzstan", "Renault Kyrgyzstan", "Peugeot Kyrgyzstan", "Citroën Kyrgyzstan",
            "Lada Kyrgyzstan", "UAZ Kyrgyzstan", "GAZ Kyrgyzstan"
        ],
        "Tajikistan": [
            "Toyota Tajikistan", "Nissan Tajikistan", "Hyundai Tajikistan", "Kia Tajikistan",
            "Ford Tajikistan", "Chevrolet Tajikistan", "Mitsubishi Tajikistan", "Honda Tajikistan",
            "Mazda Tajikistan", "BMW Tajikistan", "Mercedes Tajikistan", "Audi Tajikistan",
            "Volkswagen Tajikistan", "Renault Tajikistan", "Peugeot Tajikistan", "Citroën Tajikistan",
            "Lada Tajikistan", "UAZ Tajikistan", "GAZ Tajikistan"
        ],
        "Mongolia": [
            "Toyota Mongolia", "Nissan Mongolia", "Hyundai Mongolia", "Kia Mongolia",
            "Ford Mongolia", "Chevrolet Mongolia", "Mitsubishi Mongolia", "Honda Mongolia",
            "Mazda Mongolia", "BMW Mongolia", "Mercedes Mongolia", "Audi Mongolia",
            "Volkswagen Mongolia", "Renault Mongolia", "Peugeot Mongolia", "Citroën Mongolia",
            "Lada Mongolia", "UAZ Mongolia", "GAZ Mongolia", "Great Wall Mongolia"
        ],
        "North Korea": [
            "Pyeonghwa", "Pyongyang", "Sungri", "Taebong", "Paektusan", "Chollima",
            "Kia North Korea", "Hyundai North Korea", "Toyota North Korea", "Nissan North Korea",
            "FAW North Korea", "Dongfeng North Korea", "Chery North Korea", "BYD North Korea"
        ],
        "Myanmar": [
            "Toyota Myanmar", "Nissan Myanmar", "Hyundai Myanmar", "Kia Myanmar",
            "Ford Myanmar", "Chevrolet Myanmar", "Mitsubishi Myanmar", "Honda Myanmar",
            "Mazda Myanmar", "BMW Myanmar", "Mercedes Myanmar", "Audi Myanmar",
            "Suzuki Myanmar", "Isuzu Myanmar", "Hino Myanmar", "Fuso Myanmar", "UD Myanmar"
        ],
        "Laos": [
            "Toyota Laos", "Nissan Laos", "Hyundai Laos", "Kia Laos",
            "Ford Laos", "Chevrolet Laos", "Mitsubishi Laos", "Honda Laos",
            "Mazda Laos", "BMW Laos", "Mercedes Laos", "Audi Laos",
            "Suzuki Laos", "Isuzu Laos", "Hino Laos", "MG Laos", "Chery Laos"
        ],
        "Cambodia": [
            "Toyota Cambodia", "Nissan Cambodia", "Hyundai Cambodia", "Kia Cambodia",
            "Ford Cambodia", "Chevrolet Cambodia", "Mitsubishi Cambodia", "Honda Cambodia",
            "Mazda Cambodia", "BMW Cambodia", "Mercedes Cambodia", "Audi Cambodia",
            "Suzuki Cambodia", "Isuzu Cambodia", "Hino Cambodia", "MG Cambodia", "Chery Cambodia",
            "Great Wall Cambodia", "BYD Cambodia"
        ],
        "Sri Lanka": [
            "Toyota Sri Lanka", "Nissan Sri Lanka", "Hyundai Sri Lanka", "Kia Sri Lanka",
            "Ford Sri Lanka", "Chevrolet Sri Lanka", "Mitsubishi Sri Lanka", "Honda Sri Lanka",
            "Mazda Sri Lanka", "BMW Sri Lanka", "Mercedes Sri Lanka", "Audi Sri Lanka",
            "Suzuki Sri Lanka", "Isuzu Sri Lanka", "Micro Sri Lanka", "Datsun Sri Lanka",
            "Tata Sri Lanka", "Mahindra Sri Lanka", "Ashok Leyland Sri Lanka"
        ],
        "Bangladesh": [
            "Toyota Bangladesh", "Nissan Bangladesh", "Hyundai Bangladesh", "Kia Bangladesh",
            "Ford Bangladesh", "Chevrolet Bangladesh", "Mitsubishi Bangladesh", "Honda Bangladesh",
            "Mazda Bangladesh", "BMW Bangladesh", "Mercedes Bangladesh", "Audi Bangladesh",
            "Suzuki Bangladesh", "Isuzu Bangladesh", "Hino Bangladesh", "Tata Bangladesh",
            "Mahindra Bangladesh", "Ashok Leyland Bangladesh", "Proton Bangladesh"
        ],
        "Nepal": [
            "Toyota Nepal", "Nissan Nepal", "Hyundai Nepal", "Kia Nepal",
            "Ford Nepal", "Chevrolet Nepal", "Mitsubishi Nepal", "Honda Nepal",
            "Mazda Nepal", "BMW Nepal", "Mercedes Nepal", "Audi Nepal",
            "Suzuki Nepal", "Isuzu Nepal", "Tata Nepal", "Mahindra Nepal", "Ashok Leyland Nepal"
        ],
        "Bhutan": [
            "Toyota Bhutan", "Nissan Bhutan", "Hyundai Bhutan", "Kia Bhutan",
            "Ford Bhutan", "Chevrolet Bhutan", "Mitsubishi Bhutan", "Honda Bhutan",
            "Mazda Bhutan", "BMW Bhutan", "Mercedes Bhutan", "Audi Bhutan",
            "Suzuki Bhutan", "Isuzu Bhutan", "Tata Bhutan", "Mahindra Bhutan"
        ],
        "Maldives": [
            "Toyota Maldives", "Nissan Maldives", "Hyundai Maldives", "Kia Maldives",
            "Ford Maldives", "Chevrolet Maldives", "Mitsubishi Maldives", "Honda Maldives",
            "Mazda Maldives", "BMW Maldives", "Mercedes Maldives", "Audi Maldives",
            "Suzuki Maldives", "Isuzu Maldives", "Tata Maldives", "Mahindra Maldives"
        ],
        "Afghanistan": [
            "Toyota Afghanistan", "Nissan Afghanistan", "Hyundai Afghanistan", "Kia Afghanistan",
            "Ford Afghanistan", "Chevrolet Afghanistan", "Mitsubishi Afghanistan", "Honda Afghanistan",
            "Mazda Afghanistan", "BMW Afghanistan", "Mercedes Afghanistan", "Audi Afghanistan",
            "Suzuki Afghanistan", "Isuzu Afghanistan", "Lada Afghanistan", "UAZ Afghanistan"
        ],
        "Pakistan": [
            "Toyota Pakistan", "Nissan Pakistan", "Hyundai Pakistan", "Kia Pakistan",
            "Ford Pakistan", "Chevrolet Pakistan", "Mitsubishi Pakistan", "Honda Pakistan",
            "Mazda Pakistan", "BMW Pakistan", "Mercedes Pakistan", "Audi Pakistan",
            "Suzuki Pakistan", "Isuzu Pakistan", "Hino Pakistan", "Daihatsu Pakistan",
            "United Pakistan", "DYL Pakistan", "Ghandhara Pakistan", "Master Pakistan"
        ],
        "Mauritius": [
            "Toyota Mauritius", "Nissan Mauritius", "Hyundai Mauritius", "Kia Mauritius",
            "Ford Mauritius", "Chevrolet Mauritius", "Mitsubishi Mauritius", "Honda Mauritius",
            "Mazda Mauritius", "BMW Mauritius", "Mercedes Mauritius", "Audi Mauritius",
            "Suzuki Mauritius", "Isuzu Mauritius", "Tata Mauritius", "Mahindra Mauritius",
            "Proton Mauritius", "Chery Mauritius", "Great Wall Mauritius"
        ],
        "Seychelles": [
            "Toyota Seychelles", "Nissan Seychelles", "Hyundai Seychelles", "Kia Seychelles",
            "Ford Seychelles", "Chevrolet Seychelles", "Mitsubishi Seychelles", "Honda Seychelles",
            "Mazda Seychelles", "BMW Seychelles", "Mercedes Seychelles", "Audi Seychelles",
            "Suzuki Seychelles", "Isuzu Seychelles", "Tata Seychelles", "Mahindra Seychelles"
        ],
        "Comoros": [
            "Toyota Comoros", "Nissan Comoros", "Hyundai Comoros", "Kia Comoros",
            "Ford Comoros", "Chevrolet Comoros", "Mitsubishi Comoros", "Honda Comoros",
            "Mazda Comoros", "Suzuki Comoros", "Isuzu Comoros", "Tata Comoros", "Mahindra Comoros"
        ],
        "Madagascar": [
            "Toyota Madagascar", "Nissan Madagascar", "Hyundai Madagascar", "Kia Madagascar",
            "Ford Madagascar", "Chevrolet Madagascar", "Mitsubishi Madagascar", "Honda Madagascar",
            "Mazda Madagascar", "BMW Madagascar", "Mercedes Madagascar", "Audi Madagascar",
            "Suzuki Madagascar", "Isuzu Madagascar", "Tata Madagascar", "Mahindra Madagascar",
            "Renault Madagascar", "Peugeot Madagascar", "Citroën Madagascar"
        ],
        "Angola": [
            "Toyota Angola", "Nissan Angola", "Hyundai Angola", "Kia Angola",
            "Ford Angola", "Chevrolet Angola", "Mitsubishi Angola", "Honda Angola",
            "Mazda Angola", "BMW Angola", "Mercedes Angola", "Audi Angola",
            "Volkswagen Angola", "Renault Angola", "Peugeot Angola", "Citroën Angola",
            "Fiat Angola", "Opel Angola", "Suzuki Angola", "Isuzu Angola", "Hino Angola"
        ],
        "Mozambique": [
            "Toyota Mozambique", "Nissan Mozambique", "Hyundai Mozambique", "Kia Mozambique",
            "Ford Mozambique", "Chevrolet Mozambique", "Mitsubishi Mozambique", "Honda Mozambique",
            "Mazda Mozambique", "BMW Mozambique", "Mercedes Mozambique", "Audi Mozambique",
            "Volkswagen Mozambique", "Renault Mozambique", "Peugeot Mozambique", "Citroën Mozambique",
            "Fiat Mozambique", "Opel Mozambique", "Suzuki Mozambique", "Isuzu Mozambique"
        ],
        "Zambia": [
            "Toyota Zambia", "Nissan Zambia", "Hyundai Zambia", "Kia Zambia",
            "Ford Zambia", "Chevrolet Zambia", "Mitsubishi Zambia", "Honda Zambia",
            "Mazda Zambia", "BMW Zambia", "Mercedes Zambia", "Audi Zambia",
            "Volkswagen Zambia", "Renault Zambia", "Peugeot Zambia", "Citroën Zambia",
            "Fiat Zambia", "Opel Zambia", "Suzuki Zambia", "Isuzu Zambia", "Tata Zambia"
        ],
        "Zimbabwe": [
            "Toyota Zimbabwe", "Nissan Zimbabwe", "Hyundai Zimbabwe", "Kia Zimbabwe",
            "Ford Zimbabwe", "Chevrolet Zimbabwe", "Mitsubishi Zimbabwe", "Honda Zimbabwe",
            "Mazda Zimbabwe", "BMW Zimbabwe", "Mercedes Zimbabwe", "Audi Zimbabwe",
            "Volkswagen Zimbabwe", "Renault Zimbabwe", "Peugeot Zimbabwe", "Citroën Zimbabwe",
            "Fiat Zimbabwe", "Opel Zimbabwe", "Suzuki Zimbabwe", "Isuzu Zimbabwe", "Tata Zimbabwe",
            "Mahindra Zimbabwe", "Ashok Leyland Zimbabwe"
        ],
        "Botswana": [
            "Toyota Botswana", "Nissan Botswana", "Hyundai Botswana", "Kia Botswana",
            "Ford Botswana", "Chevrolet Botswana", "Mitsubishi Botswana", "Honda Botswana",
            "Mazda Botswana", "BMW Botswana", "Mercedes Botswana", "Audi Botswana",
            "Volkswagen Botswana", "Renault Botswana", "Peugeot Botswana", "Citroën Botswana",
            "Fiat Botswana", "Opel Botswana", "Suzuki Botswana", "Isuzu Botswana", "Tata Botswana"
        ],
        "Namibia": [
            "Toyota Namibia", "Nissan Namibia", "Hyundai Namibia", "Kia Namibia",
            "Ford Namibia", "Chevrolet Namibia", "Mitsubishi Namibia", "Honda Namibia",
            "Mazda Namibia", "BMW Namibia", "Mercedes Namibia", "Audi Namibia",
            "Volkswagen Namibia", "Renault Namibia", "Peugeot Namibia", "Citroën Namibia",
            "Fiat Namibia", "Opel Namibia", "Suzuki Namibia", "Isuzu Namibia", "Tata Namibia"
        ],
        "Malawi": [
            "Toyota Malawi", "Nissan Malawi", "Hyundai Malawi", "Kia Malawi",
            "Ford Malawi", "Chevrolet Malawi", "Mitsubishi Malawi", "Honda Malawi",
            "Mazda Malawi", "BMW Malawi", "Mercedes Malawi", "Audi Malawi",
            "Volkswagen Malawi", "Renault Malawi", "Peugeot Malawi", "Citroën Malawi",
            "Fiat Malawi", "Opel Malawi", "Suzuki Malawi", "Isuzu Malawi", "Tata Malawi"
        ],
        "Tanzania": [
            "Toyota Tanzania", "Nissan Tanzania", "Hyundai Tanzania", "Kia Tanzania",
            "Ford Tanzania", "Chevrolet Tanzania", "Mitsubishi Tanzania", "Honda Tanzania",
            "Mazda Tanzania", "BMW Tanzania", "Mercedes Tanzania", "Audi Tanzania",
            "Volkswagen Tanzania", "Renault Tanzania", "Peugeot Tanzania", "Citroën Tanzania",
            "Fiat Tanzania", "Opel Tanzania", "Suzuki Tanzania", "Isuzu Tanzania", "Tata Tanzania",
            "Mahindra Tanzania", "Ashok Leyland Tanzania"
        ],
        "Uganda": [
            "Toyota Uganda", "Nissan Uganda", "Hyundai Uganda", "Kia Uganda",
            "Ford Uganda", "Chevrolet Uganda", "Mitsubishi Uganda", "Honda Uganda",
            "Mazda Uganda", "BMW Uganda", "Mercedes Uganda", "Audi Uganda",
            "Volkswagen Uganda", "Renault Uganda", "Peugeot Uganda", "Citroën Uganda",
            "Fiat Uganda", "Opel Uganda", "Suzuki Uganda", "Isuzu Uganda", "Tata Uganda",
            "Mahindra Uganda", "Ashok Leyland Uganda", "Kiira Uganda"
        ],
        "Rwanda": [
            "Toyota Rwanda", "Nissan Rwanda", "Hyundai Rwanda", "Kia Rwanda",
            "Ford Rwanda", "Chevrolet Rwanda", "Mitsubishi Rwanda", "Honda Rwanda",
            "Mazda Rwanda", "BMW Rwanda", "Mercedes Rwanda", "Audi Rwanda",
            "Volkswagen Rwanda", "Renault Rwanda", "Peugeot Rwanda", "Citroën Rwanda",
            "Fiat Rwanda", "Opel Rwanda", "Suzuki Rwanda", "Isuzu Rwanda", "Tata Rwanda",
            "Mahindra Rwanda"
        ],
        "Burundi": [
            "Toyota Burundi", "Nissan Burundi", "Hyundai Burundi", "Kia Burundi",
            "Ford Burundi", "Chevrolet Burundi", "Mitsubishi Burundi", "Honda Burundi",
            "Mazda Burundi", "BMW Burundi", "Mercedes Burundi", "Audi Burundi",
            "Volkswagen Burundi", "Renault Burundi", "Peugeot Burundi", "Citroën Burundi",
            "Fiat Burundi", "Opel Burundi", "Suzuki Burundi", "Isuzu Burundi", "Tata Burundi"
        ],
        "Ethiopia": [
            "Toyota Ethiopia", "Nissan Ethiopia", "Hyundai Ethiopia", "Kia Ethiopia",
            "Ford Ethiopia", "Chevrolet Ethiopia", "Mitsubishi Ethiopia", "Honda Ethiopia",
            "Mazda Ethiopia", "BMW Ethiopia", "Mercedes Ethiopia", "Audi Ethiopia",
            "Volkswagen Ethiopia", "Renault Ethiopia", "Peugeot Ethiopia", "Citroën Ethiopia",
            "Fiat Ethiopia", "Opel Ethiopia", "Suzuki Ethiopia", "Isuzu Ethiopia", "Tata Ethiopia",
            "Mahindra Ethiopia", "Holland Ethiopia", "Marathon Ethiopia"
        ],
        "Eritrea": [
            "Toyota Eritrea", "Nissan Eritrea", "Hyundai Eritrea", "Kia Eritrea",
            "Ford Eritrea", "Chevrolet Eritrea", "Mitsubishi Eritrea", "Honda Eritrea",
            "Mazda Eritrea", "BMW Eritrea", "Mercedes Eritrea", "Audi Eritrea",
            "Volkswagen Eritrea", "Renault Eritrea", "Peugeot Eritrea", "Citroën Eritrea",
            "Fiat Eritrea", "Opel Eritrea", "Suzuki Eritrea", "Isuzu Eritrea", "Lada Eritrea"
        ],
        "Djibouti": [
            "Toyota Djibouti", "Nissan Djibouti", "Hyundai Djibouti", "Kia Djibouti",
            "Ford Djibouti", "Chevrolet Djibouti", "Mitsubishi Djibouti", "Honda Djibouti",
            "Mazda Djibouti", "BMW Djibouti", "Mercedes Djibouti", "Audi Djibouti",
            "Volkswagen Djibouti", "Renault Djibouti", "Peugeot Djibouti", "Citroën Djibouti",
            "Fiat Djibouti", "Opel Djibouti", "Suzuki Djibouti", "Isuzu Djibouti"
        ],
        "Somalia": [
            "Toyota Somalia", "Nissan Somalia", "Hyundai Somalia", "Kia Somalia",
            "Ford Somalia", "Chevrolet Somalia", "Mitsubishi Somalia", "Honda Somalia",
            "Mazda Somalia", "BMW Somalia", "Mercedes Somalia", "Audi Somalia",
            "Volkswagen Somalia", "Renault Somalia", "Peugeot Somalia", "Citroën Somalia",
            "Fiat Somalia", "Opel Somalia", "Suzuki Somalia", "Isuzu Somalia", "Lada Somalia"
        ],
        "Sudan": [
            "Toyota Sudan", "Nissan Sudan", "Hyundai Sudan", "Kia Sudan",
            "Ford Sudan", "Chevrolet Sudan", "Mitsubishi Sudan", "Honda Sudan",
            "Mazda Sudan", "BMW Sudan", "Mercedes Sudan", "Audi Sudan",
            "Volkswagen Sudan", "Renault Sudan", "Peugeot Sudan", "Citroën Sudan",
            "Fiat Sudan", "Opel Sudan", "Suzuki Sudan", "Isuzu Sudan", "Lada Sudan",
            "GAZ Sudan", "UAZ Sudan", "ZNA Sudan", "Giad Sudan"
        ],
        "South Sudan": [
            "Toyota South Sudan", "Nissan South Sudan", "Hyundai South Sudan", "Kia South Sudan",
            "Ford South Sudan", "Chevrolet South Sudan", "Mitsubishi South Sudan", "Honda South Sudan",
            "Mazda South Sudan", "BMW South Sudan", "Mercedes South Sudan", "Audi South Sudan",
            "Volkswagen South Sudan", "Renault South Sudan", "Peugeot South Sudan", "Citroën South Sudan",
            "Fiat South Sudan", "Opel South Sudan", "Suzuki South Sudan", "Isuzu South Sudan",
            "Toyota South Sudan", "Nissan South Sudan", "Hyundai South Sudan", "Kia South Sudan"
        ],
        "Senegal": [
            "Toyota Senegal", "Nissan Senegal", "Hyundai Senegal", "Kia Senegal",
            "Ford Senegal", "Chevrolet Senegal", "Mitsubishi Senegal", "Honda Senegal",
            "Mazda Senegal", "BMW Senegal", "Mercedes Senegal", "Audi Senegal",
            "Volkswagen Senegal", "Renault Senegal", "Peugeot Senegal", "Citroën Senegal",
            "Fiat Senegal", "Opel Senegal", "Suzuki Senegal", "Isuzu Senegal", "Dacia Senegal"
        ],
        "Mali": [
            "Toyota Mali", "Nissan Mali", "Hyundai Mali", "Kia Mali",
            "Ford Mali", "Chevrolet Mali", "Mitsubishi Mali", "Honda Mali",
            "Mazda Mali", "BMW Mali", "Mercedes Mali", "Audi Mali",
            "Volkswagen Mali", "Renault Mali", "Peugeot Mali", "Citroën Mali",
            "Fiat Mali", "Opel Mali", "Suzuki Mali", "Isuzu Mali", "Dacia Mali"
        ],
        "Burkina Faso": [
            "Toyota Burkina", "Nissan Burkina", "Hyundai Burkina", "Kia Burkina",
            "Ford Burkina", "Chevrolet Burkina", "Mitsubishi Burkina", "Honda Burkina",
            "Mazda Burkina", "BMW Burkina", "Mercedes Burkina", "Audi Burkina",
            "Volkswagen Burkina", "Renault Burkina", "Peugeot Burkina", "Citroën Burkina",
            "Fiat Burkina", "Opel Burkina", "Suzuki Burkina", "Isuzu Burkina"
        ],
        "Niger": [
            "Toyota Niger", "Nissan Niger", "Hyundai Niger", "Kia Niger",
            "Ford Niger", "Chevrolet Niger", "Mitsubishi Niger", "Honda Niger",
            "Mazda Niger", "BMW Niger", "Mercedes Niger", "Audi Niger",
            "Volkswagen Niger", "Renault Niger", "Peugeot Niger", "Citroën Niger",
            "Fiat Niger", "Opel Niger", "Suzuki Niger", "Isuzu Niger"
        ],
        "Chad": [
            "Toyota Chad", "Nissan Chad", "Hyundai Chad", "Kia Chad",
            "Ford Chad", "Chevrolet Chad", "Mitsubishi Chad", "Honda Chad",
            "Mazda Chad", "BMW Chad", "Mercedes Chad", "Audi Chad",
            "Volkswagen Chad", "Renault Chad", "Peugeot Chad", "Citroën Chad",
            "Fiat Chad", "Opel Chad", "Suzuki Chad", "Isuzu Chad"
        ],
        "Cameroon": [
            "Toyota Cameroon", "Nissan Cameroon", "Hyundai Cameroon", "Kia Cameroon",
            "Ford Cameroon", "Chevrolet Cameroon", "Mitsubishi Cameroon", "Honda Cameroon",
            "Mazda Cameroon", "BMW Cameroon", "Mercedes Cameroon", "Audi Cameroon",
            "Volkswagen Cameroon", "Renault Cameroon", "Peugeot Cameroon", "Citroën Cameroon",
            "Fiat Cameroon", "Opel Cameroon", "Suzuki Cameroon", "Isuzu Cameroon"
        ],
        "Central African Republic": [
            "Toyota CAR", "Nissan CAR", "Hyundai CAR", "Kia CAR",
            "Ford CAR", "Chevrolet CAR", "Mitsubishi CAR", "Honda CAR",
            "Mazda CAR", "BMW CAR", "Mercedes CAR", "Audi CAR",
            "Volkswagen CAR", "Renault CAR", "Peugeot CAR", "Citroën CAR",
            "Fiat CAR", "Opel CAR", "Suzuki CAR", "Isuzu CAR"
        ],
        "Equatorial Guinea": [
            "Toyota Equatorial", "Nissan Equatorial", "Hyundai Equatorial", "Kia Equatorial",
            "Ford Equatorial", "Chevrolet Equatorial", "Mitsubishi Equatorial", "Honda Equatorial",
            "Mazda Equatorial", "BMW Equatorial", "Mercedes Equatorial", "Audi Equatorial",
            "Volkswagen Equatorial", "Renault Equatorial", "Peugeot Equatorial", "Citroën Equatorial",
            "Fiat Equatorial", "Opel Equatorial", "Suzuki Equatorial", "Isuzu Equatorial"
        ],
        "Gabon": [
            "Toyota Gabon", "Nissan Gabon", "Hyundai Gabon", "Kia Gabon",
            "Ford Gabon", "Chevrolet Gabon", "Mitsubishi Gabon", "Honda Gabon",
            "Mazda Gabon", "BMW Gabon", "Mercedes Gabon", "Audi Gabon",
            "Volkswagen Gabon", "Renault Gabon", "Peugeot Gabon", "Citroën Gabon",
            "Fiat Gabon", "Opel Gabon", "Suzuki Gabon", "Isuzu Gabon"
        ],
        "Congo": [
            "Toyota Congo", "Nissan Congo", "Hyundai Congo", "Kia Congo",
            "Ford Congo", "Chevrolet Congo", "Mitsubishi Congo", "Honda Congo",
            "Mazda Congo", "BMW Congo", "Mercedes Congo", "Audi Congo",
            "Volkswagen Congo", "Renault Congo", "Peugeot Congo", "Citroën Congo",
            "Fiat Congo", "Opel Congo", "Suzuki Congo", "Isuzu Congo"
        ],
        "DRC": [
            "Toyota DRC", "Nissan DRC", "Hyundai DRC", "Kia DRC",
            "Ford DRC", "Chevrolet DRC", "Mitsubishi DRC", "Honda DRC",
            "Mazda DRC", "BMW DRC", "Mercedes DRC", "Audi DRC",
            "Volkswagen DRC", "Renault DRC", "Peugeot DRC", "Citroën DRC",
            "Fiat DRC", "Opel DRC", "Suzuki DRC", "Isuzu DRC"
        ],
        "Mauritania": [
            "Toyota Mauritania", "Nissan Mauritania", "Hyundai Mauritania", "Kia Mauritania",
            "Ford Mauritania", "Chevrolet Mauritania", "Mitsubishi Mauritania", "Honda Mauritania",
            "Mazda Mauritania", "BMW Mauritania", "Mercedes Mauritania", "Audi Mauritania",
            "Volkswagen Mauritania", "Renault Mauritania", "Peugeot Mauritania", "Citroën Mauritania",
            "Fiat Mauritania", "Opel Mauritania", "Suzuki Mauritania", "Isuzu Mauritania"
        ],
        "Liberia": [
            "Toyota Liberia", "Nissan Liberia", "Hyundai Liberia", "Kia Liberia",
            "Ford Liberia", "Chevrolet Liberia", "Mitsubishi Liberia", "Honda Liberia",
            "Mazda Liberia", "BMW Liberia", "Mercedes Liberia", "Audi Liberia",
            "Volkswagen Liberia", "Renault Liberia", "Peugeot Liberia", "Citroën Liberia",
            "Fiat Liberia", "Opel Liberia", "Suzuki Liberia", "Isuzu Liberia"
        ],
        "Sierra Leone": [
            "Toyota Sierra Leone", "Nissan Sierra Leone", "Hyundai Sierra Leone", "Kia Sierra Leone",
            "Ford Sierra Leone", "Chevrolet Sierra Leone", "Mitsubishi Sierra Leone", "Honda Sierra Leone",
            "Mazda Sierra Leone", "BMW Sierra Leone", "Mercedes Sierra Leone", "Audi Sierra Leone",
            "Volkswagen Sierra Leone", "Renault Sierra Leone", "Peugeot Sierra Leone", "Citroën Sierra Leone",
            "Fiat Sierra Leone", "Opel Sierra Leone", "Suzuki Sierra Leone", "Isuzu Sierra Leone"
        ],
        "Guinea": [
            "Toyota Guinea", "Nissan Guinea", "Hyundai Guinea", "Kia Guinea",
            "Ford Guinea", "Chevrolet Guinea", "Mitsubishi Guinea", "Honda Guinea",
            "Mazda Guinea", "BMW Guinea", "Mercedes Guinea", "Audi Guinea",
            "Volkswagen Guinea", "Renault Guinea", "Peugeot Guinea", "Citroën Guinea",
            "Fiat Guinea", "Opel Guinea", "Suzuki Guinea", "Isuzu Guinea"
        ],
        "Guinea-Bissau": [
            "Toyota Guinea-Bissau", "Nissan Guinea-Bissau", "Hyundai Guinea-Bissau", "Kia Guinea-Bissau",
            "Ford Guinea-Bissau", "Chevrolet Guinea-Bissau", "Mitsubishi Guinea-Bissau", "Honda Guinea-Bissau",
            "Mazda Guinea-Bissau", "BMW Guinea-Bissau", "Mercedes Guinea-Bissau", "Audi Guinea-Bissau",
            "Volkswagen Guinea-Bissau", "Renault Guinea-Bissau", "Peugeot Guinea-Bissau", "Citroën Guinea-Bissau",
            "Fiat Guinea-Bissau", "Opel Guinea-Bissau", "Suzuki Guinea-Bissau", "Isuzu Guinea-Bissau"
        ],
        "Ivory Coast": [
            "Toyota Ivory Coast", "Nissan Ivory Coast", "Hyundai Ivory Coast", "Kia Ivory Coast",
            "Ford Ivory Coast", "Chevrolet Ivory Coast", "Mitsubishi Ivory Coast", "Honda Ivory Coast",
            "Mazda Ivory Coast", "BMW Ivory Coast", "Mercedes Ivory Coast", "Audi Ivory Coast",
            "Volkswagen Ivory Coast", "Renault Ivory Coast", "Peugeot Ivory Coast", "Citroën Ivory Coast",
            "Fiat Ivory Coast", "Opel Ivory Coast", "Suzuki Ivory Coast", "Isuzu Ivory Coast"
        ],
        "Ghana": [
            "Toyota Ghana", "Nissan Ghana", "Hyundai Ghana", "Kia Ghana",
            "Ford Ghana", "Chevrolet Ghana", "Mitsubishi Ghana", "Honda Ghana",
            "Mazda Ghana", "BMW Ghana", "Mercedes Ghana", "Audi Ghana",
            "Volkswagen Ghana", "Renault Ghana", "Peugeot Ghana", "Citroën Ghana",
            "Fiat Ghana", "Opel Ghana", "Suzuki Ghana", "Isuzu Ghana", "Tata Ghana",
            "Mahindra Ghana", "Ashok Leyland Ghana", "Sinotruk Ghana", "FAW Ghana"
        ],
        "Togo": [
            "Toyota Togo", "Nissan Togo", "Hyundai Togo", "Kia Togo",
            "Ford Togo", "Chevrolet Togo", "Mitsubishi Togo", "Honda Togo",
            "Mazda Togo", "BMW Togo", "Mercedes Togo", "Audi Togo",
            "Volkswagen Togo", "Renault Togo", "Peugeot Togo", "Citroën Togo",
            "Fiat Togo", "Opel Togo", "Suzuki Togo", "Isuzu Togo"
        ],
        "Benin": [
            "Toyota Benin", "Nissan Benin", "Hyundai Benin", "Kia Benin",
            "Ford Benin", "Chevrolet Benin", "Mitsubishi Benin", "Honda Benin",
            "Mazda Benin", "BMW Benin", "Mercedes Benin", "Audi Benin",
            "Volkswagen Benin", "Renault Benin", "Peugeot Benin", "Citroën Benin",
            "Fiat Benin", "Opel Benin", "Suzuki Benin", "Isuzu Benin"
        ]
    }

    # Define engine types, transmissions, etc.
    engine_types = [
        "1.0L I3", "1.2L I3", "1.4L I4", "1.6L I4", "1.8L I4", "2.0L I4", "2.2L I4", "2.4L I4", "2.5L I4",
        "2.0L Turbo I4", "2.3L Turbo I4", "2.5L Turbo I4", "1.5L I4 Turbo", "1.6L I4 Turbo",
        "2.7L V6", "3.0L V6", "3.2L V6", "3.3L V6", "3.5L V6", "3.7L V6", "3.8L V6", "4.0L V6",
        "3.0L Turbo V6", "3.5L Turbo V6", "3.8L Turbo V6",
        "4.6L V8", "5.0L V8", "5.3L V8", "5.7L V8", "6.0L V8", "6.2L V8", "6.4L V8",
        "4.4L Turbo V8", "5.0L Turbo V8", "6.2L Supercharged V8", "6.8L V10", "8.0L V10",
        "5.2L V10", "6.5L V12", "6.8L V12", "7.3L V12", "Electric Motor", "Dual Motor Electric",
        "Tri-Motor Electric", "Quad-Motor Electric", "Hydrogen Fuel Cell", "Hybrid", "Plug-in Hybrid"
    ]

    # Body styles
    body_styles = [
        "Sedan", "Coupe", "Convertible", "Hatchback", "SUV", "Crossover", "Pickup Truck",
        "Minivan", "Van", "Wagon", "Sports Car", "Supercar", "Hypercar", "Muscle Car",
        "Off-Road", "Luxury", "Executive", "Compact", "Subcompact", "Midsize", "Full-size",
        "Roadster", "Targa", "Fastback", "Liftback", "Shooting Brake", "MPV", "Limousine"
    ]

    # Colors
    colors = ["Red", "Blue", "Black", "White", "Silver", "Gray", "Green", "Yellow", "Orange", 
              "Purple", "Brown", "Gold", "Cyan", "Magenta", "Lime", "Teal", "Maroon", "Navy",
              "Burgundy", "Charcoal", "Champagne", "Bronze", "Copper", "Beige", "Cream", "Ivory",
              "Pearl", "Matte Black", "Matte Gray", "Matte Blue", "Matte Red", "Metallic Silver",
              "Metallic Blue", "Metallic Red", "Metallic Gray", "Midnight Blue", "Midnight Black",
              "Sunset Orange", "Sunrise Yellow", "Forest Green", "Ocean Blue", "Volcano Red",
              "Arctic White", "Glacier Silver", "Desert Sand", "Sahara Beige", "Tundra Brown"]

    # AI levels
    ai_levels = [
        "Level 1 Driver Assist", "Level 2 Autopilot", "Level 2+ Highway Assist",
        "Level 3 Traffic Jam Pilot", "Level 3 Highway Autopilot", "Level 4 Urban Autonomy",
        "Full Self-Driving (Level 2+)", "Level 1 Park Assist", "Level 2+ Nav Assist",
        "Level 3 Autonomy", "Level 1 Safety", "Level 2 Safety Sense", "Level 2+ Safety",
        "Level 3 Safety", "Level 1 Track Assist", "Level 2 Terrain Assist", "Level 1 Drag Assist"
    ]

    # Holographic colors
    holographic_colors = [
        "Neon Red", "Electric Blue", "Neon Green", "Plasma Purple", "Inferno Orange",
        "Arctic White", "Cyber Yellow", "Quantum Pink", "Laser Violet", "Photon Cyan",
        "Holographic Silver", "Iridescent", "Chameleon", "Prismatic", "Aurora",
        "Nebula", "Galaxy", "Cosmic", "Stellar", "Nova", "Pulsar", "Quasar"
    ]

    # Generate cars
    print(f"Generating {target_count} cars... This may take a few minutes.")
    cars = []
    countries = list(manufacturers.keys())
    
    while len(cars) < target_count:
        # Pick a random country and manufacturer
        country = random.choice(countries)
        make = random.choice(manufacturers[country])
        
        # Generate multiple models per manufacturer
        num_models = random.randint(5, 20)
        for _ in range(num_models):
            if len(cars) >= target_count:
                break
                
            # Model name variations
            model_prefixes = ["", "Super", "Sport", "Ultra", "GT", "RS", "S", "R", "Performance",
                            "Elite", "Premium", "Luxury", "Limited", "Special", "Edition"]
            model_suffixes = ["", "Plus", "Pro", "Max", "X", "Z", "Alpha", "Beta", "Gamma",
                            "Delta", "Epsilon", "Omega", "Sigma", "Lambda"]
            
            model_base = f"{make} {random.choice(['Series', 'Class', 'Line', 'Model', ''])}"
            prefix = random.choice(model_prefixes)
            suffix = random.choice(model_suffixes)
            
            if prefix:
                model = f"{prefix} {model_base}"
            else:
                model = model_base
            
            if suffix and random.random() > 0.5:
                model = f"{model} {suffix}"
            
            # Random year
            year = random.randint(1990, 2025)
            
            # Generate specs
            engine = random.choice(engine_types)
            horsepower = random.randint(50, 1500)
            torque = int(horsepower * random.uniform(0.7, 1.3))
            
            drivetrain = random.choice(["FWD", "RWD", "AWD", "4WD"])
            transmission = random.choice(["5-speed manual", "6-speed manual", "7-speed manual",
                                         "4-speed auto", "5-speed auto", "6-speed auto",
                                         "8-speed auto", "10-speed auto", "CVT",
                                         "7-speed dual-clutch", "8-speed dual-clutch"])
            
            acceleration = round(random.uniform(1.5, 12.0), 1)
            top_speed = random.randint(80, 250)
            fuel_economy = random.randint(10, 120)
            price = random.randint(5000, 3000000)
            
            ai = random.choice(ai_levels)
            holo = random.choice(holographic_colors)
            color = random.choice(colors)
            body_style = random.choice(body_styles)
            
            # Create description
            description = f"The {year} {make} {model} is a {color.lower()} {body_style.lower()} " + \
                         f"featuring a {engine} engine producing {horsepower} hp and {torque} lb-ft of torque. " + \
                         f"It can accelerate from 0-60 mph in {acceleration} seconds and reach a top speed of " + \
                         f"{top_speed} mph. With {fuel_economy} mpg combined fuel economy and a starting price of " + \
                         f"${price:,}, it represents {make}'s commitment to {random.choice(['performance', 'luxury', 'efficiency', 'versatility', 'innovation'])}."
            
            car = Car(
                make=make, model=model, year=year, color=color, engine=engine,
                horsepower=horsepower, torque=torque, drivetrain=drivetrain,
                transmission=transmission, acceleration=acceleration, top_speed=top_speed,
                fuel_economy=fuel_economy, price=price, ai_level=ai, holographic_color=holo,
                description=description, country=country, body_style=body_style,
                fuel_type=random.choice(["Gasoline", "Diesel", "Electric", "Hybrid", "Plug-in Hybrid"]),
                seats=random.randint(2, 9), doors=random.randint(2, 5), msrp=price
            )
            cars.append(car)
    
    return cars

def create_initial_cars():
    """Create the initial list of special cars."""
    return [
        Car("Dodge", "Charger", 2020, "Red",
            "6.2L Supercharged HEMI V8", 707, 650,
            "RWD", "8-speed automatic", 3.6, 196, 15, 72000,
            "Level 2 Autopilot", "Neon Red",
            "The Dodge Charger SRT Hellcat is a high-performance muscle car with aggressive styling and blistering speed. It combines modern technology with classic American muscle.",
            "USA", "Muscle Car", "Sedan", 4575, 198, 78, 58, 120),
        Car("Dodge", "Durango", 2022, "Black",
            "5.7L HEMI V8", 360, 390,
            "AWD", "8-speed automatic", 6.2, 145, 19, 52000,
            "Level 1 Driver Assist", "Shadow Black",
            "The Durango is a versatile SUV that offers three rows of seating and powerful engine options. It blends utility with Dodge's signature performance attitude.",
            "USA", "SUV", "SUV", 5320, 201, 76, 71, 120),
        Car("Toyota", "Camry", 2021, "Silver",
            "2.5L 4-Cylinder", 203, 184,
            "FWD", "8-speed automatic", 7.2, 135, 32, 26000,
            "Level 2 Safety Sense", "Arctic Silver",
            "The Toyota Camry is a reliable and fuel-efficient midsize sedan known for its comfort, safety features, and long-lasting quality.",
            "Japan", "Sedan", "Sedan", 3310, 192, 72, 57, 111),
        Car("Toyota", "Corolla", 2023, "White",
            "1.8L 4-Cylinder", 139, 126,
            "FWD", "CVT", 8.5, 120, 35, 21000,
            "Level 1 Safety", "Pearl White",
            "The Corolla is a compact car that delivers excellent fuel economy and a reputation for durability. It's practical, affordable, and comes with Toyota Safety Sense.",
            "Japan", "Compact", "Sedan", 2900, 182, 70, 57, 106),
        Car("BMW", "3 Series", 2022, "Blue",
            "2.0L TwinPower Turbo", 255, 294,
            "RWD", "8-speed automatic", 5.4, 155, 30, 43000,
            "Level 3 Highway Autopilot", "Electric Blue",
            "The BMW 3 Series is the benchmark for luxury sport sedans. It offers precise handling, a refined interior, and advanced technology.",
            "Germany", "Luxury", "Sedan", 3571, 185, 72, 57, 112),
        Car("BMW", "X5", 2021, "Gray",
            "3.0L TwinPower Turbo", 335, 330,
            "AWD", "8-speed automatic", 5.3, 155, 24, 61000,
            "Level 3 Autonomy", "Titanium Gray",
            "The X5 is a midsize luxury SUV that combines on-road comfort with off-road capability. It features a plush cabin, powerful engines, and the latest iDrive system.",
            "Germany", "Luxury SUV", "SUV", 4920, 194, 79, 69, 117),
        Car("Audi", "A4", 2023, "Black",
            "2.0L TFSI", 201, 236,
            "Quattro", "7-speed dual-clutch", 6.3, 130, 28, 40000,
            "Level 2 Adaptive Cruise", "Mythos Black",
            "The Audi A4 is a sophisticated compact executive sedan. It offers a quiet, high-tech interior, Quattro all-wheel drive, and a balance of performance and efficiency.",
            "Germany", "Luxury", "Sedan", 3638, 187, 73, 56, 111),
        Car("Audi", "Q5", 2022, "White",
            "2.0L TFSI mild hybrid", 261, 273,
            "Quattro", "7-speed dual-clutch", 5.6, 135, 25, 45000,
            "Level 2+ Autonomy", "Glacier White",
            "The Q5 is a popular luxury SUV that excels in comfort and technology. It provides a smooth ride, upscale interior, and available plug-in hybrid variant.",
            "Germany", "Luxury SUV", "SUV", 4068, 184, 74, 65, 111),
        Car("Lamborghini", "Aventador", 2021, "Yellow",
            "6.5L V12", 769, 531,
            "AWD", "7-speed ISR", 2.9, 217, 11, 500000,
            "Level 1 Track Assist", "Giallo Orion",
            "The Aventador is Lamborghini's flagship V12 supercar. With its sharp design, scissor doors, and exhilarating performance, it represents the pinnacle of Italian exotic engineering.",
            "Italy", "Supercar", "Coupe", 3472, 189, 80, 44, 106),
        Car("Lamborghini", "Urus", 2023, "Orange",
            "4.0L Twin-Turbo V8", 641, 627,
            "AWD", "8-speed automatic", 3.2, 190, 15, 230000,
            "Level 2 Terrain Assist", "Arancio Borealis",
            "The Urus is the world's first Super Sport Utility Vehicle. It combines the soul of a supercar with the practicality of an SUV, offering breathtaking performance and luxury.",
            "Italy", "Super SUV", "SUV", 4850, 201, 79, 64, 118),
        Car("BMW", "M3 Competition", 2023, "Brooklyn Grey",
            "3.0L Twin-Turbo I6", 503, 479,
            "RWD", "8-speed automatic", 3.8, 155, 19, 76000,
            "Level 2 Driving Assistant", "Neon Grey",
            "The BMW M3 Competition is a high-performance sports sedan that combines track-focused capability with everyday usability.",
            "Germany", "Sports Sedan", "Sedan", 3840, 189, 74, 56, 112),
        Car("Tesla", "Model X Plaid", 2023, "Midnight Silver",
            "Tri-Motor Electric", 1020, 1050,
            "AWD", "Single-speed", 2.5, 163, 102, 110000,
            "Full Self-Driving (Level 2+)", "Electric Blue",
            "The Tesla Model X Plaid is an all-electric luxury SUV with breathtaking performance and cutting-edge technology. Its falcon-wing doors and industry-leading range make it a futuristic family hauler.",
            "USA", "Electric SUV", "SUV", 5390, 199, 89, 66, 116),
        Car("Dodge", "Challenger SRT Demon 170", 2023, "Plum Crazy",
            "6.2L Supercharged HEMI V8 (E85)", 1025, 945,
            "RWD", "8-speed automatic", 1.66, 140, 13, 100000,
            "Level 1 Drag Assist", "Inferno Red",
            "The Dodge Challenger SRT Demon 170 is the ultimate factory drag car. With up to 1,025 horsepower on E85, it's the most powerful muscle car ever produced.",
            "USA", "Muscle Car", "Coupe", 4275, 197, 76, 57, 116)
    ]

def load_cars_from_json(filename="car_database.json"):
    """Load car list from a JSON file."""
    if os.path.exists(filename):
        try:
            with open(filename, "r", encoding='utf-8') as f:
                data = json.load(f)
            cars = [Car.from_dict(item) for item in data]
            print(f"Loaded {len(cars)} cars from {filename}")
            return cars
        except Exception as e:
            print(f"Error loading {filename}: {e}")
            print("Generating new database...")
    
    # Generate new database
    print("Creating massive car database (this will take a few minutes)...")
    initial_cars = create_initial_cars()
    generated_cars = generate_massive_database(100000 - len(initial_cars))
    all_cars = initial_cars + generated_cars
    
    # Save to JSON
    data = [car.to_dict() for car in all_cars]
    with open(filename, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Saved {len(all_cars)} cars to {filename}")
    
    return all_cars

class NeonCarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("NEON CAR DATABASE 3000 - ULTIMATE EDITION")
        self.root.geometry("1400x850")
        self.root.configure(bg="#0a0f0f")

        # Futuristic fonts
        self.title_font = tkfont.Font(family="Courier New", size=24, weight="bold")
        self.header_font = tkfont.Font(family="Courier New", size=16, weight="bold")
        self.label_font = tkfont.Font(family="Consolas", size=11)
        self.value_font = tkfont.Font(family="Consolas", size=11)

        # Neon colors
        self.bg_dark = "#0a0f0f"
        self.neon_green = "#00ff9d"
        self.neon_pink = "#ff00c1"
        self.neon_cyan = "#00f3ff"
        self.neon_yellow = "#f0e68c"
        self.neon_purple = "#bf00ff"
        self.text_light = "#e0e0e0"
        self.panel_bg = "#1a1f1f"
        self.entry_bg = "#252b2b"

        # Load cars (with progress indicator)
        self.loading_label = tk.Label(
            self.root,
            text="LOADING 100,000+ VEHICLES... PLEASE WAIT...",
            font=self.header_font,
            bg=self.bg_dark,
            fg=self.neon_yellow
        )
        self.loading_label.pack(expand=True)
        self.root.update()
        
        self.cars = load_cars_from_json()
        
        self.loading_label.destroy()

        # Build UI
        self.create_header()
        self.create_main_panels()
        self.create_status_bar()
        self.create_search_bar()
        self.populate_listbox()

        # Start animations
        self.pulse_header()

    def create_header(self):
        header_frame = tk.Frame(self.root, bg=self.bg_dark, height=100)
        header_frame.pack(fill=tk.X, side=tk.TOP)
        header_frame.pack_propagate(False)

        # Animated title
        self.title_label = tk.Label(
            header_frame,
            text="⚡ ULTIMATE CAR DATABASE 3000 ⚡",
            font=self.title_font,
            bg=self.bg_dark,
            fg=self.neon_green
        )
        self.title_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Neon line
        canvas = tk.Canvas(header_frame, bg=self.bg_dark, height=4, highlightthickness=0)
        canvas.pack(fill=tk.X, side=tk.BOTTOM)
        canvas.create_line(0, 2, 1400, 2, fill=self.neon_cyan, width=4)

    def create_search_bar(self):
        search_frame = tk.Frame(self.root, bg=self.bg_dark, height=50)
        search_frame.pack(fill=tk.X, side=tk.TOP, padx=15, pady=(5,0))

        tk.Label(
            search_frame,
            text="🔍 SEARCH:",
            font=self.label_font,
            bg=self.bg_dark,
            fg=self.neon_cyan
        ).pack(side=tk.LEFT, padx=(0,10))

        self.search_var = tk.StringVar()
        self.search_var.trace('w', self.filter_cars)
        
        search_entry = tk.Entry(
            search_frame,
            textvariable=self.search_var,
            font=self.label_font,
            bg=self.entry_bg,
            fg=self.text_light,
            insertbackground=self.neon_cyan,
            width=40,
            bd=0,
            highlightthickness=1,
            highlightbackground=self.neon_cyan
        )
        search_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

    def filter_cars(self, *args):
        search_term = self.search_var.get().lower()
        self.listbox.delete(0, tk.END)
        
        for car in self.cars:
            if search_term in car.display_name().lower() or search_term in car.make.lower():
                self.listbox.insert(tk.END, car.display_name())

    def create_main_panels(self):
        main_container = tk.Frame(self.root, bg=self.bg_dark)
        main_container.pack(fill=tk.BOTH, expand=True, padx=15, pady=10)

        # Left panel
        left_panel = tk.Frame(main_container, bg=self.panel_bg, width=400)
        left_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=False, padx=(0,15))
        left_panel.pack_propagate(False)
        left_panel.config(highlightbackground=self.neon_green, highlightthickness=2, bd=0)

        list_title = tk.Label(
            left_panel,
            text=f"[ CAR ARCHIVE - {len(self.cars):,} VEHICLES ]",
            font=self.header_font,
            bg=self.panel_bg,
            fg=self.neon_green
        )
        list_title.pack(anchor=tk.W, pady=(10,5), padx=10)

        # Listbox with scrollbar
        list_frame = tk.Frame(left_panel, bg=self.panel_bg)
        list_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0,10))

        scrollbar = tk.Scrollbar(list_frame, bg=self.panel_bg, troughcolor=self.entry_bg,
                                 activebackground=self.neon_green, elementborderwidth=0)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.listbox = tk.Listbox(
            list_frame,
            yscrollcommand=scrollbar.set,
            font=self.label_font,
            bg=self.entry_bg,
            fg=self.neon_cyan,
            selectbackground=self.neon_green,
            selectforeground=self.bg_dark,
            bd=0,
            highlightthickness=0
        )
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.listbox.yview)
        self.listbox.bind('<<ListboxSelect>>', self.on_select)

        # Right panel
        right_panel = tk.Frame(main_container, bg=self.panel_bg)
        right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        right_panel.config(highlightbackground=self.neon_pink, highlightthickness=2, bd=0)

        details_title = tk.Label(
            right_panel,
            text="[ VEHICLE SPECIFICATIONS ]",
            font=self.header_font,
            bg=self.panel_bg,
            fg=self.neon_pink
        )
        details_title.pack(anchor=tk.W, pady=(10,5), padx=15)

        # Scrollable details
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
            ("MAKE", "make", self.neon_cyan),
            ("MODEL", "model", self.neon_cyan),
            ("YEAR", "year", self.neon_cyan),
            ("COLOR", "color", self.neon_cyan),
            ("COUNTRY", "country", self.neon_cyan),
            ("CATEGORY", "category", self.neon_cyan),
            ("BODY STYLE", "body_style", self.neon_cyan),
            ("ENGINE", "engine", self.neon_cyan),
            ("FUEL TYPE", "fuel_type", self.neon_cyan),
            ("HORSEPOWER", "horsepower", self.neon_cyan, " hp"),
            ("TORQUE", "torque", self.neon_cyan, " lb-ft"),
            ("DRIVETRAIN", "drivetrain", self.neon_cyan),
            ("TRANSMISSION", "transmission", self.neon_cyan),
            ("0-60 MPH", "acceleration", self.neon_cyan, " sec"),
            ("TOP SPEED", "top_speed", self.neon_cyan, " mph"),
            ("FUEL ECONOMY", "fuel_economy", self.neon_cyan, " mpg"),
            ("WEIGHT", "weight", self.neon_cyan, " lbs"),
            ("LENGTH", "length", self.neon_cyan, " in"),
            ("WIDTH", "width", self.neon_cyan, " in"),
            ("HEIGHT", "height", self.neon_cyan, " in"),
            ("WHEELBASE", "wheelbase", self.neon_cyan, " in"),
            ("SEATS", "seats", self.neon_cyan),
            ("DOORS", "doors", self.neon_cyan),
            ("BASE PRICE", "price", self.neon_cyan, " USD"),
            ("MSRP", "msrp", self.neon_cyan, " USD"),
            ("AI LEVEL", "ai_level", self.neon_pink),
            ("HOLO COLOR", "holographic_color", self.neon_pink),
        ]

        row = 0
        for attr_info in attributes:
            if len(attr_info) == 3:
                label_text, attr, color = attr_info
                unit = ""
            else:
                label_text, attr, color, unit = attr_info

            lbl = tk.Label(
                self.details_frame,
                text=label_text,
                font=self.label_font,
                bg=self.panel_bg,
                fg=color,
                anchor=tk.W
            )
            lbl.grid(row=row, column=0, sticky=tk.W, pady=3, padx=(0,20))

            val = tk.Label(
                self.details_frame,
                text="",
                font=self.value_font,
                bg=self.panel_bg,
                fg=self.text_light,
                anchor=tk.W,
                wraplength=500,
                justify=tk.LEFT
            )
            val.grid(row=row, column=1, sticky=tk.W, pady=3)
            self.detail_widgets[attr] = (val, unit)
            row += 1

        # Description
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
        desc_frame.grid(row=row+1, column=0, columnspan=2, sticky=tk.W+tk.E, pady=(0,20))

        self.description_text = tk.Text(
            desc_frame,
            height=6,
            wrap=tk.WORD,
            font=self.value_font,
            bg=self.entry_bg,
            fg=self.text_light,
            bd=0,
            highlightthickness=1,
            highlightbackground=self.neon_yellow
        )
        self.description_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        desc_scroll = tk.Scrollbar(desc_frame, orient=tk.VERTICAL, command=self.description_text.yview,
                                   bg=self.panel_bg, troughcolor=self.entry_bg,
                                   activebackground=self.neon_yellow, elementborderwidth=0)
        desc_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.description_text.config(yscrollcommand=desc_scroll.set, state=tk.DISABLED)

        self.details_frame.columnconfigure(1, weight=1)

    def create_status_bar(self):
        status_frame = tk.Frame(self.root, bg=self.bg_dark, height=30)
        status_frame.pack(fill=tk.X, side=tk.BOTTOM)
        status_frame.pack_propagate(False)

        self.status_label = tk.Label(
            status_frame,
            text="",
            font=("Consolas", 10),
            bg=self.bg_dark,
            fg=self.neon_green
        )
        self.status_label.pack(side=tk.LEFT, padx=10)

        self.update_status()

    def update_status(self):
        current_time = time.strftime("%H:%M:%S")
        car_count = len(self.cars)
        self.status_label.config(
            text=f"[ SYSTEM ONLINE ]   ⚡   {car_count:,} VEHICLES IN DATABASE   ⚡   {current_time}   ⚡   {len(self.listbox.get(0, tk.END))} DISPLAYED"
        )
        self.root.after(1000, self.update_status)

    def pulse_header(self):
        colors = [self.neon_green, self.neon_cyan, self.neon_pink, self.neon_yellow, self.neon_purple]
        current_fg = self.title_label.cget("fg")
        try:
            idx = colors.index(current_fg)
            next_color = colors[(idx + 1) % len(colors)]
        except ValueError:
            next_color = colors[0]
        self.title_label.config(fg=next_color)
        self.root.after(500, self.pulse_header)

    def populate_listbox(self):
        for car in self.cars[:1000]:  # Show first 1000 initially for performance
            self.listbox.insert(tk.END, car.display_name())

    def on_select(self, event):
        selection = self.listbox.curselection()
        if not selection:
            return
        
        # Find the actual car (need to handle filtered view)
        display_name = self.listbox.get(selection[0])
        car = next((c for c in self.cars if c.display_name() == display_name), None)
        
        if not car:
            return

        # Update all fields
        self.detail_widgets["make"][0].config(text=car.make)
        self.detail_widgets["model"][0].config(text=car.model)
        self.detail_widgets["year"][0].config(text=str(car.year))
        self.detail_widgets["color"][0].config(text=car.color)
        self.detail_widgets["country"][0].config(text=car.country)
        self.detail_widgets["category"][0].config(text=car.category)
        self.detail_widgets["body_style"][0].config(text=car.body_style)
        self.detail_widgets["engine"][0].config(text=car.engine)
        self.detail_widgets["fuel_type"][0].config(text=car.fuel_type)
        self.detail_widgets["horsepower"][0].config(text=f"{car.horsepower}{self.detail_widgets['horsepower'][1]}")
        self.detail_widgets["torque"][0].config(text=f"{car.torque}{self.detail_widgets['torque'][1]}")
        self.detail_widgets["drivetrain"][0].config(text=car.drivetrain)
        self.detail_widgets["transmission"][0].config(text=car.transmission)
        self.detail_widgets["acceleration"][0].config(text=f"{car.acceleration}{self.detail_widgets['acceleration'][1]}")
        self.detail_widgets["top_speed"][0].config(text=f"{car.top_speed}{self.detail_widgets['top_speed'][1]}")
        self.detail_widgets["fuel_economy"][0].config(text=f"{car.fuel_economy}{self.detail_widgets['fuel_economy'][1]}")
        self.detail_widgets["weight"][0].config(text=f"{car.weight:,}{self.detail_widgets['weight'][1]}")
        self.detail_widgets["length"][0].config(text=f"{car.length}{self.detail_widgets['length'][1]}")
        self.detail_widgets["width"][0].config(text=f"{car.width}{self.detail_widgets['width'][1]}")
        self.detail_widgets["height"][0].config(text=f"{car.height}{self.detail_widgets['height'][1]}")
        self.detail_widgets["wheelbase"][0].config(text=f"{car.wheelbase}{self.detail_widgets['wheelbase'][1]}")
        self.detail_widgets["seats"][0].config(text=str(car.seats))
        self.detail_widgets["doors"][0].config(text=str(car.doors))
        self.detail_widgets["price"][0].config(text=f"${car.price:,}{self.detail_widgets['price'][1]}")
        self.detail_widgets["msrp"][0].config(text=f"${car.msrp:,}{self.detail_widgets['msrp'][1]}")
        self.detail_widgets["ai_level"][0].config(text=car.ai_level)
        self.detail_widgets["holographic_color"][0].config(text=car.holographic_color)

        self.description_text.config(state=tk.NORMAL)
        self.description_text.delete(1.0, tk.END)
        self.description_text.insert(tk.END, car.description)
        self.description_text.config(state=tk.DISABLED)

    # ===== JSON FILE MANAGEMENT METHODS =====
    def save_cars_to_json(self, filename="car_database.json"):
        """Save current car list to a JSON file."""
        try:
            data = [car.to_dict() for car in self.cars]
            with open(filename, "w", encoding='utf-8') as f:
                json.dump(data, f, indent=2)
            messagebox.showinfo("Success", f"Saved {len(self.cars)} cars to {filename}")
            print(f"✓ Saved {len(self.cars)} cars to {filename}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save: {e}")
            print(f"✗ Error saving to {filename}: {e}")

    def load_cars_from_json_file(self, filename="car_database.json"):
        """Load cars from a JSON file and add to the database."""
        try:
            if not os.path.exists(filename):
                messagebox.showerror("Error", f"File not found: {filename}")
                return
            
            with open(filename, "r", encoding='utf-8') as f:
                data = json.load(f)
            
            loaded_cars = [Car.from_dict(item) for item in data]
            initial_count = len(self.cars)
            self.cars.extend(loaded_cars)
            
            # Refresh UI
            self.listbox.delete(0, tk.END)
            self.populate_listbox()
            self.update_status()
            
            messagebox.showinfo("Success", f"Loaded {len(loaded_cars)} cars from {filename}\nTotal: {len(self.cars)} cars")
            print(f"✓ Loaded {len(loaded_cars)} cars from {filename}")
        except json.JSONDecodeError as e:
            messagebox.showerror("Error", f"Invalid JSON format: {e}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load: {e}")
            print(f"✗ Error loading from {filename}: {e}")

    def add_single_car(self, car_data):
        """Add a single car to the database from a dictionary."""
        try:
            car = Car.from_dict(car_data)
            self.cars.append(car)
            self.listbox.insert(tk.END, car.display_name())
            self.update_status()
            return True
        except Exception as e:
            print(f"✗ Error adding car: {e}")
            return False

    def export_filtered_cars(self, make=None, model=None, year_min=None, year_max=None, filename="filtered_cars.json"):
        """Export filtered cars to a new JSON file."""
        filtered = self.cars[:]
        
        if make:
            filtered = [c for c in filtered if c.make.lower() == make.lower()]
        if model:
            filtered = [c for c in filtered if c.model.lower() == model.lower()]
        if year_min:
            filtered = [c for c in filtered if c.year >= year_min]
        if year_max:
            filtered = [c for c in filtered if c.year <= year_max]
        
        try:
            data = [car.to_dict() for car in filtered]
            with open(filename, "w", encoding='utf-8') as f:
                json.dump(data, f, indent=2)
            messagebox.showinfo("Success", f"Exported {len(filtered)} cars to {filename}")
            print(f"✓ Exported {len(filtered)} cars to {filename}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to export: {e}")

    def merge_json_files(self, *filenames, output="merged_cars.json"):
        """Merge multiple JSON car files into one."""
        all_cars = []
        
        for filename in filenames:
            try:
                if not os.path.exists(filename):
                    print(f"⚠ Skipping {filename} (not found)")
                    continue
                
                with open(filename, "r", encoding='utf-8') as f:
                    data = json.load(f)
                all_cars.extend([Car.from_dict(item) for item in data])
                print(f"✓ Loaded {len(data)} cars from {filename}")
            except Exception as e:
                print(f"✗ Error loading {filename}: {e}")
        
        try:
            # Remove duplicates (same make, model, year)
            unique_cars = {}
            for car in all_cars:
                key = f"{car.make}_{car.model}_{car.year}"
                if key not in unique_cars:
                    unique_cars[key] = car
            
            data = [car.to_dict() for car in unique_cars.values()]
            with open(output, "w", encoding='utf-8') as f:
                json.dump(data, f, indent=2)
            messagebox.showinfo("Success", f"Merged {len(unique_cars)} unique cars to {output}")
            print(f"✓ Merged {len(unique_cars)} unique cars to {output}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to merge: {e}")

def main():
    root = tk.Tk()
    app = NeonCarApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()