from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Standardizziamo i dati (fondamentale per K-means!)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df[["Frequenza", "ValoreCarrello", "Recency"]])

# K-means con 3 cluster (numero scelto strategicamente)
kmeans = KMeans(n_clusters=3, random_state=42)
df["Cluster"] = kmeans.fit_predict(X_scaled)

# Visualizzazione 2D (Frequenza vs ValoreCarrello)
plt.figure(figsize=(10, 6))
for cluster in range(3):
    cluster_data = df[df["Cluster"] == cluster]
    plt.scatter(
        cluster_data["Frequenza"], 
        cluster_data["ValoreCarrello"], 
        label=f"Cluster {cluster}"
    )
plt.scatter(
    kmeans.cluster_centers_[:, 0], 
    kmeans.cluster_centers_[:, 1], 
    s=300, c='red', marker='X', label='Centroidi'
)
plt.xlabel("Frequenza acquisti (ultimo anno)")
plt.ylabel("Valore medio carrello (€)")
plt.title("Segmentazione Clienti con K-means")
plt.legend()
plt.grid(True)
plt.savefig("cluster_marketing.png")  # Per Streamlit