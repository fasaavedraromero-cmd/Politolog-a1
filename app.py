import streamlit as st

st.set_page_config(page_title="Arqueología Antropológica Política", page_icon="🏛️", layout="wide")

st.title("🏛️ Simulador de Arqueología Antropológica Política")
st.markdown("---")
st.write("""
**Bienvenido al ejercicio de arqueología conceptual.** La política no nace en los programas de gobierno ni en los parlamentos; nace en las respuestas silenciosas que damos sobre qué es el hombre, cómo se ejerce el poder y qué lugar ocupamos en el mundo. 
Tómate tu tiempo en cada dilema. Al finalizar, el sistema realizará una radiografía crítica de tu edificio intelectual.
""")

# --- FORMULARIO DE DECISIONES POR CAPAS ---
with st.form("formulario_arqueologia"):
    
    # CAPA 1: ANTROPOLOGÍA
    st.header("Capa 1: La Naturaleza Humana (Antropología)")
    st.markdown("*Antes de legislar o gobernar, ¿qué suponemos que es el ser humano en su esencia?*")
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
    st.header("Capa 2: El Vínculo Social y el Poder (Ontología Política)")
    st.markdown("*Aceptando la premisa anterior, ¿cómo se relacionan los hombres y de dónde surge la autoridad?*")
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
    st.header("Capa 3: La Riqueza y el Trabajo (Economía Política)")
    st.markdown("*¿Cómo deben organizarse los recursos, la producción y el reparto de los bienes?*")
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
    st.header("Capa 4: El Tablero Global (Geopolítica)")
    st.markdown("*¿Cómo debe estructurarse el espacio mundial a escala internacional?*")
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

    submitted = st.form_submit_button("Ejecutar Auditoría y Análisis Metacognitivo")

