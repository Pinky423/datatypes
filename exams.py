import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime


class ExpenseTracker:

    VALID_CATEGORIES = [
        "Food",
        "Transport",
        "Utilities",
        "Entertainment",1

    ]

    def __init__(self, filename="expenses.csv"):
        self.filename = filename
1
        try:
            self.df = pd.read_csv(filename)

            if not self.df.empty:
                self.df["Date"] = pd.to_datetime(self.df["Date"])

        except FileNotFoundError:
            self.df = pd.DataFrame(
                columns=["Date", "Amount", "Category", "Description"]
            )
            self.save_data()

  
    def save_data(self):
        self.df.to_csv(self.filename, index=False)

    def add_expense(self, date, amount, category, description):

        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format! Use YYYY-MM-DD")
            return

        if amount <= 0:
            print("Amount must be greater than 0.")
            return

        if category not in self.VALID_CATEGORIES:
            print("Invalid category!")
            print("Choose from:", self.VALID_CATEGORIES)
            return

        new_expense = pd.DataFrame({
            "Date": [date],
            "Amount": [amount],
            "Category": [category],
            "Description": [description]
        })

        self.df = pd.concat(
            [self.df, new_expense],
            ignore_index=True
        )

        self.save_data()

        print("Expense added successfully!")

    def get_summary(self):

        if self.df.empty:
            print("No expenses available.")
            return

        amounts = self.df["Amount"].to_numpy()

        total = np.sum(amounts)
        average = np.mean(amounts)
        maximum = np.max(amounts)
        minimum = np.min(amounts)

        print("\n===== EXPENSE SUMMARY =====")
        print(f"Total Expenses : ${total:.2f}")
        print(f"Average Expense: ${average:.2f}")
        print(f"Highest Expense: ${maximum:.2f}")
        print(f"Lowest Expense : ${minimum:.2f}")

    def filter_expenses(
            self,
            category=None,
            start_date=None,
            end_date=None,
            min_amount=None,
            max_amount=None
    ):

        filtered = self.df.copy()

        if category:
            filtered = filtered[
                filtered["Category"] == category
            ]

        if start_date:
            filtered = filtered[
                pd.to_datetime(filtered["Date"])
                >= pd.to_datetime(start_date)
            ]

        if end_date:
            filtered = filtered[
                pd.to_datetime(filtered["Date"])
                <= pd.to_datetime(end_date)
            ]

        if min_amount:
            filtered = filtered[
                filtered["Amount"] >= min_amount
            ]

        if max_amount:
            filtered = filtered[
                filtered["Amount"] <= max_amount
            ]

        return filtered

    def generate_report(self):

        if self.df.empty:
            print("No data available.")
            return

        print("\n========== REPORT ==========")

        total_expense = self.df["Amount"].sum()
        avg_expense = self.df["Amount"].mean()

        print(f"Total Spending : ${total_expense:.2f}")
        print(f"Average Spending: ${avg_expense:.2f}")

        print("\nExpenses by Category:")
        category_summary = self.df.groupby(
            "Category"
        )["Amount"].sum()

        print(category_summary)

        top_category = category_summary.idxmax()

        print(f"\nTop Spending Category: {top_category}")

    def monthly_analysis(self):

        if self.df.empty:
            print("No data available.")
            return

        temp_df = self.df.copy()

        temp_df["Date"] = pd.to_datetime(temp_df["Date"])

        temp_df["Month"] = temp_df["Date"].dt.to_period("M")

        monthly = temp_df.groupby(
            "Month"
        )["Amount"].sum()

        print("\nMonthly Expenses:")
        print(monthly)

        monthly_avg = monthly.mean()

        print(
            f"\nMonthly Average Spending: ${monthly_avg:.2f}"
        )

    def spending_percentage(self):

        category_total = self.df.groupby(
            "Category"
        )["Amount"].sum()

        percentages = (
            category_total / category_total.sum()
        ) * 100

        print("\nSpending Percentage by Category")
        print(percentages.round(2))
    def visualize_data(self):

        if self.df.empty:
            print("No data available.")
            return

        sns.set_style("whitegrid")

        data = self.df.copy()
        data["Date"] = pd.to_datetime(data["Date"])
        plt.figure(figsize=(8, 5))

        category_totals = data.groupby(
            "Category"
        )["Amount"].sum()

        sns.barplot(
            x=category_totals.index,
            y=category_totals.values
        )

        plt.title("Total Expenses by Category")
        plt.xlabel("Category")
        plt.ylabel("Amount")
        plt.xticks(rotation=30)
        plt.tight_layout()
        plt.show()

        daily_expenses = data.groupby(
            "Date"
        )["Amount"].sum()

        plt.figure(figsize=(10, 5))

        plt.plot(
            daily_expenses.index,
            daily_expenses.values,
            marker="o"
        )

        plt.title("Spending Trend Over Time")
        plt.xlabel("Date")
        plt.ylabel("Amount")
        plt.grid(True)

        plt.tight_layout()
        plt.show()
        plt.figure(figsize=(8, 8))

        plt.pie(
            category_totals.values,
            labels=category_totals.index,
            autopct="%1.1f%%"
        )

        plt.title("Expense Distribution")
        plt.show()
        plt.figure(figsize=(8, 5))

        sns.histplot(
            data["Amount"],
            bins=10,
            kde=True
        )
        plt.title("Expense Amount Distribution")
        plt.xlabel("Amount")
        plt.ylabel("Frequency")
        plt.tight_layout()
        plt.show()

def menu():
    tracker = ExpenseTracker()
    while True:
        print("\n====== SMART EXPENSE TRACKER ======")
        print("1. Add Expense")
        print("2. View Summary")
        print("3. Filter Expenses")
        print("4. Generate Report")
        print("5. Monthly Analysis")
        print("6. Spending Percentage")
        print("7. Visualize Data")
        print("8. Exit")

        choice = input("\nEnter choice: ")
        if choice == "1":
            date = input("Date (YYYY-MM-DD): ")
            amount = float(input("Amount: "))
            category = input("Category: ")
            description = input("Description: ")

            tracker.add_expense(
                date,
                amount,
                category,
                description
            )

        elif choice == "2":
            tracker.get_summary()

        elif choice == "3":

            category = input(
                "Category: "
            )
            if category == "":
                category = None

            filtered = tracker.filter_expenses(
                category=category
            )
            print("\nFiltered Expenses")
            print(filtered)

        elif choice == "4":
            tracker.generate_report()

        elif choice == "5":
            tracker.monthly_analysis()

        elif choice == "6":
            tracker.spending_percentage()

        elif choice == "7":
            tracker.visualize_data()

        elif choice == "8":
            print("Thank you for using Smart Expense Tracker!")
            break

        else:
            print("Invalid choice. Try again.")
if __name__ == "__main__":
    menu()