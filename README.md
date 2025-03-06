![2025-03-06_11-33](https://github.com/user-attachments/assets/34c28d56-0ab9-481b-9cc8-1248ad1f03da)

---

# PysGhostIP - OSINT IP Scanner  

PysGhostIP is a Python-based OSINT (Open Source Intelligence) tool designed for investigation, IP analysis, reconnaissance, and target information gathering. This tool provides various techniques to help you collect valuable information about a specific target.  

## 📌 Features  

This tool includes the following features:  

- **DNS Enumeration:** Identify IP leaks through DNS enumeration.  
- **Historical IP Lookup:** Retrieve IP history using the SecurityTrails API (API key required).  
- **Direct IP Leak:** Attempt to find the real IP directly.  
- **WHOIS Lookup:** Obtain WHOIS information about the target domain.  
- **Port Scanning:** Scan open ports on the target to identify running services.  

---

## ⚙️ Installation  

Follow the steps below to install and run this tool.  

### Prerequisites  

- **Python 3:** Ensure Python 3 is installed. You can download it from the [Python website](https://www.python.org/downloads/).  
- **pip:** `pip` is the package manager for Python and is usually included.  

###  Clone Repository (Optional)  

If you are cloning the repository from GitHub, run the following command:  

```bash
git clone https://github.com/pyscodes/PysGhostIP.git
cd PysGhostIP
```

###  Create a Virtual Environment (Recommended)  

Creating a virtual environment is recommended to isolate project dependencies:  

```bash
python3 -m venv venv
```

Activate the virtual environment:  

- **Linux/macOS:**  

  ```bash
  source venv/bin/activate
  ```

- **Windows:**  

  ```bash
  .\venv\Scripts\activate
  ```

###  Install Dependencies  

Use `pip` to install the required dependencies:  

```bash
pip install -r requirements.txt
```
###  Run the Tool  

Once installation is complete, run the tool using:  

```bash
python3 pysghostip.py
```

---

## 📌 OS-Specific Installation  

### **🖥 Windows**  

- Ensure **Python** is added to **PATH** during installation.  
- **Install Nmap (Optional):** If you want to use the **Port Scanning** feature, install [Nmap](https://nmap.org/download.html) and add its installation directory to **PATH**.  
- Run the terminal as **Administrator** if needed.  
- Update `pip` if necessary:  

  ```bash
  python -m pip install --upgrade pip
  ```

### **🐧 Linux**  

- Install **Nmap** using the following command:  

  ```bash
  sudo apt update && sudo apt install nmap  # Debian/Ubuntu
  sudo yum install nmap  # Fedora/CentOS/RHEL
  ```

- Run with root privileges if required:  

  ```bash
  sudo python3 pysghostip.py
  ```

### **🍎 macOS**  

- Install **Homebrew** if not already installed:  

  ```bash
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
  ```

- Install **Nmap** using Homebrew:  

  ```bash
  brew install nmap
  ```

### **📱 Termux (Android)**  

- Install **Termux** from Google Play Store or F-Droid.  
- Update packages:  

  ```bash
  pkg update
  ```

- Install **Python** and **Git**:  

  ```bash
  pkg install python git
  ```

- Install **Nmap**:  

  ```bash
  pkg install nmap
  ```

---

## 📖 Usage  

1. Run the tool and select an option from the main menu.  
2. Some features require a domain or target IP address.  
3. Follow the on-screen instructions to input the necessary information.  

---

## ⚠️ Disclaimer  

- **This tool is for educational and testing purposes only.**  
- **Use it only on systems you have explicit permission to test.**  
- **Misuse of this tool may lead to legal consequences.**  

---

## 🤝 Contribution  

Contributions are highly welcomed! If you find any issues or have suggestions for improvements, feel free to create an **issue** or **pull request** in our GitHub repository.  

---

## 📞 Contact & Support  

🔗 **GitHub:** [Pyscodes-pro](https://github.com/pyscodes-pro)  
📸 **Instagram:** [@pyscodes](https://instagram.com/pyscodes)  
☕ **Support Me:** [Linktree](https://linktr.ee/pyscodes)  

**Developed by:** 🛠 **PYSCODES-FSOCIETY GROUP**  

---
