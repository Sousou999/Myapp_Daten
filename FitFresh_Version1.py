import streamlit as st
import pandas as pd

# Beispiel Daten für gesunde Rezepte ohne Bilder
recipes_data = {
    "Gericht": [
        "Gebackene Aubergine mit Quinoa-Füllung",
        "Gegrillter Lachs mit Zitronen-Kräuter-Sauce",
        "Gemüsecurry mit Kokosmilch",
        "Gefüllte Paprika mit Couscous und Feta",
        "Ratatouille",
        "Omelett mit Spinat und Feta"
    ],
    "Zutaten": [
        "Aubergine, Quinoa, Gemüsebrühe, Tomaten, Feta, Kräuter",
        "Lachsfilet, Zitrone, Knoblauch, Petersilie, Olivenöl",
        "Gemüse (z.B. Karotten, Zucchini, Kichererbsen), Kokosmilch, Currypaste, Reis",
        "Paprika, Couscous, Feta, Tomaten, Zwiebel, Knoblauch",
        "Zucchini, Aubergine, Paprika, Tomaten, Zwiebel, Knoblauch, Kräuter",
        "Eier, Spinat, Feta, Milch, Butter"
    ],
    "Schwierigkeitsgrad": [
        "Mittel",
        "Mittel",
        "Leicht",
        "Mittel",
        "Leicht",
        "Leicht"
    ],
    "Dauer": [
        "40 Minuten",
        "25 Minuten",
        "30 Minuten",
        "35 Minuten",
        "45 Minuten",
        "15 Minuten"
    ],
    "Anleitung": [
        "1. Die Auberginen längs halbieren und das Fruchtfleisch vorsichtig aushöhlen. Das Fruchtfleisch klein schneiden und beiseite legen. Die Auberginenhälften mit Olivenöl einreiben und im vorgeheizten Ofen bei 200°C etwa 20 Minuten backen, bis sie weich sind. 2. Während die Auberginen backen, Quinoa nach Packungsanleitung kochen. 3. Das vorbereitete Auberginenfruchtfleisch in einer Pfanne anbraten, mit gekochtem Quinoa mischen und mit Salz und Pfeffer würzen. 4. Die Quinoa-Mischung in die gebackenen Auberginenhälften füllen und mit Feta bestreuen. 5. Die gefüllten Auberginen zurück in den Ofen geben und weitere 10 Minuten backen, bis der Feta goldbraun ist. 6. Mit frischen Kräutern garnieren und servieren.",
        "1. Den Lachs mit Zitronensaft beträufeln und mit gehacktem Knoblauch, gehackter Petersilie, Salz und Pfeffer würzen. 2. Eine Grillpfanne mit Olivenöl erhitzen und den Lachs darin von beiden Seiten etwa 3-4 Minuten grillen, bis er durchgegart ist. 3. Für die Zitronen-Kräuter-Sauce Zitronensaft, gehackte Petersilie und Olivenöl verrühren und mit Salz und Pfeffer abschmecken. 4. Den gegrillten Lachs mit der Sauce beträufeln und servieren.",
        "1. Gemüse (z.B. Karotten, Zucchini, Kichererbsen) in einer Pfanne anbraten. 2. Kokosmilch und Currypaste hinzufügen und köcheln lassen, bis das Gemüse weich ist. 3. Mit Reis servieren und nach Belieben mit frischen Kräutern garnieren.",
        "1. Paprika halbieren und entkernen. 2. Couscous nach Packungsanleitung kochen. 3. Zwiebel und Knoblauch fein hacken und in Olivenöl anbraten. 4. Tomaten und Feta würfeln und mit dem gekochten Couscous vermischen. 5. Die Paprikahälften mit der Couscous-Feta-Mischung füllen und im Ofen bei 180°C etwa 20 Minuten backen.",
        "1. Zucchini, Aubergine, Paprika, Tomaten und Zwiebeln in Scheiben schneiden. 2. Die Gemüsescheiben in einer Auflaufform schichten und mit einer Mischung aus Olivenöl, gehacktem Knoblauch, Salz, Pfeffer und italienischen Kräutern würzen. 3. Die Ratatouille im vorgeheizten Ofen bei 180°C etwa 30-35 Minuten backen, bis das Gemüse weich ist. 4. Mit frischen Kräutern garnieren und servieren.",
        "1. Eier in einer Schüssel verquirlen und mit Salz und Pfeffer würzen. 2. Spinat waschen und grob hacken. 3. Etwas Butter in einer Pfanne erhitzen und die verquirlten Eier hinzufügen. 4. Den Spinat auf die Eier geben und leicht andrücken. 5. Den Feta darüber bröseln. 6. Das Omelett vorsichtig wenden und von beiden Seiten goldbraun braten. 7. Auf einem Teller servieren und nach Belieben mit frischen Kräutern garnieren."
    ]
}

# DataFrame für Rezepte erstellen
recipes_df = pd.DataFrame(recipes_data)

# Seitentitel festlegen
st.title("Willkommen bei Fit & Fresh: Gesunde Rezepte für Studenten")
st.subheader("Entdecken Sie eine Welt voller gesunder und schmackhafter Gerichte!")

# Rezeptauswahl
selected_recipe = st.selectbox("Wähle ein Rezept aus:", recipes_df["Gericht"])

# Informationen zum ausgewählten Rezept anzeigen
st.subheader(f"Rezept für {selected_recipe}:")
selected_recipe_info = recipes_df[recipes_df["Gericht"] == selected_recipe].iloc[0]
st.markdown(f"<div style='font-size: 18px'><b>Zutaten:</b> {selected_recipe_info['Zutaten']}</div>", unsafe_allow_html=True)
st.markdown(f"<div style='font-size: 18px'><b>Schwierigkeitsgrad:</b> {selected_recipe_info['Schwierigkeitsgrad']}</div>", unsafe_allow_html=True)
st.markdown(f"<div style='font-size: 18px'><b>Dauer:</b> {selected_recipe_info['Dauer']}</div>", unsafe_allow_html=True)
st.markdown(f"<div style='font-size: 18px'><b>Anleitung:</b><br>{selected_recipe_info['Anleitung']}</div>", unsafe_allow_html=True)
