import streamlit as st

st.set_page_config(page_title="Arqueología Antropológica Política", page_icon="🏛️", layout="wide")

st.title("🏛️ Simulador de Arqueología Antropológica Política")
st.markdown("---")
st.write("""
**Bienvenido al ejercicio de arqueología conceptual.** Inspirado en el flujo deductivo del pensamiento político, este simulador parte de tu **concepto de ser humano** para descender por las capas de la sociedad, el estado, la economía y el proyecto histórico. 
Tómate tu tiempo. Al finalizar, obtendrás una radiografía tabular, un diagnóstico crítico de tensiones y un riguroso modelamiento metacognitivo.
""")

# --- FORMULARIO DE DECISIONES SECUENCIALES (6 PASOS) ---
with st.form("formulario_arqueologia"):
    
    # 1. CONCEPTO DE SER HUMANO
    st.header("Paso 1: El Concepto de Ser Humano")
    st.markdown("*¿Cómo definirías la condición fundamental del ser humano?*")
    ser_humano = st.radio(
        "Selecciona la premisa con la que más te identifiques:",
        [
            "Un individuo autónomo y racional que busca maximizar su propio bienestar e interés particular.",
            "Un ser social e histórico cuya conciencia se forma a través del trabajo material y las relaciones colectivas.",
            "Un ser profundamente enraizado en su comunidad, su cultura, su familia y una herencia de valores tradicionales.",
            "Un dueño absoluto de su propio cuerpo y de su voluntad, que rechaza cualquier imposición externa.",
            "Un espíritu libre y soberano que no acepta ninguna autoridad, ley institucional o moral impuesta.",
            "Un eslabón inseparable de la tierra, la naturaleza y el bienestar colectivo de su pueblo originario."
        ],
        key="ser_choice"
    )

    st.markdown("---")

    # 2. CONCEPTO DE SOCIEDAD
    st.header("Paso 2: El Concepto de Sociedad")
    st.markdown("*¿Cómo se entienden las personas y de dónde nace el vínculo social?*")
    sociedad = st.radio(
        "Selecciona tu premisa sobre la sociedad:",
        [
            "Mediante un pacto o acuerdo contractual entre ciudadanos libres que buscan proteger sus intereses.",
            "Mediante un conflicto permanente y estructural entre grupos sociales según quién posee los medios de producción.",
            "Mediante una comunidad orgánica unida por lazos históricos, culturales, espirituales o de lealtad tradicional.",
            "Mediante la cooperación libre, voluntaria y sin coacción institucional entre individuos soberanos.",
            "Mediante la reciprocidad, el parentesco y la integración armónica con la comunidad y el territorio."
        ],
        key="soc_choice"
    )

    st.markdown("---")

    # 3. CONCEPTO DE NACIÓN
    st.header("Paso 3: El Concepto de Nación")
    st.markdown("*¿Cuál es el fundamento de la identidad colectiva o la pertenencia?*")
    nacion = st.radio(
        "Selecciona tu premisa sobre la nación:",
        [
            "Una asociación de ciudadanos bajo el imperio de la ley, abierta e integradora sin importar orígenes.",
            "Una comunidad de destino histórico, cultural o identitario que debe defender su soberanía y tradiciones.",
            "Una construcción artificial que divide a la clase trabajadora; la verdadera lealtad es internacional.",
            "Un orden político innecesario; la pertenencia se basa en comunas libres o asociaciones voluntarias.",
            "Una colectividad arraigada a la tierra ancestral y a la soberanía de los pueblos originarios."
        ],
        key="nac_choice"
    )

    st.markdown("---")

    # 4. CONCEPTO DE ESTADO
    st.header("Paso 4: El Concepto de Estado y Gobierno")
    st.markdown("*¿Cómo debe organizarse la autoridad política y el poder?*")
    estado = st.radio(
        "Selecciona tu premisa sobre el Estado:",
        [
            "Un árbitro neutral limitado por la ley y la división de poderes para garantizar las libertades individuales.",
            "Un instrumento de dominación de clase que debe ser transformado o superado mediante la praxis revolucionaria.",
            "Un custodio soberano del orden, la seguridad y la supervivencia colectiva frente a amenazas (amigo/enemigo).",
            "Una estructura ilegítima y coactiva que debe ser disuelta o reemplazada por contratos privados y autogestión.",
            "Un sistema de autoridad basado en el servicio comunal, la rotación de cargos y el mandar obedeciendo."
        ],
        key="est_choice"
    )

    st.markdown("---")

    # 5. CONCEPTO DE ECONOMÍA
    st.header("Paso 5: La Economía")
    st.markdown("*¿Cómo debe organizarse la producción y el reparto de la riqueza?*")
    economia = st.radio(
        "Selecciona tu modelo económico ideal:",
        [
            "Propiedad privada garantizada, libre mercado de precios y competencia económica sin trabas estatales.",
            "Propiedad social y planificación organizada de la producción para satisfacer las necesidades de toda la sociedad.",
            "Economía mixta regulada, donde el Estado interviene para asegurar el bienestar social y la equidad básica.",
            "Contratos estrictamente privados y voluntarios, eliminando monopolios estatales, impuestos y bancos centrales.",
            "Reciprocidad, trueque justo, trabajo comunitario y protección colectiva de los recursos naturales (Buen Vivir)."
        ],
        key="eco_choice"
    )

    st.markdown("---")

    # 6. PROYECTO HISTÓRICO Y GEOPOLÍTICA
    st.header("Paso 6: El Proyecto Histórico y el Tablero Global")
    st.markdown("*¿Cómo se proyecta este modelo hacia el mundo exterior y el futuro?*")
    proyecto = st.radio(
        "Selecciona tu visión del proyecto histórico global:",
        [
            "Integración global del mercado, apertura de fronteras y gobernanza a través de instituciones supranacionales.",
            "Un sistema multipolar de grandes bloques civilizacionales o potencias soberanas que defienden sus espacios.",
            "Superación global del capitalismo mediante la emancipación universal y la solidaridad internacional de los pueblos.",
            "Defensa radical de la pluralidad cultural y espiritual de cada civilización frente a la homogenización global.",
            "Construcción de autonomías locales autogestionadas en red, superando el sistema de Estados nacionales."
        ],
        key="pro_choice"
    )

    submitted = st.form_submit_button("Ejecutar Análisis y Modelamiento Metacognitivo")

