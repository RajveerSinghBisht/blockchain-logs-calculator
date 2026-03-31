# 🔐 Blockchain-Based Log Integrity Analysis  
### *(Comparative Study using Cryptographic Hashing & Blockchain)*

<p align="center">
  <img src="https://img.shields.io/badge/Focus-Blockchain%20Analysis-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Hashing-SHA--256-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Platforms-Ganache-purple?style=for-the-badge" />
</p>

---

## 🚀 Overview

This project is **not a full blockchain logging system**, but a **comparative study** that explores how blockchain can be used to verify log integrity.

The focus is on analyzing:

- ⚡ **Latency**
- 💰 **Transaction Cost**
- 📊 **Throughput**
- ⏱️ **Verification Time**

across different blockchain platforms like **Solana** and **Cardano**.

---

## 🧠 Core Idea

Instead of storing logs directly, we:
Log Data → SHA-256 Hash → Store Hash on Blockchain

Later:
Recalculate Hash → Compare with Blockchain → Detect Changes


✔️ If hashes match → Data is authentic  
❌ If hashes differ → Data has been modified  

---

## 🎯 Objective

The goal of this project is to:

- Evaluate blockchain performance for log verification    
- Measure cost, speed, and efficiency  
- Understand feasibility of blockchain-based integrity systems  

---

## 📊 What This Study Analyzes

| Metric            | Description |
|------------------|------------|
| ⚡ Latency        | Time taken to confirm transaction |
| 💰 Cost           | Transaction fee per log |
| 📊 Throughput     | Number of transactions per second |
| ⏱️ Verification   | Time to validate log integrity |

---

## 🖼️ Conceptual Understanding

<p align="center">
  <img src="./images/conceptual-diagram.png" width="80%" />
</p>

> Hashing ensures that even a small change in data produces a completely different output, making tampering detectable.

---

## ⚙️ Tech Used

- **Node.js** → Processing  
- **SHA-256** → Hash generation  
- **Ganache** → Local Blockchain platforms  
- **Python** → Writing Code  

---

## 🛠️ Setup & Usage

---

### 1. Clone the Repository

```bash
git clone https://github.com/RajveerSinghBisht/blockchain-logs-calculator.git
cd blockchain-log-calculator
```
### 2. Install Dependencies

```bash
npm install
```
### 3. Create Required File (IMPORTANT)
```bash
You must create a file named:
results.csv

👉 Place it in the root directory of the project.

This file will store:
-transaction time
-cost
-verification results
```
### 4. Run the Project
```bash
python experiment.py
```
