import streamlit as st
import pandas as pd

st.set_page_config(page_title="Arqueología Antropológica Política", page_icon="🏛️", layout="wide")

st.title("🏛️ Simulador de Arqueología Antropológica Política")
st.markdown("---")
st.write("""
**Bienvenido al laboratorio de arqueología conceptual.** Inspirado en el flujo deductivo del pensamiento político, este simulador ampliado a 24 preguntas parte de tu **concepto de ser humano** para descender por las capas de la sociedad, la nación, el estado, la economía y el proyecto histórico. 
Tómate tu tiempo en cada dilema. Al finalizar, obtendrás una radiografía tabular, un glosario detallado, un diagnóstico de coherencia o tensiones, un modelamiento de profundización con opciones (A, B, C) y una bibliografía primaria rigurosa con capítulos específicos.
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

    # Mapeo de respuestas a dimensiones para construir la tabla resumen
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
    es_coherente = max_puntaje >= 10  # Umbral ajustado para 24 preguntas

    nombres_vertientes = {
        "liberal": "Liberalismo Clásico",
        "marxista": "Marxismo y Teoría Crítica",
        "tradicional": "Tradicionalismo y Realismo Político",
        "libertario": "Anarcocapitalismo / Libertarismo Radical",
        "anarquista": "Anarquismo Clásico / Autonomismo",
        "comunitario": "Ontología Comunitaria y del Buen Vivir"
    }

    # --- 2. GLOSARIO DETALLADO DE LAS VERTIENTES DETECTADAS ---
    st.markdown("---")
    st.header("📖 2. Glosario Conceptual y Fundamentos Teóricos")
    st.markdown(f"""
    * **{nombres_vertientes[v1]} (Corriente Dominante):**
      * *Descripción detallada:* Sostén filosófico basado en la primacía ontológica del individuo, la neutralidad institucional, el contrato social y la limitación del poder coactivo.
      * *Principales exponentes:* John Locke, Adam Smith, Immanuel Kant, Friedrich Hayek.
      * *Fundamentos (Extranjeros y Chilenos):* Tradición republicana clásica y liberalismo político occidental; en Chile, proyectado en el pensamiento liberal decimonónico (José Victorino Lastarria) y el reformismo institucional de Valentín Letelier.

    * **{nombres_vertientes[v2]} (Corriente Secundaria / Tensión):**
      * *Descripción detallada:* Matriz analítica alternativa detectada en tus elecciones que introduce principios contrapuestos sobre la estructura social, la propiedad o la autoridad.
      * *Principales exponentes:* Referentes clásicos de su respectiva tradición doctrinal.
      * *Fundamentos (Extranjeros y Chilenos):* Movimientos históricos y corrientes de pensamiento ancladas en la historia política y social.
    """)

    # --- 3. SÍNTESIS DESCRIPTIVA DE COHERENCIA O CONTRADICCIONES ---
    st.markdown("---")
    st.header("🔍 3. Síntesis Diagnóstica: Coherencia o Tensiones Estructurales")
    if es_coherente:
        st.success(f"✔ **Perfil Coherente:** Tu arquitectura conceptual muestra una solidez notable alineada con el **{nombres_vertientes[v1]}**.")
        st.markdown(f"""
        * **Análisis detallado de adhesión:** A lo largo de las 24 dimensiones, mantienes un hilo conductor deductivo claro. Desde tu concepción del ser humano hasta tus proyecciones geopolíticas, rechazas las contradicciones sistémicas, apostando por un orden institucional unificado que prioriza los axiomas propios de esta vertiente sin disonancias cognitivas graves.
        """)
    else:
        st.warning(f"⚠️ **Perfil Híbrido / Contradictorio:** Se detecta una tensión profunda entre el **{nombres_vertientes[v1]}** y el **{nombres_vertientes[v2]}**.")
        st.markdown(f"""
        * **Análisis detallado de tensiones:** Al ampliar el cuestionario a 24 dimensiones, queda en evidencia que combinas premisas ontológicas irreconciliables en las capas intermedias (por ejemplo, mezclando contratos individuales liberales con subordinaciones comunitarias o estructuras colectivistas). Esto genera un cortocircuito lógico en tu edificio conceptual que requiere encuadre metodológico.
        """)

    # --- 4. MODELAMIENTO DE PROFUNDIZACIÓN Y/O ENCUADRE (OPCIONES A, B, C) ---
    st.markdown("---")
    st.header("🎯 4. Modelamiento de Profundización y Opciones de Encuadre")
    if es_coherente:
        st.markdown(f"""
        Dado que tu perfil muestra consistencia en el **{nombres_vertientes[v1]}**, te ofrecemos 3 subvertientes avanzadas para profundizar tu estudio teórico:
        * **Opción A (Subvertiente Reformista / Institucional):** Profundizar en cómo las instituciones estatales regulan y garantizan las condiciones marco sin perder el centro en la autonomía individual o el orden orgánico basal.
        * **Opción B (Subvertiente Radical / Ortodoxa):** Llevar los principios de tu matriz a su máxima expresión teórica, purgando cualquier concesión pragmática o intervencionista del Estado.
        * **Opción C (Subvertiente Histórica / Comparada):** Estudiar las adaptaciones geopolíticas e institucionales que esta vertiente ha sufrido en el contexto latinoamericano y chileno frente a los ciclos de crisis.
        """)
    else:
        st.markdown(f"""
        Para resolver las contradicciones entre **{nombres_vertientes[v1]}** y **{nombres_vertientes[v2]}**, la idea más fuerte detectada es la de tu matriz dominante. Te ofrecemos las siguientes opciones de encuadre y profundización:
        * **Opción A (Purificación hacia la Matriz 1 - {nombres_vertientes[v1]}):** Subordinar deductivamente todas las respuestas de las capas sociales, económicas y geopolíticas hacia los axiomas puros de esta primera vertiente, eliminando todo rezago heterodoxo.
        * **Opción B (Giro radical hacia la Matriz 2 - {nombres_vertientes[v2]}):** Reestructurar por completo el edificio conceptual desde la base (Bloque 1), asumiendo que las premisas de la segunda vertiente deben regir la totalidad de tu arquitectura política.
        * **Opción C (Síntesis Dialéctica / Tercera Vía):** Asumir conscientemente la condición híbrida mediante un marco pluralista que reconozca los límites del monismo doctrinal, estudiando la tensión agonística entre ambas tradiciones.
        """)

    # --- 5. BIBLIOGRAFÍA PRIMARIA (MÍNIMO 6 TEXTOS CON CAPÍTULOS) ---
    st.markdown("---")
    st.header("📚 5. Bibliografía Primaria Obligatoria (Obras Originales y Capítulos)")
    st.markdown("""
    De acuerdo a tus resultados, debes consultar estrictamente las siguientes **fuentes primarias** (textos de los autores originales, sin comentarios de terceros):
    
    1. **John Locke**, *Segundo tratado sobre el gobierno civil*  
       *Capítulos específicos a consultar:* Cap. 2 ("Del estado de naturaleza"), Cap. 5 ("De la propiedad") y Cap. 8 ("Del comienzo de las sociedades políticas").
    
    2. **Karl Marx**, *El Capital (Libro I)*  
       *Capítulos específicos a consultar:* Sección 1 ("La mercancía y el dinero", Cap. 1 al 3) y Sección 3 ("La producción de la plusvalía absoluta").
    
    3. **Thomas Hobbes**, *Leviatán*  
       *Capítulos específicos a consultar:* Cap. 13 ("De la condición natural del género humano...") y Cap. 17 ("De las causas, generación y definición de un Estado").
    
    4. **Murray Rothbard**, *Ética de la libertad*  
       *Capítulos específicos a consultar:* Parte I ("Ley natural") y Parte II ("La autopropiedad y el Estado").
    
    5. **Piotr Kropotkin**, *La ayuda mutua: Un factor de evolución*  
       *Capítulos específicos a consultar:* Introducción y Conclusión.
    
    6. **José Carlos Mariátegui**, *7 ensayos de interpretación de la realidad peruana*  
       *Capítulos específicos a consultar:* "El problema del indio" y "Esquema de la evolución económica".
    """)

    st.balloons()
