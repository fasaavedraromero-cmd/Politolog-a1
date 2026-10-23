import streamlit as st
import pandas as pd

st.set_page_config(page_title="Arqueología Antropológica Política", page_icon="🏛️", layout="wide")

st.title("🏛️ Simulador de Arqueología Antropológica Política")
st.markdown("---")
st.write("""
**Bienvenido al laboratorio de arqueología conceptual.** Inspirado en el flujo deductivo del pensamiento político, este simulador parte de tu **concepto de ser humano** para descender por las capas de la sociedad, la nación, el estado, la economía y el proyecto histórico. 
Tómate tu tiempo en cada dilema. Al finalizar, obtendrás una radiografía tabular, un diagnóstico crítico de tensiones y un riguroso modelamiento metacognitivo guiado por fuentes clásicas y pensadores de nuestra tradición hispanoamericana y chilena.
""")

# --- FORMULARIO DE DECISIONES SECUENCIALES (6 PASOS) ---
with st.form("formulario_arqueologia"):
    
    # 1. CONCEPTO DE SER HUMANO
    st.header("Paso 1: El Concepto de Ser Humano")
    st.markdown("*Antes de estructurar la política, ¿cómo definirías la condición fundamental del ser humano?*")
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

    # Detección de perfiles puros para las 7 vertientes
    es_liberal = ("individuo autónomo" in ser_humano) and ("pacto o acuerdo" in sociedad or "propiedad privada garantizada" in economia)
    es_marxista = ("ser social e histórico" in ser_humano or "conflicto permanente" in sociedad) and ("propiedad social" in economia)
    es_tradicional = ("profundamente enraizado" in ser_humano or "comunidad orgánica" in sociedad) and ("custodio soberano" in estado or "grandes bloques" in proyecto)
    es_libertario = ("dueño absoluto" in ser_humano) and ("contratos estrictamente privados" in economia)
    es_anarquista = ("espíritu libre y soberano" in ser_humano or "cooperación libre" in sociedad) and ("estructura ilegítima" in estado)
    es_comunitario = ("eslabón inseparable de la tierra" in ser_humano) and ("reciprocidad" in economia)

    # Detección de tensiones específicas (Cruces de vertientes híbridas)
    tension_tradicional_liberal = ("enraizado" in ser_humano or "comunidad orgánica" in sociedad) and ("propiedad privada garantizada" in economia or "libre mercado" in economia)
    tension_libertario_estatista = ("dueño absoluto" in ser_humano) and ("economía mixta" in economia or "Estado" in estado)

    # --- CASO A: TENSIONES ESPECÍFICAS (PERFILES HÍBRIDOS / MIXTOS) ---
    if tension_tradicional_liberal:
        st.warning("⚠️ Diagnóstico: Perfil Híbrido — Cruce entre Tradicionalismo Orgánico y Liberalismo de Mercado")
        st.markdown("""
        **1. Precisión de las vertientes en colisión:**  
        Estás mezclando los fundamentos del **Conservadurismo Orgánico / Tradicionalismo** (en tu concepto de ser humano y sociedad) con las premisas del **Liberalismo Clásico y Capitalismo de Mercado** (en tu modelo económico).
        
        **2. Graduación de la tensión (Qué entra en contradicción vs. qué puede ser complementario):**  
        * *Lo complementario:* En la política práctica, ambas corrientes suelen aliarse tácticamente frente a proyectos colectivistas radicales en nombre de la libertad individual y el orden institucional.
        * *Lo irreconciliable (La contradicción profunda):* A nivel ontológico, chocan violentamente. El capitalismo de mercado opera como un disolvente social que mercantiliza la vida, corroe las tradiciones locales y desarraiga a las comunidades que tu antropología busca proteger. Pretender defender el enraizamiento mediante la lógica de un mercado absoluto es una contradicción teórica mayor.
        
        **3. Modelamiento Metacognitivo (Cómo reestructurar tu postura desde el Concepto de Ser Humano):**  
        Para resolver esta incoherencia y dar consistencia a tu edificio político, debes volver obligatoriamente al **Paso 1 (Concepto de Ser Humano)** y ponderar qué principio tiene primacía para ti:  
        * *Si tu base es el individuo maximizador:* Debes aceptar que las tradiciones secundan al mercado y ceden ante su dinámica.  
        * *Si tu base es la comunidad enraizada:* Debes subordinar la economía al bien común moral y a la regulación comunitaria (mirando hacia el distributismo o el socialcristianismo histórico).
        
        **Movimientos, partidos y referentes históricos y chilenos:**  
        * *Corrientes:* El distributismo, la democracia cristiana de base social, el conservadurismo social.  
        * *Figuras y referentes:* Wilhelm Röpke, G.K. Chesterton; en el pensamiento chileno, el pensamiento social de Jaime Eyzaguirre o el corporativismo moderado.
        """)
        
        st.subheader("📚 Itinerario Bibliográfico con Aporte Temático y Guía de Lectura:")
        st.markdown("**Fuentes Principales (Autores Clásicos):**")
        st.markdown("- Karl Polanyi, *La gran transformación* (Aporte: Explica cómo el mercado desbocado destruye las instituciones sociales. Leer: Capítulos 4 al 6: *Sistemas económicos y el surgimiento del mercado*).")
        st.markdown("- G.K. Chesterton, *Esbozo de la cordura* (Aporte: Fundamenta la propiedad distribuida frente al capitalismo centralizado. Leer: Primera parte, Capítulos 1 al 3).")
        st.markdown("**Comentarios y Ensayos Críticos:**")
        st.markdown("- Wilhelm Röpke, *La crisis de nuestro tiempo* (Aporte: Diagnóstico sobre la masificación y el rescate de la economía humana. Leer: Capítulo 3: *La desintegración económica y social*).")
        st.markdown("- Michael Sandel, *Lo que el dinero no puede comprar* (Aporte: Límites morales de los mercados en la vida comunitaria. Leer: Introducción y Capítulo 1).")

    elif tension_libertario_estatista:
        st.warning("⚠️ Diagnóstico: Perfil Híbrido — Cruce entre Libertarismo Radical y Estatismo / Reformismo")
        st.markdown("""
        **1. Precisión de las vertientes en colisión:**  
        Estás combinando el **Anarcocapitalismo / Libertarismo Radical** (en tu concepto de autopropiedad absoluta) con elementos del **Estatismo Regulador o la Economía Mixta**.
        
        **2. Graduación de la tensión:**  
        * *Lo complementario:* Ambas posturas valoran la seguridad jurídica formal.
        * *Lo irreconciliable:* Para el libertarismo estricto, el Estado es una organización criminal institucionalizada basada en el monopolio de la coacción y los impuestos. Tolerar intervenciones estatales invalida el axioma moral de la autopropiedad.
        
        **3. Modelamiento Metacognitivo:**  
        Vuelve al **Concepto de Ser Humano**: define si la soberanía personal es intransigente (rechazando todo impuesto) o si adoptas un liberalismo reformista que acepta un Estado mínimo arbitral.
        
        **Movimientos y referentes:**  
        * *Corrientes:* Minarquismo, libertarismo pragmático.
        * *Figuras:* Murray Rothbard, Robert Nozick.
        """)
        
        st.subheader("📚 Itinerario Bibliográfico con Aporte Temático y Guía de Lectura:")
        st.markdown("**Fuentes Principales:**")
        st.markdown("- Murray Rothbard, *Ética de la libertad* (Aporte: Fundamentación de los derechos naturales libertarios. Leer: Parte I: Ley natural).")
        st.markdown("**Comentarios y Ensayos Críticos:**")
        st.markdown("- Robert Nozick, *Anarquía, estado y utopía* (Aporte: Defensa crítica del Estado mínimo frente al anarcocapitalismo. Leer: Capítulo 3: *Las granjas morales del Estado*).")

    # --- CASOS B A G: PERFILES COHERENTES (LAS 7 VERTIENTES) ---
    elif es_liberal:
        st.success("✔ Diagnóstico: Coherencia Estructural Sólida — Liberalismo Clásico")
        st.markdown("""
        **Ideas Fundantes y Modelamiento Coherente:**  
        Tu edificio conceptual es plenamente consistente con la **Tradición Liberal**. 
        * *Concepto de ser humano:* Agente racional, autónomo y titular de derechos inalienables.
        * *Deducción doctrinal:* Sociedad contractual, Estado neutral garante de leyes y libre mercado.
        
        **Movimientos y referentes históricos y chilenos:**  
        * *Movimientos:* Liberalismo político, reformismo republicano.
        * *Figuras:* John Locke, Adam Smith; en Chile, pensadores del liberalismo clásico decimonónico como José Victorino Lastarria.
        """)
        st.subheader("📚 Itinerario Bibliográfico con Aporte Temático y Guía de Lectura:")
        st.markdown("**Fuentes Principales:**")
        st.markdown("- John Locke, *Segundo tratado sobre el gobierno civil* (Aporte: Origen del contrato social y la propiedad. Leer: Capítulos 2, 5 y 8).")
        st.markdown("- Adam Smith, *La riqueza de las naciones* (Aporte: Funcionamiento del mercado y división del trabajo. Leer: Capítulos 1 al 3 del Libro I).")
        st.markdown("**Comentarios y Ensayos Críticos:**")
        st.markdown("- Friedrich Hayek, *Los fundamentos de la libertad* (Aporte: Defensa del orden espontáneo de mercado. Leer: Capítulos 1 y 4).")

    elif es_marxista:
        st.success("✔ Diagnóstico: Coherencia Estructural Sólida — Marxismo y Teoría Crítica")
        st.markdown("""
        **Ideas Fundantes y Modelamiento Coherente:**  
        Tu edificio conceptual sigue la línea del **Materialismo Histórico y la Teoría Crítica**.
        * *Concepto de ser humano:* Ser social constituido por el trabajo y la producción material.
        * *Deducción doctrinal:* Sociedad dividida en clases, superación del Estado burgués y planificación social de la economía.
        
        **Movimientos y referentes históricos y chilenos:**  
        * *Movimientos:* Comunismo histórico, sindicalismo revolucionario y de clase.
        * *Figuras:* Karl Marx, Antonio Gramsci; en Chile, Luis Emilio Recabarren y Clotario Blest.
        """)
        st.subheader("📚 Itinerario Bibliográfico con Aporte Temático y Guía de Lectura:")
        st.markdown("**Fuentes Principales:**")
        st.markdown("- Karl Marx, *El Capital* (Aporte: Análisis de la plusvalía y la mercancía. Leer: Sección 1, Capítulo 1).")
        st.markdown("**Comentarios y Ensayos Críticos:**")
        st.markdown("- Antonio Gramsci, *Cuadernos de la cárcel* (Aporte: Hegemonía cultural y bloque histórico. Leer: Antología sobre el Estado y los intelectuales).")

    elif es_tradicional:
        st.success("✔ Diagnóstico: Coherencia Estructural Sólida — Tradicionalismo y Geopolítica Soberana")
        st.markdown("""
        **Ideas Fundantes y Modelamiento Coherente:**  
        Tus respuestas convergen en el **Realismo Político y Conservadurismo Orgánico**.
        * *Concepto de ser humano:* Ser enraizado a una comunidad y un orden histórico.
        * *Deducción doctrinal:* Soberanía política, Estado custodio frente al conflicto y orden multipolar de civilizaciones.
        
        **Movimientos y referentes históricos y chilenos:**  
        * *Movimientos:* Soberanismos nacionales, realismo geopolítico.
        * *Figuras:* Thomas Hobbes, Carl Schmitt; en Chile, la tradición del realismo geopolítico militar y estamental (ej. Ramón Cañas Montalva).
        """)
        st.subheader("📚 Itinerario Bibliográfico con Aporte Temático y Guía de Lectura:")
        st.markdown("**Fuentes Principales:**")
        st.markdown("- Thomas Hobbes, *Leviatán* (Aporte: Necesidad de la soberanía fuerte para evitar el caos. Leer: Capítulos 13, 17 y 18).")
        st.markdown("- Carl Schmitt, *El concepto de lo político* (Aporte: La distinción amigo/enemigo. Leer: Capítulos 1 al 3).")
        st.markdown("**Comentarios y Ensayos Críticos:**")
        st.markdown("- Aleksandr Dugin, *La cuarta teoría política* (Aporte: Crítica al globalismo y defensa del *Großraum*. Leer: Capítulos iniciales).")

    elif es_libertario:
        st.success("✔ Diagnóstico: Coherencia Estructural Sólida — Anarcocapitalismo / Libertarismo")
        st.markdown("""
        **Ideas Fundantes y Modelamiento Coherente:**  
        Tu perfil responde al **Libertarismo Radical de Mercado**.
        * *Concepto de ser humano:* Propietario absoluto de su cuerpo y voluntad.
        * *Deducción doctrinal:* Rechazo total al Estado, contratos voluntarios y banca libre.
        
        **Movimientos y referentes:**  
        * *Movimientos:* Escuela austríaca de economía, movimiento libertario.
        * *Figuras:* Murray Rothbard, Ludwig von Mises.
        """)
        st.subheader("📚 Itinerario Bibliográfico con Aporte Temático y Guía de Lectura:")
        st.markdown("**Fuentes Principales:**")
        st.markdown("- Murray Rothbard, *Ética de la libertad* (Aporte: Fundamentación de los derechos naturales libertarios. Leer: Parte I: Ley natural).")
        st.markdown("**Comentarios y Ensayos Críticos:**")
        st.markdown("- Jesús Huerta de Soto, *Socialismo, cálculo económico y función empresarial* (Aporte: Imposibilidad del socialismo y defensa de la función empresarial libre. Leer: Capítulos 1 y 2).")

    elif es_anarquista:
        st.success("✔ Diagnóstico: Coherencia Estructural Sólida — Anarquismo Clásico")
        st.markdown("""
        **Ideas Fundantes y Modelamiento Coherente:**  
        Tu edificio conceptual es coherente con el **Anarquismo Autonomista**.
        * *Concepto de ser humano:* Espíritu libre incompatible con la jerarquía.
        * *Deducción doctrinal:* Acción directa, ayuda mutua y federación horizontal sin Estado.
        
        **Movimientos y referentes históricos y chilenos:**  
        * *Movimientos:* Anarcosindicalismo de principios del siglo XX en Chile, comunas autónomas.
        * *Figuras:* Piotr Kropotkin, Mijaíl Bakunin; en Chile, los precursores del movimiento obrero ácrata.
        """)
        st.subheader("📚 Itinerario Bibliográfico con Aporte Temático y Guía de Lectura:")
        st.markdown("**Fuentes Principales:**")
        st.markdown("- Piotr Kropotkin, *La ayuda mutua* (Aporte: Factor evolutivo de la cooperación social sin estado. Leer: Introducción y Conclusión).")
        st.markdown("**Comentarios y Ensayos Críticos:**")
        st.markdown("- Daniel Guérin, *El anarquismo* (Aporte: Síntesis histórica de la praxis ácrata. Leer: Capítulos introductorios).")

    elif es_comunitario:
        st.success("✔ Diagnóstico: Coherencia Estructural Sólida — Ontología Comunitaria y del Buen Vivir")
        st.markdown("""
        **Ideas Fundantes y Modelamiento Coherente:**  
        Tus respuestas se sustentan en el **Comunitarismo Indigenista y del Buen Vivir**.
        * *Concepto de ser humano:* Nodo inseparable de la comunidad y la tierra.
        * *Deducción doctrinal:* Reciprocidad, mandar obedeciendo y defensa colectiva del territorio.
        
        **Movimientos y referentes históricos y latinoamericanos:**  
        * *Movimientos:* Zapatismo, movimientos originarios andinos.
        * *Figuras:* José Carlos Mariátegui, Alberto Acosta, teóricos del Sumak Kawsay.
        """)
        st.subheader("📚 Itinerario Bibliográfico con Aporte Temático y Guía de Lectura:")
        st.markdown("**Fuentes Principales:**")
        st.markdown("- José Carlos Mariátegui, *7 ensayos de interpretación de la realidad peruana* (Aporte: El problema del indio y la raíz comunitaria agraria. Leer: Ensayo sobre el problema agrario).")
        st.markdown("**Comentarios y Ensayos Críticos:**")
        st.markdown("- Alberto Acosta, *El buen vivir: Sumak Kawsay* (Aporte: Alternativas al desarrollo capitalista desde la cosmovisión comunitaria. Leer: Capítulos 1 y 2).")

    else:
        st.warning("⚠️ Diagnóstico: Perfil Híbrido / Ecléctico en Exploración Conceptual Avanzada")
        st.markdown("""
        **1. Precisión de las vertientes en juego:**  
        Tus respuestas combinan elementos de diversas tradiciones intelectuales sin anclarse rígidamente en un solo bloque doctrinal, cruzando miradas del liberalismo, el socialismo, el comunitarismo o el realismo.
        
        **2. Análisis Crítico y Graduación de Tensiones:**  
        Este eclecticismo es propio de una etapa de profunda exploración teórica. Sin embargo, en el rigor de la ciencia política, la falta de un anclaje deductivo estricto desde tu **Concepto de Ser Humano** hacia el Estado y la economía genera cortocircuitos doctrinales en la práctica. Lo que para ti puede parecer pragmatismo, desde la teoría pura implica aceptar premisas ontológicas que se neutralizan entre sí.
        
        **3. Modelamiento Metacognitivo (Cómo reestructurar tu postura):**  
        Para ordenar y dar consistencia a tu pensamiento, parte estrictamente del **Paso 1 (Concepto de Ser Humano)**: define qué principio tiene mayor peso ontológico irrenunciable para ti (el individuo autónomo y soberano, el trabajador social transformador, o el miembro enraizado de una comunidad histórica). Una vez fijado ese "supuesto necesario", observa obligatoriamente cómo las demás capas del esquema (sociedad, estado, economía y proyecto histórico) deben subordinarse de forma lógica a esa raíz fundante para superar la incoherencia.
        
        **Movimientos y referentes históricos y chilenos de referencia transversal:**  
        * *Corrientes:* Pensamiento institucionalista, reformismo democrático.  
        * *Figuras:* Norberto Bobbio, Michael Sandel.
        """)
        st.subheader("📚 Itinerario Bibliográfico con Aporte Temático y Guía de Lectura:")
        st.markdown("**Fuentes Principales (Autores Clásicos):**")
        st.markdown("- Norberto Bobbio, *Derecha e izquierda* (Aporte: Criterios analíticos para clasificar las familias políticas. Leer: Capítulos 1 al 3).")
        st.markdown("**Comentarios y Ensayos Críticos:**")
        st.markdown("- Michael Sandel, *El descontento con la democracia* (Aporte: Crítica al liberalismo procedimental y rescate comunitarista. Leer: Introducción).")
        st.markdown("- Chantal Mouffe, *En torno a lo político* (Aporte: La dimensión agonística de la política. Leer: Capítulos 1 y 2).")

    st.balloons()
