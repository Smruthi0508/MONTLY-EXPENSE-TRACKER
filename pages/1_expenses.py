import streamlit as st
from datetime import date
from utils import load_data, save_data
import pandas as pd
import matplotlib.pyplot as plt


# Data file
DATA_FILE = "../data/data.json"

st.title("➕ Add Expense Details")
st.markdown("### Log your daily spends here! 📝")

# Load data
data = load_data(DATA_FILE)
expenses = data.get("expenses", [])

# Form for adding expense
st.subheader("📋 Add New Expense")
col1, col2 = st.columns(2)
with col1:
    expense_date = st.date_input("Date", value=date.today(), max_value=date.today())
with col2:
    category = st.selectbox("Category", ["Food", "Travel", "Personal", "Health", "Others"])

amount = st.number_input("Amount (₹)", min_value=0.0, step=0.01, format="%.2f")
description = st.text_input("Description (optional)")

if st.button("💾 Save Expense"):
    if amount > 0:
        new_expense = {
            "date": expense_date.strftime("%Y-%m-%d"),
            "amount": float(amount),
            "category": category,
            "description": description
        }
        expenses.append(new_expense)
        data["expenses"] = expenses
        if save_data(DATA_FILE, data):
            st.success("✅ Expense added successfully!")
            st.rerun()  # Refresh to clear form
        else:
            st.error("❌ Failed to save. Try again.")
    else:
        st.warning("⚠️ Amount must be greater than 0.")

# Quick preview
if expenses:
    st.subheader("📊 Recent Expenses")
    df_preview = pd.DataFrame(expenses[-5:])  # Last 5
    st.dataframe(df_preview, use_container_width=True)
else:
    st.info("ℹ️ No expenses yet. Add your first one above!")


# Data file
DATA_FILE = "../data/data.json"

st.title("📊 Monthly Charts & Insights")
st.markdown("### Visualize your spending patterns! 🎨")

# Load data
data = load_data(DATA_FILE)
expenses = data.get("expenses", [])

if expenses:
    df = pd.DataFrame(expenses)
    df['date'] = pd.to_datetime(df['date'])
    df['day'] = df['date'].dt.day  # For daily bar chart

    # Pie Chart: Category-wise
    st.subheader("🥧 Category-wise Spending")
    category_sums = df.groupby("category")["amount"].sum()
    if not category_sums.empty:
        fig1, ax1 = plt.subplots()
        ax1.pie(category_sums.values, labels=category_sums.index, autopct='%1.1f%%', startangle=90)
        ax1.axis('equal')
        ax1.set_title("Expense Distribution by Category")
        st.pyplot(fig1)
    else:
        st.warning("No data for pie chart.")

    # Bar Chart: Daily Expenses
    st.subheader("📈 Daily Expenses Trend")
    daily_sums = df.groupby("day")["amount"].sum()
    if not daily_sums.empty:
        fig2, ax2 = plt.subplots()
        daily_sums.plot(kind='bar', ax=ax2, color='skyblue')
        ax2.set_xlabel("Day of Month")
        ax2.set_ylabel("Amount (₹)")
        ax2.set_title("Daily Spending")
        plt.xticks(rotation=45)
        st.pyplot(fig2)
    else:
        st.warning("No data for bar chart.")

    # Quick Insight
    avg_spend = df["amount"].mean()
    st.info(f"💡 Average spend per expense: ₹{avg_spend:.2f}")
else:
    st.warning("⚠️ No expense data available. Add expenses first!")
