# Base directory paths

BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "output"

# Data file paths
DATA_FILES = {
    "transactions": DATA_DIR / "Account_Statement.csv",
    "credit_card_transactions": DATA_DIR / "credit_card_transactions.csv",
    "social_media": DATA_DIR / "social_media_posts.csv",
    "kyc": DATA_DIR / "KYC_Details.csv",
    "emails": DATA_DIR / "emails_to_banks.csv",
    "receiver_categories": DATA_DIR / "Receiver_vs_Category.csv",
    "credit_cards": DATA_DIR / "Credit_Card_Details.csv",
    "loans": DATA_DIR / "Loan_Details.csv",
    "credit_card_list": DATA_DIR / "credit_card_list.csv"
}

# Create output directory if it doesn't exist
OUTPUT_DIR.mkdir(exist_ok=True)