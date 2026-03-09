import streamlit as st
from datetime import datetime
import json
import os

def afficher():
    st.title("⚗️ Le Laboratoire : Métamorphose du Sel")

    # --- PROTOCOLE DÉTAILLÉ (CONSERVÉ À 100%) ---
    st.markdown("""
    ### 📜 Le Protocole de Dissolution & Cristallisation
    1. **La Base :** Utiliser de l'**eau pure** (eau de pluie ou eau de source peu minéralisée).
    2. **Le Feu :** Faire bouillir l'eau. Une fois à ébullition, verser le **Sel de Guérande**.
    3. **Saturation :** Ajouter du sel jusqu'à ce que les grains ne fondent plus au fond de la casserole. L'eau est alors "pleine".

    ### 🔬 Choisir sa Voie (La Forme)
    - **Le Cube (Fixer) :** Retirer du feu. Verser délicatement dans un bocal plat. Laisser reposer sans **aucune vibration** et à l'abri des courants d'air. Le sel va se reconstruire en cubes parfaits.
    - **Le Chou-fleur (Diffuser) :** Maintenir une ébullition douce. Le sel va saturer l'eau par évaporation rapide et "monter" sur les parois en formant des excroissances expansées.

    ⚠️ **Note Importante :** Une fois sec, le sel est une éponge à lumière. Stockez-le immédiatement dans un **bocal opaque** ou un placard sombre.
    """)

    st.divider()

    # --- FORMULAIRE DE FABRICATION ---
    st.subheader("📝 Journal de l'Œuvre")

    col1, col2 = st.columns(2)
    with col1:
        # Les 'key' garantissent la stabilité sur Replit
        date_cuisson = st.date_input("Date de la cuisson", datetime.now(), key="fab_date")
        sel_origine = st.text_input("Sel d'origine (ex: Guérande Gris)", "Sel de Guérande", key="fab_origine")
        aspect_initial = st.text_input("Aspect initial (ex: Gris, humide, gros grains)", key="fab_aspect_init")

    with col2:
        casserole = st.selectbox("Récipient utilisé", [
            "Inox", "Cuivre", "aluminium", "Fer", "Fonte", "Acier",
            "Céramique", "Terre cuite", "Verre"
        ], key="fab_recip")
        forme_voulue = st.radio("Voie choisie :",
                                ["Cubique (Stable)", "Chou-fleur (Expansé)"], key="fab_voie")
        obscurite = st.checkbox("Stocké à l'abri de la lumière ? 🌑", key="fab_lum")

    st.markdown("### 🔍 Observation de la Matière")
    aspect_final = st.text_area(
        "Aspect après opération (ex: Cristaux transparents, efflorescence blanche...)", key="fab_aspect_fin"
    )
    details_cuisson = st.text_area(
        "Observations au feu (Sifflement, réaction à l'ajout du sel...)", key="fab_details")

    # --- LOGIQUE DE SAUVEGARDE ---
    if st.button("💾 Enregistrer la Fabrication", key="fab_save_btn"):
        nouvelle_fiche = {
            "date": str(date_cuisson),
            "sel_origine": sel_origine,
            "aspect_initial": aspect_initial,
            "recipient": casserole,
            "forme_voie": forme_voulue,
            "stockage_obscur": obscurite,
            "aspect_final": aspect_final,
            "details_cuisson": details_cuisson,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        # Récupération de l'email de l'utilisateur connecté
        user_email = st.session_state.get("email", "anonyme")
        user_folder = f"data/{user_email}"

        if not os.path.exists(user_folder):
            os.makedirs(user_folder, exist_ok=True)

        # Le nom du fichier doit correspondre exactement à celui cherché par statistiques.py
        path = f"{user_folder}/suivi_Fabrication_sel.json"

        historique = []
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                try:
                    historique = json.load(f)
                except:
                    historique = []

        historique.append(nouvelle_fiche)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(historique, f, indent=4, ensure_ascii=False)

            st.success(f"✨ La métamorphose du sel a été enregistrée ! ({user_email}).")