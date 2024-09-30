import tkinter as tk

class TaskManagerApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # Set window title and size
        self.title("Task Manager")
        self.geometry("1024x768")

        # Create a container to hold different pages
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        # Dictionary to store different frames (pages)
        self.frames = {}
        for F in (DashboardPage, MyTasksPage, NotificationsPage, SettingsPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")  # Place the frame in the grid

        # Define themes for the app
        self.theme = "light"
        self.themes = {
            "light": {"bg": "#FFFFFF", "fg": "#000000"},
            "dark": {"bg": "#333333", "fg": "#FFFFFF"},
            "blue": {"bg": "#e0f7fa", "fg": "#00796b"}
        }

        # Show the default frame (DashboardPage)
        self.show_frame("DashboardPage")

    def show_frame(self, page_name):
        # Display the requested page by its name
        frame = self.frames[page_name]
        frame.tkraise()  # Bring the frame to the front
        frame.update_theme(self.theme)

    def apply_theme(self, theme):
        # Apply the selected theme to all frames
        self.theme = theme
        for frame in self.frames.values():
            frame.update_theme(theme)

class DashboardPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Dashboard label
        label = tk.Label(self, text="Dashboard", font=("Helvetica", 24))
        label.pack(pady=10)

        # Button to navigate to MyTasksPage
        button = tk.Button(self, text="Go to My Tasks", command=lambda: controller.show_frame("MyTasksPage"))
        button.pack()

    def update_theme(self, theme):
        # Update the background color based on the selected theme
        self.config(bg=self.controller.themes[theme]["bg"])

class MyTasksPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # My Tasks label
        label = tk.Label(self, text="My Tasks", font=("Helvetica", 24))
        label.pack(pady=10)

        # Button to sort tasks by due date
        sort_btn = tk.Button(self, text="Sort by Due Date", command=self.sort_by_due_date)
        sort_btn.pack(pady=5)

        # Button to filter tasks by priority
        filter_btn = tk.Button(self, text="Filter by Priority", command=self.filter_by_priority)
        filter_btn.pack(pady=5)

    def sort_by_due_date(self):
        # Placeholder for sorting functionality
        print("Sorting tasks by due date...")

    def filter_by_priority(self):
        # Placeholder for filtering functionality
        print("Filtering tasks by priority...")

    def update_theme(self, theme):
        # Update the background color based on the selected theme
        self.config(bg=self.controller.themes[theme]["bg"])

class NotificationsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Notifications label
        label = tk.Label(self, text="Notifications", font=("Helvetica", 24))
        label.pack(pady=10)

    def update_theme(self, theme):
        # Update the background color based on the selected theme
        self.config(bg=self.controller.themes[theme]["bg"])

class SettingsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Settings label
        label = tk.Label(self, text="Settings", font=("Helvetica", 24))
        label.pack(pady=10)

        # Radio buttons to select the theme
        self.theme_var = tk.StringVar(value="light")
        light_rb = tk.Radiobutton(self, text="Light Theme", variable=self.theme_var, value="light", command=self.set_theme)
        dark_rb = tk.Radiobutton(self, text="Dark Theme", variable=self.theme_var, value="dark", command=self.set_theme)
        blue_rb = tk.Radiobutton(self, text="Blue Theme", variable=self.theme_var, value="blue", command=self.set_theme)

        light_rb.pack(pady=5)
        dark_rb.pack(pady=5)
        blue_rb.pack(pady=5)

    def set_theme(self):
        # Apply the selected theme
        self.controller.apply_theme(self.theme_var.get())

    def update_theme(self, theme):
        # Update the background color based on the selected theme
        self.config(bg=self.controller.themes[theme]["bg"])

if __name__ == "__main__":
    # Start the Task Manager application
    app = TaskManagerApp()
    app.mainloop()
