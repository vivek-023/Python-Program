import json
from datetime import datetime, timedelta
import tkinter as tk
from tkinter import simpledialog, messagebox, ttk
from tkcalendar import Calendar

class AirReservationSystem:
    def __init__(self):
        self.bookings = []
        self.flights = []
        self.load_bookings()
        self.load_flights()
        self.base_price_per_mile = 3.0  # Base price per mile

    def load_bookings(self):
        """Load bookings from a JSON file."""
        try:
            with open('bookings.json', 'r') as file:
                self.bookings = json.load(file)
        except FileNotFoundError:
            self.bookings = []

    def save_bookings(self):
        """Save bookings to a JSON file."""
        with open('bookings.json', 'w') as file:
            json.dump(self.bookings, file, indent=4)

    def load_flights(self):
        """Load flight details from a JSON file."""
        try:
            with open('flights.json', 'r') as file:
                self.flights = json.load(file)
        except FileNotFoundError:
            self.flights = []

    def save_flights(self):
        """Save updated flight details to a JSON file."""
        with open('flights.json', 'w') as file:
            json.dump(self.flights, file, indent=4)

    def calculate_price(self, distance, days_until_flight):
        """Calculate the price based on the distance and days until the flight."""
        base_price = distance * self.base_price_per_mile

        if days_until_flight <= 1:
            multiplier = 7.0  # Higher multiplier for last-minute bookings
        elif days_until_flight <= 7:
            multiplier = 6.0  # Slightly lower multiplier for bookings within a week
        elif days_until_flight <= 30:
            multiplier = 4.0  # Lower multiplier for bookings within a month
        elif days_until_flight >= 90:
            multiplier = 3.0  # Discounted multiplier for early bookings (3 months or more in advance)
        else:
            multiplier = 3.5  # Standard multiplier for bookings between 1 month and 3 months in advance

        price = int(base_price * multiplier)

        # Cap maximum price at 10000
        return min(price, 10000)

    def update_vacancy(self, flight_number, num_passengers):
        """Update the vacancy for a booked flight."""
        for flight in self.flights:
            if flight["flight_number"] == flight_number:
                flight["vacancy"] += num_passengers  # Increase vacancy when booking is canceled
                break
        self.save_flights()

    def book_flight(self):
        """Book a new flight and save it to the bookings."""
        book_root = tk.Toplevel()
        book_root.withdraw()  # Hide the main window

        origin = simpledialog.askstring("Input", "Enter origin:", parent=book_root)
        destination = simpledialog.askstring("Input", "Enter destination:", parent=book_root)

        if not origin or not destination:
            messagebox.showerror("Error", "Origin and destination cannot be empty.")
            return

        origin = origin.lower()
        destination = destination.lower()

        available_flights = [flight for flight in self.flights if flight["origin"].lower() == origin and flight["destination"].lower() == destination]

        if not available_flights:
            messagebox.showinfo("No Flights Available", f"No flights available from {origin} to {destination}")
            return

        date_picker = tk.Toplevel(book_root)
        date_picker.geometry("400x400")  # Set custom size for the window
        cal = Calendar(date_picker, selectmode='day', year=datetime.now().year, month=datetime.now().month, day=datetime.now().day)
        cal.pack(pady=20)

        def proceed_to_flight_selection():
            date = cal.get_date()
            selected_date = datetime.strptime(date, "%m/%d/%y")
            current_date = datetime.now()

            if selected_date < current_date:
                messagebox.showerror("Invalid Date", "You cannot select a past date. Please select a valid date.")
                return

            if (selected_date - current_date).days > 90:
                messagebox.showerror("Invalid Date", "You cannot book a ticket more than 3 months in advance.")
                return

            date_picker.destroy()
            self.show_flight_options(origin, destination, selected_date)

        tk.Button(date_picker, text="Proceed", command=proceed_to_flight_selection).pack(pady=20)
        book_root.mainloop()

    def show_flight_options(self, origin, destination, selected_date):
        """Display flight options based on selected date."""
        flight_picker = tk.Toplevel()
        flight_picker.title("Select Flight")
        flight_picker.geometry("2000x600")  # Set custom size for the window

        columns = ("Flight Name", "Flight Number", "Origin", "Destination", "Departure Time", "Arrival Time", "Total Time", "Price", "Vacancy")
        tree = ttk.Treeview(flight_picker, columns=columns, show="headings")

        for col in columns:
            tree.heading(col, text=col)

        for flight in self.flights:
            if flight["origin"].lower() == origin and flight["destination"].lower() == destination:
                distance = flight["distance"]  # Assuming the distance is provided in the flight details
                days_until_flight = (selected_date - datetime.now()).days
                price = self.calculate_price(distance, days_until_flight)
                tree.insert("", tk.END, values=(flight["flight_name"], flight["flight_number"], flight["origin"], flight["destination"], flight["departure_time"], flight["arrival_time"], flight["total_time"], price, flight["vacancy"]))

        tree.pack(pady=20)

        def select_flight():
            selected_item = tree.selection()
            if not selected_item:
                messagebox.showerror("Error", "No flight selected")
                return

            flight_info = tree.item(selected_item)["values"]
            flight_number = flight_info[1]
            origin = flight_info[2]
            destination = flight_info[3]
            departure_time = flight_info[4]
            arrival_time = flight_info[5]
            total_time = flight_info[6]
            vacancy = flight_info[8]

            num_passengers = simpledialog.askinteger("Input", "Number of passengers (Max 5):", parent=flight_picker, minvalue=1, maxvalue=min(5, vacancy))
            if num_passengers is None or num_passengers <= 0:
                print("Invalid number of passengers.")
                return

            passenger_details = []
            for i in range(num_passengers):
                name = simpledialog.askstring("Input", f"Passenger Name {i + 1}:", parent=flight_picker)
                if not name:
                    print("Passenger name cannot be empty.")
                    return

                while True:
                    mobile = simpledialog.askstring("Input", f"Mobile Number {i + 1}:", parent=flight_picker)
                    if not mobile:
                        print("Mobile number cannot be empty.")
                        return
                    elif len(mobile) != 10:
                        print("Mobile number must be 10 digits.")
                    else:
                        break

                gender = simpledialog.askstring("Input", f"Gender for {name}:", parent=flight_picker)
                if gender.lower() not in ['male', 'female', 'other']:
                    print("Invalid gender input.")
                    return

                dob = simpledialog.askstring("Input", f"Date of Birth for {name} (DD-MM-YYYY):", parent=flight_picker)
                try:
                    dob_date = datetime.strptime(dob, "%d-%m-%Y")
                except ValueError:
                    print("Invalid date format. Please use DD-MM-YYYY.")
                    return

                passenger_details.append({
                    "name": name,
                    "mobile": mobile,
                    "gender": gender,
                    "dob": dob_date.strftime("%d-%m-%Y")
                })

            distance = flight["distance"]  # Assuming the distance is provided in the flight details
            days_until_flight = (selected_date - datetime.now()).days
            price_per_passenger = self.calculate_price(distance, days_until_flight)
            total_price = price_per_passenger * num_passengers

            booking = {
                "passenger_details": passenger_details,
                "flight_number": flight_number,
                "flight_name": flight_info[0],
                "origin": origin,
                "destination": destination,
                "date": selected_date.strftime("%m/%d/%y"),
                "departure_time": departure_time,
                "arrival_time": arrival_time,
                "total_time": total_time,
                "price": total_price
            }

            self.bookings.append(booking)
            self.save_bookings()
            self.update_vacancy(flight_number, -num_passengers)  # Decrease vacancy
            self.show_ticket(booking, total_price)
            print(f"Flight booked successfully! Total Price: {total_price}")  # Optional: Notify the user about the successful booking.

        tk.Button(flight_picker, text="Select Flight", command=select_flight).pack(pady=20)
        flight_picker.mainloop()

    def view_bookings_interface(self):
        """View all bookings within the past month."""
        bookings_root = tk.Toplevel()
        bookings_root.title("Recent Bookings")
        bookings_root.geometry("2000x600")

        if not self.bookings:
            tk.Label(bookings_root, text="No bookings found.").pack(pady=20)
            return

        columns = ("Passenger Names", "Flight Name", "Flight Number", "Origin", "Destination", "Date", "Total Price", "Cancel")
        tree = ttk.Treeview(bookings_root, columns=columns, show="headings")

        for col in columns:
            tree.heading(col, text=col)

        current_date = datetime.now()
        one_month_ago = current_date - timedelta(days=30)

        for booking in self.bookings:
            booking_date = datetime.strptime(booking['date'], "%m/%d/%y")
            if booking_date >= one_month_ago:
                passenger_list = ", ".join([passenger['name'] for passenger in booking['passenger_details']])
                total_price = booking['price']
                tree.insert("", tk.END, values=(passenger_list, booking['flight_name'], booking['flight_number'], booking['origin'], booking['destination'], booking['date'], total_price, "Cancel"))

        tree.pack(pady=20)

        def cancel_booking(event):
            selected_item = tree.selection()
            if not selected_item:
                messagebox.showerror("Error", "No booking selected")
                return

            booking_info = tree.item(selected_item)["values"]
            flight_number = booking_info[2]
            total_price = booking_info[6]
            num_passengers = len(booking_info[0].split(", "))

            def cancel_all():
                for booking in self.bookings:
                    if booking["flight_number"] == flight_number and booking["date"] == booking_info[5]:
                        self.bookings.remove(booking)
                        self.save_bookings()
                        self.update_vacancy(flight_number, num_passengers)
                        tree.delete(selected_item)
                        messagebox.showinfo("Success", f"Booking canceled successfully. Refund: Rs {total_price}")
                        break

            def cancel_partial(passenger_indexes):
                for booking in self.bookings:
                    if booking["flight_number"] == flight_number and booking["date"] == booking_info[5]:
                        remaining_passengers = [booking['passenger_details'][i] for i in range(len(booking['passenger_details'])) if i not in passenger_indexes]
                        num_to_cancel = len(passenger_indexes)
                        if num_to_cancel < num_passengers:
                            booking['passenger_details'] = remaining_passengers
                            booking['price'] -= total_price * num_to_cancel // num_passengers
                            self.save_bookings()
                            self.update_vacancy(flight_number, num_to_cancel)
                            tree.item(selected_item, values=(booking_info[0], booking['flight_name'], flight_number, booking['origin'], booking['destination'], booking['date'], booking['price'], "Cancel"))
                            messagebox.showinfo("Success", f"{num_to_cancel} ticket(s) canceled successfully. Refund: Rs {total_price * num_to_cancel // num_passengers}")
                        else:
                            self.bookings.remove(booking)
                            self.save_bookings()
                            self.update_vacancy(flight_number, num_passengers)
                            tree.delete(selected_item)
                            messagebox.showinfo("Success", f"Booking canceled successfully. Refund: Rs {total_price}")
                        break

            cancel_choice = messagebox.askyesnocancel("Cancel Booking", "Do you want to cancel the entire booking?")
            if cancel_choice:
                cancel_all()
            elif cancel_choice is None:
                return
            else:
                cancel_partial_ui(booking_info, cancel_partial)

        def cancel_partial_ui(booking_info, cancel_partial_callback):
            passengers = booking_info[0].split(", ")
            passenger_window = tk.Toplevel()
            passenger_window.title("Select Passengers to Cancel")
            passenger_window.geometry("400x300")

            tk.Label(passenger_window, text="Select passengers to cancel:").pack(pady=10)
            check_vars = [tk.BooleanVar() for _ in passengers]
            for i, passenger in enumerate(passengers):
                tk.Checkbutton(passenger_window, text=passenger, variable=check_vars[i]).pack(anchor='w')

            def submit_selection():
                selected_indexes = [i for i, var in enumerate(check_vars) if var.get()]
                if not selected_indexes:
                    messagebox.showerror("Error", "No passengers selected")
                    return
                cancel_partial_callback(selected_indexes)
                passenger_window.destroy()

            tk.Button(passenger_window, text="Cancel Selected", command=submit_selection).pack(pady=20)

            passenger_window.mainloop()

        tree.bind("<Double-1>", cancel_booking)

        bookings_root.mainloop()

    def show_ticket(self, booking, total_price):
        """Display the ticket details."""
        ticket_details = f"Passenger Details:\n"
        for passenger in booking['passenger_details']:
            masked_mobile = 'X' * (len(passenger['mobile']) - 4) + passenger['mobile'][-4:]
            ticket_details += f"Name: {passenger['name']}, Mobile: XXXXXX{masked_mobile}, Gender: {passenger['gender']}, DOB: {passenger['dob']}\n"
        ticket_details += f"\nFlight Details:\n"
        ticket_details += f"Source: {booking['origin']}\n"
        ticket_details += f"Destination: {booking['destination']}\n"
        ticket_details += f"Flight name: {booking['flight_name']}\n"
        ticket_details += f"Flight no: {booking['flight_number']}\n"
        ticket_details += f"Departure timing: {booking['departure_time']}\n"
        ticket_details += f"Arrival timing: {booking['arrival_time']}\n"
        ticket_details += f"Total time taken: {booking['total_time']}\n"
        ticket_details += f"Date of journey: {booking['date']}\n"
        ticket_details += f"Total Price: Rs {total_price}"

        ticket_window = tk.Toplevel()
        ticket_window.title("Ticket Details")
        ticket_window.geometry("800x700")
        ticket_label = tk.Label(ticket_window, text=ticket_details, font=("Arial", 14), justify="left", padx=10, pady=10)
        ticket_label.pack(expand=True, fill="both")

        ticket_window.mainloop()

    def run_interface(self):
        """Run the Air Reservation System with a GUI interface."""
        root = tk.Tk()
        root.title("Air Reservation System")
        root.geometry("400x400")

        def book_flight_wrapper():
            self.book_flight()

        def view_bookings_wrapper():
            self.view_bookings_interface()

        book_flight_button = tk.Button(root, text="Book a Flight", command=book_flight_wrapper, width=20, height=2)
        book_flight_button.pack(pady=20)

        view_bookings_button = tk.Button(root, text="View Bookings", command=view_bookings_wrapper, width=20, height=2)
        view_bookings_button.pack(pady=20)

        def exit_application():
            root.destroy()

        exit_button = tk.Button(root, text="Exit", command=exit_application, width=20, height=2)
        exit_button.pack(pady=20)

        root.mainloop()

if __name__ == "__main__":
    system = AirReservationSystem()
    system.run_interface()