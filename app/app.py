from flask import Flask, request 
import sqlite3 
import os 
import yaml 
app = Flask(__name__) 
# Demo secrets for assessment only 
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE" 
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY" 
PAYMENT_API_TOKEN = "sk_test_51AssessmentTrainingOnly" 
@app.route("/") 
def home(): 
   return "Payment Review API - Assessment Lab" 
@app.route("/payment") 
def get_payment(): 
   username = request.args.get("user") 
   conn = sqlite3.connect("payments.db") 
   cursor = conn.cursor() 
   query = "SELECT * FROM payments WHERE username = '" + username + "'" 
   cursor.execute(query) 
   result = cursor.fetchall() 
   conn.close() 
   return str(result) 
@app.route("/admin/run") 
def admin_run(): 
   cmd = request.args.get("cmd") 
   return os.popen(cmd).read() 
@app.route("/account") 
def account(): 
   account_id = request.args.get("id") 
   accounts = { 
   "1": "Alice Account Balance: 5000", 
   "2": "Bob Account Balance: 7500", 
   "3": "Admin Account Balance: 99999" 
} 
   return accounts.get(account_id, "Account not found") 
@app.route("/config/load", methods=["POST"]) 
def load_config(): 
    data = request.data.decode("utf-8") 
    parsed = yaml.load(data) 
    return str(parsed) 
if __name__ == "__main__": 
  app.run(host="0.0.0.0", port=5000, debug=os.getenv("FLASK_DEBUG", "").lower() in ("1", "true", "yes")) 
