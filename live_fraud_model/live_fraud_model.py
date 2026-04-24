import pandas as pd
from pymongo import MongoClient
from sklearn.ensemble import IsolationForest
import warnings
warnings.filterwarnings('ignore')

print("🚀 Connecting AI to Live Docker Database...\n")

try:
    # 1. CONNECT TO THE REAL MONGODB DATABASE IN DOCKER
    # Docker exposes port 27017 to your local Windows machine
    client = MongoClient("mongodb://localhost:27017/", serverSelectionTimeoutMS=5000)
    
    # Select your exact database name from your .env file
    db = client["wallet-system"] 
    
    # Select your transactions collection (Change this if yours is named differently!)
    collection = db["transactions"]

    # Fetch all transactions, specifically grabbing the 'amount' field
    real_data = list(collection.find({}, {"_id": 0, "amount": 1}))

    # 2. CHECK IF YOU HAVE ENOUGH DATA
    # AI needs a decent amount of data to figure out what a "normal" habit is
    if len(real_data) < 20:
        print(f"⚠️ Only found {len(real_data)} transactions in the live database.")
        print("The AI needs more data to learn your baseline spending habits.")
        print("Please go to your React app (localhost:3000) and make about 20 normal transfers, plus 1 massive one!")
        exit()

    df = pd.DataFrame(real_data)

    print(f"📊 Successfully loaded {len(df)} REAL transactions from MongoDB.")
    print("🧠 Training Scikit-Learn Model on LIVE data...\n")

    # 3. TRAIN THE AI MODEL ON YOUR REAL DATA
    # Contamination=0.05 means we assume ~5% of real transactions might be fraudulent
    model = IsolationForest(contamination=0.05, random_state=42)
    model.fit(df[['amount']])

    # 4. PREDICT FRAUD ON LIVE DATA
    df['is_fraud'] = model.predict(df[['amount']])

    # 5. DISPLAY ALERTS
    print("🚨 REAL-TIME FRAUD ALERTS 🚨")
    print("-" * 50)
    fraudulent_transactions = df[df['is_fraud'] == -1]
    
    if len(fraudulent_transactions) > 0:
        for index, row in fraudulent_transactions.iterrows():
            print(f"⚠️ SUSPICIOUS ACTIVITY: Live Database Record #{index} for ₹{row['amount']} flagged!")
    else:
        print("✅ All recent live transactions look safe. No anomalies detected.")
        
    print("-" * 50)

except Exception as e:
    print(f"❌ Database Connection Failed: {e}")
    print("Make sure your Docker containers (wallet-mongo) are actually running!")