import streamlit as st

st.set_page_config(page_title="Arqueología Antropológica Política", page_icon="🏛️", layout="wide")

st.title("🏛️ Simulador de Arqueología Antropológica Política")
st.markdown("---")
st.write("Responde con honestidad a cada dilema. Esta herramienta examinará las premisas profundas que sostienen tus ideas para mostrarte qué edificio conceptual, corriente teórica y geopolítica respalda tu postura.")

# --- FORMULARIO DE DECISIONES POR CAPAS ---
with st.form("formulario_arqueologia"):
    
    # CAPA 1: ANTROPOLOGÍA
    st.header("Capa 1: La Naturaleza Humana")
    st.markdown("*¿Cómo definirías la condición fundamental del ser humano?*")
    antropologia = st.radio(
        "Selecciona la premisa con la que más te identifiques:",
        [
            "Un individuo autónomo y racional que busca maximizar su propio bienestar e interés particular.",
            "Un ser social e histórico cuya conciencia se forma a través del trabajo material y las relaciones colectivas.",
            "Un ser profundamente enraizado en su comunidad, su cultura, su familia y una herencia de valores tradicionales.",
            "Un dueño absoluto de su propio cuerpo y de su voluntad, que rechaza cualquier imposición externa.",
            "Un espíritu libre y soberano que no acepta ninguna autoridad, ley institucional o moral impuesta.",
            "Un eslabón inseparable de la tierra, la naturaleza y el bienestar colectivo de su pueblo originario."
        ],
        key="ant_choice"
    )

    st.markdown("---")

    # CAPA 2: ONTOLOGÍA DEL PODER
    st.header("Capa 2: El Vínculo Social y el Poder")
    st.markdown("*¿Cómo se entienden las personas y de dónde nace la autoridad?*")
    poder = st.radio(
        "Selecciona tu premisa sobre el poder:",
        [
            "Mediante un pacto o acuerdo entre ciudadanos regulado por leyes justas y un árbitro neutral imparcial.",
            "Mediante un conflicto permanente y estructural entre grupos sociales según quién posee los medios de producción.",
            "Mediante la defensa soberana del grupo frente a amenazas externas, distinguiendo claramente entre amigos y enemigos.",
            "Mediante la cooperación libre y voluntaria, eliminando por completo cualquier jerarquía u orden impuesto por la fuerza.",
            "Mediante un orden natural jerárquico y de respeto a la autoridad histórica, espiritual o sagrada.",
            "Mediante el servicio a la comunidad, la rotación de responsabilidades y la autoridad que obedece al mandato colectivo."
        ],
        key="pod_choice"
    )

    st.markdown("---")

    # CAPA 3: ECONOMÍA
    st.header("Capa 3: La Riqueza y el Trabajo")
    st.markdown("*¿Cómo debe organizarse la producción y el reparto de los bienes?*")
    economia = st.radio(
        "Selecciona tu modelo económico ideal:",
        [
            "A través de la propiedad privada garantizada, el intercambio libre y la competencia sin trabas en el mercado.",
            "A través de la propiedad social y la planificación organizada de la producción para satisfacer las necesidades de todos.",
            "A través de una economía mixta donde el mercado opera pero el Estado regula y asegura el bienestar social básico.",
            "A través de acuerdos estrictamente privados y voluntarios, sin intervención del Estado ni control de bancos centrales.",
            "A través de la reciprocidad, el trueque justo, el trabajo comunitario y la protección de los recursos de la tierra."
        ],
        key="eco_choice"
    )

    st.markdown("---")

    # CAPA 4: GEOPOLÍTICA
    st.header("Capa 4: El Tablero Global")
    st.markdown("*¿Cómo debería funcionar el mundo a escala internacional?*")
    geopolitica = st.radio(
        "Selecciona tu visión del orden global:",
        [
            "Un mundo integrado por el libre comercio sin fronteras rígidas y gobernado por reglas e instituciones globales.",
            "Un sistema de grandes bloques civilizacionales y potencias soberanas que defienden sus propias zonas de influencia.",
            "Un escenario de permanente competencia y disputa entre potencias globales por el dominio de los mercados y recursos.",
            "Una hermandad universal de los pueblos que supera y disuelve las fronteras de los Estados nacionales.",
            "Un mundo que defiende con fuerza la diversidad cultural y espiritual de cada civilización frente a la imposición de una cultura única."
        ],
        key="geo_choice"
    )

    submitted = st.form_submit_button("Analizar mi Postura Teórica")

