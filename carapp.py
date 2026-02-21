import tkinter as tk
from tkinter import font as tkfont
import time

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
        self.ai_level = ai_level            # e.g., "Level 3 Autonomy"
        self.holographic_color = holographic_color
        self.description = description

    def display_name(self):
        return f"{self.year} {self.make} {self.model}"

def create_car_list():
    """Create a list of Car objects with detailed specs, plus futuristic attributes."""
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
        # New cars:
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
    ]
    return cars

class NeonCarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("NEON CAR DATABASE 3000")
        self.root.geometry("1200x750")  # Slightly larger for comfort
        self.root.configure(bg="#0a0f0f")  # deep dark background

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

        # Load car data
        self.cars = create_car_list()

        # Build UI
        self.create_header()
        self.create_main_panels()
        self.create_status_bar()
        self.populate_listbox()

        # Start a simple pulsing animation for the header
        self.pulse_header()

    def create_header(self):
        """Futuristic header with glowing text and neon underline."""
        header_frame = tk.Frame(self.root, bg=self.bg_dark, height=90)
        header_frame.pack(fill=tk.X, side=tk.TOP)
        header_frame.pack_propagate(False)

        # Main title with a shadow effect (two overlapping labels)
        shadow_label = tk.Label(
            header_frame,
            text="⚡ NEON CAR DATABASE 3000 ⚡",
            font=self.title_font,
            bg=self.bg_dark,
            fg="#222222"  # dark shadow
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

        # Neon line under header
        canvas = tk.Canvas(header_frame, bg=self.bg_dark, height=4, highlightthickness=0)
        canvas.pack(fill=tk.X, side=tk.BOTTOM)
        canvas.create_line(0, 2, 1200, 2, fill=self.neon_cyan, width=4)

    def create_main_panels(self):
        """Left panel (list) and right panel (details) with neon borders and scrollability."""
        main_container = tk.Frame(self.root, bg=self.bg_dark)
        main_container.pack(fill=tk.BOTH, expand=True, padx=15, pady=10)

        # Left panel (car list) - dark with neon green border
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

        # Listbox with scrollbar
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

        # Right panel (details) - dark with neon pink border
        right_panel = tk.Frame(main_container, bg=self.panel_bg)
        right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        right_panel.config(highlightbackground=self.neon_pink, highlightcolor=self.neon_pink,
                           highlightthickness=2, bd=0)

        # Title inside right panel
        details_title = tk.Label(
            right_panel,
            text="[ VEHICLE SPECIFICATIONS ]",
            font=self.header_font,
            bg=self.panel_bg,
            fg=self.neon_pink
        )
        details_title.pack(anchor=tk.W, pady=(10,5), padx=15)

        # Create a canvas and scrollbar for the right panel content
        canvas_frame = tk.Frame(right_panel, bg=self.panel_bg)
        canvas_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=(0,10))

        self.canvas = tk.Canvas(canvas_frame, bg=self.panel_bg, highlightthickness=0)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        v_scrollbar = tk.Scrollbar(canvas_frame, orient=tk.VERTICAL, command=self.canvas.yview,
                                   bg=self.panel_bg, troughcolor=self.entry_bg,
                                   activebackground=self.neon_pink, elementborderwidth=0)
        v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvas.configure(yscrollcommand=v_scrollbar.set)

        # Inner frame to hold all details
        self.details_frame = tk.Frame(self.canvas, bg=self.panel_bg)
        self.canvas.create_window((0, 0), window=self.details_frame, anchor=tk.NW)

        self.details_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        # Now populate the inner frame with details
        self.create_details_widgets()

    def create_details_widgets(self):
        """Create all the detail labels inside the scrollable frame."""
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
            # Attribute label (neon)
            lbl = tk.Label(
                self.details_frame,
                text=label_text,
                font=self.label_font,
                bg=self.panel_bg,
                fg=color,
                anchor=tk.W
            )
            lbl.grid(row=row, column=0, sticky=tk.W, pady=3, padx=(0,10))

            # Value label (light text)
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
            self.detail_widgets[attr] = (val, unit)  # store both label and unit
            row += 1

        # Description field (spans both columns)
        desc_label = tk.Label(
            self.details_frame,
            text="DESCRIPTION",
            font=self.header_font,
            bg=self.panel_bg,
            fg=self.neon_yellow,
            anchor=tk.W
        )
        desc_label.grid(row=row, column=0, columnspan=2, sticky=tk.W, pady=(15,5))

        # Frame for description text + its own scrollbar
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

        # Configure grid column weights so value column expands
        self.details_frame.columnconfigure(1, weight=1)

    def create_status_bar(self):
        """Futuristic status bar with scanning text and time."""
        status_frame = tk.Frame(self.root, bg=self.bg_dark, height=30)
        status_frame.pack(fill=tk.X, side=tk.BOTTOM)
        status_frame.pack_propagate(False)

        self.status_label = tk.Label(
            status_frame,
            text="[ SYSTEM ONLINE ]   ⚡   SCANNING DATABASE   ⚡   " + time.strftime("%H:%M:%S"),
            font=("Consolas", 9),
            bg=self.bg_dark,
            fg=self.neon_green
        )
        self.status_label.pack(side=tk.LEFT, padx=10)

        # Update time every second
        self.update_status()

    def update_status(self):
        """Update the status bar with current time."""
        current_time = time.strftime("%H:%M:%S")
        self.status_label.config(text=f"[ SYSTEM ONLINE ]   ⚡   SCANNING DATABASE   ⚡   {current_time}")
        self.root.after(1000, self.update_status)

    def pulse_header(self):
        """Simple pulsing animation for the header title color."""
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
        """Fill listbox with car names."""
        for car in self.cars:
            self.listbox.insert(tk.END, car.display_name())

    def on_select(self, event):
        """Update details panel when a car is selected."""
        selection = self.listbox.curselection()
        if not selection:
            return
        index = selection[0]
        car = self.cars[index]

        # Update simple fields (with units)
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

        # Update description
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