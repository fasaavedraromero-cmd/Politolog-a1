import streamlit as st

st.set_page_config(page_title="Arqueología Antropológica Política", page_icon="🏛️", layout="wide")

st.title("🏛️ Simulador de Arqueología Antropológica Política")
st.markdown("---")
st.write("Responde con honestidad filosófica. Esta herramienta evaluará tus premisas profundas para mostrarte qué edificio conceptual y geopolítico sostiene tus ideas.")

# --- FORMULARIO DE DECISIONES POR CAPAS (NEUTRO / CIEGO) ---
with st.form("formulario_arqueologia"):
    
    # CAPA 1: ANTROPOLOGÍA
    st.header("Capa 1: Antropología Filosófica")
    st.markdown("*¿Cuál es la naturaleza fundamental del ser humano?*")
    antropologia = st.radio(
        "Selecciona la premisa que consideres más verídica:",
        [
            "Un individuo autónomo, racional, movido por el interés propio y la maximización de su utilidad.",
            "Un ser social cuya conciencia y esencia se construyen a través del trabajo material y las relaciones sociales.",
            "Un ser histórico y comunitario, enraizado orgánicamente a una tradición, cultura u orden trascendente.",
            "Un propietario absoluto de su propio cuerpo y voluntad, regido por el principio de no agresión.",
            "Un ego soberano y único que rechaza toda coacción institucional, moral o colectiva externa.",
            "Un nodo inseparable de la comunidad ancestral y del territorio (la tierra como organismo vivo)."
        ],
        key="ant_choice"
    )

    st.markdown("---")

    # CAPA 2: ONTOLOGÍA DEL PODER
    st.header("Capa 2: Ontología del Poder y el Conflicto")
    st.markdown("*¿Cómo se organiza el vínculo social y de dónde surge la autoridad?*")
    poder = st.radio(
        "Selecciona tu premisa sobre el poder:",
        [
            "Mediante un contrato social racional regulado por un tercero neutral e imparcial (Estado de derecho).",
            "Mediante un antagonismo estructural inmanente impulsado por la lucha por la apropiación del plustrabajo.",
            "Mediante la decisión soberana sobre el conflicto existencial (la distinción fundamental entre amigo y enemigo).",
            "Mediante la cooperación voluntaria y la acción directa horizontal, negando toda jerarquía coactiva.",
            "Mediante un orden jerárquico natural u orgánico que refleja un principio cósmico, sagrado o histórico.",
            "Mediante el servicio rotativo de cargos, la reciprocidad y el mandar obedeciendo comunitario."
        ],
        key="pod_choice"
    )

    st.markdown("---")

    # CAPA 3: ECONOMÍA
    st.header("Capa 3: Estructura Económica y Distributiva")
    st.markdown("*¿Cómo debe organizarse la producción y distribución de la riqueza?*")
    economia = st.radio(
        "Selecciona tu modelo económico:",
        [
            "Mediante la propiedad privada inviolable, el libre mercado de precios y la competencia descentralizada.",
            "Mediante la socialización y planificación centralizada o democrática de los medios de producción.",
            "Mediante una economía mixta regulada, impuestos progresivos y provisión pública de bienestar social.",
            "Mediante contratos privados absolutos y un mercado totalmente libre de monopolios estatales o bancarios.",
            "Mediante la reciprocidad, el trueque, el bien vivir y la custodia colectiva de los bienes comunes."
        ],
        key="eco_choice"
    )

    st.markdown("---")

    # CAPA 4: GEOPOLÍTICA
    st.header("Capa 4: Dimensión Geopolítica y Orden Global")
    st.markdown("*¿Cómo debe estructurarse el espacio global y el tablero internacional?*")
    geopolitica = st.radio(
        "Selecciona tu visión geopolítica:",
        [
            "Mediante la integración global del mercado, la apertura total de fronteras y la gobernanza supranacional.",
            "Mediante un orden multipolar de Grandes Espacios civilizacionales soberanos que rechazan la hegemonía única.",
            "Mediante la competencia interimperialista por el control de zonas de influencia, materias primas y mercados.",
            "Mediante la emancipación universal y la solidaridad internacional de los pueblos por encima de los estados.",
            "Mediante la defensa radical de la pluralidad de identidades culturales y espirituales frente a la homogenización."
        ],
        key="geo_choice"
    )

    submitted = st.form_submit_button("Ejecutar Auditoría Teórica")

# --- PROCESAMIENTO Y DIAGNÓSTICO ---
if submitted:
    st.markdown("---")
    st.header("🔍 Resultados de la Arqueología Teórica")

    disonancias = []
    
    # Detección de tensiones basadas en el contenido neutral seleccionado
    if "enraizado orgánicamente" in antropologia and "interés propio" not in economia and "privada inviolable" in economia:
        disonancias.append({
            "alerta": "⚠️ Disonancia Teórica detectada en tu edificio conceptual",
            "explicacion": "Tus premisas combinan un enraizamiento comunitario u orgánico con un modelo económico basado en la propiedad privada capitalista absoluta. La historia del pensamiento político demuestra que el despliegue del mercado desregulado tiende a disolver los lazos comunitarios y tradicionales que tu antropología busca preservar.",
            "lecturas": [
                "Karl Polanyi - *La gran transformación*",
                "Wilhelm Röpke - *La crisis de nuestro tiempo*"
            ]
        })

    if len(disonancias) == 0:
        st.success("✔ Coherencia Estructural Sólida: Tus premisas filosóficas, antropológicas y económicas convergen sin contradicciones lógicas aparentes en este filtro.")
        st.subheader("📚 Arsenal Teórico Recomendado:")
        st.markdown("Has construido un sistema consistente. Te sugerimos profundizar en las fuentes primarias de tu corriente matriz para blindar tus argumentos conceptuales y prepararte para el debate crítico.")
    else:
        for d in disonancias:
            st.error(d["alerta"])
            st.write(d["explicacion"])
            st.subheader("📚 Ruta bibliográfica recomendada para resolver esta tensión:")
            for lib in d["lecturas"]:
                st.markdown(f"- {lib}")

    st.balloons()

    st.balloons()
