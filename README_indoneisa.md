![2025-03-06_11-33](https://github.com/user-attachments/assets/34c28d56-0ab9-481b-9cc8-1248ad1f03da)
# PysGhostIP - OSINT IP Scanner  

PysGhostIP adalah alat OSINT (Open Source Intelligence) berbasis Python yang dirancang untuk investigasi, analisis IP, pengintaian, dan pengumpulan informasi target. Alat ini menyediakan berbagai teknik untuk membantu Anda mengumpulkan informasi berharga tentang target tertentu.  

## 📌 Fitur  

Alat ini mencakup fitur-fitur berikut:  

- **DNS Enumeration:** Mengidentifikasi kebocoran IP melalui enumerasi DNS.  
- **Historical IP Lookup:** Mencari riwayat IP menggunakan SecurityTrails API (memerlukan kunci API).  
- **Direct IP Leak:** Mencoba menemukan IP asli secara langsung.  
- **WHOIS Lookup:** Mendapatkan informasi WHOIS tentang domain target.  
- **Port Scanning:** Memindai port terbuka pada target untuk mengidentifikasi layanan yang berjalan.  

---

## ⚙️ Instalasi  

Ikuti langkah-langkah di bawah ini untuk menginstal dan menjalankan alat ini.  

### Prasyarat  

- **Python 3:** Pastikan Python 3 telah terinstal. Anda dapat mengunduhnya dari [situs web Python](https://www.python.org/downloads/).  
- **pip:** `pip` adalah pengelola paket untuk Python dan biasanya sudah disertakan.  

### Klon Repository (Opsional)  

Jika Anda mengkloning repository dari GitHub, jalankan perintah berikut:  

```bash
git clone https://github.com/pyscodes/PysGhostIP.git
cd PysGhostIP
```

### Buat Lingkungan Virtual (Disarankan)  

Membuat lingkungan virtual direkomendasikan untuk mengisolasi dependensi proyek:  

```bash
python3 -m venv venv
```

Aktifkan lingkungan virtual:  

- **Linux/macOS:**  
  ```bash
  source venv/bin/activate
  ```
- **Windows:**  
  ```bash
  .\venv\Scripts\activate
  ```

### Instal Dependensi  

Gunakan `pip` untuk menginstal dependensi yang diperlukan:  

```bash
pip install -r requirements.txt
```

### Jalankan Alat  

Setelah instalasi selesai, jalankan alat ini dengan:  

```bash
python3 pysghostip.py
```

---

## 📌 Instalasi Berdasarkan Sistem Operasi  

### **🖥 Windows**  

- Pastikan **Python** telah ditambahkan ke **PATH** saat instalasi.  
- **Instal Nmap (Opsional):** Jika ingin menggunakan fitur **Port Scanning**, instal [Nmap](https://nmap.org/download.html) dan tambahkan direktori instalasi ke **PATH**.  
- Jalankan terminal sebagai **Administrator** jika diperlukan.  
- Perbarui `pip` jika diperlukan:  
  ```bash
  python -m pip install --upgrade pip
  ```

### **🐧 Linux**  

- Instal **Nmap** menggunakan perintah berikut:  
  ```bash
  sudo apt update && sudo apt install nmap  # Debian/Ubuntu
  sudo yum install nmap  # Fedora/CentOS/RHEL
  ```
- Jalankan dengan hak akses root jika diperlukan:  
  ```bash
  sudo python3 pysghostip.py
  ```

### **🍎 macOS**  

- Instal **Homebrew** jika belum ada:  
  ```bash
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
  ```
- Instal **Nmap** menggunakan Homebrew:  
  ```bash
  brew install nmap
  ```

### **📱 Termux (Android)**  

- Instal **Termux** dari Google Play Store atau F-Droid.  
- Perbarui paket:  
  ```bash
  pkg update
  ```
- Instal **Python** dan **Git**:  
  ```bash
  pkg install python git
  ```
- Instal **Nmap**:  
  ```bash
  pkg install nmap
  ```

---

## 📚 Penggunaan  

1. Jalankan alat ini dan pilih opsi dari menu utama.  
2. Beberapa fitur memerlukan domain atau alamat IP target.  
3. Ikuti petunjuk di layar untuk memasukkan informasi yang diperlukan.  

---

## ⚠️ Disclaimer  

- **Alat ini hanya untuk tujuan pendidikan dan pengujian.**  
- **Gunakan hanya pada sistem yang Anda miliki izin untuk diuji.**  
- **Penyalahgunaan alat ini dapat menyebabkan konsekuensi hukum.**  

---

## 🤝 Kontribusi  

Kontribusi sangat diterima! Jika Anda menemukan masalah atau memiliki saran untuk perbaikan, silakan buat **issue** atau **pull request** di repository GitHub kami.  

---

## 📞 Kontak & Support  

🔗 **GitHub:** [Pyscodes-pro](https://github.com/pyscodes-pro)  
📸 **Instagram:** [@pyscodes](https://instagram.com/pyscodes)  
🍵 **Dukung Saya:** [Linktree](https://linktr.ee/pyscodes)  

**Dibuat oleh:** 🛠 **PYSCODES-FSOCIETY GROUP**  

---

