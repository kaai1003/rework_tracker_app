import customtkinter as ctk

# Initialize the app
app = ctk.CTk()
app.title("REWORK STATION")
app.geometry("1024x720")

# Helper function to manage frame visibility
def show_frame(frame):
    frame2.pack_forget()
    frame3.pack_forget()
    frame4.pack_forget()
    frame5.pack_forget()
    frame.pack(side="top", fill="x")

# Frame 1: Menu Bar (always visible)
frame1 = ctk.CTkFrame(app, width=1024, height=50)
frame1.pack_propagate(False)
frame1.pack(side="top", fill="x")

menu_button_settings = ctk.CTkButton(frame1, text="Settings", width=10)
menu_button_settings.pack(side="left", padx=10, pady=5)

menu_button_exit = ctk.CTkButton(frame1, text="Exit", width=10, command=app.quit)
menu_button_exit.pack(side="right", padx=10, pady=5)

# Frame 2: Operator Code Input (default on app launch)
frame2 = ctk.CTkFrame(app, width=1024, height=650)
frame2.pack_propagate(False)

label_operator_code = ctk.CTkLabel(frame2, text="Enter Operator Code", font=("Arial", 18))
label_operator_code.pack(pady=10)

textbox_operator_code = ctk.CTkEntry(frame2, width=200)
textbox_operator_code.pack(pady=5)

button_submit_operator = ctk.CTkButton(
    frame2,
    text="Submit",
    command=lambda: show_frame(frame3)  # Go to frame3 on submit
)
button_submit_operator.pack(pady=20)

# Frame 3: Start and Finish Buttons
frame3 = ctk.CTkFrame(app, width=1024, height=650)
frame3.pack_propagate(False)

start_button = ctk.CTkButton(
    frame3,
    text="Start Rework",
    width=200,
    height=200,
    corner_radius=100,
    fg_color="green",
    command=lambda: show_frame(frame5)  # Go to frame5 on Start Rework
)
start_button.pack(side="left", padx=20, pady=20)

finish_button = ctk.CTkButton(
    frame3,
    text="Finish Rework",
    width=200,
    height=200,
    corner_radius=100,
    fg_color="red",
    command=lambda: show_frame(frame4)  # Go to frame4 on Finish Rework
)
finish_button.pack(side="right", padx=20, pady=20)

# Frame 4: Form for Reference Harness and Rework Card
frame4 = ctk.CTkFrame(app, width=1024, height=650)
frame4.pack_propagate(False)

label_form_4 = ctk.CTkLabel(frame4, text="Form", font=("Arial", 18))
label_form_4.pack(pady=10)

label_reference_harness = ctk.CTkLabel(frame4, text="Reference Harness", font=("Arial", 14))
label_reference_harness.pack(pady=5)
input_reference_harness = ctk.CTkEntry(frame4, width=300)
input_reference_harness.pack(pady=5)

label_rework_card = ctk.CTkLabel(frame4, text="Rework Card", font=("Arial", 14))
label_rework_card.pack(pady=5)
input_rework_card = ctk.CTkEntry(frame4, width=300)
input_rework_card.pack(pady=5)

button_save_print_4 = ctk.CTkButton(
    frame4,
    text="Save and Print",
    width=150,
    command=lambda: show_frame(frame2)  # Return to frame2
)
button_save_print_4.pack(pady=20)

# Frame 5: Form for Scan QR Code
frame5 = ctk.CTkFrame(app, width=1024, height=650)
frame5.pack_propagate(False)

label_form_5 = ctk.CTkLabel(frame5, text="Form", font=("Arial", 18))
label_form_5.pack(pady=10)

label_scan_qr = ctk.CTkLabel(frame5, text="Scan QR Code", font=("Arial", 14))
label_scan_qr.pack(pady=5)
input_scan_qr = ctk.CTkEntry(frame5, width=300)
input_scan_qr.pack(pady=5)

button_save_print_5 = ctk.CTkButton(
    frame5,
    text="Save and Print",
    width=150,
    command=lambda: show_frame(frame2)  # Return to frame2
)
button_save_print_5.pack(pady=20)

# Show Frame 2 on app start
show_frame(frame2)

# Start the app
app.mainloop()
