mport streamlit as st
from datetime import datetime
import json
import os

def afficher():
    st.title("💧 L'Empreinte de l'Eau")

    st.markdown("""
    > **"L'eau n'est pas juste un liquide, c'est une mémoire qui résonne avec votre intention."**
    """)

    # --- FORMULAIRE ---
    # Ajout de 'key' pour chaque élément interactif
    date = st.date_input("Date de l'observation", datetime.now(), key="eau_date")

    col1, col2 = st.columns(2)
    with col1:
        source = st.selectbox("Source", 
                              ["Robinet", "Source naturelle", "Bouteille", "Eau filtrée", "Eau informée"],
                              key="eau_source")
    with col2:
        contenant = st.selectbox("Contenant", 
                                 ["Verre", "Cristal", "Céramique", "Plastique", "Métal"],
                                 key="eau_contenant")

    st.divider()

    st.subheader("👁️ Analyse Vibratoire")
    aspect = st.multiselect("Aspect visuel", 
                            ["Cristallin", "Brillant", "Terne", "Bulles", "Mouvement"],
                            key="eau_aspect")

    gout = st.select_slider("Qualité en bouche", 
                             options=["Métallique", "Neutre", "Douce", "Vibrante", "Légère"],
                             key="eau_gout")

    note_interieure = st.text_area("Ressenti intuitif ou message reçu au contact de l'eau", 
                                    key="eau_note")

    # --- LOGIQUE DE SAUVEGARDE SÉCURISÉE ---
    if st.button("💾 Enregistrer l'empreinte", key="eau_save_btn"):
        # On récupère l'email de l'utilisateur connecté dans app.py
        user_email = st.session_state.get("email", "anonyme")
        user_folder = f"data/{user_email}"

        # Création du dossier utilisateur s'il n'existe pas
        if not os.path.exists(user_folder):
            os.makedirs(user_folder, exist_ok=True)

        # Chemin du fichier (doit correspondre à celui utilisé dans statistiques.py)
        path = f"{user_folder}/suivi_eau.json"

        fiche = {
            "date": str(date),
            "exercice": "Empreinte Eau",
            "source": source,
            "contenant": contenant,
            "aspect": aspect,
            "gout": gout,
            "note": note_interieure,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        # Chargement de l'historique existant
        historique = []
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                try:
                    historique = json.load(f)
                except:
                    historique = []

        # Ajout de la nouvelle fiche
        historique.append(fiche)

        # Sauvegarde
        with open(path, "w", encoding="utf-8") as f:
            json.dump(historique, f, indent=4, ensure_ascii=False)

        st.success(f"✨ L'empreinte de l'eau a été mémorisée dans votre espace ({user_email}).")