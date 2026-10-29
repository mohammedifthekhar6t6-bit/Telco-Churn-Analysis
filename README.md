# Telco Customer Churn Analysis

An exploratory data analysis of a telecom company's customers to find **who is leaving, why, and what the company can do about it.**

---

<img width="1350" height="675" alt="churn_by_payment" src="https://github.com/user-attachments/assets/6144cf96-8978-4ab0-9287-59b347642ccb" />
<img width="1050" height="675" alt="churn_by_internet" src="https://github.com/user-attachments/assets/8c8b94c8-4c27-4717-a09e-46b9a2ec5b86" />
<img width="1050" height="675" alt="monthly_charges_boxplot" src="https://github.com/user-attachments/assets/22bd136f-9d1f-4baf-822e-cdcb42869bd7" />


## Business Problem

Acquiring a new customer costs far more than keeping an existing one. This project analyzes customer data to:

1. Measure the overall churn rate
2. Identify which customer segments churn the most
3. Recommend practical retention actions

## Dataset

- **Source:** [Telco Customer Churn (Kaggle)](https://www.kaggle.com/datasets/blastchar/telco-customer-churn) (originally published by IBM)
- **Size:** ~7,000 customers, 21 columns
- **Target variable:** `Churn` (Yes / No)
- **Feature groups:**
  - Demographics: gender, senior citizen, partner, dependents
  - Services: phone, internet type, security, streaming, tech support
  - Account: tenure, contract type, payment method, paperless billing
  - Charges: monthly charges, total charges

## Tools Used

- Python (pandas, NumPy)
- Matplotlib and Seaborn for visualization
- Jupyter Notebook
- Git and GitHub

## Project Workflow

1. **Data loading and inspection:** checked shape, data types, and missing values
2. **Data cleaning:**
   - Converted `TotalCharges` from text to numeric (blank values appeared as spaces)
   - Removed rows with missing `TotalCharges` (about 11 new customers with tenure 0)
   - Dropped duplicates and created a numeric `Churn_flag` (1 = churned)
3. **Exploratory analysis:** calculated churn rate by contract, internet service, payment method, senior citizen status, and tenure group
4. **Visualization:** bar charts and distribution plots for the strongest patterns
5. **Insights and recommendations**

## Key Findings

> Replace these with the exact numbers from your own notebook.

- **Overall churn rate is about 26%**, so roughly 1 in 4 customers leaves.
- **Contract type is the strongest driver.** Month-to-month customers churn at roughly 43%, versus about 11% for one-year and 3% for two-year contracts.
- **New customers are the most at risk.** Customers in their first year churn at close to 48%, and churn falls steadily as tenure increases.
- **Fiber optic customers churn more (about 42%)** than DSL customers (about 19%), possibly due to higher prices or service issues.
- **Electronic check users churn the most (about 45%)** among payment methods. Automatic payment users churn far less.
- **Churned customers pay more per month** on average (about $74 vs $61).
- **Senior citizens churn at about 42%**, compared with about 24% for non-seniors.
- **Customers without add-ons** such as tech support and online security churn more.

## Recommendations

1. **Push month-to-month customers toward annual contracts** with discounts or bundled perks.
2. **Build an onboarding program for the first 12 months:** welcome calls, check-ins at months 1, 3, and 6, and early-tenure offers.
3. **Investigate fiber optic service quality and pricing**, since a high-price, high-churn pattern suggests a value or reliability problem.
4. **Encourage automatic payments** (card or bank transfer) with a small incentive, and reduce reliance on electronic checks.
5. **Promote tech support and security add-ons** to customers who lack them, as they appear to increase stickiness.
6. **Create targeted retention offers for senior customers.**

## Visualizations

| Churn by Contract |
<img width="1050" height="675" alt="churn_by_contract" src="https://github.com/user-attachments/assets/be189852-d7ab-4cbf-af5e-314fec51693f" />
 | Churn by Tenure Group |
 <img width="1050" height="675" alt="churn_by_tenure" src="https://github.com/user-attachments/assets/e72f0857-1344-4d81-9a79-7869c5079eb7" />


## Limitations

- The data is a single snapshot, so patterns show correlation, not causation.
- No information on customer satisfaction, complaints, or competitor offers.
- Insights are descriptive; no predictive model was built.

## Future Work

- Build a predictive model (logistic regression or random forest) to score churn risk
- Add a Power BI or Tableau dashboard
- Estimate revenue at risk from churn per segment
- Run statistical tests (chi-square) to confirm segment differences

## How to Run

```bash
git clone https://github.com/YOUR-USERNAME/telco-churn-analysis.git
cd telco-churn-analysis
pip install -r requirements.txt
jupyter notebook notebooks/churn_analysis.ipynb
```

## Project Structure

```
telco-churn-analysis/
├── data/
│   └── telco_churn.csv
├── notebooks/
│   └── churn_analysis.ipynb
├── images/
├── requirements.txt
├── .gitignore
└── README.md
```


