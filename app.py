import streamlit as st
import pandas as pd

st.set_page_config(page_title="Arqueología Antropológica Política", page_icon="🏛️", layout="wide")

st.title("🏛️ Radiografía de creencias e ideas políticas")
st.markdown("---")
st.write("""
**Bienvenido al laboratorio de arqueología conceptual.** Este instrumento de alta densidad analítica parte de tu **concepto de ser humano** (Bloque 1) para descender metodológicamente por el vínculo social (Bloque 2), la nación e identidad (Bloque 3), el estado y la autoridad (Bloque 4), la economía y riqueza (Bloque 5), y la geopolítica y proyecto histórico (Bloque 6). 
Tómate tu tiempo en cada uno de los 24 dilemas. Al finalizar, el sistema generará una radiografía tabular, un glosario conceptual riguroso, un diagnóstico de coherencia o cortocircuitos ontológicos, un modelamiento de profundización con opciones detalladas y una base bibliográfica primaria con capítulos específicos.
""")

# --- FORMULARIO DE DECISIONES SECUENCIALES (6 BLOQUES / 24 MICRO-PREGUNTAS) ---
with st.form("formulario_arqueologia"):
    
    # BLOQUE 1: EL CONCEPTO DE SER HUMANO
    st.header("Bloque 1: El Concepto de Ser Humano")
    
    st.markdown("*1. Motor de la acción: ¿Qué impulsa fundamentalmente al ser humano en su vida en común?*")
    p1 = st.radio("Selecciona una opción:", [
        "La búsqueda racional de su propio interés y beneficio particular.",
        "La necesidad material y su transformación a través del trabajo colectivo.",
        "El sentido de pertenencia a una comunidad orgánica, la familia y la tradición.",
        "El impulso irrenunciable hacia la soberanía absoluta de su propio cuerpo y voluntad."
    ], key="p1_choice")

    st.markdown("*2. Naturaleza y devenir: ¿Cómo consideras la condición fundamental de las personas?*")
    p2 = st.radio("Selecciona una opción:", [
        "Un individuo cuyos derechos y autonomía preceden a cualquier sociedad.",
        "Un sujeto histórico cuya conciencia cambia según las condiciones materiales.",
        "Un heredero de tradiciones e instituciones que lo trascienden históricamente.",
        "Un espíritu libre que rechaza de raíz toda imposición moral o legal externa."
    ], key="p2_choice")

    st.markdown("*3. Libertad y voluntad: ¿Cuál es el origen y el alcance de la libertad humana?*")
    p3 = st.radio("Selecciona una opción:", [
        "Es una capacidad de elección racional dentro de las reglas del mercado y la ley.",
        "Es la emancipación colectiva frente a las cadenas de la explotación económica.",
        "Es una libertad situada y concreta, enmarcada en deberes hacia la comunidad y Dios.",
        "Es un absoluto ontológico de autopropiedad que no admite restricciones externas."
    ], key="p3_choice")

    st.markdown("*4. Moral y naturaleza: ¿De dónde surge el orden moral que guía al ser humano?*")
    p4 = st.radio("Selecciona una opción:", [
        "De convenciones y contratos racionales acordados libremente por los individuos.",
        "De la superación histórica de las ideologías alienantes mediante la praxis.",
        "De un orden natural, la ley eterna o la transmisión consuetudinaria de los mayores.",
        "De la conciencia individual soberana, totalmente exenta de mandatos coactivos."
    ], key="p4_choice")

    st.markdown("---")

    # BLOQUE 2: EL VÍNCULO SOCIAL
    st.header("Bloque 2: El Vínculo Social")
    
    st.markdown("*5. Origen del lazo: ¿Cómo se constituye fundamentalmente la sociedad?*")
    p5 = st.radio("Selecciona una opción:", [
        "Mediante un contrato voluntario entre ciudadanos para proteger intereses.",
        "Mediante un conflicto estructural e histórico entre clases sociales.",
        "Mediante lazos históricos, culturales y espirituales preexistentes.",
        "Mediante la cooperación libre y espontánea, sin coacción institucional."
    ], key="p5_choice")

    st.markdown("*6. Regla de convivencia: ¿Qué debe regular la vida en común?*")
    p6 = st.radio("Selecciona una opción:", [
        "El imperio de la ley impersonal, los contratos y la neutralidad institucional.",
        "La superación de las contradicciones de clase mediante la acción colectiva.",
        "La fidelidad a los valores compartidos, las costumbres y la autoridad tradicional.",
        "La autonomía absoluta de cada asociación voluntaria o comuna libre."
    ], key="p6_choice")

    st.markdown("*7. Autoridad y obediencia: ¿Qué justifica la obediencia o el orden social?*")
    p7 = st.radio("Selecciona una opción:", [
        "El consentimiento voluntario de los gobernados regulado por procedimientos legales.",
        "La dirección consciente orientada a erradicar la injusticia y la escasez.",
        "La jerarquía natural, el honor, el respeto a los mayores y la cohesión orgánica.",
        "Ninguna autoridad; el orden solo emerge de la asociación voluntaria y la ayuda mutua."
    ], key="p7_choice")

    st.markdown("*8. Cohesión comunitaria: ¿Qué mantiene unida a una comunidad humana sana?*")
    p8 = st.radio("Selecciona una opción:", [
        "El respeto mutuo a los derechos individuales y la eficiencia de los intercambios.",
        "La conciencia de clase y la solidaridad en la lucha contra la dominación.",
        "El arraigo a la tierra, la lengua, la fe común y la memoria de los ancestros.",
        "Las redes de afecto horizontal, la afinidad y la gestión asamblearia directa."
    ], key="p8_choice")

    st.markdown("---")

    # BLOQUE 3: NACIÓN E IDENTIDAD
    st.header("Bloque 3: Nación e Identidad")
    
    st.markdown("*9. Fundamento de pertenencia: ¿Qué define la identidad colectiva o la pertenencia?*")
    p9 = st.radio("Selecciona una opción:", [
        "La adhesión cívica a un conjunto de leyes y derechos universales abiertos.",
        "Una comunidad de destino histórico, cultural y lingüístico soberano.",
        "Ninguna frontera; la verdadera lealtad es de clase internacional.",
        "El arraigo profundo a la tierra ancestral y a los pueblos originarios."
    ], key="p9_choice")

    st.markdown("*10. Escala de lealtad: ¿Dónde debe depositarse la lealtad política primordial?*")
    p10 = st.radio("Selecciona una opción:", [
        "En las instituciones democráticas globales o el derecho cosmopolita.",
        "En la defensa de la soberanía y tradiciones de la propia nación.",
        "En la solidaridad internacional de los trabajadores contra el capital.",
        "En la autogestión de las comunidades locales y territoriales."
    ], key="p10_choice")

    st.markdown("*11. Patria y cosmopolitismo: ¿Cómo valoras el concepto de patria frente a la globalización?*")
    p11 = st.radio("Selecciona una opción:", [
        "Debe diluirse en favor de la apertura comercial y la gobernanza global neutral.",
        "Es el espacio vital indispensable para la supervivencia y el despliegue civilizacional.",
        "Es una construcción burguesa destinada a dividir a los proletarios del mundo.",
        "Debe ser reemplazada por federaciones de pueblos libres y comunas autónomas."
    ], key="p11_choice")

    st.markdown("*12. Diversidad cultural: ¿Cómo debe gestionarse la pluralidad identitaria dentro de un territorio?*")
    p12 = st.radio("Selecciona una opción:", [
        "Mediante la tolerancia liberal de mercado y la no discriminación jurídica.",
        "Mediante la integración igualitaria bajo un proyecto de transformación social.",
        "Mediante la preservación celosa de la identidad histórica y los valores heredados.",
        "Mediante el reconocimiento de autonomías plurinacionales y reciprocidad de saberes."
    ], key="p12_choice")

    st.markdown("---")

    # BLOQUE 4: EL ESTADO Y LA AUTORIDAD
    st.header("Bloque 4: El Estado y la Autoridad")
    
    st.markdown("*13. Naturaleza del poder: ¿Qué rol debe cumplir la autoridad política y el Estado?*")
    p13 = st.radio("Selecciona una opción:", [
        "Ser un árbitro neutral y mínimo que garantice la libertad individual.",
        "Funcionar como un aparato de dominación de clase a transformar/superar.",
        "Actuar como custodio soberano del orden frente a las amenazas externas.",
        "Ser desmantelado por completo por ser una estructura coactiva e ilegítima."
    ], key="p13_choice")

    st.markdown("*14. Forma de autoridad: ¿Cómo debe ejercerse el mando?*")
    p14 = st.radio("Selecciona una opción:", [
        "Mediante representantes elegidos bajo estrictas normas de control legal.",
        "Mediante la dirección revolucionaria orientada a la justicia social.",
        "Mediante la jerarquía legítima basada en el honor, la historia y el orden.",
        "Mediante la rotación de cargos y el mandato colectivo horizontal."
    ], key="p14_choice")

    st.markdown("*15. Burocracia y control: ¿Cuál es tu juicio sobre la burocracia estatal?*")
    p15 = st.radio("Selecciona una opción:", [
        "Es un mal necesario pero peligroso que debe reducirse al mínimo indispensable.",
        "Es un instrumento que debe ser tomado y redirigido al servicio de las mayorías.",
        "Es el esqueleto técnico que garantiza la continuidad y el orden de la soberanía.",
        "Es una forma patológica de dominación jerárquica que debe ser abolida de inmediato."
    ], key="p15_choice")

    st.markdown("*16. Ley y coacción: ¿Qué lugar ocupa la coacción legal en la convivencia?*")
    p16 = st.radio("Selecciona una opción:", [
        "Solo se justifica para prevenir la agresión de terceros y hacer cumplir contratos.",
        "Se justifica temporalmente para disolver los privilegios de las clases opresoras.",
        "Es la columna vertebral insustituible para mantener a raya el caos y la anomia.",
        "Toda coacción legal es tiranía; la verdadera convivencia nace de la espontaneidad."
    ], key="p16_choice")

    st.markdown("---")

    # BLOQUE 5: ECONOMÍA Y RIQUEZA
    st.header("Bloque 5: Economía y Riqueza")
    
    st.markdown("*17. Modelo de producción: ¿Cómo debe organizarse la riqueza?*")
    p17 = st.radio("Selecciona una opción:", [
        "Mediante la propiedad privada inviolable y el libre mercado competitivo.",
        "Mediante la propiedad social y la planificación centralizada/social.",
        "Mediante contratos estrictamente privados, sin impuestos ni Estado.",
        "Mediante la reciprocidad, el trueque y el trabajo comunitario."
    ], key="p17_choice")

    st.markdown("*18. Criterio de distribución: ¿Qué debe guiar el reparto de bienes?*")
    p18 = st.radio("Selecciona una opción:", [
        "La productividad y el mérito individual medidos por el mercado.",
        "La satisfacción planificada de las necesidades de toda la sociedad.",
        "La protección de la propiedad distribuida y la economía familiar.",
        "El equilibrio ecológico y la sustentabilidad de la vida comunitaria."
    ], key="p18_choice")

    st.markdown("*19. Propiedad y acumulación: ¿Cuál es tu postura ante la propiedad de los medios de producción?*")
    p19 = st.radio("Selecciona una opción:", [
        "Deben estar en manos privadas de manera absoluta e inviolable.",
        "Deben ser socializados y gestionados colectivamente por los trabajadores o el Estado.",
        "Deben estar ampliamente distribuidas entre familias y corporaciones morales (distributismo).",
        "Deben ser de uso comunal o gestionadas mediante cooperativas autónomas autogestionadas."
    ], key="p19_choice")

    st.markdown("*20. Moneda y finanzas: ¿Cómo visualizas el sistema monetario y financiero ideal?*")
    p20 = st.radio("Selecciona una opción:", [
        "Basado en banca libre competitiva o dinero respaldado por activos de mercado.",
        "Bajo control y planificación pública centralizada al servicio del plan económico.",
        "Regulado estrictamente por la soberanía nacional para evitar la usura internacional.",
        "Sustituido por monedas locales, trueque, reciprocidad o sistemas de crédito mutuo."
    ], key="p20_choice")

    st.markdown("---")

    # BLOQUE 6: GEOPOLÍTICA Y PROYECTO HISTÓRICO
    st.header("Bloque 6: Geopolítica y Proyecto Histórico")
    
    st.markdown("*21. Arquitectura global: ¿Cómo debe estructurarse el orden geopolítico mundial?*")
    p21 = st.radio("Selecciona una opción:", [
        "Mediante la integración global de los mercados y la gobernanza supranacional.",
        "Mediante un sistema multipolar de grandes bloques soberanos o civilizacionales.",
        "Mediante la superación global del capitalismo por la solidaridad internacional.",
        "Mediante redes de autonomías locales autogestionadas al margen de los Estados."
    ], key="p21_choice")

    st.markdown("*22. Seguridad y soberanía exterior: ¿Cuál debe ser la prioridad en las relaciones internacionales?*")
    p22 = st.radio("Selecciona una opción:", [
        "La apertura comercial, la interdependencia y la disolución de barreras arancelarias.",
        "La defensa estricta de la soberanía nacional y la supervivencia frente al enemigo.",
        "La emancipación universal de los pueblos oprimidos frente al imperialismo global.",
        "La desmilitarización y la cooperación horizontal entre comunas y pueblos libres."
    ], key="p22_choice")

    st.markdown("*23. Conflicto global: ¿Cómo interpretas las tensiones y guerras entre potencias o bloques?*")
    p23 = st.radio("Selecciona una opción:", [
        "Como fricciones comerciales superables mediante tratados y derecho internacional.",
        "Como la lucha inevitable entre grandes espacios civilizacionales (*Großraum*).",
        "Como la contradicción última del imperialismo y la competencia interimperialista.",
        "Como el producto artificial de los Estados, que oprimen a los pueblos en beneficio propio."
    ], key="p23_choice")

    st.markdown("*24. Horizonte histórico: ¿Cuál es la meta última de la evolución política de la humanidad?*")
    p24 = st.radio("Selecciona una opción:", [
        "El progreso indefinido de la libertad individual y la prosperidad tecnocapitalista.",
        "La conservación de un orden equilibrado, jerárquico, espiritual y enraizado.",
        "La sociedad sin clases, sin estado y plenamente emancipada del reino de la necesidad.",
        "La federación mundial de comunidades autogestionadas en armonía con la naturaleza."
    ], key="p24_choice")

    submitted = st.form_submit_button("Ejecutar Análisis y Modelamiento Metacognitivo Avanzado")

