import streamlit as st
from datetime import datetime
import json
import os

def afficher():
    st.title("💫 Diagnostique de circulation énergétique")

    # --- ENSEIGNEMENT PRÉSERVÉ ---
    st.markdown("""
    ### Ressentir le Lieu avant d'agir
    Selon l'enseignement alchimique, le lieu possède sa propre signature. Avant de vouloir "changer" ou "placer" quoi que ce soit, il faut **vérifier le fond**. 

    * **La Main comme Antenne :** Présentez votre main (souvent la droite) vers le sol ou un objet. On ne cherche pas à imaginer, on cherche à *recevoir*.
    * **La Connexion :** Si un objet (même sacré) n'est pas "branché" ou connecté à l'énergie du lieu, il reste inerte.
    * **Polarité :** Le ressenti peut être ascendant (léger/positif) ou descendant (lourd/négatif).
    """)

    # --- INTRODUCTION À LA PRÉSENCE ---
    st.info("""
    **« Pour capter la vibration du lieu, ne cherchez pas à faire. Soyez simplement là. 
    Ne soyez pas le poste de radio qui fait du bruit, soyez la musique qui s'accorde au Silence. »**
    """)

    st.divider()

    # --- FORMULAIRE DE RESSENTI ---
    st.subheader("🕵️ Exploration du Fond")

    col1, col2 = st.columns(2)
    with col1:
        # Ajout de 'key' pour la stabilité technique
        date = st.date_input("Date de l'exploration", datetime.now(), key="diag_date")
        lieu_nom = st.text_input("Lieu exploré (ex: Salon, Église, Jardin)", key="diag_lieu")
        methode_capte = st.selectbox(
            "Technique utilisée :",
            ["Main Antenne", "Ressenti global (corps)", "Déplacement lent"],
            key="diag_methode"
        )

    with col2:
        polarite = st.radio(
            "Qualité du lieu (le Fond) :",
            ["Vibrant / Ascendant (+)", "Neutre", "Lourd / Descendant (-)"],
            key="diag_polarite"
        )
        connexion_objet = st.checkbox("Présence d'objets 'déconnectés' ?", key="diag_objets")

    st.markdown("### 🖐️ Sensations dans la main / le corps")
    sensations = st.text_area(
        "Décrivez le ressenti physique (Chaleur, picotements, fraîcheur, pression, vide...)",
        key="diag_sensations"
    )

    # --- ANALYSE DU LIEU ---
    st.subheader("🧐 Analyse & Action")
    recommandation = st.selectbox("Action préconisée après ressenti :", [
        "Laisser tel quel", "Nettoyer le fond", "Reconnecter les objets",
        "Placer une charge (Sel)"
    ], key="diag_action")

    commentaires = st.text_area(
        "Observations sur la circulation énergétique du lieu :",
        key="diag_commentaires"
    )

    # --- LOGIQUE DE SAUVEGARDE SÉCURISÉE ---
    if st.button("💾 Enregistrer dans le Grimoire", key="diag_save_btn"):
        # Identification de l'utilisateur connecté
        user_email = st.session_state.get("email", "anonyme")
        user_folder = f"data/{user_email}"

        if not os.path.exists(user_folder):
            os.makedirs(user_folder, exist_ok=True)

        # Le nom du fichier correspond à celui du module statistiques
        path = f"{user_folder}/suivi_captation_energie.json"

        fiche = {
            "date": str(date),
            "lieu": lieu_nom,
            "polarite": polarite,
            "sensations": sensations,
            "objets_deconnectes": connexion_objet,
            "action": recommandation,
            "commentaires": commentaires,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        historique = []
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                try:
                    historique = json.load(f)
                except:
                    historique = []

        historique.append(fiche)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(historique, f, indent=4, ensure_ascii=False)

        st.success(f"✨ L'état des lieux de '{lieu_nom}' a été archivé pour {user_email}.")