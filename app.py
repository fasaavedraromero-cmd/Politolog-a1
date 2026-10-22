import streamlit as st

st.set_page_config(page_title="Arqueología Antropológica Política", page_icon="🏛️", layout="wide")

st.title("🏛️ Simulador de Arqueología Antropológica Política")
st.markdown("---")
st.write("Esta herramienta explora las premisas filosóficas, antropológicas y geopolíticas que sostienen tus ideas políticas, evaluando la coherencia de tu edificio conceptual.")

# --- FORMULARIO DE DECISIONES POR CAPAS ---
with st.form("formulario_arqueologia"):
    
    # CAPA 1: ANTROPOLOGÍA
    st.header("Capa 1: Antropología Filosófica")
    st.markdown("*¿Cuál es la premisa fundamental sobre la naturaleza del ser humano?*")
    antropologia = st.radio(
        "Selecciona tu premisa antropológica:",
        [
            "Atomista / Liberal: Un individuo autónomo, racional y maximizador de interés propio.",
            "Materialista / Práxico: Un ser social constituido por el trabajo y las relaciones materiales.",
            "Tradicional / Enraizado: Un ser histórico anclado a una comunidad, tradición o orden sagrado.",
            "Libertario / Autopropiedad: Un propietario absoluto de su propio cuerpo y voluntad.",
            "Anarquista Individualista: Un ego soberano que rechaza toda coacción institucional y moral externa.",
            "Comunitario / Indigenismo: Un nodo inseparable de la comunidad y del territorio (Pacha)."
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
            "Contrato Institucional: Un pacto racional regulado por un árbitro neutral (Estado de derecho).",
            "Lucha de Clases: Un antagonismo estructural inmanente basado en la propiedad y el plustrabajo.",
            "Amigo / Enemigo: Una decisión soberana sobre el conflicto existencial y la supervivencia.",
            "Anarquía / Autogestión: La negación de toda jerarquía coactiva; orden mediante la cooperación voluntaria.",
            "Orden Orgánico y Jerárquico: Un reflejo de un orden cósmico o tradicional donde cada estamento cumple un deber."
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
            "Capitalismo de Mercado: Propiedad privada inviolable, libre competencia y precios descentralizados.",
            "Economía Planificada / Socializada: Medios de producción bajo control social o de los trabajadores.",
            "Economía Mixta / Bienestar: Mercado regulado con fuerte intervención estatal y redistribución social.",
            "Anarcocapitalismo / Libre Mercado Radical: Contratos privados absolutos sin monopolio estatal ni banca central.",
            "Economía Comunal / Recíproca: Bien vivir, reciprocidad, trueque y custodia colectiva del territorio."
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
            "Globalización Mercantil: Integración global sin fronteras, libre comercio e instituciones supranacionales.",
            "Multipolaridad de Grandes Espacios: Un sistema de civilizaciones y potencias soberanas (*Großraum*) que rechazan la hegemonía única.",
            "Imperialismo / Competencia Global: Lucha de centros y periferias por el control de mercados y zonas de influencia.",
            "Internacionalismo Proletario: Emancipación global de los pueblos más allá de las fronteras estatales.",
            "Etnopluralismo / Tradicionalismo: Defensa radical de la diversidad de identidades espirituales y culturales frente a la homogenización."
        ],
        key="geo_choice"
    )

    submitted = st.form_submit_button("Ejecutar Auditoría Teórica")

# --- PROCESAMIENTO Y DIAGNÓSTICO ---
if submitted:
    st.markdown("---")
    st.header("🔍 Resultados de la Arqueología Teórica")

    # Lógica de detección de disonancias y coherencia
    disonancias = []
    
    # Detección 1: Tradicional/Comunitario vs Capitalismo Salvaje
    if "Tradicional" in antropologia and "Capitalismo de Mercado" in economia:
        disonancias.append({
            "alerta": "⚠️ Disonancia Teórica: Antropología Tradicional vs. Economía de Mercado Desregulado",
            "explicacion": "Sostienes una visión enraizada o tradicional del hombre, pero defiendes un sistema económico capitalista de libre mercado. Históricamente, los pensadores de la tradición advierten que el mercado absoluto disuelve los lazos comunitarios, familiares y espirituales que pretendes proteger.",
            "lecturas": [
                "Karl Polanyi - *La gran transformación*",
                "Wilhelm Röpke - *La crisis de nuestro tiempo*"
            ]
        })
        
    # Detección 2: Atomista vs Planificación Central
    if "Atomista" in antropologia and "Planificada" in economia:
        disonancias.append({
            "alerta": "⚠️ Disonancia Teórica: Antropología Atomista vs. Economía Planificada",
            "explicacion": "Partes de un individuo racional maximizador de su interés privado, pero propones una economía colectivizada y planificada centralmente. Esto genera una contradicción insalvable con los incentivos de la acción individual y la propiedad.",
            "lecturas": [
                "Ludwig von Mises - *El socialismo: un análisis económico y sociológico*",
                "Karl Marx - *Crítica del Programa de Gotha*"
            ]
        })

    # Si no hay grandes contradicciones críticas detectadas en este filtro base:
    if len(disonancias) == 0:
        st.success("✔ Edificio Conceptual Estable: Tus premisas muestran una convergencia lógica sólida a lo largo de las capas evaluadas.")
        st.subheader("📚 Arsenal Teórico para Profundizar y Defender tu Postura:")
        st.markdown("- Estudia a los autores clásicos de tu corriente matriz para blindar tus argumentos en los debates académicos.")
        st.markdown("- Revisa textos críticos internos de tu misma escuela para identificar posibles puntos ciegos doctrinales.")
    else:
        for d in disonancias:
            st.error(d["alerta"])
            st.write(d["explicacion"])
            st.subheader("📚 Ruta bibliográfica recomendada para resolver esta tensión:")
            for lib in d["lecturas"]:
                st.markdown(f"- {lib}")

    st.balloons()
