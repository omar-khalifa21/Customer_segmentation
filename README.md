# 🧭 Customer Segmentation App

A simple Streamlit web app that uses **K-Means clustering** to predict customer segments based on demographic and behavioral data.  
This project can be used by businesses to better understand their customers and target them effectively.

---

## 🚀 Features
- Predicts customer segment using a pre-trained **KMeans clustering model**.
- User-friendly **Streamlit UI** with dark theme.
- Accepts inputs like:
  - Age
  - Income
  - Total Spending
  - Number of Web Purchases
  - Number of Store Purchases
  - Number of Web Visits per Month
  - Recency (days since last purchase)
- Displays customer cluster with a clear label (e.g., **High Income – High Spending**).

---

## 🛠 Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/customer-segmentation-app.git
   cd customer-segmentation-app
2. Create a virtual environment (optional but recommended):

   python -m venv venv
   source venv/bin/activate  # On Mac/Linux
   venv\Scripts\activate     # On Windows
3. Install dependencies:

  pip install -r requirements.txt
