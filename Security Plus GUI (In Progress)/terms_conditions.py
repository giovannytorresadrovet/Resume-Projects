import tkinter as tk
from tkinter import messagebox

class TermsConditionsWindow(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Terms and Conditions")
        self.geometry("800x600")  # Keep the same size

        # Frame for the terms text with a scrollbar
        text_frame = tk.Frame(self)
        text_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Scrollable Text widget
        scrollbar = tk.Scrollbar(text_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        terms_textbox = tk.Text(text_frame, wrap=tk.WORD, yscrollcommand=scrollbar.set, font=("Arial", 12))
        terms_textbox.insert(tk.END, (
            "By using this software, you agree to the following terms and conditions...\n\n"
            "1. You will not share the content of this test with others.\n"
            "2. You will not attempt to reverse engineer the software.\n"
            "3. You agree that this software is provided as-is without any warranties.\n\n"
            "Please read all the terms carefully before proceeding."
        ))
        terms_textbox.config(state=tk.DISABLED)  # Make the text read-only
        terms_textbox.pack(fill=tk.BOTH, expand=True)
        scrollbar.config(command=terms_textbox.yview)

        # Frame for the buttons
        button_frame = tk.Frame(self)
        button_frame.pack(pady=10)

        accept_button = tk.Button(button_frame, text="Accept", command=self.accept_terms, bg="green", font=("Arial", 14), width=12)
        accept_button.pack(side=tk.LEFT, padx=20)

        not_accept_button = tk.Button(button_frame, text="Not Accept", command=self.not_accept_terms, bg="red", font=("Arial", 14), width=12)
        not_accept_button.pack(side=tk.LEFT, padx=20)

    def accept_terms(self):
        # Confirm acceptance
        if messagebox.askyesno("Confirm Acceptance", "Do you confirm that you have read and accept the terms and conditions?"):
            messagebox.showinfo("Accepted", "You have accepted the terms and conditions.")
            self.destroy()  # Close the terms window after acceptance

    def not_accept_terms(self):
        # Handle non-acceptance of terms
        messagebox.showwarning("Not Accepted", "You must accept the terms and conditions to proceed.")
        self.lift()  # Bring the Terms and Condition window to the front
