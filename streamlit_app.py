import streamlit as st

# --------------------- Impostazione della Configurazione della Pagina ---------------------
st.set_page_config(
    page_title="Powerplexity Chatbot",
    page_icon="💬",
    layout="wide"  # Imposta il layout su wide
)

# --------------------- Iniezione CSS Personalizzato per Tema Arancione e Chat ---------------------
def inject_css():
    st.markdown("""
    <style>
    /* Imposta il colore primario su arancione */
    :root {
        --primary-color: #F76C6C; /* Arancione Intesa */
        --secondary-color: #FFBA49;
    }

    /* Modifica la barra laterale */
    .css-1d391kg {
        background-color: var(--primary-color);
    }

    /* Intestazione e Titolo */
    .css-1aumxhk {
        color: var(--primary-color);
    }

    /* Pulsanti */
    .stButton>button {
        background-color: var(--secondary-color);
        color: white;
        border: none;
        border-radius: 5px;
        padding: 10px 20px;
    }

    .stButton>button:hover {
        background-color: #FFA500;
        color: white;
    }

    /* Espanditori */
    .css-1r6slb0 .streamlit-expanderHeader {
        color: var(--primary-color);
    }

    /* Link */
    a {
        color: var(--primary-color);
        text-decoration: none;
    }

    a:hover {
        text-decoration: underline;
        color: #FFA500;
    }

    /* Footer */
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #f1f1f1;
        color: #333;
        text-align: center;
        padding: 10px;
    }

    /* Etichette Checkbox */
    .stCheckbox label {
        color: #333;
    }

    /* Campi di Testo e Aree di Testo */
    .stTextInput>div>div>input {
        border-color: var(--primary-color);
    }

    .stTextArea>div>div>textarea {
        border-color: var(--primary-color);
    }

    /* Pulsanti di Download */
    .stDownloadButton>button {
        background-color: var(--secondary-color);
        color: white;
        border: none;
        border-radius: 5px;
        padding: 8px 16px;
    }

    .stDownloadButton>button:hover {
        background-color: #FFA500;
        color: white;
    }

    /* Stile per le Chat */
    .user-message {
        background-color: #FFEBCC;
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 10px;
        max-width: 80%;
        align-self: flex-end;
    }

    .assistant-message {
        background-color: #D9EAD3;
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 10px;
        max-width: 80%;
        align-self: flex-start;
    }

    .chat-container {
        display: flex;
        flex-direction: column;
    }
    </style>
    """, unsafe_allow_html=True)

inject_css()

# --------------------- Inizializzazione dello stato della sessione ---------------------
# Assicurati che tutte le chiavi necessarie in st.session_state siano inizializzate
if 'selected_feedback' not in st.session_state:
    st.session_state['selected_feedback'] = []

if 'additional_feedback_expander' not in st.session_state:
    st.session_state['additional_feedback_expander'] = ""

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []  # Lista di tuple: (sender, message)

# --------------------- Barra Laterale con Logo di Intesa Sanpaolo ---------------------
with st.sidebar:
    # Aggiungi il logo di Intesa Sanpaolo
    logo_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/3/33/Intesa_Sanpaolo_logo.svg/1200px-Intesa_Sanpaolo_logo.svg.png"  # Sostituisci con l'URL del tuo logo o il percorso locale
    st.image(logo_url, use_column_width=True)
    
    st.title("Powerplexity Chatbot")
    st.markdown("**Applicazione di Chatbot con Funzionalità Avanzate**")
    st.markdown("---")
    st.markdown("🔍 **Esplora**")
    st.button("Fonti")
    st.button("Domande Correlate")

# --------------------- Contenuto Principale ---------------------
st.title("💬 Mockup Avanzato di Powerplexity Chatbot")
st.write("")

# --------------------- Sezione Chatbot ---------------------
st.header("Chatbot Data Lineage delle Tabelle Bancarie")

# Layout per la chat
chat_placeholder = st.empty()

