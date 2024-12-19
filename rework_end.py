import customtkinter
import os
from tkinter import messagebox
from PIL import Image
from app_logic.csv_handler import get_csv_name
from app_logic.csv_handler import check_ref
from app_logic.csv_handler import read_from_csv
from app_logic.csv_handler import save_to_csv
from app_logic.csv_handler import update_csv
from app_logic.print_label import generate_label
from datetime import datetime


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("START REWORK STATION")
        self.geometry("1050x800")
        self.operator = ""

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_images")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "rework_icon.png")), size=(50, 50))
        self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "Rework-OUT.png")), size=(500, 170))
        self.large_login_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "Reworkstart.png")), size=(500, 150))
        self.info_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "infoout.png")), size=(500, 100))
        self.login_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "login.png")), size=(300, 300))
        self.qrcode_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "qrcode.png")), size=(300, 300))
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "image_icon_light.png")), size=(20, 20))
        self.user_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "user.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "user.png")), size=(30, 30))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "home_light.png")), size=(20, 20))
        self.chat_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "chat_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "chat_light.png")), size=(20, 20))
        self.add_user_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "add_user_dark.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "add_user_light.png")), size=(20, 20))

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="  Rework station", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=20, weight="bold"), text_color="red")
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Home",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.settings_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="SETTINGS",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.chat_image, anchor="w", command=self.settings_button_event)
        self.settings_button.grid(row=2, column=0, sticky="ew")

        self.data_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="DATA",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.add_user_image, anchor="w", command=self.data_button_event)
        self.data_button.grid(row=3, column=0, sticky="ew")

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Light", "Dark", "System"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")
        
        # create login frame
        self.login_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.login_frame.grid_columnconfigure(0, weight=1)
        
        self.login_frame_large_image_label = customtkinter.CTkLabel(self.login_frame, text="", image=self.large_login_image)
        self.login_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)
        self.login_frame_image_label = customtkinter.CTkLabel(self.login_frame, text="", image=self.login_image)
        self.login_frame_image_label.grid(row=1, column=0, padx=20, pady=10)
        
        # Matricule Input
        self.login_frame_entry_1 = customtkinter.CTkEntry(self.login_frame, placeholder_text="ex: 12345",
                                                         height=50,
                                                         width=400,
                                                         font=("Helvetica", 30),
                                                         corner_radius=10,
                                                         text_color="black",
                                                         placeholder_text_color="#fc9522",
                                                         fg_color=("#b9dbfc"),
                                                         state="normal")
        self.login_frame_entry_1.grid(row=2, column=0, padx=20, pady=0)
        
        self.login_button = customtkinter.CTkButton(self.login_frame,
                                                    corner_radius=10,
                                                    height=60,
                                                    width=200,
                                                    border_spacing=10,
                                                    text="Login",
                                                    fg_color=("#066603"),
                                                    text_color=("gray10", "gray90"),
                                                    hover_color=("gray70", "gray30"),
                                                    image=self.user_image,
                                                    font=customtkinter.CTkFont(size=20, weight="bold"),
                                                    command=self.login_button_event)
        self.login_button.grid(row=4, column=0, padx=20, pady=40)
        # create home frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)

        self.home_frame_large_image_label = customtkinter.CTkLabel(self.home_frame, text="", image=self.large_test_image)
        self.home_frame_large_image_label.grid(row=0, column=0, padx=20, pady=0)

        self.home_frame_label = customtkinter.CTkLabel(self.home_frame,
                                                       text="",
                                                       image=self.info_image)
        self.home_frame_label.grid(row=1, column=0, padx=20, pady=0)
        self.home_frame_image_label = customtkinter.CTkLabel(self.home_frame, text="", image=self.qrcode_image)
        self.home_frame_image_label.grid(row=2, column=0, padx=20, pady=10)
        
        # scan QR code
        self.home_frame_entry_1 = customtkinter.CTkEntry(self.home_frame, placeholder_text="SCAN QR CODE LABEL",
                                                         height=50,
                                                         width=400,
                                                         font=("Helvetica", 30),
                                                         corner_radius=10,
                                                         text_color="black",
                                                         placeholder_text_color="#fc9522",
                                                         fg_color=("#b9dbfc"),
                                                         state="normal",
                                                         show='*')
        self.home_frame_entry_1.grid(row=3, column=0, padx=20, pady=0)
        
        # Button save and Print
        self.home_frame_button_1 = customtkinter.CTkButton(self.home_frame,
                                                           text="Save and Print",
                                                           font=customtkinter.CTkFont(size=17, weight="bold"),
                                                           command=self.on_submit,
                                                           fg_color=("#066603"),
                                                           height=50,
                                                           width=200)
        self.home_frame_button_1.grid(row=5, column=0, padx=20, pady=20)
        # create second frame
        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # create third frame
        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # select default frame
        self.select_frame_by_name("login")
        
        #enter key event
        self.login_frame_entry_1.bind("<Return>", self.login_button_event)
        self.home_frame_entry_1.bind("<Return>", self.on_submit)

    def on_submit(self, event=None):
        """save harness info"""
        filename = get_csv_name('end_rework')
        label_data = {}
        csv_data = []
        label_data['OPERATOR'] = self.operator
        csv_data.append(self.operator)
        # check Reference
        qr_code = self.home_frame_entry_1.get()
        reword_data = qr_code.split(';')
        if len(reword_data) < 3:
            self.home_frame_entry_1.delete(0, customtkinter.END)
            messagebox.showerror("Error", "Invalid QRCode!!!")
            return
        ref = check_ref(reword_data[1])
        if ref is None:
            self.home_frame_entry_1.delete(0, customtkinter.END)
            messagebox.showerror("Error", "Invalid Reference!!!")
            return
        label_data['PROJECT'] = ref[0]
        csv_data.append(ref[0])
        label_data['REFERENCE'] = ref[1]
        csv_data.append(ref[1])
        csv_data.append('None')
        csv_data.append('None')
        # Rework Card Check
        rework_card = reword_data[0]
        path = 'data/data_rework/{}'.format(filename)
        data = read_from_csv(path, rework_card)
        if data:
            self.home_frame_entry_1.delete(0, customtkinter.END)
            messagebox.showerror("Error", "Harness Already Exist!!!")
            return
        csv_data.append(rework_card)
        # check Fault Description
        csv_data.append('None')
        # check Failure Process
        csv_data.append('None')
        start_time = datetime.strptime(reword_data[2], "%Y-%m-%d %H:%M:%S")
        csv_data.append(start_time)
        end_time = datetime.now()
        csv_data.append(end_time.strftime("%Y-%m-%d %H:%M:%S"))
        rework_time = end_time - start_time
        rework_time = rework_time.total_seconds() / 60
        csv_data.append(round(rework_time, 2))
        label_data['DATETIME'] = end_time.strftime("%Y-%m-%d %H:%M:%S")
        label_data['REWORKDATA'] = rework_card
        label_data['REWORKTIME'] = rework_card
        
        # print Label
        generate_label(rework_card, 'end', label_data)
        # save data to csv
        save_to_csv(path,csv_data)
        self.home_frame_entry_1.delete(0, customtkinter.END)
        
    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.settings_button.configure(fg_color=("gray75", "gray25") if name == "settings" else "transparent")
        self.data_button.configure(fg_color=("gray75", "gray25") if name == "data" else "transparent")

        # show selected frame
        if name == "login":
            self.login_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.login_frame.grid_forget()
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "settings":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "data":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()

    def login_button_event(self, event=None):
        self.operator = self.login_frame_entry_1.get()
        if self.operator == "" or len(self.operator) != 5:
            self.login_frame_entry_1.delete(0, customtkinter.END)
            messagebox.showerror("Error", "Invalid Operator Code!!!")
            self.operator = ""
            return
        self.select_frame_by_name("home")
        self.login_frame_entry_1.delete(0, customtkinter.END)

    def home_button_event(self):
        self.operator = ""
        self.select_frame_by_name("login")

    def settings_button_event(self):
        self.select_frame_by_name("settings")

    def data_button_event(self):
        self.select_frame_by_name("data")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def clear_home_entries(self):
        """clear entries"""
        self.home_frame_entry_1.delete(0, customtkinter.END)
        self.home_frame_entry_2.delete(0, customtkinter.END)
        self.home_frame_entry_3.delete(0, customtkinter.END)
        self.home_frame_entry_4.delete(0, customtkinter.END)
        self.home_frame_entry_5.delete(0, customtkinter.END)
        self.home_frame_entry_6.delete(0, customtkinter.END)

if __name__ == "__main__":
    app = App()
    app.mainloop()