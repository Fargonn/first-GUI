import tkinter as tk

root=tk.Tk()
root.title("tkinter GUI test")
root.geometry("600x400")
root.config(bg="#f0f0f0")

def update_label():
    input_text=text_entry.get()

    if input_text:
        new_text=f"Entered text: '{input_text}'"
    else:
        new_text=f"Button clicked. No text to show."
    
    main_label.config(
        text=new_text,
        fg="yellow"
    )

frame1=tk.Frame(root, bg="#FF8800", padx=15, pady=15)
frame1.pack(pady=10, padx=15)

frame2=tk.Frame(root, bg="#D400FF", padx=15, pady=15)
frame2.pack(pady=10, padx=15)

main_label=tk.Label(
    frame1,
    text="Hello. Create a large green label.",
    font=("Arial", 16, "bold"),
    fg="#00FF00",
    bg="#0099FF"
)
main_label.pack()

text_entry=tk.Entry(
    frame2,
    width=35,
    font=("Arial", 12),
    bd=2,
    relief=tk.SUNKEN
)
text_entry.pack(pady=10)

action_button=tk.Button(
    frame2,
    text="Update label",
    command=update_label,
    font=("Arial", 12),
    bg="#FF0000",
    fg="#FFFFFF",
    activebackground="#990000"
)
action_button.pack(pady=10, ipadx=10, ipady=5)

root.mainloop()