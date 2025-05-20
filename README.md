# 🎯 Segmentazione Clienti con K-means - Demo AI per Marketing

**App Streamlit** che dimostra l'uso del clustering K-means per segmentare clienti fittizi in gruppi omogenei.

## 🚀 Come Usare
1. **Online**: [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://tuo-link-streamlit.streamlit.app)
2. **Localmente**:
   ```bash
   git clone https://github.com/tuo-username/nome-repo.git
   cd nome-repo
   pip install -r requirements.txt
   streamlit run app.py
   ```

## 📊 Dataset
Dati sintetici generati con:
- `Frequenza acquisti` (n. transazioni/anno)
- `Valore medio carrello` (€)
- `Recency` (giorni dall'ultimo acquisto)

## 🔧 Dipendenze
Listate in `requirements.txt`:
```plaintext
streamlit==1.17.0
scikit-learn==1.2.2
pandas==1.5.3
```

## 📝 Note
- Progetto didattico per il corso *AI e Machine Learning per il Marketing*
- **K-means** applicato a dati standardizzati (`StandardScaler`)
