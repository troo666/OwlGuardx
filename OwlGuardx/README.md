
### **How to Install Requirements and Run the Python Script**

#### **Step 1: Install Python 3**

If you don't have Python 3 installed yet, follow these steps:

1. **Download Python 3**:
   - Go to the official Python website: [https://www.python.org/downloads/](https://www.python.org/downloads/)
   - Download the latest version of Python 3 for your operating system (Windows, macOS, or Linux).

2. **Install Python 3**:
   - On **Windows**, during installation, **make sure to check the box** that says "Add Python to PATH."
   - On **macOS/Linux**, Python 3 is usually pre-installed. If not, you can install it using Homebrew (macOS) or your package manager (Linux).

---

#### **Step 2: Install the Required Libraries**

Now that Python 3 is installed, you need to install the required dependencies for the script.

1. **Navigate to your project folder** where the `OwlGuardx.py` file and the `requirements.txt` file are located. You can do this using the terminal/command prompt:

   **For Windows**:
   - Open **Command Prompt** (press `Win + R`, type `cmd`, and press Enter).
   - Use the `cd` command to navigate to the folder where your `OwlGuardx.py` file is located:
     ```bash
     cd path\to\your\OwlGuardx
     ```

   **For macOS/Linux**:
   - Open **Terminal**.
   - Use the `cd` command to navigate to the folder where your `OwlGuardx.py` file is located:
     ```bash
     cd path/to/your/OwlGuardx
     ```

2. **Install the required libraries** by running the following command:

   ```bash
   pip3 install -r requirements.txt
   ```

   This will install all the dependencies listed in the `requirements.txt` file. The necessary libraries are:
   - **requests** – for making HTTP requests to the HIBP API.
   - **colorama** – for adding colors to your terminal output.

   If you're using **Windows** and `pip3` doesn't work, try using `pip` instead:

   ```bash
   pip install -r requirements.txt
   ```

---

#### **Step 3: Run the Python Script**

Once the dependencies are installed, you can run the Python script. Here’s how:

1. In the terminal/command prompt, navigate to the folder where the `OwlGuardx.py` file is located (if you haven't done that yet).

2. **Run the Python script** with Python 3 by using the following command:

   **For Windows**:
   ```bash
   python OwlGuardx.py
   ```

   **For macOS/Linux**:
   ```bash
   python3 OwlGuardx.py
   ```

   If everything is set up correctly, the script should now execute, and you will see the output in the terminal.

---

#### **Step 4: Done!**

- After running the script, the program will check passwords and display the results.
- When you’re done, simply close the terminal or press `Ctrl + C` to stop the script.

---

### **Summary**

1. **Install Python 3** from the official website.
2. **Navigate to your project folder** in the terminal/command prompt.
3. **Install dependencies** with `pip3 install -r requirements.txt`.
4. **Run the Python script** with `python OwlGuardx.py` (or `python3` on macOS/Linux).

That's it! If you need any further assistance, feel free to ask.