# --- PROCESAMIENTO Y DIAGNÓSTICO FORMATIVO ---
if submitted:
    st.markdown("---")
    st.header("🔍 Radiografía Crítica y Metacognición")

    # Clasificación de perfiles
    es_liberal = ("individuo autónomo" in antropologia) and ("pacto o acuerdo" in poder or "propiedad privada garantizada" in economia)
    es_marxista = ("ser social e histórico" in antropologia or "conflicto permanente" in poder) and ("propiedad social" in economia)
    es_tradicional = ("profundamente enraizado" in antropologia or "orden natural jerárquico" in poder) and ("grandes bloques civilizacionales" in geopolitica or "orden natural" in poder)
    es_libertario = ("dueño absoluto" in antropologia) and ("acuerdos estrictamente privados" in economia)
    es_anarquista = ("espíritu libre y soberano" in antropologia or "cooperación libre" in poder) and ("hermandad universal" in geopolitica or "cooperación libre" in poder)
    es_comunitario = ("eslabón inseparable de la tierra" in antropologia) and ("reciprocidad" in economia or "servicio a la comunidad" in poder)

    # Evaluación de tensiones internas (Perfil Híbrido / Incoherente)
    tension_detectada = False
    es_antropologia_comunitaria = ("enraizado" in antropologia) or ("eslabón inseparable de la tierra" in antropologia) or ("orden natural jerárquico" in poder)
    es_economia_capitalista = ("propiedad privada garantizada" in economia) or ("acuerdos estrictamente privados" in economia)
    
    if es_antropologia_comunitaria and es_economia_capitalista:
        tension_detectada = True

    # --- CASO A: PERFIL HÍBRIDO / TENSIONADO (INCOHERENTE) ---
    if tension_detectada:
        st.warning("⚠️ Diagnóstico: Perfil Conceptual Híbrido / En Tensión")
        st.markdown("""
        **Análisis Crítico y Metacognición:**  
        Has construido una postura que dialoga con mundos teóricos contrapuestos. Por un lado, tus premisas antropológicas y sociales buscan proteger el valor del enraizamiento, la comunidad o los vínculos orgánicos; por el otro, adoptas un modelo económico fundado en la competencia mercantil y la propiedad privada desregulada.
        
        **¿Por qué genera fricción teórica?**  
        La historia del pensamiento político demuestra que el despliegue del mercado capitalista absoluto actúa como un solvente universal: disuelve las tradiciones, los lazos comunitarios estables y las identidades locales que tu antropología pretende defender. No se trata de un "error", sino de una **contradicción sintomática** muy común en el debate contemporáneo (habitual en posturas conservadoras de mercado o populismos identitarios). El desafío pedagógico para ti es decidir qué principio cede ante el otro.
        
        **Movimientos, partidos y figuras históricas que inspiran o han intentado articular esta tensión:**
        * *Movimientos y partidos:* El distributismo católico, partidos democristianos de raigambre social, y diversas expresiones del nacionalismo económico proteccionista.
        * *Personajes históricos:* Wilhelm Röpke, Konrad Adenauer (con su economía social de mercado), o intelectuales del conservadurismo popular.
        """)
        
        st.subheader("📚 Itinerario Bibliográfico Sugerido:")
        st.markdown("**Fuentes Principales (Autores Clásicos):**")
        st.markdown("- Karl Polanyi, *La gran transformación*")
        st.markdown("- G.K. Chesterton, *Outline of Sanity (Esbozo de la cordura)*")
        st.markdown("**Comentarios y Ensayos Críticos:**")
        st.markdown("- Wilhelm Röpke, *La crisis de nuestro tiempo*")
        st.markdown("- Michael Sandel, *Lo que el dinero no puede comprar*")

    # --- CASO B: PERFIL COHERENTE - LIBERAL / CAPITALISTA ---
    elif es_liberal:
        st.success("✔ Diagnóstico: Coherencia Estructural Sólida — Tradición Liberal y Capitalista")
        st.markdown("""
        **Análisis Crítico y Metacognición (Ideas Fundantes):**  
        Tus respuestas convergen armónicamente en el núcleo de la **modernidad liberal**. 
        * **Idea fundante:** El individuo precede a la sociedad. Los seres humanos son agentes racionales, libres y titulares de derechos negativos que deben ser blindados frente a la coacción colectiva.
        * **El orden y la economía:** La sociedad se organiza mediante el contrato legal y un Estado mínimo o neutral que arbitra las reglas del juego, mientras que la asignación de recursos descansa en el libre mercado y la iniciativa privada.
        
        **Movimientos, partidos y figuras históricas que encarnan esta tradición:**
        * *Movimientos y partidos:* El liberalismo clásico del siglo XIX, partidos liberales y reformistas europeos, vertientes del socioliberalismo contemporáneo.
        * *Personajes históricos:* John Locke, Adam Smith, Alexis de Tocqueville, John Stuart Mill.
        """)
        
        st.subheader("📚 Itinerario Bibliográfico Sugerido:")
        st.markdown("**Fuentes Principales (Autores Clásicos):**")
        st.markdown("- John Locke, *Segundo tratado sobre el gobierno civil*")
        st.markdown("- Adam Smith, *La riqueza de las naciones*")
        st.markdown("**Comentarios y Ensayos Críticos:**")
        st.markdown("- Friedrich Hayek, *Los fundamentos de la libertad*")
        st.markdown("- Norberto Bobbio, *Liberalismo y democracia*")

    # --- CASO C: PERFIL COHERENTE - MARXISTA / SOCIALISTA ---
    elif es_marxista:
        st.success("✔ Diagnóstico: Coherencia Estructural Sólida — Tradición Crítica y Materialista")
        st.markdown("""
        **Análisis Crítico y Metacognición (Ideas Fundantes):**  
        Tus respuestas se alinean de manera consistente con el **materialismo histórico y la emancipación obrera**.
        * **Idea fundante:** El hombre es un ser social que se autoconstruye mediante el trabajo. La conciencia está determinada por las condiciones materiales de producción.
        * **El orden y la economía:** La política no es un pacto neutral entre iguales, sino la superestructura de un antagonismo de clases. La transformación exige abolir la propiedad privada capitalista y planificar la producción socialmente.
        
        **Movimientos, partidos y figuras históricas que encarnan esta tradición:**
        * *Movimientos y partidos:* Los partidos comunistas del siglo XX, movimientos socialistas revolucionarios, sindicatos de clase e internacionalismo proletario.
        * *Personajes históricos:* Karl Marx, Vladimir Lenin, Rosa Luxemburgo, Antonio Gramsci.
        """)
        
        st.subheader("📚 Itinerario Bibliográfico Sugerido:")
        st.markdown("**Fuentes Principales (Autores Clásicos):**")
        st.markdown("- Karl Marx, *El Capital* (Libro I)")
        st.markdown("- Vladimir Lenin, *El Estado y la revolución*")
        st.markdown("**Comentarios y Ensayos Críticos:**")
        st.markdown("- Antonio Gramsci, *Cuadernos de la cárcel* (Antología)")
        st.markdown("- Ernst Mandel, *El pensamiento económico de Karl Marx*")

    # --- CASO D: PERFIL COHERENTE - TRADICIONALISTA / SOBERANO ---
    elif es_tradicional:
        st.success("✔ Diagnóstico: Coherencia Estructural Sólida — Tradición Conservadora, Realista y Geopolítica")
        st.markdown("""
        **Análisis Crítico y Metacognición (Ideas Fundantes):**  
        Tus respuestas reflejan una arquitectura conceptual propia del **realismo político, el tradicionalismo y la multipolaridad civilizacional**.
        * **Idea fundante:** El ser humano es un heredero, un ser enraizado en su comunidad histórica, su cultura y un orden trascendente o de autoridad legítima.
        * **El orden y la economía:** El poder político se funda en la soberanía y la capacidad de preservar la supervivencia colectiva frente al caos, rechazando tanto el individualismo disolvente como el universalismo globalizador.
        
        **Movimientos, partidos y figuras históricas que encarnan esta tradición:**
        * *Movimientos y partidos:* Movimientos tradicionalistas históricos, corrientes soberanistas contemporáneas y bloques de geopolítica nacional-estatista.
        * *Personajes históricos:* Thomas Hobbes, Carl Schmitt, Charles de Gaulle, Juan Donoso Cortés.
        """)
        
        st.subheader("📚 Itinerario Bibliográfico Sugerido:")
        st.markdown("**Fuentes Principales (Autores Clásicos):**")
        st.markdown("- Thomas Hobbes, *Leviatán*")
        st.markdown("- Carl Schmitt, *El concepto de lo político*")
        st.markdown("**Comentarios y Ensayos Críticos:**")
        st.markdown("- Julien Freund, *Sociología del conflicto*")
        st.markdown("- Aleksandr Dugin, *La cuarta teoría política*")

    # --- CASO E: PERFIL COHERENTE - LIBERTARIO / ANARCOCAPITALISTA ---
    elif es_libertario:
        st.success("✔ Diagnóstico: Coherencia Estructural Sólida — Tradición Libertaria / Autopropiedad")
        st.markdown("""
        **Análisis Crítico y Metacognición (Ideas Fundantes):**  
        Tus respuestas se estructuran firmemente bajo los principios del **libertarismo radical y la autopropiedad**.
        * **Idea fundante:** El axioma de la autopropiedad (*self-ownership*). Todo individuo es dueño absoluto de su cuerpo, su esfuerzo y su propiedad legítimamente adquirida.
        * **El orden y la economía:** Cualquier coacción estatal (impuestos, regulaciones, monopolios monetarios) es considerada una violación ilegítima de la libertad individual. La sociedad se articula mediante contratos privados voluntarios.
        
        **Movimientos, partidos y figuras históricas que encarnan esta tradición:**
        * *Movimientos y partidos:* El movimiento libertario contemporáneo, corrientes anarcocapitalistas y partidos de corte minarquista o libertario en América y Europa.
        * *Personajes históricos:* Murray Rothbard, Ludwig von Mises, Ayn Rand, Robert Nozick.
        """)
        
        st.subheader("📚 Itinerario Bibliográfico Sugerido:")
        st.markdown("**Fuentes Principales (Autores Clásicos):**")
        st.markdown("- Murray Rothbard, *Ética de la libertad*")
        st.markdown("- Ludwig von Mises, *La acción humana*")
        st.markdown("**Comentarios y Ensayos Críticos:**")
        st.markdown("- Robert Nozick, *Anarquía, estado y utopía*")
        st.markdown("- Jesús Huerta de Soto, *Socialismo, cálculo económico y función empresarial*")

    # --- CASO F: PERFIL COHERENTE - ANARQUISTA / AUTONOMISTA ---
    elif es_anarquista:
        st.success("✔ Diagnóstico: Coherencia Estructural Sólida — Tradición Ácrata y Autonomista")
        st.markdown("""
        **Análisis Crítico y Metacognición (Ideas Fundantes):**  
        Tus premisas convergen sólidamente en el horizonte del **anarquismo clásico y el autonomismo radical**.
        * **Idea fundante:** La emancipación radical frente a toda forma de dominación jerárquica, sea estatal, religiosa o económica.
        * **El orden y la economía:** El orden social no necesita coacción vertical; brota espontáneamente de la cooperación voluntaria, la ayuda mutua y la federación horizontal de los pueblos.
        
        **Movimientos, partidos y figuras históricas que encarnan esta tradición:**
        * *Movimientos y partidos:* El sindicalismo revolucionario histórico, comunas anarquistas (como en la Revolución Española), movimientos autonomistas contemporáneos.
        * *Personajes históricos:* Piotr Kropotkin, Mijaíl Bakunin, Pierre-Joseph Proudhon, Emma Goldman.
        """)
        
        st.subheader("📚 Itinerario Bibliográfico Sugerido:")
        st.markdown("**Fuentes Principales (Autores Clásicos):**")
        st.markdown("- Piotr Kropotkin, *La ayuda mutua*")
        st.markdown("- Mijaíl Bakunin, *Dios y el Estado*")
        st.markdown("**Comentarios y Ensayos Críticos:**")
        st.markdown("- Daniel Guérin, *El anarquismo: de la doctrina a la acción*")
        st.markdown("- Colin Ward, *Anarchy in Action*")

    # --- CASO G: PERFIL COHERENTE - COMUNITARIO / INDIGENISTA ---
    elif es_comunitario:
        st.success("✔ Diagnóstico: Coherencia Estructural Sólida — Ontología Comunitaria y del Bien Vivir")
        st.markdown("""
        **Análisis Crítico y Metacognición (Ideas Fundantes):**  
        Tus respuestas se sustentan en una matriz de **pensamiento comunitario e indigenista**.
        * **Idea fundante:** El ser humano no es un átomo aislado, sino un nodo inseparable de un organismo social y territorial más amplio (la comunidad y la Pacha).
        * **El orden y la economía:** El poder se concibe como servicio y reciprocidad (*mandar obedeciendo*). La economía prioriza la reproducción de la vida y el equilibrio ecológico por encima del lucro mercantil.
        
        **Movimientos, partidos y figuras históricas que encarnan esta tradición:**
        * *Movimientos y partidos:* Movimientos indígenas latinoamericanos, comunidades zapatistas, corrientes de socialismo indoamericano y ecologismo popular.
        * *Personajes históricos:* José Carlos Mariátegui, Túpac Katari, líderes comunales históricos y teóricos del Buen Vivir.
        """)
        
        st.subheader("📚 Itinerario Bibliográfico Sugerido:")
        st.markdown("**Fuentes Principales (Autores Clásicos):**")
        st.markdown("- José Carlos Mariátegui, *7 ensayos de interpretación de la realidad peruana*")
        st.markdown("- Manifiestos y documentos políticos de movimientos comunitarios originarios")
        st.markdown("**Comentarios y Ensayos Críticos:**")
        st.markdown("- Álvaro García Linera, *Forma valor y forma comunidad*")
        st.markdown("- Alberto Acosta, *El buen vivir: Sumak Kawsay, una oportunidad para imaginar otros mundos*")

    # --- CASO H: PERFIL ECLÉCTICO GENERAL ---
    else:
        st.info("ℹ️ Diagnóstico: Perfil Ecléctico / En Construcción")
        st.markdown("""
        **Análisis Crítico y Metacognición:**  
        Tus elecciones reflejan una combinación singular de diferentes tradiciones intelectuales. No te encasillas en un dogma cerrado, sino que amalgamas elementos de diversas procedencias sobre la naturaleza del poder, la economía y el individuo.
        
        **Desafío formativo:**  
        Este eclecticismo es propio de una mente en exploración, pero en la teoría política conlleva el riesgo de la incoherencia operativa si los supuestos chocan entre sí. Te invitamos a examinar qué puente une tus premisas para construir un discurso propio sólidamente argumentado.
        """)
        
        st.subheader("📚 Itinerario Bibliográfico Sugerido:")
        st.markdown("**Fuentes Principales (Autores Clásicos):**")
        st.markdown("- Norberto Bobbio, *Derecha e izquierda*")
        st.markdown("- Isaiah Berlin, *Cuatro ensayos sobre la libertad*")
        st.markdown("**Comentarios y Ensayos Críticos:**")
        st.markdown("- Michael Sandel, *El descontento con la democracia*")
        st.markdown("- Chantal Mouffe, *En torno a lo político*")

    st.balloons()
