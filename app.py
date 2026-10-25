import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="Radiografía de creencias e ideas políticas", page_icon="🏛️", layout="wide")

st.title("🏛️ Radiografía de creencias e ideas políticas")
st.markdown("---")
st.write("""
**Bienvenido al laboratorio de arqueología conceptual.** Este instrumento de alta densidad analítica parte de tu **concepto de ser humano** (Bloque 1) para descender metodológicamente por el vínculo social (Bloque 2), la nación e identidad (Bloque 3), el estado y la autoridad (Bloque 4), la economía y riqueza (Bloque 5), y la geopolítica y proyecto histórico (Bloque 6). 
Tómate tu tiempo en cada uno de los 24 dilemas. Al finalizar, el sistema generará una radiografía cuantitativa de tus vertientes, un glosario conceptual riguroso, un diagnóstico multidoctrinal de tensiones, un modelamiento de opciones y una base bibliográfica primaria con capítulos específicos.
""")

# --- DEFINICIÓN DE PREGUNTAS Y OPCIONES CON SUS ETIQUETAS INTERNAS PARA EVITAR SESGOS ---
# Cada opción define explícitamente a qué vertiente aporta puntos, permitiendo barajarlas de forma aleatoria.
banco_preguntas = [
    # Bloque 1: El Concepto de Ser Humano
    [
        "1. Motor de la acción: ¿Qué impulsa fundamentalmente al ser humano en su vida en común?",
        [
            ("La búsqueda racional de su propio interés y beneficio particular.", "Liberalismo Clásico"),
            ("La necesidad material y su transformación a través del trabajo colectivo.", "Marxismo y Teoría Crítica"),
            ("El sentido de pertenencia a una comunidad orgánica, la familia y la tradición.", "Tradicionalismo y Realismo"),
            ("El impulso irrenunciable hacia la soberanía absoluta de su propio cuerpo y voluntad.", "Libertarismo Radical")
        ]
    ],
    [
        "2. Naturaleza y devenir: ¿Cómo consideras la condición fundamental de las personas?",
        [
            ("Un individuo cuyos derechos y autonomía preceden a cualquier sociedad.", "Liberalismo Clásico"),
            ("Un sujeto histórico cuya conciencia cambia según las condiciones materiales.", "Marxismo y Teoría Crítica"),
            ("Un heredero de tradiciones e instituciones que lo trascienden históricamente.", "Tradicionalismo y Realismo"),
            ("Un espíritu libre que rechaza de raíz toda imposición moral o legal externa.", "Anarquismo Clásico")
        ]
    ],
    [
        "3. Libertad y voluntad: ¿Cuál es el origen y el alcance de la libertad humana?",
        [
            ("Es una capacidad de elección racional dentro de las reglas del mercado y la ley.", "Liberalismo Clásico"),
            ("Es la emancipación colectiva frente a las cadenas de la explotación económica.", "Marxismo y Teoría Crítica"),
            ("Es una libertad situada y concreta, enmarcada en deberes hacia la comunidad y Dios.", "Tradicionalismo y Realismo"),
            ("Es un absoluto ontológico de autopropiedad que no admite restricciones externas.", "Libertarismo Radical")
        ]
    ],
    [
        "4. Moral y naturaleza: ¿De dónde surge el orden moral que guía al ser humano?",
        [
            ("De convenciones y contratos racionales acordados libremente por los individuos.", "Liberalismo Clásico"),
            ("De la superación histórica de las ideologías alienantes mediante la praxis.", "Marxismo y Teoría Crítica"),
            ("De un orden natural, la ley eterna o la transmisión consuetudinaria de los mayores.", "Tradicionalismo y Realismo"),
            ("De la conciencia individual soberana, totalmente exenta de mandatos coactivos.", "Anarquismo Clásico")
        ]
    ],
    
    # Bloque 2: El Vínculo Social
    [
        "5. Origen del lazo: ¿Cómo se constituye fundamentalmente la sociedad?",
        [
            ("Mediante un contrato voluntario entre ciudadanos para proteger intereses.", "Liberalismo Clásico"),
            ("Mediante un conflicto estructural e histórico entre clases sociales.", "Marxismo y Teoría Crítica"),
            ("Mediante lazos históricos, culturales y espirituales preexistentes.", "Tradicionalismo y Realismo"),
            ("Mediante la cooperación libre y espontánea, sin coacción institucional.", "Anarquismo Clásico")
        ]
    ],
    [
        "6. Regla de convivencia: ¿Qué debe regular la vida en común?",
        [
            ("El imperio de la ley impersonal, los contratos y la neutralidad institucional.", "Liberalismo Clásico"),
            ("La superación de las contradicciones de clase mediante la acción colectiva.", "Marxismo y Teoría Crítica"),
            ("La fidelidad a los valores compartidos, las costumbres y la autoridad tradicional.", "Tradicionalismo y Realismo"),
            ("La autonomía absoluta de cada asociación voluntaria o comuna libre.", "Anarquismo Clásico")
        ]
    ],
    [
        "7. Autoridad y obediencia: ¿Qué justifica la obediencia o el orden social?",
        [
            ("El consentimiento voluntario de los gobernados regulado por procedimientos legales.", "Liberalismo Clásico"),
            ("La dirección consciente orientada a erradicar la injusticia y la escasez.", "Marxismo y Teoría Crítica"),
            ("La jerarquía natural, el honor, el respeto a los mayores y la cohesión orgánica.", "Tradicionalismo y Realismo"),
            ("Ninguna autoridad; el orden solo emerge de la asociación voluntaria y la ayuda mutua.", "Anarquismo Clásico")
        ]
    ],
    [
        "8. Cohesión comunitaria: ¿Qué mantiene unida a una comunidad humana sana?",
        [
            ("El respeto mutuo a los derechos individuales y la eficiencia de los intercambios.", "Liberalismo Clásico"),
            ("La conciencia de clase y la solidaridad en la lucha contra la dominación.", "Marxismo y Teoría Crítica"),
            ("El arraigo a la tierra, la lengua, la fe común y la memoria de los ancestros.", "Tradicionalismo y Realismo"),
            ("Las redes de afecto horizontal, la afinidad y la gestión asamblearia directa.", "Anarquismo Clásico")
        ]
    ],

    # Bloque 3: Nación e Identidad
    [
        "9. Fundamento de pertenencia: ¿Qué define la identidad colectiva o la pertenencia?",
        [
            ("La adhesión cívica a un conjunto de leyes y derechos universales abiertos.", "Liberalismo Clásico"),
            ("Una comunidad de destino histórico, cultural y lingüístico soberano.", "Tradicionalismo y Realismo"),
            ("Ninguna frontera; la verdadera lealtad es de clase internacional.", "Marxismo y Teoría Crítica"),
            ("El arraigo profundo a la tierra ancestral y a los pueblos originarios.", "Postdesarrollismo y Biocentrismo")
        ]
    ],
    [
        "10. Escala de lealtad: ¿Dónde debe depositarse la lealtad política primordial?",
        [
            ("En las instituciones democráticas globales o el derecho cosmopolita.", "Liberalismo Clásico"),
            ("En la defensa de la soberanía y tradiciones de la propia nación.", "Tradicionalismo y Realismo"),
            ("En la solidaridad internacional de los trabajadores contra el capital.", "Marxismo y Teoría Crítica"),
            ("En la autogestión de las comunidades locales y territoriales.", "Anarquismo Clásico")
        ]
    ],
    [
        "11. Patria y cosmopolitismo: ¿Cómo valoras el concepto de patria frente a la globalización?",
        [
            ("Debe diluirse en favor de la apertura comercial y la gobernanza global neutral.", "Liberalismo Clásico"),
            ("Es el espacio vital indispensable para la supervivencia y el despliegue civilizacional.", "Tradicionalismo y Realismo"),
            ("Es una construcción burguesa destinada a dividir a los proletarios del mundo.", "Marxismo y Teoría Crítica"),
            ("Debe ser reemplazada por federaciones de pueblos libres y comunas autónomas.", "Anarquismo Clásico")
        ]
    ],
    [
        "12. Diversidad cultural: ¿Cómo debe gestionarse la pluralidad identitaria dentro de un territorio?",
        [
            ("Mediante la tolerancia liberal de mercado y la no discriminación jurídica.", "Liberalismo Clásico"),
            ("Mediante la integración igualitaria bajo un proyecto de transformación social.", "Marxismo y Teoría Crítica"),
            ("Mediante la preservación celosa de la identidad histórica y los valores heredados.", "Tradicionalismo y Realismo"),
            ("Mediante el reconocimiento de autonomías plurinacionales y reciprocidad de saberes.", "Postdesarrollismo y Biocentrismo")
        ]
    ],

    # Bloque 4: El Estado y la Autoridad
    [
        "13. Naturaleza del poder: ¿Qué rol debe cumplir la autoridad política y el Estado?",
        [
            ("Ser un árbitro neutral y mínimo que garantice la libertad individual.", "Liberalismo Clásico"),
            ("Funcionar como un aparato de dominación de clase a transformar/superar.", "Marxismo y Teoría Crítica"),
            ("Actuar como custodio soberano del orden frente a las amenazas externas.", "Tradicionalismo y Realismo"),
            ("Ser desmantelado por completo por ser una estructura coactiva e ilegítima.", "Libertarismo Radical")
        ]
    ],
    [
        "14. Forma de autoridad: ¿Cómo debe ejercerse el mando?",
        [
            ("Mediante representantes elegidos bajo estrictas normas de control legal.", "Liberalismo Clásico"),
            ("Mediante la dirección revolucionaria orientada a la justicia social.", "Marxismo y Teoría Crítica"),
            ("Mediante la jerarquía legítima basada en el honor, la historia y el orden.", "Tradicionalismo y Realismo"),
            ("Mediante la rotación de cargos y el mandato colectivo horizontal.", "Anarquismo Clásico")
        ]
    ],
    [
        "15. Burocracia y control: ¿Cuál es tu juicio sobre la burocracia estatal?",
        [
            ("Es un mal necesario pero peligroso que debe reducirse al mínimo indispensable.", "Liberalismo Clásico"),
            ("Es un instrumento que debe ser tomado y redirigido al servicio de las mayorías.", "Marxismo y Teoría Crítica"),
            ("Es el esqueleto técnico que garantiza la continuidad y el orden de la soberanía.", "Tradicionalismo y Realismo"),
            ("Es una forma patológica de dominación jerárquica que debe ser abolida de inmediato.", "Anarquismo Clásico")
        ]
    ],
    [
        "16. Ley y coacción: ¿Qué lugar ocupa la coacción legal en la convivencia?",
        [
            ("Solo se justifica para prevenir la agresión de terceros y hacer cumplir contratos.", "Liberalismo Clásico"),
            ("Se justifica temporalmente para disolver los privilegios de las clases opresoras.", "Marxismo y Teoría Crítica"),
            ("Es la columna vertebral insustituible para mantener a raya el caos y la anomia.", "Tradicionalismo y Realismo"),
            ("Toda coacción legal es tiranía; la verdadera convivencia nace de la espontaneidad.", "Anarquismo Clásico")
        ]
    ],

    # Bloque 5: Economía y Riqueza
    [
        "17. Modelo de producción: ¿Cómo debe organizarse la riqueza?",
        [
            ("Mediante la propiedad privada inviolable y el libre mercado competitivo.", "Liberalismo Clásico"),
            ("Mediante la propiedad social y la planificación centralizada/social.", "Marxismo y Teoría Crítica"),
            ("Mediante contratos estrictamente privados, sin impuestos ni Estado.", "Libertarismo Radical"),
            ("Mediante la reciprocidad, el trueque y el trabajo comunitario.", "Postdesarrollismo y Biocentrismo")
        ]
    ],
    [
        "18. Criterio de distribución: ¿Qué debe guiar el reparto de bienes?",
        [
            ("La productividad y el mérito individual medidos por el mercado.", "Liberalismo Clásico"),
            ("La satisfacción planificada de las necesidades de toda la sociedad.", "Marxismo y Teoría Crítica"),
            ("La protección de la propiedad distribuida y la economía familiar.", "Tradicionalismo y Realismo"),
            ("El equilibrio ecológico y la sustentabilidad de la vida comunitaria.", "Postdesarrollismo y Biocentrismo")
        ]
    ],
    [
        "19. Propiedad y acumulación: ¿Cuál es tu postura ante la propiedad de los medios de producción?",
        [
            ("Deben estar en manos privadas de manera absoluta e inviolable.", "Libertarismo Radical"),
            ("Deben ser socializados y gestionados colectivamente por los trabajadores o el Estado.", "Marxismo y Teoría Crítica"),
            ("Deben estar ampliamente distribuidas entre familias y corporaciones morales (distributismo).", "Tradicionalismo y Realismo"),
            ("Deben ser de uso comunal o gestionadas mediante cooperativas autónomas autogestionadas.", "Anarquismo Clásico")
        ]
    ],
    [
        "20. Moneda y finanzas: ¿Cómo visualizas el sistema monetario y financiero ideal?",
        [
            ("Basado en banca libre competitiva o dinero respaldado por activos de mercado.", "Libertarismo Radical"),
            ("Bajo control y planificación pública centralizada al servicio del plan económico.", "Marxismo y Teoría Crítica"),
            ("Regulado estrictamente por la soberanía nacional para evitar la usura internacional.", "Tradicionalismo y Realismo"),
            ("Sustituido por monedas locales, trueque, reciprocidad o sistemas de crédito mutuo.", "Postdesarrollismo y Biocentrismo")
        ]
    ],

    # Bloque 6: Geopolítica y Proyecto Histórico
    [
        "21. Arquitectura global: ¿Cómo debe estructurarse el orden geopolítico mundial?",
        [
            ("Mediante la integración global de los mercados y la gobernanza supranacional.", "Liberalismo Clásico"),
            ("Mediante un sistema multipolar de grandes bloques soberanos o civilizacionales.", "Tradicionalismo y Realismo"),
            ("Mediante la superación global del capitalismo por la solidaridad internacional.", "Marxismo y Teoría Crítica"),
            ("Mediante redes de autonomías locales autogestionadas al margen de los Estados.", "Anarquismo Clásico")
        ]
    ],
    [
        "22. Seguridad y soberanía exterior: ¿Cuál debe ser la prioridad en las relaciones internacionales?",
        [
            ("La apertura comercial, la interdependencia y la disolución de barreras arancelarias.", "Liberalismo Clásico"),
            ("La defensa estricta de la soberanía nacional y la supervivencia frente al enemigo.", "Tradicionalismo y Realismo"),
            ("La emancipación universal de los pueblos oprimidos frente al imperialismo global.", "Marxismo y Teoría Crítica"),
            ("La desmilitarización y la cooperación horizontal entre comunas y pueblos libres.", "Anarquismo Clásico")
        ]
    ],
    [
        "23. Conflicto global: ¿Cómo interpretas las tensiones y guerras entre potencias o bloques?",
        [
            ("Como fricciones comerciales superables mediante tratados y derecho internacional.", "Liberalismo Clásico"),
            ("Como la lucha inevitable entre grandes espacios civilizacionales (*Großraum*).", "Tradicionalismo y Realismo"),
            ("Como la contradicción última del imperialismo y la competencia interimperialista.", "Marxismo y Teoría Crítica"),
            ("Como el producto artificial de los Estados, que oprimen a los pueblos en beneficio propio.", "Anarquismo Clásico")
        ]
    ],
    [
        "24. Horizonte histórico: ¿Cuál es la meta última de la evolución política de la humanidad?",
        [
            ("El progreso indefinido de la libertad individual y la prosperidad tecnocapitalista.", "Liberalismo Clásico"),
            ("La conservación de un orden equilibrado, jerárquico, espiritual y enraizado.", "Tradicionalismo y Realismo"),
            ("La sociedad sin clases, sin estado y plenamente emancipada del reino de la necesidad.", "Marxismo y Teoría Crítica"),
            ("La federación mundial de comunidades autogestionadas en armonía con la naturaleza.", "Postdesarrollismo y Biocentrismo")
        ]
    ]
]

