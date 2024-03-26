import threading
import time

class BankAccount:
    def __init__(self, initial_balance):
        self.balance = initial_balance
        self.lock = threading.Lock()

    def deposit(self, amount):
        if amount > 0:
            with self.lock:
                self.balance += amount
                print(f"Deposited {amount} units. New balance: {self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0:
            with self.lock:
                if amount <= self.balance:
                    self.balance -= amount
                    print(f"Withdrew {amount} units. New balance: {self.balance}")
                else:
                    print("Insufficient funds.")
        else:
            print("Invalid withdrawal amount.")


# Example usage:
account = BankAccount(1000)  # Starting balance of 1000 units
def make_withdrow(account, amount):
    account.withdraw(amount)

def make_deposit(account, amount):
    account.deposit(amount)

# Simulate concurrent deposits from multiple sources
threads = []
start = time.perf_counter()
for i in range(5):
    t = threading.Thread(target=make_withdrow, args=(account, 300))
    threads.append(t)
    print(f"(thread {i} started now")
    print(account.balance)
    t.start()

# Wait for all threads to complete
for t in threads:
    t.join()
end = time.perf_counter()
total_time = end - start
print(total_time)

# After all deposits, try a withdrawal
account.withdraw(600)



