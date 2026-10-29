"""
Telco Customer Churn Analysis (standalone script version)

Run from anywhere:
    python churn_analysis.py

Expects the dataset at:  <project_root>/data/telco_churn.csv
Saves charts to:         <project_root>/images/
Project layout:
    churn-analysis/
    ├── data/telco_churn.csv
    ├── images/
    └── churn_analysis.py
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")  # save charts to files; no pop-up windows
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# ---------- Paths (work no matter where you run the script from) ----------
ROOT = Path(__file__).resolve().parent
DATA_FILE = ROOT / "data" / "telco_churn.csv"
IMG_DIR = ROOT / "images"
IMG_DIR.mkdir(exist_ok=True)

sns.set_theme(style="whitegrid")


def section(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


def save_bar(data, x, y, title, filename, order=None):
    """Bar chart of churn rate (%) and save it as a PNG."""
    plt.figure(figsize=(7, 4.5))
    ax = sns.barplot(data=data, x=x, y=y, order=order, color="#1F3A5F")
    ax.set_title(title)
    ax.set_ylabel("Churn rate (%)")
    for p in ax.patches:
        ax.annotate(f"{p.get_height():.1f}%", (p.get_x() + p.get_width() / 2, p.get_height()),
                    ha="center", va="bottom", fontsize=9)
    plt.tight_layout()
    plt.savefig(IMG_DIR / filename, dpi=150)
    plt.close()
    print(f"Saved chart: images/{filename}")


# ---------- 1. Load and inspect ----------
section("1. LOAD AND INSPECT")
df = pd.read_csv(DATA_FILE)
print("Shape:", df.shape)
print(df.dtypes.head(25))

# ---------- 2. Clean ----------
section("2. CLEAN")
# TotalCharges loads as text because a few rows are blank spaces
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
print("Missing values after conversion:\n", df.isnull().sum()[df.isnull().sum() > 0])
df = df.dropna(subset=["TotalCharges"])
df = df.drop_duplicates()
df["Churn_flag"] = (df["Churn"] == "Yes").astype(int)
print("Rows after cleaning:", len(df))

# ---------- 3. Overall churn rate ----------
section("3. OVERALL CHURN RATE")
print(f"Overall churn rate: {df['Churn_flag'].mean() * 100:.1f}%")

# ---------- 4. Churn by segment ----------
section("4. CHURN BY SEGMENT (%)")
for col in ["Contract", "InternetService", "PaymentMethod", "SeniorCitizen"]:
    rates = (df.groupby(col)["Churn_flag"].mean() * 100).sort_values(ascending=False)
    print(f"\n{col}:\n{rates.round(1)}")

# ---------- 5. Tenure and charges ----------
section("5. TENURE AND CHARGES")
df["tenure_group"] = pd.cut(df["tenure"], [0, 12, 24, 48, 72],
                            labels=["0-1yr", "1-2yr", "2-4yr", "4-6yr"])
tenure_rates = df.groupby("tenure_group", observed=True)["Churn_flag"].mean() * 100
print("Churn by tenure group (%):\n", tenure_rates.round(1))
print("\nAverage monthly charges:\n", df.groupby("Churn")["MonthlyCharges"].mean().round(2))

# ---------- 6. Charts ----------
section("6. SAVING CHARTS")
contract = (df.groupby("Contract")["Churn_flag"].mean() * 100).reset_index()
save_bar(contract, "Contract", "Churn_flag", "Churn Rate by Contract Type", "churn_by_contract.png")

tenure_df = tenure_rates.reset_index()
save_bar(tenure_df, "tenure_group", "Churn_flag", "Churn Rate by Tenure Group", "churn_by_tenure.png")

internet = (df.groupby("InternetService")["Churn_flag"].mean() * 100).reset_index()
save_bar(internet, "InternetService", "Churn_flag", "Churn Rate by Internet Service", "churn_by_internet.png")

payment = (df.groupby("PaymentMethod")["Churn_flag"].mean() * 100).reset_index()
plt.figure(figsize=(9, 4.5))
ax = sns.barplot(data=payment, x="PaymentMethod", y="Churn_flag", color="#1F3A5F")
ax.set_title("Churn Rate by Payment Method")
ax.set_ylabel("Churn rate (%)")
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig(IMG_DIR / "churn_by_payment.png", dpi=150)
plt.close()
print("Saved chart: images/churn_by_payment.png")

plt.figure(figsize=(7, 4.5))
sns.boxplot(data=df, x="Churn", y="MonthlyCharges", hue="Churn",
            palette=["#7FA6C9", "#1F3A5F"], legend=False)
plt.title("Monthly Charges: Retained vs Churned")
plt.tight_layout()
plt.savefig(IMG_DIR / "monthly_charges_boxplot.png", dpi=150)
plt.close()
print("Saved chart: images/monthly_charges_boxplot.png")

# ---------- 7. Conclusions ----------
section("7. CONCLUSIONS")
print("""
- Month-to-month contracts, new customers, fiber optic users and electronic
  check payers show the highest churn.
- Recommendations: annual-plan discounts, a first-year onboarding program,
  review fiber optic pricing/quality, and incentives for automatic payments.
""")