# Finance-Tracker

## DATA WAREHOUSING

### Scenario

I am a **Data Engineer** at **SpendIQ**, a startup that developed a personal finance app designed to help users understand and improve their financial behavior.  
The app connects to bank accounts, automatically categorizes transactions, and generates insights about:

- monthly spending
- savings patterns
- recurring costs

---

### Business Requirements

The **SpendIQ** app connects to users' bank accounts via a secure API and collects transaction data. It offers:

- Personalized reports
- Smart notifications
- Interactive dashboards

All designed to help users better understand their money habits and take control of their financial future.

---

### Core Business Goals

- **Spending Behavior Analysis** – Aggregate and visualize monthly spending habits
- **Saving Trends** – Identify if users are saving or overspending month over month
- **Budget Planning Insights** – Evaluate whether budgets are respected and suggest adjustments
- **Subscription Tracking** – Monitor recurring expenses such as streaming services
- **User Motivation** – Use KPIs to reward users who meet saving goals

---

### Reports

- **Monthly Spending per Category** (Food, Fashion, Utilities, Transport, Subscriptions, etc.)
- **Recurring Subscriptions List per User**
- **Savings vs. Expenses per Month**
- **Budget vs. Actual Spending by Category**

---

### Dashboards

- **Personal Budget Compliance Dashboard**
- **Spending Heatmap** – Days with the Highest Expenses
- **Spending vs. Saving Trendline** – Last 6 Months
- **Category Breakdown Pie Chart** – Current Month
- **Subscriptions Overview** – Recurring Payments Summary

---

### KPIs

- **% of Income Saved per Month**
- **Average Daily Spending**
- **Total Monthly Expenses**
- **Number of Recurring Payments**
- **Top 3 Spending Categories per User**

---

## Data Warehouse Design

### Data Sources

---

#### BankAPI – Bank Transactions

**Table:** `bank_transactions`

| Column           | Type         | Description                                         |
| ---------------- | ------------ | --------------------------------------------------- |
| transaction_id   | INT          | Unique ID of the transaction                        |
| user_id          | INT          | References user who made the transaction            |
| transaction_date | DATE         | Date of the transaction                             |
| amount           | DECIMAL      | Amount spent or received                            |
| currency         | VARCHAR(3)   | Currency code (e.g., USD, EUR)                      |
| merchant_name    | VARCHAR(100) | Name of the merchant                                |
| category         | VARCHAR(50)  | food, transport, rent, fashion, subscriptions, etc. |
| is_recurring     | BOOLEAN      | Marks if it's a recurring transaction               |

---

#### BudgetPlanner – User-defined Budgets

**Table:** `user_budgets`

| Column        | Type        | Description                          |
| ------------- | ----------- | ------------------------------------ |
| budget_id     | INT         | Unique ID for each budget            |
| user_id       | INT         | Reference to the user                |
| month         | VARCHAR(7)  | Format: "YYYY-MM" (e.g. "2025-05")   |
| category      | VARCHAR(50) | Spending category (food, rent, etc.) |
| budget_amount | DECIMAL     | Budgeted amount for the category     |

---

#### UserProfile – Basic Info for Segmentation

**Table:** `users`

| Column         | Type         | Description           |
| -------------- | ------------ | --------------------- |
| user_id        | INT          | Unique user ID        |
| name           | VARCHAR(100) | Full name             |
| age            | INT          | Age of the user       |
| gender         | VARCHAR(10)  | Gender                |
| monthly_income | DECIMAL      | User’s monthly income |
| signup_date    | DATE         | Date of registration  |
