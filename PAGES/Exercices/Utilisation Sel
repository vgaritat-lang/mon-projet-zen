import streamlit as st
from datetime import datetime
import json
import os

def afficher():
    st.title("La Pratique : Donner l'Information")

    st.markdown("""
    ### 🌬️ L'In-formation par le Souffle
    Le sel est une boîte vide. Sans votre intention, il ne reste qu'un minéral.

    1. **Le Contact :** Prenez une poignée de votre sel entre vos mains jointes.
    2. **Le Verbe :** Formulez clairement votre intention.
    3. **Le Souffle :** Expirez doucement sur le sel pour transporter l'information. 
    4. **Le Lieu :** Le sel peut être chargé 24h sur un haut lieu énergétique.
    """)

    st.divider()

    # --- FORMULAIRE D'USAGE ---
    st.subheader("📡 Mise en place de la Charge")

    c1, c2 = st.columns(2)
    with c1:
        date_pratique = st.date_input("Date de la charge", datetime.now(), key="util_date")
        sel_utilise = st.selectbox("Type de sel chargé :", ["Cube (pour Bloquer)", "Chou-fleur (pour Saturer)"], key="util_sel")
        lieu_charge = st.text_input("Lieu de charge (ex: Chez moi, Mont St-Michel)", key="util_lieu_ch")

    with c2:
        methode = st.multiselect("Méthode employée :", ["Le Souffle", "Le Verbe/Prière", "Charge sur Lieu", "Visualisation"], key="util_methode")
        lieu_pose = st.text_input("Lieu de dépose finale (ex: Seuil de la porte)", key="util_lieu_pos")
        but_recherche = st.text_input("But (ex: Sommeil paisible)", key="util_but")

    intention_precise = st.text_area("Information déposée (Ce que vous avez dit ou ressenti) :", key="util_intent")

    # --- LOGIQUE DE SAUVEGARDE ---
    if st.button("💾 Archiver la Pratique", key="util_save_btn"):
        # 1. Récupération de l'utilisateur connecté
        user_email = st.session_state.get("email", "anonyme")
        user_folder = f"data/{user_email}"

        # 2. Chemin du fichier spécifique (On utilise 'path' partout)
        path = f"{user_folder}/suivi_Utilisation_Sel.json"

        # 3. Création du dossier si besoin
        if not os.path.exists(user_folder):
            os.makedirs(user_folder, exist_ok=True)

        # 4. Chargement de l'historique existant avec sécurité
        historique = []
        if os.path.exists(path):
            try:
                with open(path, "r", encoding="utf-8") as f:
                    historique = json.load(f)
            except (json.JSONDecodeError, FileNotFoundError):
                historique = []

        # 5. Préparation de la nouvelle fiche
        nouvelle_fiche = {
            "date": str(date_pratique),
            "sel": sel_utilise,
            "lieu_charge": lieu_charge,
            "methode": methode,
            "lieu_pose": lieu_pose,
            "but": but_recherche,
            "intention": intention_precise,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        # 6. Ajout et Enregistrement
        historique.append(nouvelle_fiche)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(historique, f, indent=4, ensure_ascii=False)

        # 7. Célébration Zen
        st.success(f"✨ L'information est scellée dans votre espace personnel ({user_email}).")

    # --- SIGNATURE ---
    st.markdown("""
        <div style="text-align: center; margin-top: 40px;">
            <p style="font-family: serif; font-size: 1.8em; color: #f39c12;">
                Vivez joyeux !
            </p>
        </div>
    """, unsafe_allow_html=True)