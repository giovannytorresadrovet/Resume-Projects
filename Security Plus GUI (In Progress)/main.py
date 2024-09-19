import tkinter as tk #For GUI
from tkinter import messagebox #For Terms and Conditions
import base64
from io import BytesIO
from PIL import Image, ImageTk
from logo_base64 import image_base64 #Import the Base64 image string
from terms_conditions import TermsConditionsWindow #Import the T&C Window class

class WelcomeWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Security+ 701 Practice Test")
        self.geometry("1200x800") # Width x Height in pixels
        self.terms_window = None #Initialize terms_window to None

        # Load and display the Security+ logo
        self.load_logo()

        # Welcome message
        self.welcome_label = tk.Label(self, text="Welcome to the Security+ 701 Practice Test!", font=("Arial", 24))
        self.welcome_label.pack(pady=10)

        # Introduction message
        intro_message = (
            "The process of answering a test question is our ultimate test of knowledge.\n"
            "After hours of video watching, book reading, and note taking, do you really\n"
            "know the material? If you're trying to prove yourself, nothing beats getting the\n"
            "right answer.\n\n"
            "This book contains three sample exams containing performance-based and\n"
            "multiple-choice questions for the Security+ exam. I've personally curated every\n"
            "question to make sure this Q&A matches the expectations of the SY0-701\n"
            "Security+ exam.\n\n"
            "I hope this book will help you be the smartest one in the room. Best of luck\n"
            "with your studies!\n\n"
            "- Professor Messer"
        )
        self.intro_label = tk.Label(self, text=intro_message, font=("Arial", 14), justify="left", wraplength=700)
        self.intro_label.pack(pady=10)

        # Continue button
        self.continue_button = tk.Button(self, text="Continue", command=self.go_to_next_page, bg="white", font=("Arial", 14))
        self.continue_button.pack(pady=20)

    def load_logo(self):
        # Base64 encoded image string
        image_data = base64.b64decode(image_base64)
        image = Image.open(BytesIO(image_data))
        
        # Decode the Base64 string
        image_data = base64.b64decode(image_base64)
        image = Image.open(BytesIO(image_data))
        photo = ImageTk.PhotoImage(image)

        # Resize the image to make it smaller
        image = image.resize((150, 75), Image.LANCZOS)  # Adjust the size (width, height) as needed

        # Create a Label to display the image
        self.logo_label = tk.Label(self.master, image=photo)
        self.logo_label.image = photo  # Keep a reference to avoid garbage collection
        self.logo_label.pack(pady=10)  # Adjust padding as needed

    def go_to_next_page(self):
        if self.terms_window is None or not self.terms_window.winfo_exists():
            self.terms_window = TermsConditionsWindow(self)
        else:
            self.terms_window.lift()

if __name__ == "__main__":
    app = WelcomeWindow()
    app.mainloop()
