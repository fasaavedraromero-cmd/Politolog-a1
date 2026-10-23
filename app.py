import streamlit as st
import pandas as pd

st.set_page_config(page_title="Arqueología Antropológica Política", page_icon="🏛️", layout="wide")

st.title("🏛️ Simulador de Arqueología Antropológica Política")
st.markdown("---")
st.write("""
**Bienvenido al laboratorio de arqueología conceptual.** Inspirado en el flujo deductivo del pensamiento político, este simulador parte de tu **concepto de ser humano** para descender por las capas de la sociedad, la nación, el estado, la economía y el proyecto histórico. 
Tómate tu tiempo en cada dilema. Al finalizar, obtendrás una radiografía tabular, un diagnóstico crítico de tensiones y un riguroso modelamiento metacognitivo guiado por fuentes clásicas y pensadores de nuestra tradición hispanoamericana y chilena.
""")

# --- FORMULARIO DE DECISIONES SECUENCIALES (6 BLOQUES / 12 MICRO-PREGUNTAS) ---
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

    st.markdown("---")

    # BLOQUE 2: EL VÍNCULO SOCIAL
    st.header("Bloque 2: El Vínculo Social")
    
    st.markdown("*3. Origen del lazo: ¿Cómo se constituye fundamentalmente la sociedad?*")
    p3 = st.radio("Selecciona una opción:", [
        "Mediante un contrato voluntario entre ciudadanos para proteger intereses.",
        "Mediante un conflicto estructural e histórico entre clases sociales.",
        "Mediante lazos históricos, culturales y espirituales preexistentes.",
        "Mediante la cooperación libre y espontánea, sin coacción institucional."
    ], key="p3_choice")

    st.markdown("*4. Regla de convivencia: ¿Qué debe regular la vida en común?*")
    p4 = st.radio("Selecciona una opción:", [
        "El imperio de la ley impersonal, los contratos y la neutralidad institucional.",
        "La superación de las contradicciones de clase mediante la acción colectiva.",
        "La fidelidad a los valores compartidos, las costumbres y la autoridad tradicional.",
        "La autonomía absoluta de cada asociación voluntaria o comuna libre."
    ], key="p4_choice")

    st.markdown("---")

    # BLOQUE 3: NACIÓN E IDENTIDAD
    st.header("Bloque 3: Nación e Identidad")
    
    st.markdown("*5. Fundamento de pertenencia: ¿Qué define la identidad colectiva o la pertenencia?*")
    p5 = st.radio("Selecciona una opción:", [
        "La adhesión cívica a un conjunto de leyes y derechos universales abiertos.",
        "Una comunidad de destino histórico, cultural y lingüístico soberano.",
        "Ninguna frontera; la verdadera lealtad es de clase internacional.",
        "El arraigo profundo a la tierra ancestral y a los pueblos originarios."
    ], key="p5_choice")

    st.markdown("*6. Escala de lealtad: ¿Dónde debe depositarse la lealtad política primordial?*")
    p6 = st.radio("Selecciona una opción:", [
        "En las instituciones democráticas globales o el derecho cosmopolita.",
        "En la defensa de la soberanía y tradiciones de la propia nación.",
        "En la solidaridad internacional de los trabajadores contra el capital.",
        "En la autogestión de las comunidades locales y territoriales."
    ], key="p6_choice")

    st.markdown("---")

    # BLOQUE 4: EL ESTADO Y LA AUTORIDAD
    st.header("Bloque 4: El Estado y la Autoridad")
    
    st.markdown("*7. Naturaleza del poder: ¿Qué rol debe cumplir la autoridad política y el Estado?*")
    p7 = st.radio("Selecciona una opción:", [
        "Ser un árbitro neutral y mínimo que garantice la libertad individual.",
        "Funcionar como un aparato de dominación de clase a transformar/superar.",
        "Actuar como custodio soberano del orden frente a las amenazas externas.",
        "Ser desmantelado por completo por ser una estructura coactiva e ilegítima."
    ], key="p7_choice")

    st.markdown("*8. Forma de autoridad: ¿Cómo debe ejercerse el mando?*")
    p8 = st.radio("Selecciona una opción:", [
        "Mediante representantes elegidos bajo estrictas normas de control legal.",
        "Mediante la dirección revolucionaria orientada a la justicia social.",
        "Mediante la jerarquía legítima basada en el honor, la historia y el orden.",
        "Mediante la rotación de cargos y el mandato colectivo horizontal."
    ], key="p8_choice")

    st.markdown("---")

    # BLOQUE 5: ECONOMÍA Y RIQUEZA
    st.header("Bloque 5: Economía y Riqueza")
    
    st.markdown("*9. Modelo de producción: ¿Cómo debe organizarse la riqueza?*")
    p9 = st.radio("Selecciona una opción:", [
        "Mediante la propiedad privada inviolable y el libre mercado competitivo.",
        "Mediante la propiedad social y la planificación centralizada/social.",
        "Mediante contratos estrictamente privados, sin impuestos ni Estado.",
        "Mediante la reciprocidad, el trueque y el trabajo comunitario."
    ], key="p9_choice")

    st.markdown("*10. Criterio de distribución: ¿Qué debe guiar el reparto de bienes?*")
    p10 = st.radio("Selecciona una opción:", [
        "La productividad y el mérito individual medidos por el mercado.",
        "La satisfacción planificada de las necesidades de toda la sociedad.",
        "La protección de la propiedad distribuida y la economía familiar.",
        "El equilibrio ecológico y la sustentabilidad de la vida comunitaria."
    ], key="p10_choice")

    st.markdown("---")

    # BLOQUE 6: GEOPOLÍTICA Y PROYECTO HISTÓRICO
    st.header("Bloque 6: Geopolítica y Proyecto Histórico")
    
    st.markdown("*11. Arquitectura global: ¿Cómo debe estructurarse el orden geopolítico mundial?*")
    p11 = st.radio("Selecciona una opción:", [
        "Mediante la integración global de los mercados y la gobernanza supranacional.",
        "Mediante un sistema multipolar de grandes bloques soberanos o civilizacionales.",
        "Mediante la superación global del capitalismo por la solidaridad internacional.",
        "Mediante redes de autonomías locales autogestionadas al margen de los Estados."
    ], key="p11_choice")

    st.markdown("*12. Seguridad y soberanía exterior: ¿Cuál debe ser la prioridad en las relaciones internacionales?*")
    p12 = st.radio("Selecciona una opción:", [
        "La apertura comercial, la interdependencia y la disolución de barreras arancelarias.",
        "La defensa estricta de la soberanía nacional y la supervivencia frente al enemigo.",
        "La emancipación universal de los pueblos oprimidos frente al imperialismo global.",
        "La desmilitarización y la cooperación horizontal entre comunas y pueblos libres."
    ], key="p12_choice")

    submitted = st.form_submit_button("Ejecutar Análisis y Modelamiento Metacognitivo")