# --- PROCESAMIENTO Y DIAGNÓSTICO FORMATIVO ---
if submitted:
    st.markdown("---")
    st.header("📊 Radiografía Tabular de tu Edificio Conceptual")

    import pandas as pd
    tabla_resumen = pd.DataFrame({
        "Dimensión del Esquema": [
            "1. Concepto de Ser Humano",
            "2. Concepto de Sociedad",
            "3. Concepto de Nación",
            "4. Concepto de Estado",
            "5. Economía",
            "6. Proyecto Histórico"
        ],
        "Elección del Estudiante": [
            ser_humano, sociedad, nacion, estado, economia, proyecto
        ]
    })
    st.table(tabla_resumen)

    st.markdown("---")
    st.header("🔍 Diagnóstico Crítico y Modelamiento Metacognitivo")

    # Detección de perfiles puros
    es_liberal = ("individuo autónomo" in ser_humano) and ("pacto o acuerdo" in sociedad or "propiedad privada garantizada" in economia)
    es_marxista = ("ser social e histórico" in ser_humano or "conflicto permanente" in sociedad) and ("propiedad social" in economia)
    es_tradicional = ("profundamente enraizado" in ser_humano or "comunidad orgánica" in sociedad) and ("custodio soberano" in estado or "grandes bloques" in proyecto)
    es_libertario = ("dueño absoluto" in ser_humano) and ("contratos estrictamente privados" in economia)
    es_anarquista = ("espíritu libre y soberano" in ser_humano or "cooperación libre" in sociedad) and ("estructura ilegítima" in estado)
    es_comunitario = ("eslabón inseparable de la tierra" in ser_humano) and ("reciprocidad" in economia)

    # Detecciones de tensiones específicas (Cruces de vertientes)
    tension_tradicional_liberal = ("enraizado" in ser_humano or "comunidad orgánica" in sociedad) and ("propiedad privada garantizada" in economia or "libre mercado" in economia)
    tension_libertario_estatista = ("dueño absoluto" in ser_humano) and ("economía mixta" in economia or "Estado" in estado)
    tension_socialdemocrata_radical = ("individuo autónomo" in ser_humano) and ("planificación" in economia or "propiedad social" in economia)

    # --- CASO A: TENSIONES ESPECÍFICAS (PERFILES HÍBRIDOS / MIXTOS) ---
    if tension_tradicional_liberal:
        st.warning("⚠️ Diagnóstico: Perfil Híbrido — Cruce entre Tradicionalismo Orgánico y Liberalismo de Mercado")
        st.markdown("""
        **1. Precisión de las vertientes en colisión:**  
        Estás mezclando los fundamentos del **Conservadurismo Orgánico / Tradicionalismo** (en tus pasos 1 y 2 sobre el ser humano y la comunidad) con las premisas del **Liberalismo Clásico y Capitalismo de Mercado** (en tu paso 5 sobre la economía).
        
        **2. Graduación de la tensión (Qué entra en contradicción vs. qué puede ser complementario):**  
        * *Lo complementario:* En la superficie política práctica, ambas corrientes suelen aliarse tácticamente frente a proyectos colectivistas o estatistas radicales en nombre de la libertad y el orden institucional.
        * *Lo irreconciliable (La contradicción profunda):* A nivel ontológico e histórico, chocan de forma violenta. El capitalismo de mercado opera como un motor de desintegración social que mercantiliza la vida, disuelve las lealtades familiares, erosiona las tradiciones locales y desarraiga a las comunidades. Pretender defender el enraizamiento orgánico mediante los mecanismos de un mercado absoluto es teóricamente contradictorio.
        
        **3. Modelamiento Metacognitivo (Cómo reestructurar tu postura desde el Concepto de Ser Humano):**  
        Para resolver esta tensión y dar consistencia a tu edificio político, debes volver obligatoriamente al **Paso 1 (Concepto de Ser Humano)** y preguntarte qué valor tiene el peso fundante para ti:  
        * **Opción A (Girar hacia el Liberalismo):** Si concluyes que el individuo autónomo y maximizador es lo primario, debes aceptar que las tradiciones y los vínculos comunitarios son secundarios y deben subordinarse a las leyes del libre mercado.  
        * **Opción B (Girar hacia el Tradicionalismo/Comunitarismo):** Si concluyes que el ser humano enraizado y la comunidad orgánica son lo primario, debes subordinar la economía al bien común moral, limitando o regulando el mercado desregulado (mirando hacia doctrinas como el distributismo o el corporativismo social).
        
        **Movimientos y personajes históricos que han intentado abordar este cruce:**  
        * *Corrientes:* El distributismo, la democracia cristiana de base social, el conservadurismo popular de posguerra.  
        * *Figuras:* Wilhelm Röpke, G.K. Chesterton, Konrad Adenauer.
        """)
        
        st.subheader("📚 Itinerario Bibliográfico Riguroso:")
        st.markdown("**Fuentes Principales (Autores Clásicos):**")
        st.markdown("- Karl Polanyi, *La gran transformación*")
        st.markdown("- G.K. Chesterton, *Esbozo de la cordura*")
        st.markdown("**Comentarios y Ensayos Críticos:**")
        st.markdown("- Wilhelm Röpke, *La crisis de nuestro tiempo*")
        st.markdown("- Michael Sandel, *Lo que el dinero no puede comprar*")

    elif tension_libertario_estatista:
        st.warning("⚠️ Diagnóstico: Perfil Híbrido — Cruce entre Libertarismo Radical y Estatismo / Reformismo")
        st.markdown("""
        **1. Precisión de las vertientes en colisión:**  
        Estás combinando el **Anarcocapitalismo / Libertarismo Radical** (en tu concepto de autopropiedad absoluta) con elementos del **Estatismo Regulador o la Economía Mixta** (en tus opciones sobre estado o economía).
        
        **2. Graduación de la tensión:**  
        * *Lo complementario:* Ambas posturas valoran la vigencia formal del orden legal y la estabilidad institucional frente al caos.
        * *Lo irreconciliable:* Para el libertarismo estricto, el Estado es una agencia ilegítima de agresión basada en el monopolio de la coacción y los impuestos. Tolerar intervenciones estatales o regulaciones anula el axioma moral de la autopropiedad.
        
        **3. Modelamiento Metacognitivo:**  
        Vuelve al **Concepto de Ser Humano**: define si la soberanía individual es absoluta e intransigente (lo que exige rechazar cualquier forma de coerción estatal) o si adoptas un pragmatismo liberal reformista que acepta un Estado mínimo regulador.
        """)
        
        st.subheader("📚 Itinerario Bibliográfico Riguroso:")
        st.markdown("**Fuentes Principales:**")
        st.markdown("- Murray Rothbard, *Ética de la libertad*")
        st.markdown("**Comentarios y Ensayos Críticos:**")
        st.markdown("- Robert Nozick, *Anarquía, estado y utopía*")

    # --- CASOS B A G: PERFILES COHERENTES ---
    elif es_liberal:
        st.success("✔ Diagnóstico: Coherencia Estructural Sólida — Liberalismo Clásico")
        st.markdown("""
        **Ideas Fundantes y Modelamiento Coherente:**  
        Tu edificio conceptual es plenamente consistente con el **Liberalismo Clásico**. 
        * *Concepto de ser humano:* Agente racional, autónomo y titular de derechos inalienables.
        * *Deducción doctrinal:* Sociedad contractual, Estado neutral garante de leyes y economía de libre mercado.
        
        **Movimientos y figuras históricas:**  
        * *Movimientos:* Liberalismo decimonónico, reformismo republicano.
        * *Personajes:* John Locke, Adam Smith, Alexis de Tocqueville.
        """)
        st.subheader("📚 Itinerario Bibliográfico Riguroso:")
        st.markdown("**Fuentes Principales:**")
        st.markdown("- John Locke, *Segundo tratado sobre el gobierno civil*")
        st.markdown("- Adam Smith, *La riqueza de las naciones*")
        st.markdown("**Comentarios y Ensayos Críticos:**")
        st.markdown("- Friedrich Hayek, *Los fundamentos de la libertad*")

    elif es_marxista:
        st.success("✔ Diagnóstico: Coherencia Estructural Sólida — Marxismo y Teoría Crítica")
        st.markdown("""
        **Ideas Fundantes y Modelamiento Coherente:**  
        Tu edificio conceptual sigue la línea del **Materialismo Histórico**.
        * *Concepto de ser humano:* Ser social constituido por el trabajo y la producción material.
        * *Deducción doctrinal:* Sociedad dividida en clases, superación del Estado burgués y planificación social de la economía.
        
        **Movimientos y figuras históricas:**  
        * *Movimientos:* Comunismo histórico, sindicalismo revolucionario.
        * *Personajes:* Karl Marx, Vladimir Lenin, Antonio Gramsci.
        """)
        st.subheader("📚 Itinerario Bibliográfico Riguroso:")
        st.markdown("**Fuentes Principales:**")
        st.markdown("- Karl Marx, *El Capital*")
        st.markdown("**Comentarios y Ensayos Críticos:**")
        st.markdown("- Antonio Gramsci, *Cuadernos de la cárcel*")

    elif es_tradicional:
        st.success("✔ Diagnóstico: Coherencia Estructural Sólida — Tradicionalismo y Geopolítica Soberana")
        st.markdown("""
        **Ideas Fundantes y Modelamiento Coherente:**  
        Tus respuestas convergen en el **Realismo Político y Conservadurismo Orgánico**.
        * *Concepto de ser humano:* Ser enraizado a una comunidad y un orden histórico.
        * *Deducción doctrinal:* Soberanía política, Estado custodio frente al conflicto y orden multipolar de civilizaciones.
        
        **Movimientos y figuras históricas:**  
        * *Movimientos:* Soberanismos nacionales, tradicionalismo político.
        * *Personajes:* Thomas Hobbes, Carl Schmitt, Charles de Gaulle.
        """)
        st.subheader("📚 Itinerario Bibliográfico Riguroso:")
        st.markdown("**Fuentes Principales:**")
        st.markdown("- Thomas Hobbes, *Leviatán*")
        st.markdown("- Carl Schmitt, *El concepto de lo político*")
        st.markdown("**Comentarios y Ensayos Críticos:**")
        st.markdown("- Aleksandr Dugin, *La cuarta teoría política*")

    elif es_libertario:
        st.success("✔ Diagnóstico: Coherencia Estructural Sólida — Anarcocapitalismo / Libertarismo")
        st.markdown("""
        **Ideas Fundantes y Modelamiento Coherente:**  
        Tu perfil responde al **Libertarismo Radical de Mercado**.
        * *Concepto de ser humano:* Propietario absoluto de su cuerpo y voluntad.
        * *Deducción doctrinal:* Rechazo total al Estado, contratos voluntarios y banca libre.
        
        **Movimientos y figuras históricas:**  
        * *Movimientos:* Movimiento libertario austríaco.
        * *Personajes:* Murray Rothbard, Ludwig von Mises.
        """)
        st.subheader("📚 Itinerario Bibliográfico Riguroso:")
        st.markdown("**Fuentes Principales:**")
        st.markdown("- Murray Rothbard, *Ética de la libertad*")
        st.markdown("**Comentarios y Ensayos Críticos:**")
        st.markdown("- Jesús Huerta de Soto, *Socialismo, cálculo económico y función empresarial*")

    elif es_anarquista:
        st.success("✔ Diagnóstico: Coherencia Estructural Sólida — Anarquismo Clásico")
        st.markdown("""
        **Ideas Fundantes y Modelamiento Coherente:**  
        Tu edificio conceptual es coherente con el **Anarquismo Autonomista**.
        * *Concepto de ser humano:* Espíritu libre incompatible con la jerarquía.
        * *Deducción doctrinal:* Acción directa, ayuda mutua y federación horizontal sin Estado.
        
        **Movimientos y figuras históricas:**  
        * *Movimientos:* Anarcosindicalismo, comunas autónomas.
        * *Personajes:* Piotr Kropotkin, Mijaíl Bakunin.
        """)
        st.subheader("📚 Itinerario Bibliográfico Riguroso:")
        st.markdown("**Fuentes Principales:**")
        st.markdown("- Piotr Kropotkin, *La ayuda mutua*")
        st.markdown("**Comentarios y Ensayos Críticos:**")
        st.markdown("- Daniel Guérin, *El anarquismo*")

    elif es_comunitario:
        st.success("✔ Diagnóstico: Coherencia Estructural Sólida — Ontología Comunitaria y del Buen Vivir")
        st.markdown("""
        **Ideas Fundantes y Modelamiento Coherente:**  
        Tus respuestas se sustentan en el **Comunitarismo Indigenista**.
        * *Concepto de ser humano:* Nodo inseparable de la comunidad y la tierra.
        * *Deducción doctrinal:* Reciprocidad, mandar obedeciendo y defensa del territorio.
        
        **Movimientos y figuras históricas:**  
        * *Movimientos:* Movimientos indígenas de los Andes, zapatismo.
        * *Personajes:* José Carlos Mariátegui, líderes comunitarios del Buen Vivir.
        """)
        st.subheader("📚 Itinerario Bibliográfico Riguroso:")
        st.markdown("**Fuentes Principales:**")
        st.markdown("- José Carlos Mariátegui, *7 ensayos de interpretación de la realidad peruana*")
        st.markdown("**Comentarios y Ensayos Críticos:**")
        st.markdown("- Álvaro García Linera, *Forma valor y forma comunidad*")

    else:
        st.info("ℹ️ Diagnóstico: Perfil Ecléctico / En Exploración Conceptual")
        st.markdown("""
        **1. Precisión de las vertientes en juego:**  
        Tus respuestas combinan múltiples tradiciones sin encasillarse en una estructura cerrada, cruzando elementos de diversas escuelas sobre la naturaleza del poder, la sociedad y la economía.
        
        **2. Análisis Crítico y Graduación de Tensiones:**  
        Este eclecticismo refleja una mente en plena exploración teórica. Sin embargo, al no anclar claramente las capas inferiores (sociedad y estado) al supuesto necesario inicial (tu **Concepto de Ser Humano**), el edificio corre el riesgo de volverse incoherente en la práctica política.
        
        **3. Modelamiento Metacognitivo:**  
        Para ordenar tu pensamiento, modela tu postura partiendo estrictamente del **Paso 1 (Concepto de Ser Humano)**: define qué principio tiene mayor peso ontológico para ti (el individuo soberano, el trabajador social o el miembro enraizado de una comunidad) y observa cómo las demás capas del esquema deben subordinarse lógicamente a esa elección fundante.
        """)
        st.subheader("📚 Itinerario Bibliográfico Riguroso:")
        st.markdown("**Fuentes Principales (Autores Clásicos):**")
        st.markdown("- Norberto Bobbio, *Derecha e izquierda*")
        st.markdown("- Isaiah Berlin, *Cuatro ensayos sobre la libertad*")
        st.markdown("**Comentarios y Ensayos Críticos:**")
        st.markdown("- Michael Sandel, *El descontento con la democracia*")
        st.markdown("- Chantal Mouffe, *En torno a lo político*")

    st.balloons()