# --- PROCESAMIENTO Y DIAGNÓSTICO METACOGNITIVO ---
if submitted:
    st.markdown("---")
    st.header("🔍 Radiografía y Diagnóstico de tu Arqueología Política")

    # Clasificación de perfiles basada en concordancias temáticas clave
    
    # Perfil Liberal / Capitalista
    es_liberal = ("individuo autónomo" in antropologia) and ("pacto o acuerdo" in poder or "propiedad privada garantizada" in economia)
    # Perfil Marxista / Socialista
    es_marxista = ("ser social e histórico" in antropologia or "conflicto permanente" in poder) and ("propiedad social" in economia)
    # Perfil Tradicionalista / Soberano
    es_tradicional = ("profundamente enraizado" in antropologia or "orden natural jerárquico" in poder) and ("grandes bloques civilizacionales" in geopolitica or "orden natural" in poder)
    # Perfil Libertario / Anarcocapitalista
    es_libertario = ("dueño absoluto" in antropologia) and ("acuerdos estrictamente privados" in economia)
    # Perfil Anarquista / Autonomista
    es_anarquista = ("espíritu libre y soberano" in antropologia or "cooperación libre" in poder) and ("hermandad universal" in geopolitica or "cooperación libre" in poder)
    # Perfil Comunitario / Indigenista
    es_comunitario = ("eslabón inseparable de la tierra" in antropologia) and ("reciprocidad" in economia or "servicio a la comunidad" in poder)

    # Evaluación de tensiones internas (Meclado / Incoherente)
    tension_detectada = False
    
    es_antropologia_comunitaria = ("enraizado" in antropologia) or ("eslabón inseparable de la tierra" in antropologia) or ("orden natural jerárquico" in poder)
    es_economia_capitalista = ("propiedad privada garantizada" in economia) or ("acuerdos estrictamente privados" in economia)
    
    if es_antropologia_comunitaria and es_economia_capitalista:
        tension_detectada = True

    # --- CASO A: PERFIL MEZCLADO / CON TENSIONES ---
    if tension_detectada:
        st.warning("⚠️ Diagnóstico: Perfil Conceptual Híbrido o en Tensión")
        st.markdown("""
        **Retroalimentación Metacognitiva:**  
        Has seleccionado un conjunto de premisas que provienen de tradiciones filosóficas divergentes. Por un lado, apelas a valores de enraizamiento, comunidad o protección orgánica de la sociedad; por el otro, adoptas un modelo económico basado en la competencia individual y el libre mercado absoluto. 
        
        En la historia de la teoría política, esta combinación suele generar una contradicción profunda: los pensadores críticos y tradicionales advierten que la expansión implacable del mercado liberal tiende a disolver precisamente los lazos comunitarios, familiares y culturales que tu antropología busca preservar. Pulir y profundizar en estas ideas te ayudará a clarificar si tu visión prioriza la conservación comunitaria o la libertad económica individual.
        """)
        
        st.subheader("📚 Bibliografía recomendada para pulir y resolver esta tensión:")
        st.markdown("- Karl Polanyi, *La gran transformación*")
        st.markdown("- Wilhelm Röpke, *La crisis de nuestro tiempo*")
        st.markdown("- Michael Sandel, *Lo que el dinero no puede comprar*")

    # --- CASO B: PERFIL COHERENTE - LIBERAL / CAPITALISTA ---
    elif es_liberal:
        st.success("✔ Diagnóstico: Coherencia Estructural Sólida — Tradición Liberal y Capitalista")
        st.markdown("""
        **Retroalimentación Metacognitiva y Ideas Fundantes:**  
        Tus respuestas convergen armónicamente en el edificio del **liberalismo político y económico**. 
        * **Idea fundante principal:** Partes de una antropología individualista donde el ser humano es un agente racional, autónomo y titular de derechos inalienables. 
        * **Visión del orden:** La sociedad no es una comunidad orgánica con un fin sagrado predeterminado, sino un artificio contractual diseñado para garantizar la convivencia pacífica mediante la ley y un Estado imparcial.
        * **Economía y Mundo:** La propiedad privada, el libre intercambio y la globalización mercantil constituyen los pilares más eficientes para el desarrollo humano y la libertad negativa.
        """)
        
        st.subheader("📚 Bibliografía fundamental para profundizar en tu postura:")
        st.markdown("- John Locke, *Segundo tratado sobre el gobierno civil*")
        st.markdown("- Adam Smith, *La riqueza de las naciones*")
        st.markdown("- Friedrich Hayek, *Los fundamentos de la libertad*")
        st.markdown("- Karl Popper, *La sociedad abierta y sus enemigos*")

    # --- CASO C: PERFIL COHERENTE - MARXISTA / SOCIALISTA ---
    elif es_marxista:
        st.success("✔ Diagnóstico: Coherencia Estructural Sólida — Tradición Crítica y Materialista")
        st.markdown("""
        **Retroalimentación Metacognitiva y Ideas Fundantes:**  
        Tus respuestas se alinean de manera consistente con las vertientes del **materialismo histórico y la teoría crítica**.
        * **Idea fundante principal:** El ser humano no posee una naturaleza fija o abstracta, sino que se autoconstruye a través del trabajo y las relaciones sociales materiales.
        * **Visión del orden:** La política no es un pacto neutral, sino el escenario de un antagonismo estructural (lucha de clases) impulsado por la apropiación del plustrabajo.
        * **Economía y Mundo:** La superación de la alienación exige la socialización de los medios de producción y la emancipación global frente a las jerarquías del capital transnacional.
        """)
        
        st.subheader("📚 Bibliografía fundamental para profundizar en tu postura:")
        st.markdown("- Karl Marx, *El Capital*")
        st.markdown("- Antonio Gramsci, *Cuadernos de la cárcel*")
        st.markdown("- Vladimir Lenin, *El imperialismo, fase superior del capitalismo*")
        st.markdown("- Ernst Mandel, *El pensamiento económico de Karl Marx*")

    # --- CASO D: PERFIL COHERENTE - TRADICIONALISTA / SOBERANO ---
    elif es_tradicional:
        st.success("✔ Diagnóstico: Coherencia Estructural Sólida — Tradición Conservadora, Realista y Geopolítica")
        st.markdown("""
        **Retroalimentación Metacognitiva y Ideas Fundantes:**  
        Tus respuestas reflejan una arquitectura conceptual propia del **realismo político, el tradicionalismo y la geopolítica de los grandes espacios**.
        * **Idea fundante principal:** El hombre es un ser histórico y enraizado, vinculado orgánicamente a su comunidad, su cultura y a un orden de autoridad superior.
        * **Visión del orden:** El poder no nace de contratos abstractos, sino de la soberanía, la capacidad de decisión frente al conflicto y el respeto a la jerarquía institucional y espiritual.
        * **Economía y Mundo:** Se rechaza tanto el colectivismo estéril como el mercado globalizador desraizado, prefiriendo un orden multipolar de civilizaciones soberanas que protejan la identidad de los pueblos.
        """)
        
        st.subheader("📚 Bibliografía fundamental para profundizar en tu postura:")
        st.markdown("- Thomas Hobbes, *Leviatán*")
        st.markdown("- Carl Schmitt, *El concepto de lo político*")
        st.markdown("- Julius Evola, *Revuelta contra el mundo moderno*")
        st.markdown("- Aleksandr Dugin, *La cuarta teoría política*")

    # --- CASO E: PERFIL COHERENTE - LIBERTARIO / ANARCOCAPITALISTA ---
    elif es_libertario:
        st.success("✔ Diagnóstico: Coherencia Estructural Sólida — Tradición Libertaria / Autopropiedad")
        st.markdown("""
        **Retroalimentación Metacognitiva y Ideas Fundantes:**  
        Tus respuestas se estructuran firmemente bajo los principios del **libertarismo radical y el anarcocapitalismo**.
        * **Idea fundante principal:** El individuo es dueño absoluto de su propio cuerpo y de su voluntad (*self-ownership*), siendo la soberanía personal el axioma moral indiscutible.
        * **Visión del orden:** Toda coacción institucional externa, monopolio estatal o impuesto es considerado una agresión ilegítima que vulnera el Principio de No Agresión (PNA).
        * **Economía y Mundo:** El orden social y la asignación de recursos deben depender exclusivamente de contratos privados voluntarios, eliminando bancos centrales, fronteras coactivas y regulaciones estatales.
        """)
        
        st.subheader("📚 Bibliografía fundamental para profundizar en tu postura:")
        st.markdown("- Murray Rothbard, *Ética de la libertad*")
        st.markdown("- Ludwig von Mises, *La acción humana*")
        st.markdown("- Robert Anarchy, *Anarquía, estado y utopía*")

    # --- CASO F: PERFIL COHERENTE - ANARQUISTA / AUTONOMISTA ---
    elif es_anarquista:
        st.success("✔ Diagnóstico: Coherencia Estructural Sólida — Tradición Ácrata y Autonomista")
        st.markdown("""
        **Retroalimentación Metacognitiva y Ideas Fundantes:**  
        Tus premisas convergen sólidamente en el horizonte del **anarquismo clásico y el autonomismo radical**.
        * **Idea fundante principal:** La libertad humana es incompatible con cualquier forma de autoridad heterónoma, jerarquía institucional o dominación impuesta.
        * **Visión del orden:** El orden social no requiere al Estado ni a la coacción vertical, sino que surge espontáneamente de la cooperación voluntaria, la ayuda mutua y la acción directa horizontal.
        * **Economía y Mundo:** Se rechaza tanto la explotación del capital privado como el control burocrático estatal, apostando por la emancipación y solidaridad universal de los pueblos.
        """)
        
        st.subheader("📚 Bibliografía fundamental para profundizar en tu postura:")
        st.markdown("- Piotr Kropotkin, *La ayuda mutua*")
        st.markdown("- Mijaíl Bakunin, *Dios y el Estado*")
        st.markdown("- Pierre-Joseph Proudhon, *¿Qué es la propiedad?*")

    # --- CASO G: PERFIL COHERENTE - COMUNITARIO / INDIGENISTA ---
    elif es_comunitario:
        st.success("✔ Diagnóstico: Coherencia Estructural Sólida — Ontología Comunitaria y del Bien Vivir")
        st.markdown("""
        **Retroalimentación Metacognitiva y Ideas Fundantes:**  
        Tus respuestas se sustentan en una matriz de **pensamiento comunitario e indigenista**.
        * **Idea fundante principal:** El ser humano no es un átomo aislado ni un propietario individual, sino un nodo inseparable de un organismo social y territorial más amplio (la comunidad y la tierra).
        * **Visión del orden:** El poder se concibe como servicio, reciprocidad y rotación de responsabilidades (*mandar obedeciendo*), rechazando la dominación vertical.
        * **Economía y Mundo:** La producción y el bienestar se orientan a la reproducción de la vida, el equilibrio con los ciclos naturales y la protección colectiva de los bienes comunes (*Sumak Kawsay*).
        """)
        
        st.subheader("📚 Bibliografía fundamental para profundizar en tu postura:")
        st.markdown("- José Carlos Mariátegui, *7 ensayos de interpretación de la realidad peruana*")
        st.markdown("- Álvaro García Linera, *Forma valor y forma comunidad*")
        st.markdown("- Alberto Acosta, *El buen vivir: Sumak Kawsay, una oportunidad para imaginar otros mundos*")

    # --- CASO H: PERFIL ECLÉCTICO GENERAL (SI NO CAE EN UN BLOQUE ESTRICTO) ---
    else:
        st.info("ℹ️ Diagnóstico: Perfil Ecléctico / En Construcción")
        st.markdown("""
        **Retroalimentación Metacognitiva:**  
        Tus respuestas muestran una combinación singular de diferentes escuelas de pensamiento. No te encasillas rígidamente en una sola corriente doctrinal, sino que amalgamas elementos variados sobre el poder, el hombre y la economía. 
        
        Esto refleja un pensamiento en plena construcción exploratoria. Para consolidar tu postura y dotarla de mayor solidez analítica, es muy útil contrastar cómo distintos autores clásicos resuelven la tensión entre libertad individual, orden comunitario y justicia distributiva.
        """)
        
        st.subheader("📚 Bibliografía sugerida para estructurar y profundizar tus reflexiones:")
        st.markdown("- Norberto Bobbio, *Derecha e izquierda*")
        st.markdown("- Isaiah Berlin, *Cuatro ensayos sobre la libertad*")
        st.markdown("- Michael Sandel, *El descontento con la democracia*")

    st.balloons()
