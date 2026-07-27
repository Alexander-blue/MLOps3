def generate_llm_retention_outreach(customer_dict, churn_prob, risk_factors=None):
    geo = customer_dict.get('Geography', 'valued customer')
    
    email_body = f"""Subject: Special VIP Banking Offer & Exclusive Relationship Benefits

Dear Valued Customer,

Thank you for choosing our banking services in {geo}. We noticed your ongoing relationship with us and would love to offer you exclusive benefits tailored to your financial journey:

• **0% Transfer Fees** on international transfers for the next 12 months.
• **Bonus High-Yield Savings Account** rate bump of +1.5% APY.
• **Dedicated Personal Financial Advisor** available 24/7.

We are committed to helping you reach your financial goals. Please reach out to your personal advisor or reply to this email to activate your VIP perks today!

Warm regards,  
*Customer Retention & Loyalty Team*
"""

    sms_copy = "VIP Bank Offer: Exclusive rate bump + 0% transfer fees! Reply VIP to claim your perks today or call your advisor."

    return {
        'Email_Body': email_body,
        'SMS_Copy': sms_copy
    }