# Funzione per generare la risposta dell'assistente
def generate_response(user_input):
    """
    Genera una risposta basata sull'input dell'utente.
    In un'applicazione reale, questa funzione potrebbe integrare un modello NLP o altre logiche di business.
    Per questo esempio, utilizzeremo una risposta predefinita basata sulle fonti.
    """
    # Per semplicità, la risposta sarà una sintesi delle informazioni di data lineage
    response = """
    Il **data lineage** nelle banche rappresenta il tracciamento dettagliato del flusso dei dati attraverso le varie tabelle e sistemi. Questo processo è fondamentale per garantire trasparenza, qualità e conformità dei dati. Le principali componenti includono l'origine dei dati, i processi di trasformazione e le destinazioni finali. Implementare un efficace data lineage permette di identificare e correggere errori, ottimizzare i processi e assicurare il rispetto delle normative vigenti.
    """
    return response

# Visualizza la cronologia della chat
def display_chat():
    if st.session_state.chat_history:
        with chat_placeholder.container():
            for sender, message in st.session_state.chat_history:
                if sender == "user":
                    st.markdown(f'<div class="user-message">{message}</div>', unsafe_allow_html=True)
                else:
                    st.markdown(f'<div class="assistant-message">{message}</div>', unsafe_allow_html=True)

display_chat()

# Campo di input per l'utente
user_input = st.chat_input("Tu:")

if user_input:
    # Aggiungi la domanda dell'utente alla cronologia
    st.session_state.chat_history.append(("user", user_input))
    
    # Genera la risposta dell'assistente
    assistant_response = generate_response(user_input)
    st.session_state.chat_history.append(("assistant", assistant_response))
    
    # Aggiorna la visualizzazione della chat
    display_chat()

# --------------------- Sezione Fonti con Icone Realistiche ---------------------
with st.expander("📚 Fonti", expanded=False):
    st.markdown("Questi sono i file che forniscono informazioni dettagliate relative al data lineage delle tabelle bancarie. Espandi per visualizzare le fonti:")

    # Funzione per simulare il recupero delle fonti dei file
    def get_sources():
        return [
            {
                "title": "Diagramma Data Lineage delle Tabelle",
                "link": "https://example.com/files/data_lineage_diagram.pptx",
                "summary": "Diagramma che illustra il flusso dei dati attraverso le principali tabelle del sistema bancario.",
                "publisher": "Powerplexity Analytics",
                "date": "15 Marzo 2024",
                "file_type": "pptx"
            },
            {
                "title": "Report sul Data Lineage",
                "link": "https://example.com/files/data_lineage_report.pdf",
                "summary": "Rapporto dettagliato sull'implementazione del data lineage nelle operazioni bancarie.",
                "publisher": "Middle East Research Institute",
                "date": "20 Marzo 2024",
                "file_type": "pdf"
            },
            {
                "title": "Manuale di Implementazione Data Lineage",
                "link": "https://example.com/files/data_lineage_manual.docx",
                "summary": "Documento Word che descrive le best practice per implementare il data lineage nelle banche.",
                "publisher": "Global Trade Watch",
                "date": "25 Marzo 2024",
                "file_type": "docx"
            },
            {
                "title": "Statistiche sul Data Lineage",
                "link": "https://example.com/files/data_lineage_stats.xlsx",
                "summary": "Analisi statistica delle performance e dell'efficacia del data lineage nelle tabelle bancarie.",
                "publisher": "Powerplexity Strategy",
                "date": "30 Marzo 2024",
                "file_type": "excel"
            },
        ]

    sources = get_sources()

    # Mappatura dei tipi di file alle icone realistiche
    file_icons = {
        "excel": "https://img.icons8.com/color/48/000000/microsoft-excel-2019--v1.png",
        "pdf": "https://img.icons8.com/color/48/000000/pdf-2--v1.png",
        "pptx": "https://img.icons8.com/color/48/000000/microsoft-powerpoint-2019--v1.png",
        "docx": "https://img.icons8.com/color/48/000000/microsoft-word-2019--v1.png"
    }

    # Visualizzazione di ciascuna fonte con l'icona appropriata e il link mock
    for source in sources:
        icon_url = file_icons.get(source["file_type"], "https://img.icons8.com/ios-filled/50/000000/file.png")  # Icona di default se il tipo di file non è trovato
        # Costruzione del markdown con l'icona e il titolo cliccabile
        source_markdown = f"""
        <div style="display: flex; align-items: center;">
            <img src="{icon_url}" alt="{source['file_type']} icon" style="width:24px;height:24px;margin-right:10px;">
            <a href="{source['link']}" target="_blank" style="font-size: 18px; text-decoration: none; color: #F76C6C;">{source['title']}</a>
        </div>
        <div style="margin-left:34px;">
            <strong>Editore:</strong> {source['publisher']}  
            <strong>Data:</strong> {source['date']}  
            <strong>Sintesi:</strong> {source['summary']}
        </div>
        <hr style="border: 0; height: 1px; background-color: #ccc; margin: 10px 0;">
        """
        st.markdown(source_markdown, unsafe_allow_html=True)

