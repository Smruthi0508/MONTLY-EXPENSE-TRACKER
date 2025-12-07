# Savings System & Goal Tracker

A Streamlit-based personal finance management application to track expenses, set budgets, and monitor savings goals.

## Features

✨ **Core Features:**
- 💰 Set and manage monthly budget
- 📊 Track expenses by category
- 🎯 Create and monitor savings goals
- 📈 Real-time savings calculation
- ⚙️ Settings and data management

## Project Structure

```
miniproject/
├── app.py                 # Main Streamlit app (Dashboard)
├── utils.py               # Utility functions (load/save data)
├── requirements.txt       # Python dependencies
├── data/
│   └── data.json          # Data storage (expenses, budget, goals)
├── pages/
│   ├── 1_expenses.py      # Expense management page
│   └── 2_settings.py      # Settings and statistics page
└── README.md              # This file
```

## Installation

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application:**
   ```bash
   streamlit run app.py
   ```

## How to Use

### Dashboard (Main Page)
- Set your monthly budget
- View total expenses and current savings
- Create and track savings goals
- Monitor goal progress with visual indicators

### Expenses Page
- Add new expenses by category
- Track all expenses with description
- View expense summary
- Delete expenses as needed

### Settings Page
- View summary statistics
- Inspect raw JSON data
- Reset all data (if needed)

## Data Format

The `data/data.json` file stores:
```json
{
  "expenses": [
    {
      "category": "Food",
      "amount": 500.0,
      "description": "Lunch"
    }
  ],
  "monthly_budget": 5000.0,
  "goals": [
    {
      "name": "New Phone",
      "target": 30000.0
    }
  ]
}
```

## Tips

💡 **Budget Management:**
- Set a realistic monthly budget first
- Regularly add expenses to track spending
- Create specific, achievable goals

📌 **Goal Tracking:**
- Set savings goals with clear targets
- Monitor progress through visual indicators
- Adjust spending to reach your goals

🎯 **Financial Health:**
- Review your expenses regularly
- Aim to save consistently
- Adjust budget as income changes

## Requirements

- Python 3.8+
- Streamlit 1.32.0
- Pandas 2.1.3

## License

Free to use and modify for personal use.