# Inicializar orden aleatorio de opciones por sesión para evitar sesgo de posición fijo
if "orden_opciones" not in st.session_state:
    st.session_state.orden_opciones = []
    for q in banco_preguntas:
        opciones_copia = list(q[1])
        random.shuffle(opciones_copia)
        st.session_state.orden_opciones.append(opciones_copia)

# --- FORMULARIO DE DECISIONES SECUENCIALES ---
with st.form("formulario_arqueologia"):
    
    respuestas_usuario = []
    
    bloques_titulos = [
        "Bloque 1: El Concepto de Ser Humano",
        "Bloque 2: El Vínculo Social",
        "Bloque 3: Nación e Identidad",
        "Bloque 4: El Estado y la Autoridad",
        "Bloque 5: Economía y Riqueza",
        "Bloque 6: Geopolítica y Proyecto Histórico"
    ]
    
    idx_preg = 0
    for b_idx, titulo_bloque in enumerate(bloques_titulos):
        st.header(titulo_bloque)
        for p_i in range(4):
            enunciado, _ = banco_preguntas[idx_preg]
            st.markdown(f"*{enunciado}*")
            
            # Obtener las opciones barajadas para esta pregunta
            opciones_actuales = st.session_state.orden_opciones[idx_preg]
            textos_opciones = [op[0] for op in opciones_actuales]
            
            eleccion = st.radio(f"q_{idx_preg}", textos_opciones, key=f"radio_{idx_preg}", label_visibility="collapsed")
            
            # Guardar la vertiente asociada a la elección del usuario
            for texto_op, vertiente_op in opciones_actuales:
                if texto_op == eleccion:
                    respuestas_usuario.append(vertiente_op)
                    break
            idx_preg += 1
        st.markdown("---")

    submitted = st.form_submit_button("Ejecutar Análisis y Radiografía Metacognitiva Avanzada")

