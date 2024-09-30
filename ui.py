import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar

class TaskManagerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Task Manager")  # Set the window title
        self.geometry("1024x768")   # Set the window size
        self.configure(bg="#d3d3d3")  # Configure background color
        self.theme = "light"  # Default theme
        # Define themes with colors for light and dark modes
        self.themes = {
            "light": {"bg": "#d3d3d3", "fg": "#000000", "border": "#aaaaaa"},
            "dark": {"bg": "#333333", "fg": "#FFFFFF", "border": "#444444"}
        }
        self.mode_var = tk.StringVar(value="Light Mode")  # Variable to track the current mode
        self.create_sidebar()  # Create the sidebar
        self.create_topbar()   # Create the top bar
        self.frames = {}       # Dictionary to hold different frames (pages)
        self.create_main_page()  # Create main page
        self.create_my_tasks_page()  # Create my tasks page
        self.create_settings_page()  # Create settings page
        self.create_notifications_page()  # Create notifications page
        self.create_add_task_page()  # Create add task page
        self.apply_theme()  # Apply the current theme
        self.show_frame("MainPage")  # Show the main page initially

    def create_sidebar(self):
        # Create the sidebar frame
        self.sidebar = tk.Frame(self, bg=self.themes[self.theme]["bg"], width=200, bd=2, relief="ridge")
        self.sidebar.pack(side=tk.LEFT, fill=tk.Y, padx=0, pady=0)
        logo_image = tk.PhotoImage(file="assets/logo.png").subsample(3, 3)  # Load and resize logo
        self.logo_label = tk.Label(self.sidebar, image=logo_image, bg=self.themes[self.theme]["bg"], bd=0)
        self.logo_label.image = logo_image  # Keep a reference to the image
        self.logo_label.pack(pady=(10, 20))  # Add logo to sidebar
        # Button style definition for the sidebar buttons
        button_style = {"width": 15, "height": 1, "bg": self.themes[self.theme]["bg"], 
                        "fg": self.themes[self.theme]["fg"], "relief": "raised", "bd": 2, "anchor": "center"}
        # Create sidebar buttons for navigation
        self.dashboard_button = tk.Button(self.sidebar, text="Dashboard", **button_style, command=lambda: self.show_frame("MainPage"))
        self.dashboard_button.pack(padx=10, pady=10, fill=tk.X)
        self.tasks_button = tk.Button(self.sidebar, text="My Tasks", **button_style, command=lambda: self.show_frame("MyTasksPage"))
        self.tasks_button.pack(padx=10, pady=10, fill=tk.X)
        self.notifications_button = tk.Button(self.sidebar, text="Notifications", **button_style, command=lambda: self.show_frame("NotificationsPage"))
        self.notifications_button.pack(padx=10, pady=10, fill=tk.X)
        self.spacer = tk.Frame(self.sidebar, bg=self.themes[self.theme]["bg"])  # Spacer to push buttons to the top
        self.spacer.pack(expand=True, fill=tk.Y, pady=0)
        self.settings_button = tk.Button(self.sidebar, text="Settings", **button_style, command=lambda: self.show_frame("SettingsPage"))
        self.settings_button.pack(padx=10, pady=10, fill=tk.X)
        self.logout_button = tk.Button(self.sidebar, text="Log Out", **button_style, command=self.quit)  # Log out button
        self.logout_button.pack(padx=10, pady=10, fill=tk.X)

    def create_topbar(self):
        # Create the top bar frame
        self.top_frame = tk.Frame(self, bg=self.themes[self.theme]["bg"], height=50, bd=2, relief="ridge")
        self.top_frame.pack(side=tk.TOP, fill=tk.X, padx=0, pady=0)
        # Button style definition for the top bar buttons
        self.top_button_style = {"width": 15, "height": 1, "bg": self.themes[self.theme]["bg"], 
                                 "fg": self.themes[self.theme]["fg"], "relief": "raised", "bd": 2}
        # Create buttons for log in and adding a task
        self.login_button = tk.Button(self.top_frame, text="Log In", **self.top_button_style, command=lambda: print("Log In clicked"))
        self.login_button.pack(side=tk.RIGHT, padx=10, pady=10)
        self.add_task_button = tk.Button(self.top_frame, text="+ Add Task", **self.top_button_style, command=lambda: self.show_frame("AddTaskPage"))
        self.add_task_button.pack(side=tk.RIGHT, padx=10, pady=10)

    def create_main_page(self):
        # Create the main page frame
        self.main_frame = tk.Frame(self, bg=self.themes[self.theme]["bg"], bd=2, relief="ridge")
        self.main_frame.pack(expand=True, fill="both", padx=0, pady=0)
        # Create a calendar frame
        calendar_frame = tk.Frame(self.main_frame, bg="#ffffff", bd=1, relief="solid")
        calendar_frame.place(relx=0.05, rely=0.05, relwidth=0.4, relheight=0.4)
        calendar = Calendar(calendar_frame, selectmode='day', year=2024, month=9, day=30)  # Initialize calendar
        calendar.pack(expand=True, fill="both")
        # Create task and category frames
        tasks_frame = tk.Frame(self.main_frame, bg="#ffffff", bd=1, relief="solid")
        tasks_frame.place(relx=0.55, rely=0.05, relwidth=0.4, relheight=0.4)
        categories_frame = tk.Frame(self.main_frame, bg="#ffffff", bd=1, relief="solid")
        categories_frame.place(relx=0.05, rely=0.55, relwidth=0.4, relheight=0.4)
        status_frame = tk.Frame(self.main_frame, bg="#ffffff", bd=1, relief="solid")
        status_frame.place(relx=0.55, rely=0.55, relwidth=0.4, relheight=0.4)
        # Add headers and tables for tasks, categories, and status
        tasks_header = tk.Label(tasks_frame, text="My Tasks", font=("Arial", 12, "bold"), anchor="center", bg="#f2f2f2")
        tasks_header.pack(fill="x")
        tasks_table = tk.Listbox(tasks_frame, borderwidth=0)  # Listbox for tasks
        tasks_table.pack(expand=True, fill="both")
        categories_header = tk.Label(categories_frame, text="My Categories", font=("Arial", 12, "bold"), anchor="center", bg="#f2f2f2")
        categories_header.pack(fill="x")
        categories_table = tk.Listbox(categories_frame, borderwidth=0)  # Listbox for categories
        categories_table.pack(expand=True, fill="both")
        status_header = tk.Label(status_frame, text="Status", font=("Arial", 12, "bold"), anchor="center", bg="#f2f2f2")
        status_header.pack(fill="x")
        status_table = tk.Listbox(status_frame, borderwidth=0)  # Listbox for status
        status_table.pack(expand=True, fill="both")
        self.frames["MainPage"] = self.main_frame  # Store the main page frame

    def create_my_tasks_page(self):
        # Create the my tasks page frame
        self.my_tasks_frame = tk.Frame(self, bg=self.themes[self.theme]["bg"])
        self.frames["MyTasksPage"] = self.my_tasks_frame  # Store the my tasks page frame

    def create_add_task_page(self):
        # Create the add task page frame
        self.add_task_frame = tk.Frame(self, bg=self.themes[self.theme]["bg"])
        self.frames["AddTaskPage"] = self.add_task_frame  # Store the add task page frame

    def create_notifications_page(self):
        # Create the notifications page frame
        self.notifications_frame = tk.Frame(self, bg=self.themes[self.theme]["bg"])
        self.frames["NotificationsPage"] = self.notifications_frame  # Store the notifications page frame

    def create_settings_page(self):
        # Create the settings page frame
        self.settings_frame = tk.Frame(self, bg=self.themes[self.theme]["bg"], bd=2, relief="ridge")
        self.mode_frame = tk.Frame(self.settings_frame, bg=self.themes[self.theme]["bg"])
        self.mode_frame.pack(pady=10, padx=50, anchor="w")
        self.mode_label = tk.Label(self.mode_frame, text="Select Mode:", font=("Arial", 12), bg=self.themes[self.theme]["bg"], fg=self.themes[self.theme]["fg"])
        self.mode_label.pack(side="left", padx=(0, 10))  # Label for mode selection
        self.mode_button = ttk.Combobox(self.mode_frame, textvariable=self.mode_var, values=["Light Mode", "Dark Mode"])  # Combobox for mode selection
        self.mode_button.pack(side="left")
        self.mode_button.bind("<<ComboboxSelected>>", lambda event: self.apply_theme_from_combobox())  # Update theme on selection
        self.task_prefs_frame = tk.Frame(self.settings_frame, bg=self.themes[self.theme]["bg"])
        self.task_prefs_frame.pack(pady=10, padx=50, anchor="w")
        self.task_sort_label = tk.Label(self.task_prefs_frame, text="Task Sorting:", font=("Arial", 12), bg=self.themes[self.theme]["bg"], fg=self.themes[self.theme]["fg"])
        self.task_sort_label.pack(side="left", padx=(0, 10))  # Label for task sorting
        self.task_sort_options = ttk.Combobox(self.task_prefs_frame, values=["By Date", "By Priority", "By Category"])  # Combobox for sorting options
        self.task_sort_options.pack(side="left")
        self.task_sort_options.set("By Date")  # Default sorting option
        self.frames["SettingsPage"] = self.settings_frame  # Store the settings page frame

    def show_frame(self, frame_name):
        # Hide all frames and show the selected frame
        for frame in self.frames.values():
            frame.pack_forget()
        frame = self.frames.get(frame_name)
        if frame:
            frame.pack(fill="both", expand=True)  # Show the selected frame
        else:
            print(f"Frame '{frame_name}' not found!")  # Error message if frame not found

    def apply_theme(self):
        # Apply the current theme to all frames and widgets
        self.theme = "light" if self.mode_var.get() == "Light Mode" else "dark"
        current_theme = self.themes[self.theme]
        self.sidebar.config(bg=current_theme["bg"], bd=2, relief="ridge")
        self.logo_label.config(bg=current_theme["bg"])
        self.spacer.config(bg=current_theme["bg"])
        self.main_frame.config(bg=current_theme["bg"], bd=2, relief="ridge")
        self.my_tasks_frame.config(bg=current_theme["bg"])
        self.notifications_frame.config(bg=current_theme["bg"])
        self.add_task_frame.config(bg=current_theme["bg"])
        self.settings_frame.config(bg=current_theme["bg"], bd=2, relief="ridge")
        self.top_frame.config(bg=current_theme["bg"], bd=2, relief="ridge")
        self.mode_frame.config(bg=current_theme["bg"])
        self.mode_label.config(bg=current_theme["bg"], fg=current_theme["fg"])
        self.task_prefs_frame.config(bg=current_theme["bg"])
        self.task_sort_label.config(bg=current_theme["bg"], fg=current_theme["fg"])
        # Update button styles in sidebar
        for widget in self.sidebar.winfo_children():
            if isinstance(widget, tk.Button):
                widget.config(bg=current_theme["bg"], fg=current_theme["fg"], relief="raised")
        # Update button styles in top frame
        for widget in self.top_frame.winfo_children():
            if isinstance(widget, tk.Button):
                widget.config(bg=current_theme["bg"], fg=current_theme["fg"], relief="raised")

    def apply_theme_from_combobox(self):
        self.apply_theme()  # Apply the selected theme

if __name__ == "__main__":
    app = TaskManagerApp()  # Create an instance of the app
    app.mainloop()  # Start the main event loop
