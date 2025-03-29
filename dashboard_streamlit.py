from re import sub
from pyparsing import col
import streamlit as st
import terminado 
from main import setup_dashboard_data
from terminverwaltung import Terminverwaltung

termin_verwaltung, studienfortschritt, notendurchschnitt, chatbot, data_manager = setup_dashboard_data()

# Lade gespeicherte Termine und setzt Standardtermine
data = data_manager.load_data()
if "termine" in data and data["termine"]:
    termin_verwaltung.load_from_dict_list(data["termine"])
else:
    termin_verwaltung = Terminverwaltung.with_default_termine()
    data_manager.save_termine(termin_verwaltung)

st.set_page_config(page_title="Studien-Dashboard", layout="centered")

st.title("📊 Studien-Dashboard")
st.header("Willkommen zurück, Johannes")

# Studienfortschritt
st.subheader("🎓 Studienfortschritt")
col1, col2 = st.columns([1,2])

with col1: 
    st.metric(label=" 📘 Abgeschlossene Module",
              value=f"{studienfortschritt.completed_modules}")
    st.metric(label=" 📚 ECTS-Punkte",
              value=f"{studienfortschritt.completed_ects}", delta=f"{studienfortschritt.total_ects}")

with col2:
    st.progress(studienfortschritt.progress_percentage/100)
    st.success(f"{studienfortschritt.progress_percentage}% deines Studiums abgeschlossen")
    
# Terminverwaltung
st.subheader("📅 Terminverwaltung")

col_links, col_rechts = st.columns([2, 2])

# Neuen Termin hinzufügen
with col_links:
    with st.expander(" Anstehende Termine anzeigen", expanded=True):
        if termin_verwaltung.termine:
            for termin in termin_verwaltung.termine:
                st.write(f"⚪️ {termin}")
        else:
            st.info("Es sind keine Termine vorhanden.")


with col_rechts:
    with st.expander("➕ Termin hinzufügen"):
        with st.form(key="add_termin_form"):
            title = st.text_input("Titel des Termins")
            date = st.date_input("Datum")
            time = st.time_input("Uhrzeit")
            location = st.text_input("Ort")

            submitted = st.form_submit_button("Termin hinzufügen")
            if submitted:
                from termin import Termin
                neuer_termin = Termin(str(title), str(date), str(time), str(location))
                termin_verwaltung.add_termin(neuer_termin)
                data_manager.save_termine(termin_verwaltung)
                st.success("✅ Termin erfolgreich hinzugefügt.")
                st.experimental_rerun()
    
    with st.expander("🗑️ Termin entfernen"):
        if termin_verwaltung.termine:
            for idx, termin in enumerate(termin_verwaltung.termine):
                col1, col2 = st.columns([5,3])
                with col1:
                    st.write(f"{idx+1}. {termin}")
                with col2:
                    if "(Voreingestellt)" in str(termin):
                        st.button("Termin ist GESPERRT", key=f"locked_termin_{idx}", disabled=True)
                    
                    else:
                        if st.button("Löschen", key=f"delete_termin_{idx}"):
                            termin_verwaltung.remove_termin_by_index(idx)
                            data_manager.save_termine(termin_verwaltung)
                            st.success("✅ Termin erfolgreich gelöscht.")
                            st.experimental_rerun()



# Notendurchschnitt
st.subheader("📈 Notendurchschnitt")

col1, col2 = st.columns(2)

with col1:
    st.metric(label="Aktueller Durchschnitt", value=f"{notendurchschnitt.current_average}")

with col2:
    st.write(notendurchschnitt.compare_with_target())

# Anzeige aller Noten
st.markdown("**Einzele Noten:**")
for grade in notendurchschnitt.grades:
    st.write(f"⚪️ {str(grade)}")

# Chatbot
st.subheader("🤖 Chatbot")

frage = st.text_input("Stelle dem Chatbot eine Frage:")
if frage: 
    antwort = chatbot.get_response(frage)
    st.write(f"💬 {antwort}")