import streamlit as st
import pandas as pd

st.set_page_config(page_title="Arqueología Antropológica Política", page_icon="🏛️", layout="wide")

st.title("🏛️ Simulador de Arqueología Antropológica Política")
st.markdown("---")
st.write("""
**Bienvenido al laboratorio de arqueología conceptual.** Inspirado en el flujo deductivo del pensamiento político, este simulador parte de tu **concepto de ser humano** para descender por las capas de la sociedad, la nación, el estado, la economía y el proyecto histórico. 
Tómate tu tiempo en cada dilema. Al finalizar, obtendrás una radiografía tabular, un diagnóstico crítico de tensiones y un riguroso modelamiento metacognitivo guiado por fuentes clásicas y pensadores de nuestra tradición hispanoamericana y chilena.
""")

# --- FORMULARIO DE DECISIONES SECUENCIALES (6 BLOQUES / 12 MICRO-PREGUNTAS - OPCIONES ALEATORIZADAS) ---
with st.form("formulario_arqueologia"):
    
    # BLOQUE 1: EL CONCEPTO DE SER HUMANO
    st.header("Bloque 1: El Concepto de Ser Humano")
    
    st.markdown("*1. Motor de la acción: ¿Qué impulsa fundamentalmente al ser humano en su vida en común?*")
    p1 = st.radio("Selecciona una opción:", [
        "C) El sentido de pertenencia a una comunidad orgánica, la familia y la tradición.",
        "A) La búsqueda racional de su propio interés y beneficio particular.",
        "D) El impulso irrenunciable hacia la soberanía absoluta de su propio cuerpo y voluntad.",
        "B) La necesidad material y su transformación a través del trabajo colectivo."
    ], key="p1_choice")

    st.markdown("*2. Naturaleza y devenir: ¿Cómo consideras la condición fundamental de las personas?*")
    p2 = st.radio("Selecciona una opción:", [
        "B) Un sujeto histórico cuya conciencia cambia según las condiciones materiales.",
        "D) Un espíritu libre que rechaza de raíz toda imposición moral o legal externa.",
        "A) Un individuo cuyos derechos y autonomía preceden a cualquier sociedad.",
        "C) Un heredero de tradiciones e instituciones que lo trascienden históricamente."
    ], key="p2_choice")

    st.markdown("---")

    # BLOQUE 2: EL VÍNCULO SOCIAL
    st.header("Bloque 2: El Vínculo Social")
    
    st.markdown("*3. Origen del lazo: ¿Cómo se constituye fundamentalmente la sociedad?*")
    p3 = st.radio("Selecciona una opción:", [
        "D) Mediante la cooperación libre y espontánea, sin coacción institucional.",
        "B) Mediante un conflicto estructural e histórico entre clases sociales.",
        "A) Mediante un contrato voluntario entre ciudadanos para proteger intereses.",
        "C) Mediante lazos históricos, culturales y espirituales preexistentes."
    ], key="p3_choice")

    st.markdown("*4. Regla de convivencia: ¿Qué debe regular la vida en común?*")
    p4 = st.radio("Selecciona una opción:", [
        "C) La fidelidad a los valores compartidos, las costumbres y la autoridad tradicional.",
        "A) El imperio de la ley impersonal, los contratos y la neutralidad institucional.",
        "D) La autonomía absoluta de cada asociación voluntaria o comuna libre.",
        "B) La superación de las contradicciones de clase mediante la acción colectiva."
    ], key="p4_choice")

    st.markdown("---")

    # BLOQUE 3: NACIÓN E IDENTIDAD
    st.header("Bloque 3: Nación e Identidad")
    
    st.markdown("*5. Fundamento de pertenencia: ¿Qué define la identidad colectiva o la pertenencia?*")
    p5 = st.radio("Selecciona una opción:", [
        "B) Una comunidad de destino histórico, cultural y lingüístico soberano.",
        "D) El arraigo profundo a la tierra ancestral y a los pueblos originarios.",
        "A) La adhesión cívica a un conjunto de leyes y derechos universales abiertos.",
        "C) Ninguna frontera; la verdadera lealtad es de clase internacional."
    ], key="p5_choice")

    st.markdown("*6. Escala de lealtad: ¿Dónde debe depositarse la lealtad política primordial?*")
    p6 = st.radio("Selecciona una opción:", [
        "C) En la solidaridad internacional de los trabajadores contra el capital.",
        "A) En las instituciones democráticas globales o el derecho cosmopolita.",
        "D) En la autogestión de las comunidades locales y territoriales.",
        "B) En la defensa de la soberanía y tradiciones de la propia nación."
    ], key="p6_choice")

    st.markdown("---")

    # BLOQUE 4: EL ESTADO Y LA AUTORIDAD
    st.header("Bloque 4: El Estado y la Autoridad")
    
    st.markdown("*7. Naturaleza del poder: ¿Qué rol debe cumplir la autoridad política y el Estado?*")
    p7 = st.radio("Selecciona una opción:", [
        "D) Ser desmantelado por completo por ser una estructura coactiva e ilegítima.",
        "A) Ser un árbitro neutral y mínimo que garantice la libertad individual.",
        "C) Actuar como custodio soberano del orden frente a las amenazas externas.",
        "B) Funcionar como un aparato de dominación de clase a transformar/superar."
    ], key="p7_choice")

    st.markdown("*8. Forma de autoridad: ¿Cómo debe ejercerse el mando?*")
    p8 = st.radio("Selecciona una opción:", [
        "B) Mediante la dirección revolucionaria orientada a la justicia social.",
        "D) Mediante la rotación de cargos y el mandato colectivo horizontal.",
        "C) Mediante la jerarquía legítima basada en el honor, la historia y el orden.",
        "A) Mediante representantes elegidos bajo estrictas normas de control legal."
    ], key="p8_choice")

    st.markdown("---")

    # BLOQUE 5: ECONOMÍA Y RIQUEZA
    st.header("Bloque 5: Economía y Riqueza")
    
    st.markdown("*9. Modelo de producción: ¿Cómo debe organizarse la riqueza?*")
    p9 = st.radio("Selecciona una opción:", [
        "C) Mediante la reciprocidad, el trueque y el trabajo comunitario.",
        "A) Mediante la propiedad privada inviolable y el libre mercado competitivo.",
        "D) Mediante contratos estrictamente privados, sin impuestos ni Estado.",
        "B) Mediante la propiedad social y la planificación centralizada/social."
    ], key="p9_choice")

    st.markdown("*10. Criterio de distribución: ¿Qué debe guiar el reparto de bienes?*")
    p10 = st.radio("Selecciona una opción:", [
        "B) La satisfacción planificada de las necesidades de toda la sociedad.",
        "D) El equilibrio ecológico y la sustentabilidad de la vida comunitaria.",
        "A) La productividad y el mérito individual medidos por el mercado.",
        "C) La protección de la propiedad distribuida y la economía familiar."
    ], key="p10_choice")

    st.markdown("---")

    # BLOQUE 6: GEOPOLÍTICA Y PROYECTO HISTÓRICO
    st.header("Bloque 6: Geopolítica y Proyecto Histórico")
    
    st.markdown("*11. Arquitectura global: ¿Cómo debe estructurarse el orden geopolítico mundial?*")
    p11 = st.radio("Selecciona una opción:", [
        "B) Mediante la superación global del capitalismo por la solidaridad internacional.",
        "D) Mediante redes de autonomías locales autogestionadas al margen de los Estados.",
        "A) Mediante la integración global de los mercados y la gobernanza supranacional.",
        "C) Mediante un sistema multipolar de grandes bloques soberanos o civilizacionales."
    ], key="p11_choice")

    st.markdown("*12. Seguridad y soberanía exterior: ¿Cuál debe ser la prioridad en las relaciones internacionales?*")
    p12 = st.radio("Selecciona una opción:", [
        "C) La emancipación universal de los pueblos oprimidos frente al imperialismo global.",
        "A) La apertura comercial, la interdependencia y la disolución de barreras arancelarias.",
        "D) La desmilitarización y la cooperación horizontal entre comunas y pueblos libres.",
        "B) La defensa estricta de la soberanía nacional y la supervivencia frente al enemigo."
    ], key="p12_choice")

    submitted = st.form_submit_button("Ejecutar Análisis y Modelamiento Metacognitivo")

