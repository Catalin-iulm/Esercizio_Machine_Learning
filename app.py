import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from clustering import df, cluster_analysis

st.set_page_config(layout="wide")
st.title("📊 Segmentazione Clienti per Marketing AI")

# Sidebar per controlli
st.sidebar.header("Parametri")
n_clusters = st.sidebar.slider("Numero di Cluster", 2, 5, 3)

# Ricostruisci il clustering se cambia il numero di cluster
if n_clusters != 3:
    from sklearn.cluster import KMeans
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    df["Cluster"] = kmeans.fit_predict(X_scaled)

# Mostra i dati
st.subheader("Dati Clienti")
st.dataframe(df.head())

# Visualizzazione
st.subheader("Segmentazione")
fig, ax = plt.subplots()
for cluster in range(n_clusters):
    cluster_data = df[df["Cluster"] == cluster]
    ax.scatter(cluster_data["Frequenza"], cluster_data["ValoreCarrello"], label=f"Cluster {cluster}")
ax.set_xlabel("Frequenza acquisti")
ax.set_ylabel("Valore carrello (€)")
st.pyplot(fig)

# Analisi dei cluster
st.subheader("Profilo Medio dei Cluster")
st.table(cluster_analysis)