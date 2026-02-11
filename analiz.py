import matplotlib
matplotlib.use('Agg') # Arka planda çalıştırır

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random
from datetime import datetime, timedelta

print("🚀 LEVEL 3: ENGLISH & DARK THEME RFM ANALYSIS STARTING...")

# --- 0. STYLE SETUP (KARANLIK MOD AYARLARI) ---
# Grafiğin senin istediğin gibi karanlık ve havalı görünmesi için ayarlar
sns.set(style='darkgrid', context='talk', 
        rc={"axes.facecolor": "#2b2b2b", "figure.facecolor": "#2b2b2b", "grid.color": "#444444", "text.color": "white", "axes.labelcolor": "white", "xtick.color": "white", "ytick.color": "white"})

# --- 1. DATA GENERATION SIMULATION (İNGİLİZCE) ---
print("Step 1: Simulating database...")
customer_ids = [f'Cust_{i}' for i in range(1000, 1500)] # 500 Customers
data = []

current_date = datetime.now()

for _ in range(3000): # 3000 transactions
    cust_id = random.choice(customer_ids)
    # Random date within last year
    days_back = random.randint(1, 365)
    order_date = current_date - timedelta(days=days_back)
    # Random amount (Some spenders up to 5000 USD)
    amount = round(random.uniform(50, 5000), 2)
    data.append([cust_id, order_date, amount])

df = pd.DataFrame(data, columns=['customer_id', 'order_date', 'total_amount'])

# --- 2. RFM CALCULATION ---
print("Step 2: Calculating Recency, Frequency, Monetary...")

rfm = df.groupby('customer_id').agg({
    'order_date': lambda date: (current_date - date.max()).days, # Recency (Days since last order)
    'customer_id': lambda num: len(num),      # Frequency (Total transaction count)
    'total_amount': lambda price: price.sum() # Monetary (Total spent)
})

rfm.columns = ['Recency', 'Frequency', 'Monetary']

# --- 3. SEGMENTATION (ENGLISH LABELS) ---
# Müşterileri İngilizce etiketleyelim
def segment_customer(row):
    if row['Frequency'] > 12 and row['Monetary'] > 25000:
        return 'Champions (VIP)' # Yıldızlar
    elif row['Recency'] < 30 and row['Frequency'] > 4:
        return 'Loyal Customers' # Kareler
    elif row['Recency'] > 150:
        return 'At Risk / Churn' # Üçgenler
    elif row['Monetary'] < 2000:
        return 'Low Spenders'
    else:
        return 'Potential Loyalists' # Yuvarlaklar

rfm['Segment'] = rfm.apply(segment_customer, axis=1)

# --- 4. VISUALIZATION (PRO DARK THEME) ---
print("Step 3: Generating professional dark theme chart...")

plt.figure(figsize=(14, 10)) # Biraz daha büyük bir tuval

# Özel Renk ve Şekil Tanımları (Senin attığın görsele benzetmek için)
# Renkler (Kırmızı, Yeşil, Mavi, Turuncu)
custom_colors = ['#ff4d4d', '#00cc66', '#3399ff', '#ff9933', '#ffff66'] 
# Şekiller (Yıldız, Kare, Yuvarlak, Üçgen, Baklava)
custom_markers = ['*', 's', 'o', '^', 'D'] 

# Segment sırasını belirleyelim ki efsane (legend) düzgün görünsün
segment_order = ['Champions (VIP)', 'Loyal Customers', 'Potential Loyalists', 'At Risk / Churn', 'Low Spenders']

# Scatter Plot çizimi
sns.scatterplot(
    data=rfm, 
    x='Frequency', 
    y='Monetary', 
    hue='Segment',      # Renkleri segmente göre ayır
    style='Segment',    # Şekilleri segmente göre ayır
    palette=custom_colors, # Kendi renk paletimizi kullan
    markers=custom_markers,# Kendi şekil paletimizi kullan
    hue_order=segment_order, # Sıralamayı uygula
    style_order=segment_order,
    s=150, # Nokta büyüklüğü (Daha belirgin olsun)
    alpha=0.8, # Hafif şeffaflık
    edgecolor='black' # Nokta kenarlıkları
)

# İngilizce Başlıklar ve Etiketler
plt.title('Customer Value Analysis (RFM Segmentation)', fontsize=20, fontweight='bold', pad=20)
plt.xlabel('Purchase Frequency (Total Orders)', fontsize=14, labelpad=15)
plt.ylabel('Monetary Value (Total Spent $)', fontsize=14, labelpad=15)

# Efsane (Legend) ayarları - Kutunun dışına, sağ üste alalım
plt.legend(title='CUSTOMER SEGMENTS', title_fontsize='13', bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0., frameon=False)

# Dosyayı kaydet (Yüksek kalitede)
file_name = "final_english_dark_analysis.png"
plt.tight_layout()
plt.savefig(file_name, dpi=300, facecolor="#2b2b2b") # Arka plan rengiyle kaydet

print(f"\n✅ SUCCESS! Professional English chart saved as '{file_name}'.")
print("Check your file explorer on the left!")