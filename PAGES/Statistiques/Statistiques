import streamlit as st
import json
import os
import pandas as pd

def afficher_stats():
    st.title("📊 Votre Progression Alchimique")
    
    user_email = st.session_state.get("email", "anonyme")
    path_sel = f"data/{user_email}/suivi_Fabrication_sel.json"

    if not os.path.exists(path_sel):
        st.info("✨ Vous n'avez pas encore enregistré d'expériences dans le Laboratoire.")
        return

    # Chargement des données
    with open(path_sel, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    df = pd.DataFrame(data)

    # --- AFFICHAGE DES INDICATEURS CLÉS ---
    col1, col2, col3 = st.columns(3)
    col1.metric("Expériences totales", len(df))
    
    # Compter les formes réussies
    cubes = len(df[df['forme_voie'].str.contains("Cubique")])
    col2.metric("Cristallisations Cubiques", cubes)
    
    # Ratio de protection (Lumière)
    protege = len(df[df['stockage_obscur'] == True])
    col3.metric("Stockages conformes", f"{int(protege/len(df)*100)}%")

    st.divider()

    # --- HISTORIQUE DÉTAILLÉ ---
    st.subheader("📜 Journal des opérations")
    # On affiche un tableau propre
    st.dataframe(df[['date', 'sel_origine', 'forme_voie', 'recipient']], use_container_width=True)

    # --- GRAPHIQUE DE RÉPARTITION (Simple et Robuste) ---
    st.subheader("📈 Répartition des Voies")
    st.bar_chart(df['forme_voie'].value_counts())