# Personal Expense Tracker

A modern, engaging personal expense tracker built with Streamlit and Python. Visualizes spending patterns and promotes financial literacy with a user-friendly interface. Log, track, and chart monthly spending to improve financial awareness and savings.

## Features

🎯 Budget management & tracking
📊 Track expenses by category & date
🎯 Savings goals with progress tracking
📈 Visual charts & analytics
📥 CSV export functionality
💡 Daily motivational quotes

## Project Structure

```
miniproject/
├── app.py                 # Main Streamlit Dashboard
├── utils.py               # Utility functions (load/save data)
├── requirements.txt       # Python dependencies
├── data/
│   └── data.json          # Data storage (expenses, budget, goals)
├── pages/
│   ├── 1_expenses.py      # Add expense details with date picker & charts
│   ├── 2_budget.py        # Budget and savings goal tracker
│   └── 3_history.py       # Expense history with filters & CSV export
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

**💸 Dashboard** 
◦ View summary, budget, savings & motivational quotes
◦ Real-time feedback on spending status
◦ Check if on track or over budget

**➕ Page 1: Add Expenses** 
◦ Log expenses with date picker (past dates only)
◦ Select from 5 categories: Food, Travel, Personal, Health, Others
◦ Add descriptions for context
◦ View recent expenses preview
◦ Matplotlib charts for visual analysis
◦ Category breakdown visualization

**💰 Page 2: Budget & Goals**
◦ Set monthly budget with easy updates
◦ Create multiple savings goals
◦ Track progress with visual indicators
◦ Delete or modify goals as needed
◦ Real-time savings calculation

**📜 Page 3: History**
◦ View all expenses in table format
◦ Filter by category
◦ See formatted dates & amounts
◦ Download as CSV file
◦ Total filtered expenses summary

## Data Format

The `data/data.json` file stores:
```json
{
  "expenses": [
    {
      "date": "2025-12-07",
      "amount": 500.0,
      "category": "Food",
      "description": "Lunch at restaurant"
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

◦ Set realistic budget & track regularly
◦ Analyze patterns with charts
◦ Create specific savings goals
◦ Export CSV for detailed analysis

## Requirements

- Python 3.8+
- Streamlit 1.32.0
- Pandas 2.1.3
- Matplotlib (for charts)

## Running the App

**On Windows:**
```bash
python -m streamlit run app.py
```

**Using Python directly:**
```bash
streamlit run app.py
```

The app will open at: `http://localhost:8501`

## License

Free to use and modify for personal use.
