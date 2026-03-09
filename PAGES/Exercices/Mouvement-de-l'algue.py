import streamlit as st
from datetime import datetime
import json
import os

def afficher():
    st.title("🌿 Le Mouvement de l'Algue")

    st.markdown("""
    *« Pour que l'énergie circule, il faut redevenir fluide. »*
    """)

    # --- MENU 1 : LA THÉORIE (CONSERVÉ) ---
    with st.expander("💡 Pourquoi faire cet exercice ?", expanded=False):
        st.write("""
        L'énergie ne circule pas en ligne droite, mais en vagues (sinusoïdes). 
        Le stress nous rend rigides comme du bois sec. En imitant le mouvement de l'algue, 
        on débloque les "noeuds" énergétiques situés le long de la colonne vertébrale.
        """)

    # --- MENU 2 : LA PRÉPARATION (CONSERVÉ) ---
    with st.expander("🧘 Préparation & Posture", expanded=False):
        st.write("""
        - **Ancrage** : Tenez-vous debout, les pieds écartés de la largeur du bassin. Vous pouvez aussi vous asseoir, trouvez la position la plus confortable pour vous.
        - **Relâchement** : Déverrouillez légèrement les genoux (ne soyez pas tendu).
        - **Respiration** : Laissez votre respiration être naturelle, sans forcer.
        """)

    # --- MENU 3 : LA PRATIQUE (PAS À PAS - CONSERVÉ) ---
    with st.expander("🌊 Le Protocole (Le Pas-à-Pas)", expanded=True):
        st.info("Suivez l'ordre : le bassin dirige, la tête suit.")
        st.write("""
        1. **Bassin à Droite** : Poussez votre hanche vers la droite (latéralement).
        2. **Tête à Droite** : Laissez l'oreille droite tomber vers l'épaule droite.
        3. **Bassin à Gauche** : Gardez la tête inclinée et déplacez le bassin vers la gauche.
        4. **Tête à Gauche** : Une fois le bassin au bout, basculez la tête à gauche.

        *Répétez ce cycle en créant une ondulation fluide, sans à-coups.*
        """)

    # --- MENU 4 : LES SIGNES DE RÉUSSITE (CONSERVÉ) ---
    with st.expander("✨ Signes de libération énergétique", expanded=False):
        st.write("""
        Si vous ressentez ces réflexes, ne vous arrêtez pas, c'est que le fluide circule :
        - Baillements profonds.
        - Yeux qui pleurent ou piquent.
        - Nez qui se bouche ou se libère.
        - Sensation de chaleur ou de picotements.
        """)

    st.divider()

    # --- FORMULAIRE DE SUIVI ---
    st.subheader("📝 Votre Journal de Pratique")

    col1, col2 = st.columns(2)

    with col1:
        # Ajout de 'key' pour chaque widget
        date = st.date_input("Date du jour", datetime.now(), key="algue_date")
        duree = st.slider("Durée de la session (min)", 1, 15, 5, key="algue_duree")

    with col2:
        etat_initial = st.select_slider("État avant l'exercice", 
                                        options=["Bloqué", "Tendu", "Neutre", "Souple"],
                                        key="algue_etat")

    signes = st.multiselect("Qu'avez-vous observé ?", 
                             ["Baillements", "Larmes", "Chaleur", "Déblocage nuque/dos", "Légèreté"],
                             key="algue_signes")

    position = st.radio("Position choisie :", ["Assis", "Debout"], key="algue_pos")

    commentaire = st.text_area("Ressenti personnel", key="algue_note")

    # --- LOGIQUE DE SAUVEGARDE SÉCURISÉE ---
    if st.button("💾 Enregistrer la pratique", key="algue_save_btn"):
        # Récupération de l'email de l'utilisateur (défini dans app.py)
        user_email = st.session_state.get("email", "anonyme")
        user_folder = f"data/{user_email}"

        # Création du dossier utilisateur si besoin
        if not os.path.exists(user_folder):
            os.makedirs(user_folder, exist_ok=True)

        # Chemin du fichier (doit correspondre à statistiques.py)
        path = f"{user_folder}/suivi_algue.json"

        fiche = {
            "date": str(date),
            "exercice": "L'Algue",
            "duree": duree,
            "position": position,
            "etat_initial": etat_initial,
            "signes": signes,
            "note": commentaire,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        # Chargement de l'historique
        historique = []
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                try:
                    historique = json.load(f)
                except:
                    historique = []

        # Sauvegarde au format JSON
        historique.append(fiche)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(historique, f, indent=4, ensure_ascii=False)

        st.success(f"🌊 Mouvement mémorisé pour {user_email}. Votre fluide remonte à la source !")