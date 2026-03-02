# Tkinter GUI Test App

A simple Python GUI project built using **Tkinter**.  
This application demonstrates basic GUI concepts such as:
<img width="593" height="425" alt="image" src="https://github.com/user-attachments/assets/3a9d0aa1-bd61-4450-89e3-a3fa389e96c4" />

- Windows and layouts
- Frames
- Labels
- Text input fields
- Buttons
- Event handling

When the user enters text and presses a button, the label updates dynamically.

---

## 📸 Preview

The app creates a window containing:
- A styled label
- A text input box
- A button that updates the label text

---

## 🚀 Features

✅ Custom window styling  
✅ Multiple frames for layout organization  
✅ User text input handling  
✅ Button-triggered events  
✅ Dynamic label updates  
✅ Basic Tkinter styling (colors, fonts, padding)

---

## 🧱 Project Structure

```

tkinter-gui-test/
│
├── main.py        # Application source code
└── README.md      # Project documentation

````

---

## ⚙️ Requirements

- Python **3.8+**
- Tkinter (included with standard Python installation)

To check Python version:

```bash
python --version
````

---

## ▶️ Running the Project

1. Clone the repository:

```bash
git clone https://github.com/yourusername/tkinter-gui-test.git
```

2. Navigate into the project folder:

```bash
cd tkinter-gui-test
```

3. Run the program:

```bash
python main.py
```

---

## 🧠 How It Works

### 1. Window Creation

The program creates a main Tkinter window:

```python
root = tk.Tk()
```

It sets:

* Title
* Window size
* Background color

---

### 2. Layout System

Two frames are used to organize UI elements:

* **Frame 1** → contains the main label
* **Frame 2** → contains input field and button

This keeps the layout clean and modular.

---

### 3. User Input

The `Entry` widget allows users to type text:

```python
text_entry.get()
```

This retrieves the entered value.

---

### 4. Button Event

When the button is clicked:

```python
command=update_label
```

The function:

* Reads input text
* Checks if text exists
* Updates the label accordingly

---

### 5. Dynamic Label Update

If text is entered:

```
Entered text: 'your text'
```

If empty:

```
Button clicked. No text to show.
```

The label color also changes to yellow.

---

## 🎨 GUI Components Used

| Component | Purpose                 |
| --------- | ----------------------- |
| `Tk()`    | Main application window |
| `Frame`   | Layout grouping         |
| `Label`   | Display text            |
| `Entry`   | Text input              |
| `Button`  | User interaction        |

---

## 🛠️ Possible Improvements

Ideas for extending the project:

* ✅ Add multiple buttons
* ✅ Change colors dynamically
* ✅ Add keyboard shortcuts
* ✅ Save entered text to a file
* ✅ Add dark/light mode toggle
* ✅ Use grid layout instead of pack

---

## 📚 Learning Goals

This project helps beginners learn:

* Event-driven programming
* GUI layout management
* Widget configuration
* Tkinter basics
* Python UI development

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch
3. Make changes
4. Submit a pull request

---

## 📄 License

This project is open-source and available under the MIT License.

---

## 👨‍💻 Author

Created as a beginner Tkinter GUI learning project.

```

---

If you want, I can also make a **more “student assignment” version**, a **professional portfolio version**, or a **GitHub classroom rubric version** depending on what this is for.
```
