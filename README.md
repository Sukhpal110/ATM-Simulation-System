# 🏦 ATM Simulation System (Python + PostgreSQL)

A simple **ATM simulation system** built with **Python** and **PostgreSQL**.  
This project demonstrates how to perform **bank-like operations** (Deposit, Withdraw, Balance Check, PIN Generation) using database integration.

---

## 🚀 Features
- **PIN Verification** – Login with card number and PIN.  
- **OTP-Based PIN Generation** – Generate a new PIN using registered phone number.  
- **Deposit & Withdraw** – Securely update account balance.  
- **Balance Inquiry** – Check current account balance.  
- **Database Integration** – All transactions stored in PostgreSQL.  

---

## 📂 Project Structure
```
ATM-Simulation/
│── atm.py          # Main Python script
│── README.md        # Documentation
```

---

## ⚙️ Requirements
- Python 3.x  
- PostgreSQL  
- `psycopg2` library  

Install dependencies:
```bash
pip install -r requirements.txt
```

---

## 🛠️ Database Setup
1. Open PostgreSQL and create a database:
   ```sql
   CREATE DATABASE test;
   ```

2. Create the table:
   ```sql
   CREATE TABLE acc_details (
       acc_no BIGINT PRIMARY KEY CHECK (LENGTH(acc_no::TEXT) = 11) NOT NULL,
       name VARCHAR(100) NOT NULL,
       phone_no BIGINT CHECK (LENGTH(phone_no::TEXT) = 10) NOT NULL,
       balance DECIMAL(10, 2) NOT NULL,
       pin INT CHECK (LENGTH(pin::TEXT) = 4),
       card_no BIGINT UNIQUE CHECK (card_no >= 1000000000000000 AND card_no <= 9999999999999999)
   );
   ```

3. Insert sample records:
   ```sql
   INSERT INTO acc_details (acc_no, name, phone_no, balance, pin, card_no) 
   VALUES 
   (12345678901, 'John Doe', 9876543210, 1500.50, 1234, 1234123412341234),
   (23456789012, 'Jane Smith', 8765432109, 3200.75, 2345, 2345234523452345);
   ```

---

## ▶️ Usage
Run the ATM program:
```bash
python atm.py
```

Steps:
1. Enter your **card number**.  
2. If a PIN is not set → Verify with **phone number & OTP** → Set a new PIN.  
3. If PIN exists → Enter PIN to login.  
4. Choose an option:  
   - `1` Deposit  
   - `2` Withdraw  
   - `3` Check Balance  
   - `4` Quit  

---

## 🔮 Future Improvements
- Add **transaction history**.  
- Implement **GUI version** (Tkinter/Flask).  
- Add **password hashing** for PIN security.  




