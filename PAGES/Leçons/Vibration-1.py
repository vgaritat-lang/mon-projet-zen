import streamlit as st


def afficher():
    # --- STYLE CSS (Isolé pour cette leçon) ---
    st.markdown("""
        <style>
        .citation-box {
            font-style: italic;
            color: #2c3e50;
            border-left: 5px solid #d4af37;
            padding: 15px;
            background-color: #fcfaf2;
            margin: 20px 0;
            border-radius: 0 10px 10px 0;
        }
        .lesson-title { color: #d4af37; text-align: center; font-size: 28px; font-weight: bold; }
        </style>
    """,
                unsafe_allow_html=True)

    # --- EN-TÊTE ---
    st.markdown(
        "<h1 class='lesson-title'>🧬 La Nature Vibratoire de l'Univers</h1>",
        unsafe_allow_html=True)
    
    st.markdown("#### *Thématique : Métaphysique et Phénoménologie*")

    st.info(
        "**Objectif :** Comprendre l'interaction entre la vibration (le souffle), la matière et la conscience."
    )

    # --- CHAPITRE I ---
    with st.expander("🌬️ I. Le Souffle Initial : Origine de la Forme",
                     expanded=True):
        st.write("""
        Dans les textes anciens comme dans l'observation physique, le mouvement naît d'une impulsion immatérielle appelée **"souffle"** ou **"vibration"**. 
        Ce déclencheur est la condition sine qua non de l'existence du temps, de l'espace et de la matière.
        """)

        st.write("""
        * **Le concept de "Ruah" :** En hébreu, le mot pour "souffle" est le même que pour "vibration".
        * **La trinité universelle :** Le souffle engendre une oscillation (début/fin) qui crée le **temps**, un mouvement (point A vers B) qui crée l'**espace**, et une ondulation qui crée la **forme** (matière).
        """)

        st.markdown(
            '<div class="citation-box">« D’un souffle immatériel, nous allons créer une agitation, un mouvement. [...] La vague n\'est plus plate, elle a une forme : il va y avoir de la matière, du temps, de l\'espace. »</div>',
            unsafe_allow_html=True)

    # --- CHAPITRE II ---
    with st.expander("🎶 II. La Vibration préside à la Matière"):
        st.write("""
        La matière n'est pas une substance fixe, mais le résultat d'une fréquence spécifique qui ordonne des "briques" élémentaires identiques.
        """)

        st.write("""
        * **L'expérience du sable :** Sur une enceinte, le sable change de structure selon le son émis. La forme n'est pas dans le grain de sable, mais dans la vibration qui le traverse.
        * **L'analogie de la chanson :** Chaque être vivant est une mélodie unique organisant ses propres cellules.
        """)

        st.markdown(
            '<div class="citation-box">« Finalement, tout ce qu\'il y a sur terre [...] on est peut-être juste une chanson particulière qui ordonne la matière. »</div>',
            unsafe_allow_html=True)

    # --- CHAPITRE III ---
    with st.expander("⚖️ III. Accord, Résonance et Santé"):
        st.write("""
        Le bien-être de l'individu dépend de sa capacité à être **"en accord"** avec son environnement. Un désaccord vibratoire se manifeste physiquement par la maladie ou la lourdeur.
        """)

        st.write("""
        * **La densité émotionnelle :** Le langage reflète cette réalité (être **"grave"** ou **"pesant"** lors d'un mal-être, vs se sentir **"léger"** en harmonie).
        * **La fausse note :** Un conflit entre soi et l'extérieur déstructure la matière biologique.
        """)

        st.markdown(
            '<div class="citation-box">« Si je ne suis pas en accord avec ce qu\'il y a autour de moi, il va y avoir une fausse note et cette fausse note agissant sur la matière va déstructurer la matière. »</div>',
            unsafe_allow_html=True)

    # --- CHAPITRE IV ---
    with st.expander("📻 IV. La Conscience : Le 'Poste de Radio'"):
        st.write("""
        Le corps physique ne produit pas l'intelligence ou l'âme ; il sert d'antenne réceptrice pour capter une fréquence de conscience préexistante.
        """)

        st.write("""
        * **La spécialisation cellulaire :** Au 4ème jour du développement embryonnaire, les cellules cessent de se multiplier à l'identique pour se spécialiser. C'est le moment où "l'antenne" biologique capte son signal (l'âme).
        * **La mort comme extinction :** Mourir n'est pas la fin de l'être, mais l'extinction du récepteur.
        """)

        st.markdown(
            '<div class="citation-box">« Le corps n\'est qu\'un poste de radio et ce poste de radio capte à un moment son âme. [...] Mourir, j\'éteins le poste. Mais c\'est pas pour ça que je tue le chanteur qui est dedans. »</div>',
            unsafe_allow_html=True)

    # --- CONCLUSION ÉPURÉE (Sans menu, sans plantage) ---
    st.divider()
    st.markdown("""
        <div style="text-align: center; margin-top: 40px; padding-bottom: 40px;">
            <p style="font-family: serif; font-size: 2em; color: #f39c12;">
                Vivez joyeux !
            </p>
        </div>
    """,
                unsafe_allow_html=True)