# --- PROCESAMIENTO Y DIAGNÓSTICO FORMATIVO AMPLIADO (24 PREGUNTAS) ---
if submitted:
    st.markdown("---")
    st.header("📊 1. Radiografía Tabular de Ideas Fuerza y Vertientes")

    respuestas = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, p21, p22, p23, p24]
    
    puntos = {
        "liberal": 0.0,
        "marxista": 0.0,
        "tradicional": 0.0,
        "libertario": 0.0,
        "anarquista": 0.0,
        "comunitario": 0.0
    }

    for r in respuestas:
        if "interés y beneficio" in r or "contrato voluntario" in r or "adhesión cívica" in r or "árbitro neutral" in r or "propiedad privada inviolable" in r or "integración global de los mercados" in r:
            puntos["liberal"] += 1.0
        elif "necesidad material" in r or "conflicto estructural" in r or "verdadera lealtad es de clase" in r or "aparato de dominación" in r or "propiedad social y la planificación" in r or "superación global del capitalismo" in r:
            puntos["marxista"] += 1.0
        elif "comunidad orgánica" in r or "lazos históricos, culturales y espirituales" in r or "comunidad de destino histórico" in r or "custodio soberano del orden" in r or "sistema multipolar" in r or "defensa estricta de la soberanía nacional" in r:
            puntos["tradicional"] += 1.0
        elif "soberanía absoluta de su propio cuerpo" in r or "cooperación libre y espontánea, sin coacción" in r or "desmantelado por completo" in r or "contratos estrictamente privados" in r:
            puntos["libertario"] += 1.0
        elif "espíritu libre que rechaza de raíz" in r or "autonomía absoluta de cada asociación" in r or "autogestión de las comunidades locales" in r or "rotación de cargos" in r or "redes de autonomías locales" in r or "cooperación horizontal entre comunas" in r:
            puntos["anarquista"] += 1.0
        elif "eslabón" in r or "reciprocidad, el trueque" in r or "tierra ancestral" in r or "equilibrio ecológico" in r:
            puntos["comunitario"] += 1.0

    tabla_resumen = pd.DataFrame({
        "Bloque / Dimensión": [
            "1. Ser Humano (Motor)", "2. Ser Humano (Naturaleza)", "3. Ser Humano (Libertad)", "4. Ser Humano (Moral)",
            "5. Vínculo (Origen)", "6. Vínculo (Regla)", "7. Vínculo (Autoridad)", "8. Vínculo (Cohesión)",
            "9. Nación (Pertenencia)", "10. Nación (Lealtad)", "11. Nación (Patria/Global)", "12. Nación (Diversidad)",
            "13. Estado (Poder)", "14. Estado (Mando)", "15. Estado (Burocracia)", "16. Estado (Coacción)",
            "17. Economía (Producción)", "18. Economía (Distribución)", "19. Economía (Propiedad)", "20. Economía (Moneda)",
            "21. Geopolítica (Global)", "22. Geopolítica (Seguridad)", "23. Geopolítica (Conflicto)", "24. Geopolítica (Horizonte)"
        ],
        "Idea Fuerza Seleccionada": respuestas
    })
    st.table(tabla_resumen)

    vertientes_ordenadas = sorted(puntos.items(), key=lambda x: x[1], reverse=True)
    v1, p_v1 = vertientes_ordenadas[0]
    v2, p_v2 = vertientes_ordenadas[1]

    max_vertiente = v1
    max_puntaje = p_v1
    es_coherente = max_puntaje >= 9.0  # Umbral de consistencia para 24 preguntas

    nombres_vertientes = {
        "liberal": "Liberalismo Clásico",
        "marxista": "Marxismo y Teoría Crítica",
        "tradicional": "Tradicionalismo y Realismo Político",
        "libertario": "Anarcocapitalismo / Libertarismo Radical",
        "anarquista": "Anarquismo Clásico / Autonomismo",
        "comunitario": "Ontología Comunitaria y del Buen Vivir"
    }

    # --- 2. GLOSARIO DETALLADO DE LAS VERTIENTES ---
    st.markdown("---")
    st.header("📖 2. Glosario Conceptual, Exponentes y Fundamentos Históricos")
    st.markdown(f"""
    * **Liberalismo Clásico:**
      * *Descripción:* Sostén filosófico basado en la primacía ontológica del individuo racional, la neutralidad institucional del Estado de derecho, el contrato social y la propiedad privada como garantía de libertad.
      * *Exponentes:* John Locke, Adam Smith, Immanuel Kant, Alexis de Tocqueville, Friedrich Hayek.
      * *Fundamentos:* Tradición contractualista occidental; en Chile, proyectado en el pensamiento liberal decimonónico (José Victorino Lastarria) y el reformismo institucional de Valentín Letelier.

    * **Marxismo y Teoría Crítica:**
      * *Descripción:* Matriz materialista histórica que concibe la política y la conciencia como superestructuras determinadas por las relaciones de producción y la lucha de clases, buscando la emancipación universal mediante la socialización de los medios.
      * *Exponentes:* Karl Marx, Friedrich Engels, Vladimir Lenin, Rosa Luxemburgo, Antonio Gramsci.
      * *Fundamentos:* Crítica de la economía política y socialismo científico; en Chile, encarnado en el sindicalismo de clase de Luis Emilio Recabarren y el pensamiento de Clotario Blest.

    * **Tradicionalismo y Realismo Político:**
      * *Descripción:* Corriente centrada en el enraizamiento histórico, la soberanía estatal fuerte, el orden orgánico y la seguridad frente a las amenazas del entorno geopolítico (espectro amigo/enemigo).
      * *Exponentes:* Thomas Hobbes, Carl Schmitt, Edmund Burke, Juan Donoso Cortés, Hans Morgenthau.
      * *Fundamentos:* Filosofía de la soberanía y realismo westfaliano; en Chile, arraigado en la tradición geopolítica nacional y el pensamiento de estrategas como Ramón Cañas Montalva.

    * **Anarcocapitalismo / Libertarismo Radical:**
      * *Descripción:* Doctrina fundamentada en el axioma de la autopropiedad y el principio de no agresión. Rechaza toda coacción estatal e impositiva, apostando por mercados libres absolutos y la privatización de la justicia y la seguridad.
      * *Exponentes:* Murray Rothbard, Ludwig von Mises, Ayn Rand, Hans-Hermann Hoppe.
      * *Fundamentos:* Escuela Austríaca de Economía y derecho natural libertario contemporáneo.

    * **Anarquismo Clásico / Autonomismo:**
      * *Descripción:* Tradición antiautoritaria que postula la incompatibilidad de la libertad con cualquier jerarquía (Estado, capital, Iglesia). Propone la autoorganización horizontal, la ayuda mutua y el federalismo comunal.
      * *Exponentes:* Piotr Kropotkin, Mijaíl Bakunin, Pierre-Joseph Proudhon, Elisée Reclus.
      * *Fundamentos:* Sindicalismo revolucionario y cooperación mutualista global.

    * **Ontología Comunitaria y del Buen Vivir:**
      * *Descripción:* Matriz basada en la cosmovisión relacional y comunitaria donde la persona es un nodo inalienable de un tejido social y ecológico. Subordina el mercado a la reproducción de la vida y la reciprocidad (*Pachamama*).
      * *Exponentes:* José Carlos Mariátegui, Alberto Acosta, Álvaro García Linera, Fausto Reinaga.
      * *Fundamentos:* Pensamiento indigenista andino y ecología política comunitaria.
    """)

    # --- 3. SÍNTESIS DIAGNÓSTICA PROFUNDA Y DETALLADA ---
    st.markdown("---")
    st.header("🔍 3. Síntesis Diagnóstica: Coherencia Deductiva o Tensiones Estructurales")
    
    if es_coherente:
        st.success(f"✔ **Diagnóstico de Coherencia Estructural Sólida:** Tu arquitectura conceptual se alinea de manera consistente con los axiomas del **{nombres_vertientes[v1]}**.")
        st.markdown(f"""
        * **Desglose Analítico del Perfil:** A lo largo de las 24 dimensiones, demuestras un hilo conductor deductivo sumamente riguroso. Al descender desde tu concepción inicial del ser humano (Bloque 1) hasta tus proyecciones geopolíticas e históricas (Bloque 6), rechazas de forma metódica las disonancias con otras escuelas. No caes en contradicciones sistémicas: mantienes una fidelidad conceptual pura que prioriza los principios ontológicos, institucionales y económicos de esta matriz, logrando un edificio teórico cohesionado, inmune a contradicciones internas graves y listo para un despliegue académico avanzado.
        """)
    else:
        st.warning(f"⚠️ **Diagnóstico de Perfil Híbrido y Contradictorio:** Se detecta un entrecruzamiento de tensiones doctrinales profundas entre el **{nombres_vertientes[v1]}** y el **{nombres_vertientes[v2]}**.")
        st.markdown(f"""
        * **Análisis Quirúrgico del Cortocircuito Ontológico:** Al expandir el análisis a 24 micro-preguntas, el simulador evidencia que tu edificio conceptual sufre de un choque de placas tectónicas teóricas. Estás combinando premisas ontológicas que se neutralizan mutuamente en las capas intermedias (por ejemplo, adoptando el individualismo metodológico o contractual en el plano económico, pero deslizando pulsiones colectivistas, coactivas u orgánicas en el plano estatal o comunitario; o viceversa). Esta hibridación, aunque común en el pragmatismo político cotidiano, genera una disonancia lógica severa en tu arquitectura deductiva que debe ser resuelta mediante un encuadre metodológico consciente.
        """)

    # --- 4. MODELAMIENTO DE PROFUNDIZACIÓN Y OPCIONES DE ENCUADRE ---
    st.markdown("---")
    st.header("🎯 4. Modelamiento de Profundización y Opciones de Encuadre Metodológico")
    
    if es_coherente:
        st.markdown(f"""
        Puesto que tu arquitectura muestra solidez y consistencia en el **{nombres_vertientes[v1]}**, te ofrecemos **tres rutas de profundización teórica avanzada (Subvertientes)** para encauzar tu investigación académica:
        * **Opción A (La Vía Reformista / Institucional):** Estudiar cómo los fundamentos de tu matriz se adaptan a las exigencias de regulación estatal moderada, justicia distributiva de mínimos y estabilidad democrática representativa sin fracturar el núcleo individual o el orden orgánico basal.
        * **Opción B (La Vía Ortodoxa / Radical):** Llevar los axiomas de tu vertiente hacia su formulación más pura e intransigente, purgando cualquier concesión pragmática, intervencionismo estatal o concesión keynesiana/colectivista.
        * **Opción C (La Vía Histórica / Geopolítica Comparada):** Analizar la evolución y las tensiones prácticas que ha sufrido esta doctrina al ser aplicada en los procesos institucionales y geopolíticos de América Latina y Chile a lo largo de su historia republicana.
        """)
    else:
        st.markdown(f"""
        Para resolver el cortocircuito ontológico detectado entre **{nombres_vertientes[v1]}** y **{nombres_vertientes[v2]}**, tu edificio conceptual te exige adoptar una de las siguientes **opciones de encuadre estratégico**:
        * **Opción A (Purificación Deductiva hacia la Matriz Dominante - {nombres_vertientes[v1]}):** Decidir someter la totalidad de tu arquitectura teórica a los principios de tu vertiente principal. Esto implica revisar y reescribir deductivamente las respuestas de los bloques intermedios (Estado, economía y geopolítica) para eliminar por completo los elementos heterodoxos de la segunda matriz.
        * **Opción B (Giro Radical hacia la Matriz Secundaria - {nombres_vertientes[v2]}):** Reconocer que tus convicciones más profundas residen en la segunda vertiente detectada, lo que te obliga a realizar un ejercicio inverso: reestructurar tu concepción del ser humano y del vínculo social (Bloques 1 y 2) para subordinarlas a los principios colectivistas, orgánicos o soberanistas de esta matriz.
        * **Opción C (Asunción del Pluralismo Agonístico / Síntesis Dialéctica):** Abandonar la búsqueda de un monismo deductivo puro y aceptar de manera consciente tu perfil híbrido. Esto implica construir un marco teórico pluralista que asuma teóricamente la tensión entre ambas tradiciones, fundamentando su estudio en la fricción democrática y los límites del pensamiento político tradicional.
        """)

    # --- 5. BASE DE DATOS BIBLIOGRÁFICA MASIVA (42 FUENTES PRIMARIAS) ---
    st.markdown("---")
    st.header("📚 5. Base de Datos Bibliográfica Primaria (Selección por Vertientes con Capítulos)")
    st.markdown("""
    A continuación se despliega el repertorio masivo de **fuentes primarias puras** (autores originales, sin comentarios de terceros). El sistema selecciona y presenta los textos fundamentales correspondientes a las vertientes activadas en tu diagnóstico:
    """)

    # Diccionario masivo con las 7 vertientes (6 libros c/u = 42 obras primarias)
    repo_bibliografico = {
        "liberal": [
            "**John Locke**, *Segundo tratado sobre el gobierno civil* (Caps. 2: 'Del estado de naturaleza', 5: 'De la propiedad', y 8: 'Del comienzo de las sociedades políticas').",
            "**Adam Smith**, *La riqueza de las naciones* (Libro I, Caps. 1-3: División del trabajo y origen del valor de cambio).",
            "**Immanuel Kant**, *La metafísica de las costumbres* (Parte I: Principios metafísicos de la doctrina del derecho).",
            "**Alexis de Tocqueville**, *La democracia en América* (Volumen II, Segunda Parte: Influencia de la democracia en los sentimientos).",
            "**Benjamin Constant**, *De la libertad de los antiguos comparada con la de los modernos* (Discurso íntegro en el Ateneo de París).",
            "**Friedrich Hayek**, *Los fundamentos de la libertad* (Caps. 1 al 4: Libertad y orden económico)."
        ],
        "marxista": [
            "**Karl Marx**, *El Capital (Libro I)* (Sección 1, Caps. 1 al 3: La mercancía, el proceso de cambio y el dinero).",
            "**Karl Marx y Friedrich Engels**, *Manifiesto del Partido Comunista* (Cap. 1: Burgueses y proletarios).",
            "**Vladimir Lenin**, *El Estado y la revolución* (Caps. 1: La sociedad de clases y el Estado, y 3: La experiencia de la Comuna de París).",
            "**Rosa Luxemburgo**, *La acumulación del capital* (Secciones iniciales sobre la reproducción ampliada del capital).",
            "**Antonio Gramsci**, *Cuadernos de la cárcel* (Antología sobre Estado integral, hegemonía e intelectuales orgánicos).",
            "**Georg Lukács**, *Historia y conciencia de clase* (Ensayo: 'La reificación y la conciencia del proletariado')."
        ],
        "tradicional": [
            "**Thomas Hobbes**, *Leviatán* (Caps. 13: 'De la condición natural del género humano', 17 y 18: Generación y derechos del soberano).",
            "**Carl Schmitt**, *El concepto de lo político* (Caps. 1 al 3: Definición ontológica de lo político y la distinción amigo/enemigo).",
            "**Edmund Burke**, *Reflexiones sobre la revolución en Francia* (Fragmentos esenciales sobre la herencia institucional y el prejuicio racional).",
            "**Juan Donoso Cortés**, *Ensayos sobre el catolicismo, el liberalismo y el socialismo* (Ensayos fundamentales sobre la dictadura y el orden).",
            "**Hans Morgenthau**, *Política entre las naciones* (Caps. 1 y 2: Los seis principios del realismo político).",
            "**Julien Freund**, *L'essence du politique* (Caps. sobre el mando, la obediencia y la naturaleza jerárquica del poder)."
        ],
        "libertario": [
            "**Murray Rothbard**, *Ética de la libertad* (Parte I: Ley natural, y Parte II: La autopropiedad y el Estado).",
            "**Ludwig von Mises**, *La acción humana* (Caps. 1 al 4: Introducción a la praxeología y el orden de mercado).",
            "**Ayn Rand**, *La virtud del egoísmo* (Ensayos 1 al 4: La objeción objetivista al altruismo y el estatismo).",
            "**Lysander Spooner**, *No Treason* (Escritos completos sobre la ilegitimidad contractual del Estado).",
            "**Gustave de Molinari**, *La producción de seguridad* (Ensayo íntegro sobre la privatización de la ley y el orden).",
            "**Hans-Hermann Hoppe**, *Democracia: el Dios que fracasó* (Caps. 1 al 3: Monarquía, democracia y orden natural)."
        ],
        "anarquista": [
            "**Piotr Kropotkin**, *La ayuda mutua: Un factor de evolución* (Introducción y Conclusión).",
            "**Mijaíl Bakunin**, *Dios y el Estado* (Texto fragmentado completo sobre la autoridad y la ciencia).",
            "**Pierre-Joseph Proudhon**, *¿Qué es la propiedad?* (Caps. 1 al 3: Investigaciones sobre el principio del derecho y del gobierno).",
            "**Elisée Reclus**, *El hombre y la tierra* (Introducción geográfica sobre la libertad humana y el medio).",
            "**Errico Malatesta**, *Anarquia* (Opúsculo fundamental sobre la organización libre sin autoridad).",
            "**Max Stirner**, *El único y su propiedad* (Parte I: El hombre y la soberanía del ego autónomo)."
        ],
        "comunitario": [
            "**José Carlos Mariátegui**, *7 ensayos de interpretación de la realidad peruana* (Ensayo sobre el problema agrario y el ayllu).",
            "**Alberto Acosta**, *El buen vivir: Sumak Kawsay* (Caps. 1 al 3: Opciones al desarrollo capitalista).",
            "**Fausto Reinaga**, *La revolución india* (Caps. esenciales sobre la conciencia amindia y el colonialismo).",
            "**Silvia Rivera Cusicanqui**, *Oprimidos pero no vencidos* (Caps. metodológicos sobre la historia oral y comunitaria andina).",
            "**Álvaro García Linera**, *Forma valor y forma comunidad* (Introducción y capítulos centrales sobre economía comunitaria).",
            "**Eduardo Gudynas**, *Derechos de la naturaleza y buen vivir* (Caps. iniciales sobre biocentricismo y alternativas al extractivismo)."
        ]
    }

    # Despliegue dinámico de la bibliografía de las vertientes en juego
    st.markdown(f"### 📌 Bibliografía Fundamental para tu Vertiente Dominante ({nombres_vertientes[v1]}):")
    for obra in repo_bibliografico.get(v1, []):
        st.markdown(f"- {obra}")

    st.markdown(f"### 📌 Bibliografía Fundamental para tu Vertiente de Tensión / Secundaria ({nombres_vertientes[v2]}):")
    for obra in repo_bibliografico.get(v2, []):
        st.markdown(f"- {obra}")

    st.markdown("### 📌 Bibliografía Transversal de Pluralismo, Estado y Teoría Política Crítica:")
    st.markdown("""
    - **Norberto Bobbio**, *Derecha e izquierda* (Caps. 1 al 3: Criterios analíticos de distinción política).
    - **Chantal Mouffe**, *En torno a lo político* (Caps. 1 y 2: La dimensión agonística y los antagonismos doctrinales).
    - **Isaiah Berlin**, *Cuatro ensayos sobre la libertad* (Ensayo: 'Dos conceptos de libertad').
    - **Michael Sandel**, *El descontento con la democracia* (Introducción y Conclusión sobre el liberalismo y las lealtades morales).
    """)

    st.balloons()
