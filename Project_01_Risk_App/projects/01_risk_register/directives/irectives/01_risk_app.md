# 01 Risk Register App

## Goal

Create a local "Security Risk Register" application using Python and Streamlit.
The app allows me to input a risk (e.g., "Hardcoded API Key"), and it logs it to a CSV file.

## Inputs

- User types: Risk Description, Severity (High/Med/Low), and Date.

## Tools (Execution Layer)

- `execution/app_risk.py`: The main application script.
- `data/risk_log.csv`: The storage file (auto-created if missing).

## Process

1. **Setup**: Check if `data/` folder exists; create if not.
2. **Frontend**: Use Streamlit to create a form with:
    - Text Input: "Risk Title"
    - Select Box: "Severity" ["High", "Medium", "Low"]
    - Button: "Log Risk"
3. **Backend**: When button is clicked:
    - Append the data to `data/risk_log.csv`.
    - Show a success message "Risk Logged".
    - Display the current contents of the CSV in a table below the form.

## Edge Cases

- If CSV is locked/open, show "Error: File in use".
- Ensure the CSV header is written only once.