# --------------------- Sezione Feedback con Espanditore ---------------------
with st.expander("🛠️ Fornisci Feedback", expanded=False):
    st.markdown("**Aiutaci a Migliorare Questa Risposta**")
    st.markdown("Seleziona tutte le opzioni applicabili:")

    # Opzioni di feedback
    feedback_options = {
        "imprecise": "⚠️ Impréciso",
        "not_updated": "🔄 Non aggiornato",
        "too_short": "📏 Troppo breve",
        "too_long": "📜 Troppo lungo",
        "harmful_offensive": "🚨 Danno o offensivo",
        "not_useful": "❌ Non utile"
    }

    # Disposizione delle checkbox in tre colonne
    cols = st.columns(3)
    for idx, (key, label) in enumerate(feedback_options.items()):
        with cols[idx % 3]:
            if st.checkbox(label, key=f"checkbox_{key}"):
                if key not in st.session_state['selected_feedback']:
                    st.session_state['selected_feedback'].append(key)
            else:
                if key in st.session_state['selected_feedback']:
                    st.session_state['selected_feedback'].remove(key)

    # Area di testo per feedback aggiuntivo
    additional_feedback = st.text_area("Come possiamo migliorare la risposta? (Opzionale)", height=100, key="additional_feedback_expander")

    # Pulsanti Invia e Annulla
    submit_cancel_cols = st.columns(2)
    with submit_cancel_cols[0]:
        if st.button("Invia Feedback", key="submit_feedback_expander"):
            if st.session_state['selected_feedback']:
                # Gestisci il feedback (es. salva nel database o invia tramite email)
                st.success("Grazie per il tuo feedback!")
                # Resetta lo stato del feedback
                st.session_state['selected_feedback'] = []
                st.session_state['additional_feedback_expander'] = ""
                st.experimental_rerun()
            else:
                st.warning("Per favore, seleziona almeno un'opzione di feedback.")
    with submit_cancel_cols[1]:
        if st.button("Annulla Feedback", key="cancel_feedback_expander"):
            st.session_state['selected_feedback'] = []
            st.session_state['additional_feedback_expander'] = ""
            st.experimental_rerun()

# --------------------- Sezione Domande Correlate ---------------------
st.subheader("🔗 Domande Correlate")
related_questions = [
    "Cos'è il data lineage e perché è importante per le banche?",
    "Come implementare efficacemente il data lineage nelle tabelle bancarie?",
    "Quali strumenti sono disponibili per monitorare il data lineage in un istituto bancario?"
]
for question in related_questions:
    st.markdown(f"- {question}")

# --------------------- Sezione Footer ---------------------
st.markdown("""
<style>
.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: #f1f1f1;
    color: #333;
    text-align: center;
    padding: 10px;
}
</style>
<div class="footer">
    <p>© 2024 Powerplexity. Tutti i diritti riservati.</p>
</div>
""", unsafe_allow_html=True)
