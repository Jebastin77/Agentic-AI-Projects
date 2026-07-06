# Finance Investment Assistant using Google ADK

A simple AI-powered **Finance Investment Assistant** built using the **Google Agent Development Kit (ADK)** and **Gemini**.

The assistant helps users understand personal finance, create savings plans, analyze expenses, and retrieve the latest financial information using **Google Search**.

---

## Features

- Personal finance guidance
- Savings plan recommendations
- Investment planning assistance
- Monthly income and expense analysis
- Real-time financial news using Google Search
- Latest stock prices
- Company information
- Market trends
- Mutual fund and ETF information
- Cryptocurrency prices
- Government financial schemes
- Friendly conversational AI powered by Gemini

---

## Technologies Used

- Python
- Google Agent Development Kit (ADK)
- Gemini API
- Google Search Tool

---

## Project Structure

```text
finance-investment-assistant/
│
├── investment_plan_agent/
│   ├── __init__.py
│   └── agent.py
│
├── .env.example
├── requirements.txt
├── README.md
└── LICENSE
```

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/finance-investment-assistant.git
```

### 2. Navigate to the Project Directory

```bash
cd finance-investment-assistant
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate the Virtual Environment

#### Windows (Command Prompt)

```cmd
.venv\Scripts\activate
```

#### Windows (PowerShell)

```powershell
.\.venv\Scripts\Activate.ps1
```

#### macOS / Linux

```bash
source .venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure Environment Variables

Create a `.env` file in the project root.

```env
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY
```

### 7. Run the Agent

Launch the ADK Web Interface:

```bash
adk web
```

or run the agent directly:

```bash
adk run
```

---

## Example Questions

- What is the current price of Tesla stock?
- Give me the latest NIFTY market update.
- Suggest a savings plan for a monthly salary of ₹40,000.
- Compare SIP and Fixed Deposit.
- Explain mutual funds.
- What are today's gold prices?
- What are the latest interest rates in India?
- Give me the latest financial news.

---

## Disclaimer

This project is intended for **educational purposes only**. It does **not** provide financial, investment, tax, or legal advice. Investment decisions involve risk. Always consult a qualified financial advisor before making investment decisions.

---

## License

This project is licensed under the **MIT License**.

---

## Author

**Jebastin A**

GitHub: https://github.com/Jebastin77

LinkedIn:www.linkedin.com/in/jebastin77

---

⭐ If you found this project useful, consider giving it a **Star** on GitHub!