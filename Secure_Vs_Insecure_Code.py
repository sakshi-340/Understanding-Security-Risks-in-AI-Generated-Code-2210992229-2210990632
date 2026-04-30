"""
Research Justification: Understanding Security Risks in AI-Generated Code
Authors: Sakshi Rani & Palak  [cite: 2, 6]
This script demonstrates the 1.8x vulnerability density found in AI code[cite: 22, 46].
"""

import sqlite3
import os
import threading
import time

# =================================================================
# CASE STUDY 1: SQL Injection (CWE-89)
# =================================================================

def login_handler_insecure(username, password):
    # Vulnerable: AI suggests direct string interpolation [cite: 168]
    # This allows 'OR 1=1' attacks to bypass authentication [cite: 170]
    sql_query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    return f"Executing Insecure Query: {sql_query}"

def login_handler_secure(username, password):
    # Mitigation: Use Parameterized queries as recommended [cite: 101, 229]
    # The database driver handles sanitization, preventing injection [cite: 231]
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    return "Executing Secure Parameterized Query"


# =================================================================
# CASE STUDY 2: Hard-coded Credentials (CWE-798)
# =================================================================

def upload_to_s3_insecure():
    # Vulnerable: AI provides hard-coded placeholders [cite: 174]
    # Developers often forget to remove these, leading to leaks [cite: 175, 176]
    aws_access_key_id = "AKIA-DUMMY-KEY-123" 
    aws_secret_access_key = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
    print(f"VULNERABILITY: Credentials {aws_access_key_id[:4]}... leaked in code.")

def upload_to_s3_secure():
    # Mitigation: Loading from Environment Variables [cite: 101]
    # Prevents sensitive data from being committed to version control [cite: 230]
    access_key = os.getenv('AWS_ACCESS_KEY_ID', 'NOT_FOUND')
    if access_key == 'NOT_FOUND':
        print("SUCCESS: No credentials found in source code.")


# =================================================================
# CASE STUDY 3: Race Condition (CWE-362)
# =================================================================

shared_counter = 0
shared_counter_secure = 0
counter_lock = threading.Lock()

def process_file_insecure():
    global shared_counter
    # Vulnerable: Non-atomic increment suggested by AI [cite: 181]
    # Under production load, this causes data corruption [cite: 183, 184]
    temp = shared_counter
    time.sleep(0.000001) # Simulating processing delay
    shared_counter = temp + 1

def process_file_secure():
    global shared_counter_secure
    # Mitigation: Thread primitives (Locking) 
    with counter_lock:
        shared_counter_secure += 1

# =================================================================
# EXECUTION BLOCK (Proof of Concept)
# =================================================================

if __name__ == "__main__":
    print("--- 1. SQL INJECTION DEMO ---")
    print(login_handler_insecure("' OR '1'='1' --", "password"))
    
    print("\n--- 2. CREDENTIAL LEAK DEMO ---")
    upload_to_s3_insecure()
    upload_to_s3_secure()

    print("\n--- 3. RACE CONDITION DEMO (Running 100 threads) ---")
    threads_insecure = [threading.Thread(target=process_file_insecure) for _ in range(100)]
    threads_secure = [threading.Thread(target=process_file_secure) for _ in range(100)]

    for t in threads_insecure: t.start()
    for t in threads_insecure: t.join()
    
    for t in threads_secure: t.start()
    for t in threads_secure: t.join()

    print(f"Insecure Counter: {shared_counter} (Likely < 100 due to Race Condition)")
    print(f"Secure Counter: {shared_counter_secure} (Exactly 100)")
