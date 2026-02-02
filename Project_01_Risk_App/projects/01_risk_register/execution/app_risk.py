import streamlit as st
import pandas as pd
import os
from datetime import datetime

# Configuration
DATA_DIR = "data"
CSV_FILE = os.path.join(DATA_DIR, "risk_log.csv")

def ensure_data_dir():
    """Ensure the data directory exists."""
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

def load_data():
    """Load the risk log CSV if it exists, otherwise return an empty DataFrame."""
    if os.path.exists(CSV_FILE):
        try:
            return pd.read_csv(CSV_FILE)
        except Exception as e:
            st.error(f"Error reading CSV file: {e}")
            return pd.DataFrame(columns=["Date", "Risk Title", "Severity"])
    return pd.DataFrame(columns=["Date", "Risk Title", "Severity"])

def log_risk(title, severity):
    """Log a new risk to the CSV file."""
    ensure_data_dir()
    
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_data = pd.DataFrame([[current_time, title, severity]], columns=["Date", "Risk Title", "Severity"])
    
    # Check if header needs to be written
    header = not os.path.exists(CSV_FILE)
    
    try:
        new_data.to_csv(CSV_FILE, mode='a', header=header, index=False)
        return True, "Risk Logged Successfully"
    except PermissionError:
        return False, "Error: File in use. Please close the CSV file and try again."
    except Exception as e:
        return False, f"An unexpected error occurred: {e}"

def main():
    st.title("Security Risk Register")

    # Form
    with st.form("risk_form"):
        risk_title = st.text_input("Risk Title")
        severity = st.selectbox("Severity", ["High", "Medium", "Low"])
        submitted = st.form_submit_button("Log Risk")

        if submitted:
            if risk_title:
                success, message = log_risk(risk_title, severity)
                if success:
                    st.success(message)
                else:
                    st.error(message)
            else:
                st.warning("Please enter a Risk Title.")

    # Display Data
    st.subheader("Current Risk Log")
    df = load_data()
    st.dataframe(df)

if __name__ == "__main__":
    main()