# --- PROCESAMIENTO Y DIAGNÓSTICO FORMATIVO CON PUNTAJE PONDERADO ---
if submitted:
    st.markdown("---")
    st.header("📊 Radiografía Tabular de tu Edificio Conceptual")

    tabla_resumen = pd.DataFrame({
        "Dimensión del Esquema": [
            "1. Concepto de Ser Humano",
            "2. Vínculo Social",
            "3. Nación e Identidad",
            "4. Estado y Autoridad",
            "5. Economía y Riqueza",
            "6. Geopolítica y Proyecto"
        ],
        "Elección del Estudiante": [
            p1, p3, p5, p7, p9, p11
        ]
    })
    st.table(tabla_resumen)

    st.markdown("---")
    st.header("🔍 Diagnóstico Crítico y Modelamiento Metacognitivo")

    # Sistema de puntaje por cada una de las grandes matrices teóricas
    puntos = {
        "liberal": 0,
        "marxista": 0,
        "tradicional": 0,
        "libertario": 0,
        "anarquista": 0,
        "comunitario": 0
    }

    # Ponderación basada en las opciones seleccionadas (Opción 0=Liberal, 1=Marxista, 2=Tradicional/Comunitario, 3=Libertario/Anarquista)
    respuestas = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12]
    
    for r in respuestas:
        if "interés" in r or "contrato voluntario" in r or "adhesión cívica" in r or "árbitro" in r or "propiedad privada" in r or "integración global" in r:
            puntos["liberal"] += 1
        elif "material" in r or "conflicto" in r or "clase internacional" in r or "dominación" in r or "planificación" in r or "superación global" in r:
            puntos["marxista"] += 1
        elif "comunidad orgánica" in r or "lazos históricos" in r or "comunidad de destino" in r or "custodio soberano" in r or "multipolar" in r:
            puntos["tradicional"] += 1
        elif "soberanía absoluta" in r or "cooperación libre" in r or "desmantelado" in r or "contratos estrictamente privados" in r:
            puntos["libertario"] += 1
        elif "espíritu libre" in r or "comuna libre" in r or "rotación de cargos" in r or "autonomías locales" in r:
            puntos["anarquista"] += 1
        elif "eslabón" in r or "reciprocidad" in r or "tierra ancestral" in r or "trabajo comunitario" in r:
            puntos["comunitario"] += 1

    max_vertiente = max(puntos, key=puntos.get)
    max_puntaje = puntos[max_vertiente]
    es_coherente = max_puntaje >= 6  # Umbral de consistencia sobre 12 preguntas

    # --- DIAGNÓSTICO FINAL ---
    if not es_coherente:
        st.warning("⚠️ Diagnóstico: Perfil Híbrido / En Cruzamiento Doctrinal")
        st.markdown("""
        **1. Precisión de las vertientes en juego:**  
        Tus respuestas combinan elementos de diversas tradiciones intelectuales sin un dominio absoluto de un solo bloque, cruzando premisas que provienen de distintas familias doctrinales.
        
        **2. Análisis Crítico y Graduación de Tensiones:**  
        * *Lo complementario:* En la acción política pragmática, es habitual tomar herramientas de distintas tradiciones para resolver problemas coyunturales.
        * *Lo irreconciliable (La ambigüedad teórica):* A nivel de la arquitectura conceptual, este cruce genera un cortocircuito. Estás aceptando simultáneamente premisas que se neutralizan entre sí.
        
        **3. Modelamiento Metacognitivo (Cómo reestructurar tu postura):**  
        Para ordenar y dar consistencia lógica a tu pensamiento, debes volver al **Bloque 1 (Ser Humano)** y decidir cuál de tus elecciones ejerce el "supuesto necesario" que funda tu doctrina:  
        * *Opción A (Girar hacia el Eje Individualista / Contractual):* Alinear las capas siguientes hacia el mercado y el pacto legal neutral.  
        * *Opción B (Girar hacia el Eje Colectivo / Comunitario u Orgánico):* Subordinar la economía a la planificación o a la reciprocidad comunitaria.
        
        **Movimientos y referentes históricos y chilenos de referencia transversal:**  
        * *Corrientes:* Pensamiento institucionalista, reformismo democrático.  
        * *Figuras:* Norberto Bobbio, Michael Sandel.
        """)
        st.subheader("📚 Itinerario Bibliográfico Enriquecido (Aporte Temático y Guía de Lectura):")
        st.markdown("**Fuentes Principales (Autores Clásicos):**")
        st.markdown("- Norberto Bobbio, *Derecha e izquierda* (Aporte: Criterios analíticos para clasificar las familias políticas. Leer: Capítulos 1 al 3).")
        st.markdown("**Comentarios y Ensayos Críticos:**")
        st.markdown("- Michael Sandel, *El descontento con la democracia* (Aporte: Crítica al liberalismo procedimental y rescate comunitarista. Leer: Introducción).")

    elif max_vertiente == "liberal":
        st.success("✔ Diagnóstico: Coherencia Estructural Sólida — Liberalismo Clásico")
        st.markdown("""
        **1. Explicación reveladora de tu postura (A qué adhiere tu perfil):**  
        Tus respuestas revelan una adhesión profunda a la **Tradición Liberal Clásica**. Operas bajo la convicción de que el individuo precede a la sociedad. Para ti, la convivencia política garantiza un marco neutral de leyes donde cada quien persigue su propia felicidad.
        
        **2. Modelamiento de Profundización (Cómo robustecer y llevar al siguiente nivel tus ideas):**  
        * *Opción A (Liberalismo Social / Reformista):* Asumir que la libertad formal requiere garantías materiales básicas proporcionadas por el Estado mediante impuestos moderados.  
        * *Opción B (Liberalismo Mínimo / Ortodoxo):* Endurecer el principio de no agresión fiscal, apostando por un Estado estrictamente limitado a la seguridad y la justicia.
        
        **Movimientos y referentes históricos y chilenos:**  
        * *Movimientos:* Liberalismo político, reformismo republicano.  
        * *Figuras:* John Locke, Adam Smith; en Chile: José Victorino Lastarria.
        """)
        st.subheader("📚 Itinerario Bibliográfico Enriquecido:")
        st.markdown("- John Locke, *Segundo tratado sobre el gobierno civil* (Aporte: Contrato social y propiedad. Leer: Capítulos 2, 5 y 8).")
        st.markdown("- Adam Smith, *La riqueza de las naciones* (Aporte: Mercado y división del trabajo. Leer: Capítulos 1 al 3).")
        st.markdown("- Friedrich Hayek, *Los fundamentos de la libertad* (Aporte: Orden espontáneo de mercado. Leer: Capítulos 1 al 4).")

    elif max_vertiente == "marxista":
        st.success("✔ Diagnóstico: Coherencia Estructural Sólida — Marxismo y Teoría Crítica")
        st.markdown("""
        **1. Explicación reveladora de tu postura (A qué adhiere tu perfil):**  
        Te sitúas firmemente en la órbita del **Materialismo Histórico y la Teoría Crítica**. Para ti, el ser humano es un producto social moldeado por las condiciones materiales y el trabajo; la injusticia es una contradicción estructural de las relaciones de clase.
        
        **2. Modelamiento de Profundización (Cómo robustecer y llevar al siguiente nivel tus ideas):**  
        * *Opción A (Vía Gramsciana / Hegemónica):* Construcción paciente de un bloque histórico y hegemonía cultural en la sociedad civil.  
        * *Opción B (Vía Revolucionaria / Ortodoxa):* Ruptura frontal con el Estado burgués y planificación social centralizada de la economía.
        
        **Movimientos y referentes históricos y chilenos:**  
        * *Movimientos:* Comunismo histórico, sindicalismo de clase.  
        * *Figuras:* Karl Marx, Antonio Gramsci; en Chile: Luis Emilio Recabarren y Clotario Blest.
        """)
        st.subheader("📚 Itinerario Bibliográfico Enriquecido:")
        st.markdown("- Karl Marx, *El Capital* (Aporte: Análisis de la plusvalía y la mercancía. Leer: Sección 1, Capítulo 1).")
        st.markdown("- Antonio Gramsci, *Cuadernos de la cárcel* (Aporte: Hegemonía cultural y bloque histórico. Leer: Antología sobre el Estado).")

    elif max_vertiente == "tradicional":
        st.success("✔ Diagnóstico: Coherencia Estructural Sólida — Tradicionalismo y Geopolítica Soberana")
        st.markdown("""
        **1. Explicación reveladora de tu postura (A qué adhiere tu perfil):**  
        Adhieres al **Realismo Político y Conservadurismo Orgánico**. El ser humano está enraizado a una comunidad histórica, cultura y lealtades espirituales o nacionales que debe custodiar frente al caos exterior.
        
        **2. Modelamiento de Profundización:**  
        * *Opción A (Vía Estado-Nación Soberano):* Fortalecimiento del Estado nacional centralizado y protección de fronteras económicas.  
        * *Opción B (Vía Multipolaridad Civilizacional):* Mundo policéntrico de grandes civilizaciones (*Großraum*) frente al globalismo.
        
        **Movimientos y referentes:**  
        * *Figuras:* Thomas Hobbes, Carl Schmitt; en Chile: Ramón Cañas Montalva.
        """)
        st.subheader("📚 Itinerario Bibliográfico Enriquecido:")
        st.markdown("- Thomas Hobbes, *Leviatán* (Aporte: Soberanía fuerte para evitar el caos. Leer: Capítulos 13, 17 y 18).")
        st.markdown("- Carl Schmitt, *El concepto de lo político* (Aporte: La distinción amigo/enemigo. Leer: Capítulos 1 al 3).")

    elif max_vertiente == "libertario":
        st.success("✔ Diagnóstico: Coherencia Estructural Sólida — Anarcocapitalismo / Libertarismo")
        st.markdown("""
        **1. Explicación reveladora de tu postura:**  
        Tu perfil se enmarca en el **Libertarismo de Mercado y la Autopropiedad**. Todo individuo es dueño absoluto de su cuerpo y trabajo; cualquier monopolio coactivo estatal es ilegítimo.
        
        **2. Modelamiento de Profundización:**  
        * *Opción A (Anarcocapitalismo radical):* Eliminar el Estado y confiar la seguridad y moneda al mercado libre.  
        * *Opción B (Minarquismo):* Estado mínimo limitado a la seguridad y tribunales.
        
        **Movimientos y referentes:**  
        * *Figuras:* Murray Rothbard, Ludwig von Mises.
        """)
        st.subheader("📚 Itinerario Bibliográfico Enriquecido:")
        st.markdown("- Murray Rothbard, *Ética de la libertad* (Aporte: Derechos naturales libertarios. Leer: Parte I).")

    elif max_vertiente == "anarquista":
        st.success("✔ Diagnóstico: Coherencia Estructural Sólida — Anarquismo Clásico")
        st.markdown("""
        **1. Explicación reveladora de tu postura:**  
        Adhieres al **Anarquismo Autonomista**. La libertad humana y la dominación jerárquica son incompatibles; el orden surge de la cooperación voluntaria y la ayuda mutua.
        
        **2. Modelamiento de Profundización:**  
        * *Opción A (Anarcosindicalismo):* Producción económica mediante sindicatos autogestionados.  
        * *Opción B (Comunalismo):* Municipalismo libertario y redes de comunas autónomas.
        
        **Movimientos y referentes:**  
        * *Figuras:* Piotr Kropotkin, Mijaíl Bakunin.
        """)
        st.subheader("📚 Itinerario Bibliográfico Enriquecido:")
        st.markdown("- Piotr Kropotkin, *La ayuda mutua* (Aporte: Cooperación sin estado. Leer: Introducción y Conclusión).")

    elif max_vertiente == "comunitario":
        st.success("✔ Diagnóstico: Coherencia Estructural Sólida — Ontología Comunitaria y del Buen Vivir")
        st.markdown("""
        **1. Explicación reveladora de tu postura:**  
        Te alineas con la **Ontología Comunitaria y el Buen Vivir**. La persona es un nodo inalienable de un tejido vivo que incluye a la comunidad y al territorio.
        
        **2. Modelamiento de Profundización:**  
        * *Opción A (Autonomía Territorial):* Autogobierno local y propiedad colectiva frente al extractivismo.  
        * *Opción B (Socialismo Comunitario):* Proyecto estatal plurinacional.
        
        **Movimientos y referentes:**  
        * *Figuras:* José Carlos Mariátegui, Alberto Acosta.
        """)
        st.subheader("📚 Itinerario Bibliográfico Enriquecido:")
        st.markdown("- José Carlos Mariátegui, *7 ensayos de interpretación de la realidad peruana* (Aporte: Raíz comunitaria agraria).")

    st.balloons()
