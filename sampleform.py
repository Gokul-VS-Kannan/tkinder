import tkinter as tk
from tkinter import messagebox

# Function to handle form submission
def submit_form():
    name = entry_name.get()
    age = entry_age.get()
    gender = gender_var.get()
    email = entry_email.get()

    # Print the form data to the console
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Gender: {gender}")
    print(f"Email: {email}")

    # Display a confirmation message
    messagebox.showinfo("Form Submitted", "The form has been submitted successfully!")

# Create the main application window
root = tk.Tk()
root.title("Model Form Example")
root.geometry("400x300")

# Name Label and Entry
label_name = tk.Label(root, text="Name:")
label_name.pack(pady=5)
entry_name = tk.Entry(root, width=30)
entry_name.pack(pady=5)

# Age Label and Entry
label_age = tk.Label(root, text="Age:")
label_age.pack(pady=5)
entry_age = tk.Entry(root, width=30)
entry_age.pack(pady=5)

# Gender Label and Radiobuttons
label_gender = tk.Label(root, text="Gender:")
label_gender.pack(pady=5)
gender_var = tk.StringVar(value="Male")  # Default value
radio_male = tk.Radiobutton(root, text="Male", variable=gender_var, value="Male")
radio_female = tk.Radiobutton(root, text="Female", variable=gender_var, value="Female")
radio_male.pack()
radio_female.pack()

# Email Label and Entry
label_email = tk.Label(root, text="Email:")
label_email.pack(pady=5)
entry_email = tk.Entry(root, width=30)
entry_email.pack(pady=5)

# Submit Button
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.pack(pady=20)

# Run the application
root.mainloop()