# --- PROCESAMIENTO Y DIAGNÓSTICO FORMATIVO MULTIDOCTRINAL ---
if submitted:
    st.markdown("---")
    st.header("📊 1. Radiografía Cuantitativa de tus Vertientes")

    puntos = {
        "Liberalismo Clásico": 0.0,
        "Marxismo y Teoría Crítica": 0.0,
        "Tradicionalismo y Realismo": 0.0,
        "Libertarismo Radical": 0.0,
        "Anarquismo Clásico": 0.0,
        "Postdesarrollismo y Biocentrismo": 0.0
    }

    for vertiente in respuestas_usuario:
        if vertiente in puntos:
            puntos[vertiente] += 1.0

    # Gráfico de barras nativo limpio y eficiente
    df_chart = pd.DataFrame(list(puntos.items()), columns=["Vertiente", "Puntaje"]).set_index("Vertiente")
    st.bar_chart(df_chart)

    # Identificación de vertientes activas (con puntaje > 0)
    vertientes_activas = {k: v for k, v in sorted(puntos.items(), key=lambda item: item[1], reverse=True) if v > 0}
    top_vertientes = list(vertientes_activas.keys())

    # --- 2. GLOSARIO CONCEPTUAL FILTRADO DINÁMICAMENTE ---
    st.markdown("---")
    st.header("📖 2. Glosario Conceptual (Solo Vertientes con Presencia en tu Respuesta)")
    
    glosario_maestro = {
        "Liberalismo Clásico": ("Sostén filosófico basado en la primacía ontológica del individuo racional, la neutralidad institucional del Estado de derecho, el contrato social y la propiedad privada como garantía de libertad.", "John Locke, Adam Smith, Immanuel Kant, Alexis de Tocqueville, Friedrich Hayek.", "Tradición contractualista occidental; en Chile, proyectado en el pensamiento liberal decimonónico (José Victorino Lastarria) y el reformismo institucional de Valentín Letelier."),
        "Marxismo y Teoría Crítica": ("Matriz materialista histórica que concibe la política y la conciencia como superestructuras determinadas por las relaciones de producción y la lucha de clases, buscando la emancipación universal mediante la socialización de los medios.", "Karl Marx, Friedrich Engels, Vladimir Lenin, Rosa Luxemburgo, Antonio Gramsci.", "Crítica de la economía política y socialismo científico; en Chile, encarnado en el sindicalismo de clase de Luis Emilio Recabarren y el pensamiento de Clotario Blest."),
        "Tradicionalismo y Realismo": ("Corriente centrada en el enraizamiento histórico, la soberanía estatal fuerte, el orden orgánico y la seguridad frente a las amenazas del entorno geopolítico (espectro amigo/enemigo).", "Thomas Hobbes, Carl Schmitt, Edmund Burke, Juan Donoso Cortés, Hans Morgenthau.", "Filosofía de la soberanía y realismo westfaliano; en Chile, arraigado en la tradición geopolítica nacional y el pensamiento de estrategas como Ramón Cañas Montalva."),
        "Libertarismo Radical": ("Doctrina fundamentada en el axioma de la autopropiedad y el principio de no agresión. Rechaza toda coacción estatal e impositiva, apostando por mercados libres absolutos y la privatización de la justicia y la seguridad.", "Murray Rothbard, Ludwig von Mises, Ayn Rand, Hans-Hermann Hoppe.", "Escuela Austríaca de Economía y derecho natural libertario contemporáneo."),
        "Anarquismo Clásico": ("Tradición antiautoritaria que postula la incompatibilidad de la libertad con cualquier jerarquía (Estado, capital, Iglesia). Propone la autoorganización horizontal, la ayuda mutua y el federalismo comunal.", "Piotr Kropotkin, Mijaíl Bakunin, Pierre-Joseph Proudhon, Elisée Reclus.", "Sindicalismo revolucionario y cooperación mutualista global."),
        "Postdesarrollismo y Biocentrismo": ("Enfoque contemporáneo que conceptualiza al ser humano como un nodo inalienable de un tejido vivo y ecológico. Subordina el mercado al equilibrio de la naturaleza y al autogobierno comunitario frente al extractivismo.", "José Carlos Mariátegui, Alberto Acosta, Eduardo Gudynas, Silvia Rivera Cusicanqui.", "Constitucionalismo plurinacional iberoamericano y ecología política comunitaria.")
    }

    for v in top_vertientes:
        desc, exp, fund = glosario_maestro[v]
        st.markdown(f"""
        * **{v} (Puntaje obtenido: {int(vertientes_activas[v])}):**
          * *Descripción:* {desc}
          * *Exponentes:* {exp}
          * *Fundamentos:* {fund}
        """)

    # --- 3. SÍNTESIS DIAGNÓSTICA MULTIDOCTRINAL ADAPTATIVA ---
    st.markdown("---")
    st.header("🔍 3. Síntesis Diagnóstica: Coherencia o Cruce Multidoctrinal")
    
    if len(vertientes_activas) == 1:
        v_unica = top_vertientes[0]
        st.success(f"✔ **Perfil Coherente Sólido:** Tu arquitectura conceptual muestra una fidelidad pura hacia la matriz de **{v_unica}**.")
        st.markdown(f"""
        * **Análisis detallado:** A lo largo de las 24 dimensiones, demuestras un hilo conductor deductivo sumamente riguroso. Al descender desde tu concepción inicial del ser humano (Bloque 1) hasta tus proyecciones geopolíticas e históricas (Bloque 6), rechazas de forma metódica las disonancias con otras escuelas. Mantienes una consistencia teórica pura que prioriza los principios ontológicos, institucionales y económicos de esta vertiente, logrando un edificio conceptual cohesionado, inmune a contradicciones internas graves y listo para un despliegue académico avanzado.
        """)
    else:
        st.warning(f"⚠️ **Perfil Multidoctrinal / Híbrido Complejo:** Se detecta un cruce dinámico entre las siguientes corrientes: **{', '.join(top_vertientes)}**.")
        st.markdown(f"""
        * **Análisis de Tensiones Múltiples:** Al expandir el análisis a 24 micro-preguntas, el simulador evidencia que tu edificio conceptual no responde al canon de una sola matriz pura, sino a una constelación híbrida. Estás combinando premisas de distintas tradiciones a lo largo de las capas del test. 
        * *¿Qué implica este cruce?* En la práctica ciudadana cotidiana, es habitual tomar herramientas de diversas vertientes para resolver problemas concretos. Sin embargo, a nivel de arquitectura teórica, esto genera un **cortocircuito socrático**. Por ejemplo, intentar compaginar el individualismo mercantil con la planificación social, o la soberanía estatal tradicional con la autogestión anarquista o comunitaria, exige examinar el punto exacto de quiebre deductivo para asumir conscientemente las fricciones de tu modelo de pensamiento.
        """)

    # --- 4. MODELAMIENTO DE PROFUNDIZACIÓN Y OPCIONES DE ENCUADRE ---
    st.markdown("---")
    st.header("🎯 4. Modelamiento de Profundización y Opciones de Encuadre Metodológico")
    
    if len(vertientes_activas) == 1:
        st.markdown(f"""
        Puesto que tu arquitectura muestra solidez en **{top_vertientes[0]}**, te ofrecemos **tres rutas de profundización teórica avanzada**:
        * **Opción A (La Vía Reformista / Institucional):** Estudiar cómo los fundamentos de tu matriz se adaptan a las exigencias de regulación institucional y estabilidad sistémica.
        * **Opción B (La Vía Ortodoxa / Radical):** Llevar los axiomas de tu vertiente hacia su formulación más pura, purgando cualquier concesión pragmática o intervencionista.
        * **Opción C (La Vía Histórica / Comparada):** Analizar la evolución y las tensiones prácticas de esta doctrina en América Latina y Chile a lo largo de su historia republicana.
        """)
    else:
        st.markdown(f"""
        Para dar sentido metodológico a tu perfil multidoctrinal entre **{', '.join(top_vertientes)}**, te ofrecemos tres opciones de encuadre estratégico:
        * **Opción A (Purificación Deductiva hacia la Matriz Mayoritaria):** Subordinar la totalidad de tu arquitectura teórica a la vertiente que acumuló mayor puntaje, revisando los bloques intermedios para eliminar los elementos heterodoxos de las corrientes secundarias.
        * **Opción B (Reorientación hacia la Corriente Alternativa):** Realizar el ejercicio inverso, asumiendo que tus respuestas reflejan una transición o un anhelo de cambio hacia los principios de la segunda matriz detectada.
        * **Opción C (Asunción del Pluralismo Agonístico):** Aceptar conscientemente tu condición híbrida y construir un marco teórico pluralista que estudie rigurosamente la fricción y el diálogo entre estas tradiciones inconciliables.
        """)

    # --- 5. BASE DE DATOS BIBLIOGRÁFICA DINÁMICA (42 FUENTES PRIMARIAS) ---
    st.markdown("---")
    st.header("📚 5. Base de Datos Bibliográfica Primaria (Filtrada según tus Vertientes Activas)")
    st.markdown("""
    A continuación se despliegan estrictamente las **fuentes primarias puras** (autores originales, sin comentarios de terceros) correspondientes a las vertientes que arrojaron presencia en tu test:
    """)

    repo_bibliografico = {
        "Liberalismo Clásico": [
            "**John Locke**, *Segundo tratado sobre el gobierno civil* (Caps. 2: 'Del estado de naturaleza', 5: 'De la propiedad', y 8: 'Del comienzo de las sociedades políticas').",
            "**Adam Smith**, *La riqueza de las naciones* (Libro I, Caps. 1-3: División del trabajo y origen del valor de cambio).",
            "**Immanuel Kant**, *La metafísica de las costumbres* (Parte I: Principios metafísicos de la doctrina del derecho).",
            "**Alexis de Tocqueville**, *La democracia en América* (Volumen II, Segunda Parte: Influencia de la democracia en los sentimientos).",
            "**Benjamin Constant**, *De la libertad de los antiguos comparada con la de los modernos* (Discurso íntegro en el Ateneo de París).",
            "**Friedrich Hayek**, *Los fundamentos de la libertad* (Caps. 1 al 4: Libertad y orden económico)."
        ],
        "Marxismo y Teoría Crítica": [
            "**Karl Marx**, *El Capital (Libro I)* (Sección 1, Caps. 1 al 3: La mercancía, el proceso de cambio y el dinero).",
            "**Karl Marx y Friedrich Engels**, *Manifiesto del Partido Comunista* (Cap. 1: Burgueses y proletarios).",
            "**Vladimir Lenin**, *El Estado y la revolución* (Caps. 1: La sociedad de clases y el Estado, y 3: La experiencia de la Comuna de París).",
            "**Rosa Luxemburgo**, *La acumulación del capital* (Secciones iniciales sobre la reproducción ampliada del capital).",
            "**Antonio Gramsci**, *Cuadernos de la cárcel* (Antología sobre Estado integral, hegemonía e intelectuales orgánicos).",
            "**Georg Lukács**, *Historia y conciencia de clase* (Ensayo: 'La reificación y la conciencia del proletariado')."
        ],
        "Tradicionalismo y Realismo": [
            "**Thomas Hobbes**, *Leviatán* (Caps. 13: 'De la condición natural del género humano', 17 y 18: Generación y derechos del soberano).",
            "**Carl Schmitt**, *El concepto de lo político* (Caps. 1 al 3: Definición ontológica de lo político y la distinción amigo/enemigo).",
            "**Edmund Burke**, *Reflexiones sobre la revolución en Francia* (Fragmentos esenciales sobre la herencia institucional y el prejuicio racional).",
            "**Juan Donoso Cortés**, *Ensayos sobre el catolicismo, el liberalismo y el socialismo* (Ensayos fundamentales sobre la dictadura y el orden).",
            "**Hans Morgenthau**, *Política entre las naciones* (Caps. 1 y 2: Los seis principios del realismo político).",
            "**Julien Freund**, *L'essence du politique* (Caps. sobre el mando, la obediencia y la naturaleza jerárquica del poder)."
        ],
        "Libertarismo Radical": [
            "**Murray Rothbard**, *Ética de la libertad* (Parte I: Ley natural, y Parte II: La autopropiedad y el Estado).",
            "**Ludwig von Mises**, *La acción humana* (Caps. 1 al 4: Introducción a la praxeología y el orden de mercado).",
            "**Ayn Rand**, *La virtud del egoísmo* (Ensayos 1 al 4: La objeción objetivista al altruismo y el estatismo).",
            "**Lysander Spooner**, *No Treason* (Escritos completos sobre la ilegitimidad contractual del Estado).",
            "**Gustave de Molinari**, *La producción de seguridad* (Ensayo íntegro sobre la privatización de la ley y el orden).",
            "**Hans-Hermann Hoppe**, *Democracia: el Dios que fracasó* (Caps. 1 al 3: Monarquía, democracia y orden natural)."
        ],
        "Anarquismo Clásico": [
            "**Piotr Kropotkin**, *La ayuda mutua: Un factor de evolución* (Introducción y Conclusión).",
            "**Mijaíl Bakunin**, *Dios y el Estado* (Texto fragmentado completo sobre la autoridad y la ciencia).",
            "**Pierre-Joseph Proudhon**, *¿Qué es la propiedad?* (Caps. 1 al 3: Investigaciones sobre el principio del derecho y del gobierno).",
            "**Elisée Reclus**, *El hombre y la tierra* (Introducción geográfica sobre la libertad humana y el medio).",
            "**Errico Malatesta**, *Anarquia* (Opúsculo fundamental sobre la organización libre sin autoridad).",
            "**Max Stirner**, *El único y su propiedad* (Parte I: El hombre y la soberanía del ego autónomo)."
        ],
        "Postdesarrollismo y Biocentrismo": [
            "**José Carlos Mariátegui**, *7 ensayos de interpretación de la realidad peruana* (Ensayo sobre el problema agrario y el ayllu).",
            "**Alberto Acosta**, *El buen vivir: Sumak Kawsay* (Caps. 1 al 3: Opciones al desarrollo capitalista).",
            "**Fausto Reinaga**, *La revolución india* (Caps. esenciales sobre la conciencia amindia y el colonialismo).",
            "**Silvia Rivera Cusicanqui**, *Oprimidos pero no vencidos* (Caps. metodológicos sobre la historia oral y comunitaria andina).",
            "**Álvaro García Linera**, *Forma valor y forma comunidad* (Introducción y capítulos centrales sobre economía comunitaria).",
            "**Eduardo Gudynas**, *Derechos de la naturaleza y buen vivir* (Caps. iniciales sobre biocentricismo y alternativas al extractivismo)."
        ]
    }

    for v in top_vertientes:
        st.markdown(f"### 📌 Bibliografía Fundamental para tu Vertiente Activa: *{v}*")
        for obra in repo_bibliografico.get(v, []):
            st.markdown(f"- {obra}")

    st.markdown("### 📌 Bibliografía Transversal de Pluralismo y Teoría Política Crítica:")
    st.markdown("""
    - **Norberto Bobbio**, *Derecha e izquierda* (Caps. 1 al 3: Criterios analíticos de distinción política).
    - **Chantal Mouffe**, *En torno a lo político* (Caps. 1 y 2: La dimensión agonística y los antagonismos doctrinales).
    - **Isaiah Berlin**, *Cuatro ensayos sobre la libertad* (Ensayo: 'Dos conceptos de libertad').
    - **Michael Sandel**, *El descontento con la democracia* (Introducción y Conclusión sobre el liberalismo y las lealtades morales).
    """)

    st.balloons()