# --- PROCESAMIENTO Y DIAGNÓSTICO FORMATIVO CON PUNTAJE PONDERADO SEGURO ---
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

    # Inicialización limpia y explícita de los acumuladores de puntaje
    puntos = {
        "liberal": 0.0,
        "marxista": 0.0,
        "tradicional": 0.0,
        "libertario": 0.0,
        "anarquista": 0.0,
        "comunitario": 0.0
    }

    respuestas = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12]
    
    for r in respuestas:
        if r.startswith("A)"):
            puntos["liberal"] += 1.0
        elif r.startswith("B)"):
            puntos["marxista"] += 1.0
        elif r.startswith("C)"):
            puntos["tradicional"] += 0.5
            puntos["comunitario"] += 0.5
        elif r.startswith("D)"):
            puntos["anarquista"] += 0.5
            puntos["libertario"] += 0.5

    vertientes_ordenadas = sorted(puntos.items(), key=lambda x: x[1], reverse=True)
    v1, p_v1 = vertientes_ordenadas[0]
    v2, p_v2 = vertientes_ordenadas[1]

    max_vertiente = v1
    max_puntaje = p_v1
    es_coherente = max_puntaje >= 5

    nombres_vertientes = {
        "liberal": "Liberalismo Clásico",
        "marxista": "Marxismo y Teoría Crítica",
        "tradicional": "Tradicionalismo y Realismo Político",
        "libertario": "Anarcocapitalismo / Libertarismo Radical",
        "anarquista": "Anarquismo Clásico / Autonomismo",
        "comunitario": "Ontología Comunitaria y del Buen Vivir"
    }

    fuentes_hibridas = {
        "liberal": "1. John Locke, *Segundo tratado sobre el gobierno civil* (Leer: Capítulos 2, 5 y 8).\n2. Adam Smith, *La riqueza de las naciones* (Leer: Capítulos 1 al 3).",
        "marxista": "1. Karl Marx, *El Capital* (Leer: Sección 1, Capítulos 1 y 2).\n2. Karl Marx y Friedrich Engels, *Manifiesto del Partido Comunista* (Leer: Capítulo 1).",
        "tradicional": "1. Thomas Hobbes, *Leviatán* (Leer: Capítulos 13, 17 y 18).\n2. Carl Schmitt, *El concepto de lo político* (Leer: Capítulos 1 al 3).",
        "libertario": "1. Murray Rothbard, *Ética de la libertad* (Leer: Parte I).\n2. Ludwig von Mises, *La acción humana* (Leer: Capítulos 1 al 3).",
        "anarquista": "1. Piotr Kropotkin, *La ayuda mutua* (Leer: Introducción y Conclusión).\n2. Mijaíl Bakunin, *Dios y el Estado* (Leer: Textos fragmentados).",
        "comunitario": "1. José Carlos Mariátegui, *7 ensayos de interpretación de la realidad peruana* (Leer: Ensayo agrario).\n2. Alberto Acosta, *El buen vivir* (Leer: Capítulos 1 al 3)."
    }

    # --- DIAGNÓSTICO FINAL ---
    if not es_coherente:
        st.warning(f"⚠️ Diagnóstico: Perfil Híbrido — Entrecruzamiento Doctrinal entre {nombres_vertientes[v1]} y {nombres_vertientes[v2]}")
        st.markdown(f"""
        **1. Definiciones Fundamentales (Las vertientes en juego):**  
        * **{nombres_vertientes[v1]}:** Matriz teórica dominante en tus respuestas, centrada en sus propios ejes deductivos sobre la sociedad y la autoridad.
        * **{nombres_vertientes[v2]}:** Segunda matriz doctrinal detectada, la cual introduce principios alternativos o contrapuestos en tu arquitectura conceptual.  
        * *El cruce:* Estás combinando los fundamentos de ambas tradiciones sin un anclaje unificado, generando un choque entre sus respectivas premisas ontológicas.

        **2. Análisis Crítico y Graduación de Tensiones:**  
        * *Lo complementario:* En la acción política pragmática, es habitual tomar herramientas de distintas tradiciones para resolver problemas coyunturales.
        * *Lo irreconciliable (La contradicción profunda):* A nivel de la arquitectura conceptual, este cruce genera un cortocircuito. Estás aceptando simultáneamente premisas que se neutralizan mutuamente.
        
        **3. Modelamiento Metacognitivo (Reestructuración quirúrgica del edificio conceptual):**  
        Para resolver este cortocircuito deductivo, debes obligatoriamente volver al **Bloque 1 (Concepto de Ser Humano)** y asumir las consecuencias institucionales de tu elección:  
        * *Opción A (Someter la estructura a los principios de {nombres_vertientes[v1]}):* Si asumes esta vía, debes reescribir deductivamente tus capas subsiguientes (sociedad, estado y economía), descartando los mecanismos colectivistas, coactivos o intervencionistas de la segunda vertiente para evitar la disonancia teórica.  
        * *Opción B (Someter la estructura a los principios de {nombres_vertientes[v2]}):* Si asumes esta vía opuesta, debes subordinar radicalmente el orden institucional y económico a las premisas comunitarias, de clase u orgánicas de esta segunda matriz, purgando todo axioma individualista o mercantil abstracto.
        
        **Movimientos y referentes históricos y chilenos:**  
        * *Corrientes:* Síntesis doctrinales, pensamiento institucionalista y reformismo democrático.  
        * *Figuras:* Pensadores clásicos de ambas tradiciones en colisión intelectual.
        """)
        st.subheader("📚 Itinerario Bibliográfico Híbrido (Obras Clásicas de las Vertientes en Colisión):")
        st.markdown(f"**Fuentes Fundamentales de {nombres_vertientes[v1]}:**")
        st.markdown(fuentes_hibridas.get(v1, "- Obras clásicas de la matriz."))
        st.markdown(f"**Fuentes Fundamentales de {nombres_vertientes[v2]}:**")
        st.markdown(fuentes_hibridas.get(v2, "- Obras clásicas de la matriz."))
        st.markdown("**Comentarios y Ensayos Críticos sobre Pluralismo y Tensiones Doctrinales:**")
        st.markdown("1. Norberto Bobbio, *Derecha e izquierda* (Aporte: Criterios analíticos para clasificar las familias políticas y sus oposiciones. Leer: Capítulos 1 al 3).")
        st.markdown("2. Chantal Mouffe, *En torno a lo político* (Aporte: La dimensión agonística y los antagonismos doctrinales inconciliables. Leer: Capítulos 1 y 2).")
        st.markdown("3. Isaiah Berlin, *Cuatro ensayos sobre la libertad* (Aporte: El pluralismo de valores y sus contradicciones inevitables. Leer: Ensayo sobre los dos conceptos de libertad).")
        st.markdown("4. Michael Sandel, *El descontento con la democracia* (Aporte: Colisión entre el liberalismo procedimental y las lealtades comunitarias. Leer: Introducción).")

    elif max_vertiente == "liberal":
        st.success("✔ Diagnóstico: Coherencia Estructural Sólida — Liberalismo Clásico")
        st.markdown("""
        **1. Definiciones Fundamentales (La vertiente en juego):**  
        * **Liberalismo Clásico:** Tradición político-filosófica que sostiene que el individuo autónomo y racional precede ontológicamente a la sociedad. La convivencia política se funda en un contrato social voluntario, un Estado neutral e imparcial limitado por el imperio de la ley, y un orden económico basado en la propiedad privada y el libre mercado.
        
        **2. Explicación reveladora de tu postura (A qué adhiere tu perfil):**  
        Tus respuestas revelan una adhesión profunda y consistente a esta matriz. Operas bajo la convicción de que las instituciones deben garantizar un marco neutral donde cada quien persiga su propia felicidad sin imposiciones morales colectivas.
        
        **3. Modelamiento Metacognitivo (Despliegue y profundización de tu matriz):**  
        Partiendo de tu base individualista y contractual, tu edificio conceptual te exige decidir tu ruta de despliegue institucional:  
        * *Opción A (Despliegue hacia el Liberalismo Social / Reformista):* Asumir que la libertad formal del individuo requiere de garantías materiales básicas provistas por el Estado mediante impuestos moderados, asegurando igualdad de oportunidades sin destruir la competencia mercantil.  
        * *Opción B (Despliegue hacia el Liberalismo Mínimo / Ortodoxo):* Endurecer el principio de no agresión fiscal, apostando por un Estado estrictamente limitado a la seguridad y los tribunales, confiando la superación de la pobreza exclusivamente al dinamismo del mercado y la filantropía civil.
        
        **Movimientos y referentes históricos y chilenos:**  
        * *Movimientos:* Liberalismo político, reformismo republicano.  
        * *Figuras:* John Locke, Adam Smith, Alexis de Tocqueville, Friedrich Hayek; en Chile: José Victorino Lastarria y Valentín Letelier.
        """)
        st.subheader("📚 Itinerario Bibliográfico Basal (4 Autores Clásicos y 4 Comentaristas con Capítulos):")
        st.markdown("**Autores Clásicos (Doctrinarios):**")
        st.markdown("1. John Locke, *Segundo tratado sobre el gobierno civil* (Aporte: Origen del contrato social, estado de naturaleza y propiedad privada. Leer: Capítulos 2, 5 y 8).")
        st.markdown("2. Adam Smith, *La riqueza de las naciones* (Aporte: Funcionamiento del mercado, precios, mano invisible y división del trabajo. Leer: Capítulos 1 al 3 del Libro I).")
        st.markdown("3. Alexis de Tocqueville, *La democracia en América* (Aporte: Análisis de los peligros del centralismo estatal y el valor insustituible de la libertad civil. Leer: Volumen II, Segunda Parte).")
        st.markdown("4. Immanuel Kant, *Filosofía de la historia* (Aporte: El derecho cosmopolita, la paz perpetua y el Estado de derecho republicano. Leer: *Idea de una historia universal en sentido cosmopolita*).")
        st.markdown("**Comentarios y Ensayos Críticos:**")
        st.markdown("1. Friedrich Hayek, *Los fundamentos de la libertad* (Aporte: Defensa rigurosa del orden espontáneo de mercado frente al constructivismo racionalista. Leer: Capítulos 1 al 4).")
        st.markdown("2. Robert Nozick, *Anarquía, estado y utopía* (Aporte: Justificación del Estado mínimo desde los derechos individuales inviolables. Leer: Capítulos 3 al 7).")
        st.markdown("3. John Rawls, *Teoría de la justicia* (Aporte: El liberalismo político contemporáneo y la justicia como equidad. Leer: Capítulos 1 y 2: *El papel de la justicia* y *Los principios de la justicia*).")
        st.markdown("4. Norberto Bobbio, *Liberalismo y democracia* (Aporte: Síntesis crítica de la relación histórica entre los derechos liberales y las formas democráticas. Leer: Capítulos 1 al 3).")

    elif max_vertiente == "marxista":
        st.success("✔ Diagnóstico: Coherencia Estructural Sólida — Marxismo y Teoría Crítica")
        st.markdown("""
        **1. Definiciones Fundamentales (La vertiente en juego):**  
        * **Marxismo y Teoría Crítica:** Matriz teórico-política basada en el materialismo histórico. Sostiene que la conciencia y la política están determinadas por las condiciones materiales de producción y el conflicto estructural de clases. Busca la emancipación universal mediante la superación del capitalismo y la socialización de los medios de producción.
        
        **2. Explicación reveladora de tu postura (A qué adhiere tu perfil):**  
        Te sitúas firmemente en esta órbita. Tu visión rechaza las abstracciones contractuales y entiende que la injusticia no es un fallo moral individual, sino una contradicción estructural del sistema capitalista.
        
        **3. Modelamiento Metacognitivo (Despliegue y profundización de tu matriz):**  
        Partiendo del materialismo histórico, tu profundización te enfrenta a la disyuntiva estratégica sobre el método de transformación:  
        * *Opción A (La Vía Gramsciana / Hegemónica):* Enfocar la praxis en la construcción paciente de un "bloque histórico" y una nueva hegemonía cultural dentro de las instituciones de la sociedad civil y la democracia representativa.  
        * *Opción B (La Vía Revolucionaria / Ortodoxa):* Sostener que la superación del capital exige la ruptura frontal e insurreccional con el Estado burgués y la toma centralizada de la producción para organizar la economía bajo planificación social estricta.
        
        **Movimientos y referentes históricos y chilenos:**  
        * *Movimientos:* Comunismo histórico, sindicalismo de clase, internacionalismo proletario.  
        * *Figuras:* Karl Marx, Antonio Gramsci, Rosa Luxemburgo, Vladimir Lenin; en Chile: Luis Emilio Recabarren y Clotario Blest.
        """)
        st.subheader("📚 Itinerario Bibliográfico Basal (4 Autores Clásicos y 4 Comentaristas con Capítulos):")
        st.markdown("**Autores Clásicos (Doctrinarios):**")
        st.markdown("1. Karl Marx, *El Capital* (Aporte: Análisis riguroso de la plusvalía, la mercancía y la explotación capitalista. Leer: Sección 1, Capítulos 1 y 2).")
        st.markdown("2. Karl Marx y Friedrich Engels, *Manifiesto del Partido Comunista* (Aporte: La lucha de clases como motor de la historia y crítica al orden burgués. Leer: Capítulo 1: *Burgueses y proletarios*).")
        st.markdown("3. Vladimir Lenin, *El Estado y la revolución* (Aporte: Naturaleza coercitiva del Estado burgués y estrategia de transición proletaria. Leer: Capítulos 1 y 3).")
        st.markdown("4. Rosa Luxemburgo, *La acumulación del capital* (Aporte: Expansión imperialista y contradicciones sistémicas globales del capital. Leer: Secciones iniciales).")
        st.markdown("**Comentarios y Ensayos Críticos:**")
        st.markdown("1. Antonio Gramsci, *Cuadernos de la cárcel* (Aporte: Teoría de la hegemonía cultural, el bloque histórico y los intelectuales orgánicos. Leer: Antología sobre el Estado y la sociedad civil).")
        st.markdown("2. Ernst Mandel, *El pensamiento económico de Karl Marx* (Aporte: Clarificación sistemática de las crisis cíclicas y la ley del valor. Leer: Capítulos 1 al 3).")
        st.markdown("3. Georg Lukács, *Historia y conciencia de clase* (Aporte: El concepto de reificación y la conciencia de clase proletaria. Leer: Ensayo sobre *La reificación y la conciencia del proletariado*).")
        st.markdown("4. Louis Althusser, *Ideología y aparatos ideológicos del Estado* (Aporte: Funcionamiento de los aparatos represivos e ideológicos en la reproducción social. Leer: Ensayo completo).")

    elif max_vertiente == "tradicional":
        st.success("✔ Diagnóstico: Coherencia Estructural Sólida — Tradicionalismo y Realismo Político")
        st.markdown("""
        **1. Definiciones Fundamentales (La vertiente en juego):**  
        * **Tradicionalismo y Realismo Político:** Corriente que concibe al ser humano como un ser enraizado en comunidades históricas y culturales. Prioriza el orden, la soberanía estatal, la seguridad frente al conflicto geopolítico (*amigo/enemigo*) y la defensa de las instituciones orgánicas frente al desarraigo moderno.
        
        **2. Explicación reveladora de tu postura (A qué adhiere tu perfil):**  
        Adhieres coherentemente a una visión donde la política es ante todo conservación del orden, soberanía efectiva y defensa de la identidad colectiva frente a las amenazas del entorno global.
        
        **3. Modelamiento Metacognitivo (Despliegue y profundización de tu matriz):**  
        Partiendo del principio de soberanía y enraizamiento, tu arquitectura te exige definir tu proyección geopolítica institucional:  
        * *Opción A (Vía Estado-Nación Soberano):* Enfocar la defensa de la identidad nacional fortaleciendo el Estado nacional centralizado, protegiendo las fronteras económicas y apostando al realismo clásico westfaliano.  
        * *Opción B (Vía Multipolaridad Civilizacional / Cuarta Teoría):* Elevar la mirada hacia un mundo policéntrico de grandes espacios civilizacionales (*Großraum*) que rechazan frontalmente el universalismo y la hegemonía de la modernidad occidental liberal.
        
        **Movimientos y referentes históricos y chilenos:**  
        * *Movimientos:* Soberanismos nacionales, realismo político clásico.  
        * *Figuras:* Thomas Hobbes, Carl Schmitt, Juan Donoso Cortés, Edmund Burke; en Chile: la tradición de geopolítica nacional y el pensamiento de Ramón Cañas Montalva.
        """)
        st.subheader("📚 Itinerario Bibliográfico Basal (4 Autores Clásicos y 4 Comentaristas con Capítulos):")
        st.markdown("**Autores Clásicos (Doctrinarios):**")
        st.markdown("1. Thomas Hobbes, *Leviatán* (Aporte: Necesidad fundacional de una soberanía fuerte e indivisible para evitar el caos. Leer: Capítulos 13, 17 y 18).")
        st.markdown("2. Carl Schmitt, *El concepto de lo político* (Aporte: Definición ontológica de la política a través de la distinción amigo/enemigo. Leer: Capítulos 1 al 3).")
        st.markdown("3. Juan Donoso Cortés, *Ensayos sobre el catolicismo, el liberalismo y el socialismo* (Aporte: Crítica teológica y política al racionalismo moderno. Leer: Ensayos fundamentales).")
        st.markdown("4. Edmund Burke, *Reflexiones sobre la revolución en Francia* (Aporte: Defensa del orden consuetudinario, la historia y la prudencia frente al abstractismo político. Leer: Fragmentos esenciales sobre la herencia institucional).")
        st.markdown("**Comentarios y Ensayos Críticos:**")
        st.markdown("1. Aleksandr Dugin, *La cuarta teoría política* (Aporte: Crítica radical al globalismo liberal/marxista y defensa de los grandes espacios civilizacionales. Leer: Capítulos iniciales).")
        st.markdown("2. Ramón Cañas Montalva, *Geopolítica de Chile* (Aporte: Estrategia territorial, bioceánica y antártica del Estado soberano. Leer: Capítulos sobre espacios vitales y soberanía nacional).")
        st.markdown("3. Hans Morgenthau, *Política entre las naciones* (Aporte: Los principios rectores del realismo político y el interés nacional. Leer: Capítulos 1 y 2).")
        st.markdown("4. Julien Freund, *L'essence du politique* (Aporte: Análisis sistemático de las constantes del mando, la obediencia y el espectro político. Leer: Capítulos sobre el poder y la autoridad).")

    elif max_vertiente == "libertario":
        st.success("✔ Diagnóstico: Coherencia Estructural Sólida — Anarcocapitalismo / Libertarismo Radical")
        st.markdown("""
        **1. Definiciones Fundamentales (La vertiente en juego):**  
        * **Libertarismo Radical y Anarcocapitalismo:** Doctrina basada en el axioma de la autopropiedad y el principio de no agresión. Sostiene que todo individuo es dueño absoluto de su cuerpo y de los frutos de su trabajo, considerando cualquier intervención estatal o tributaria como una forma ilegítima de coacción.
        
        **2. Explicación reveladora de tu postura (A qué adhiere tu perfil):**  
        Tu perfil se alinea con la defensa intransigente del libre mercado absoluto y la soberanía individual radical, rechazando toda forma de monopolio estatal sobre la moneda, la justicia o la seguridad.
        
        **3. Modelamiento Metacognitivo (Despliegue y profundización de tu matriz):**  
        Partiendo del axioma de la autopropiedad, tu profundización doctrinal te lleva a elegir entre dos caminos de aplicación:  
        * *Opción A (La vía anarcocapitalista radical):* Abolición total del Estado y su monopolio de la fuerza, confiando la seguridad, la justicia y la emisión monetaria a agencias privadas de libre mercado y contratos voluntarios.  
        * *Opción B (La vía minarquista / liberal de ley y orden):* Aceptación pragmática de un Estado mínimo estrictamente limitado a la defensa nacional, la policía y los tribunales, prohibiendo toda intervención económica adicional.
        
        **Movimientos y referentes:**  
        * *Movimientos:* Escuela austríaca de economía, movimiento libertario contemporáneo.  
        * *Figuras:* Murray Rothbard, Ludwig von Mises, Ayn Rand, Robert Nozick.
        """)
        st.subheader("📚 Itinerario Bibliográfico Basal (4 Autores Clásicos y 4 Comentaristas con Capítulos):")
        st.markdown("**Autores Clásicos (Doctrinarios):**")
        st.markdown("1. Murray Rothbard, *Ética de la libertad* (Aporte: Deducción axiomática de los derechos de propiedad y la autopropiedad. Leer: Parte I: *Ley natural* y Parte II).")
        st.markdown("2. Ludwig von Mises, *La acción humana* (Aporte: Tratado fundamental de praxeología y demostración de la superioridad económica del mercado libre. Leer: Capítulos 1 al 4).")
        st.markdown("3. Ayn Rand, *La virtud del egoísmo* (Aporte: Justificación ética del interés propio y el capitalismo de laissez-faire. Leer: Ensayos 1 al 4).")
        st.markdown("4. Friedrich Hayek, *Camino de servidumbre* (Aporte: Demostración de cómo la planificación económica conduce inexorablemente al totalitarismo. Leer: Capítulos 1 al 5).")
        st.markdown("**Comentarios y Ensayos Críticos:**")
        st.markdown("1. Jesús Huerta de Soto, *Socialismo, cálculo económico y función empresarial* (Aporte: Imposibilidad teórica del socialismo y vindicación de la función empresarial. Leer: Capítulos 1 al 3).")
        st.markdown("2. Robert Nozick, *Anarquía, estado y utopía* (Aporte: Defensa crítica del Estado mínimo frente a las pretensiones anarcocapitalistas. Leer: Capítulos 3 al 5).")
        st.markdown("3. Hans-Hermann Hoppe, *Democracia: el Dios que fracasó* (Aporte: Crítica radical al sufragio universal y defensa de órdenes sociales de derecho privado. Leer: Capítulos 1 al 3).")
        st.markdown("4. Tom Bethell, *The Noblest Triumph: Property and Prosperity through the Ages* (Aporte: Historia institucional de cómo la propiedad privada fundamenta la civilización. Leer: Introducción y conclusiones).")

    elif max_vertiente == "anarquista":
        st.success("✔ Diagnóstico: Coherencia Estructural Sólida — Anarquismo Clásico / Autonomismo")
        st.markdown("""
        **1. Definiciones Fundamentales (La vertiente en juego):**  
        * **Anarquismo Clásico y Autonomismo:** Tradición político-social que postula la incompatibilidad absoluta entre la libertad humana y toda estructura de dominación jerárquica (Estado, capitalismo, Iglesia). Propone la autoorganización horizontal, la ayuda mutua, el federalismo comunal y la acción directa.
        
        **2. Explicación reveladora de tu postura (A qué adhiere tu perfil):**  
        Adhieres a una concepción donde el orden social no requiere de mandos verticales ni coacción institucional, sino de la cooperación voluntaria y la federación autónoma desde las bases.
        
        **3. Modelamiento Metacognitivo (Despliegue y profundización de tu matriz):**  
        Partiendo del rechazo a la autoridad coactiva, tu profundización exige definir los mecanismos socioeconómicos de integración:  
        * *Opción A (La vía anarcosindicalista):* Organizar la producción económica mediante sindicatos de trabajadores autogestionados y federados que suplanten tanto al capital privado como al Estado.  
        * *Opción B (La vía comunalista / municipalismo libertario):* Apostar por redes de comunas autónomas autogestionadas basadas en la cooperación ecológica local, el mandato revocable y la ayuda mutua vecinal.
        
        **Movimientos y referentes históricos y chilenos:**  
        * *Movimientos:* Anarcosindicalismo histórico, cooperativismo obrero.  
        * *Figuras:* Piotr Kropotkin, Mijaíl Bakunin, Pierre-Joseph Proudhon, Elisée Reclus; en Chile: la prensa mutualista y precursores del movimiento obrero ácrata.
        """)
        st.subheader("📚 Itinerario Bibliográfico Basal (4 Autores Clásicos y 4 Comentaristas con Capítulos):")
        st.markdown("**Autores Clásicos (Doctrinarios):**")
        st.markdown("1. Piotr Kropotkin, *La ayuda mutua* (Aporte: Demostración histórica de la cooperación como factor evolutivo social al margen del Estado. Leer: Introducción y Conclusión).")
        st.markdown("2. Mijaíl Bakunin, *Dios y el Estado* (Aporte: Crítica frontal a la autoridad teológica, política y a los dogmas jerárquicos. Leer: Texto completo fragmentado).")
        st.markdown("3. Pierre-Joseph Proudhon, *¿Qué es la propiedad?* (Aporte: La tesis sobre la propiedad como dominación y el mutualismo económico. Leer: Capítulos 1 al 3).")
        st.markdown("4. Elisée Reclus, *El hombre y la tierra* (Aporte: Relación simbiótica entre las comunidades humanas libres y el entorno ecológico. Leer: Introducción geográfica).")
        st.markdown("**Comentarios y Ensayos Críticos:**")
        st.markdown("1. Daniel Guérin, *El anarquismo* (Aporte: Síntesis histórica rigurosa de las corrientes y praxis ácratas mundiales. Leer: Capítulos introductorios).")
        st.markdown("2. Colin Ward, *Anarchy in Action* (Aporte: Ejemplos prácticos y cotidianos de cómo la sociedad se autoorganiza sin necesidad de gobierno. Leer: Capítulos 1 al 4).")
        st.markdown("3. Murray Bookchin, *The Ecology of Freedom* (Aporte: Fundamentación del municipalismo libertario y la ecología social. Leer: Capítulos sobre la jerarquía y la libertad).")
        st.markdown("4. Rudolf Rocker, *Anarcosindicalismo* (Aporte: Expresa la relación clásica entre el sindicalismo obrero y la emancipación antiautoritaria. Leer: Capítulos 1 al 3).")

    elif max_vertiente == "comunitario":
        st.success("✔ Diagnóstico: Coherencia Estructural Sólida — Ontología Comunitaria y del Buen Vivir")
        st.markdown("""
        **1. Definiciones Fundamentales (La vertiente en juego):**  
        * **Ontología Comunitaria y Buen Vivir:** Matriz inspirada en el pensamiento indígena y comunitario que concibe a la persona como un nodo inalienable de un tejido vivo que integra a la comunidad humana, los antepasados y la naturaleza (*Pachamama*). Opone la reciprocidad y el mandar obedeciendo al individualismo mercantil.
        
        **2. Explicación reveladora de tu postura (A qué adhiere tu perfil):**  
        Te alineas con una visión donde la economía y la política deben estar subordinadas a la reproducción de la vida comunitaria, el equilibrio territorial y la reciprocidad frente al extractivismo.
        
        **3. Modelamiento Metacognitivo (Despliegue y profundización de tu matriz):**  
        Partiendo de la matriz comunitaria y territorial, tu profundización exige definir el cauce político de tu proyecto:  
        * *Opción A (Vía Autonomía Territorial y Comunal):* Consolidar el autogobierno local, la justicia indígena y la propiedad colectiva de la tierra como espacios blindados frente al extractivismo global.  
        * *Opción B (Vía Socialismo Comunitario / Plurinacional):* Articular las comunidades originarias con un proyecto político estatal plurinacional que transforme las estructuras de dominación económica a escala nacional.
        
        **Movimientos y referentes históricos y latinoamericanos:**  
        * *Movimientos:* Zapatismo, confederaciones indígenas andinas, movimientos por el Buen Vivir.  
        * *Figuras:* José Carlos Mariátegui, Alberto Acosta, Álvaro García Linera, Fausto Reinaga.
        """)
        st.subheader("📚 Itinerario Bibliográfico Basal (4 Autores Clásicos y 4 Comentaristas con Capítulos):")
        st.markdown("**Autores Clásicos (Doctrinarios):**")
        st.markdown("1. José Carlos Mariátegui, *7 ensayos de interpretación de la realidad peruana* (Aporte: El problema del indio y la pervivencia del ayllu y la raíz comunitaria agraria. Leer: Ensayo sobre el problema agrario).")
        st.markdown("2. Alberto Acosta, *El buen vivir: Sumak Kawsay* (Aporte: Crítica al desarrollismo capitalista y formulación de alternativas desde la cosmovisión comunitaria. Leer: Capítulos 1 al 3).")
        st.markdown("3. Fausto Reinaga, *La revolución india* (Aporte: Conciencia amindia y reivindicación de civilización comunitaria frente al colonialismo. Leer: Capítulos esenciales).")
        st.markdown("4. Silvia Rivera Cusicanqui, *Oprimidos pero no vencidos* (Aporte: Luchas campesinas, aymaras y sociología de la imagen comunitaria. Leer: Capítulos metodológicos).")
        st.markdown("**Comentarios y Ensayos Críticos:**")
        st.markdown("1. Álvaro García Linera, *Forma valor y forma comunidad* (Aporte: Articulación teórica entre el marxismo crítico y las estructuras comunitarias andinas. Leer: Introducción y capítulos centrales).")
        st.markdown("2. Arturo Escobar, *Territorios de diferencia* (Aporte: Geografías de la diferencia, ontologías relacionales y defensa de los mundos socio-naturales. Leer: Capítulos 1 al 3).")
        st.markdown("3. Eduardo Gudynas, *Derechos de la naturaleza y buen vivir* (Aporte: Sistematización jurídica y filosófica del biocentrismo comunitario. Leer: Capítulos iniciales).")
        st.markdown("4. Boaventura de Sousa Santos, *Descolonizar el saber, reinventar el poder* (Aporte: Las epistemologías del sur frente a la hegemonía de la modernidad occidental. Leer: Ensayos sobre el Estado plurinacional).")

    st.balloons()
