import streamlit as st
from github_contents import GithubContents
import pandas as pd
import random 

DATA_FILE = "Rezepte.csv"

def init_github():
    if 'github' not in st.session_state:
        st.session_state.github = GithubContents(
            st.secrets["github"]["owner"],
            st.secrets["github"]["repo"],
            st.secrets["github"]["token"])

# Funktion zum Laden der Rezeptdaten
def load_recipe_data():
    github = st.session_state.github
    return github.read_df(DATA_FILE)

# Funktion zum Speichern der Rezeptdaten
def save_recipe_data(recipe_data):
    github = st.session_state.github
    github.write_df(DATA_FILE, recipe_data, "Update recipe data")

# Funktion zum Löschen eines Rezepts
def delete_recipes(recipes_to_delete, recipe_data):
    if recipes_to_delete:
        recipe_data = recipe_data[~recipe_data["Gericht"].isin(recipes_to_delete)]
        save_recipe_data(recipe_data)
        st.success("Das Rezept wurde erfolgreich gelöscht!")

def main():
    init_github()

    # Load the recipe data
    recipe_data = load_recipe_data()

    # Check if user has entered a username
    if 'username' not in st.session_state:
        st.title("🍳 Willkommen bei FoodisGood")
        username = st.text_input("Bitte gib deinen Benutzernamen ein:")
        if username:
            st.session_state.username = username
            st.success(f"Willkommen bei FoodisGood, {username}!")

    # Show main app content if username is entered
    if 'username' in st.session_state and st.session_state.username:
        st.title(f"Willkommen bei FoodisGood, {st.session_state.username}!")

        # Tabs für Rezeptverwaltung und Nahrungsergänzungsmittel
        tab_options = ["Über die App", "Rezepte anzeigen", "Rezepte hinzufügen", "Rezepte löschen"]
        selected_tab = st.sidebar.radio("Optionen:", tab_options)

        if selected_tab == "Rezepte anzeigen":
            # Rezeptsuche nach Frühstücksrezepten
            search_term = st.text_input("Suche nach einem Frühstücksrezept:")
            if search_term:
                filtered_recipes = recipe_data[recipe_data["Gericht"].str.contains(search_term, case=False)]
            else:
                filtered_recipes = recipe_data

            # Dropdown-Menü für Rezeptauswahl
            selected_recipe = st.selectbox("Wähle ein Frühstücksrezept aus:", filtered_recipes["Gericht"])

            # Informationen zum ausgewählten Rezept anzeigen
            st.subheader(f"Rezept für {selected_recipe}:")
            selected_recipe_info = filtered_recipes[filtered_recipes["Gericht"] == selected_recipe].iloc[0]
            
            # Anzeige der Rezeptdetails
            st.markdown(f"**Zutaten:** {selected_recipe_info['Zutaten']}")
            st.markdown(f"**Anleitung:** {selected_recipe_info['Anleitung']}")
            st.markdown(f"**Schwierigkeitsgrad:** {selected_recipe_info['Schwierigkeitsgrad']}")
            st.markdown(f"**Dauer:** {selected_recipe_info['Dauer']}")

            # Bild des ausgewählten Rezepts anzeigen
            st.image(selected_recipe_info["Bild"], caption=selected_recipe_info["Gericht"], use_column_width=True)

            # Einkaufsliste direkt unter den Zutaten anzeigen
            st.subheader("Einkaufsliste:")
            ingredients_list = selected_recipe_info["Zutaten"].split(", ")
            for ingredient in ingredients_list:
                # Checkbox für jedes Zutat hinzufügen
                buy = st.checkbox(ingredient)

            # Frühstücksüberraschung mit Emojis
            emoji_surprises = [
                "🍓 Beeren sind voller Antioxidantien und passen perfekt zu Müsli und Joghurt!",
                "🥑 Avocados sind reich an gesunden Fetten und machen jedes Frühstück cremig und sättigend!",
                "🥚 Eier sind eine hervorragende Proteinquelle und können vielseitig in Frühstücksgerichten verwendet werden!",
                "🥛 Mandelmilch ist eine köstliche pflanzliche Milchalternative für Smoothies und Müsli!",
                "🍌 Bananen sind reich an Kalium und ein perfekter natürlicher Süßstoff für Smoothies und Oatmeal!",
                "🥞 Pancakes sind ein klassisches Frühstücksgericht und lassen sich vielseitig kombinieren!",
                "🥣 Chia-Pudding ist eine gesunde und sättigende Option für einen guten Start in den Tag!",
                "🍣 Lachs ist reich an Omega-3-Fettsäuren und passt perfekt zu einem herzhaften Frühstück!",
                "🍇 Acai-Bowls sind eine leckere Möglichkeit, viele Vitamine und Antioxidantien zu genießen!",
                "🍏 Äpfel sind gesund, knackig und eine perfekte Ergänzung für jedes Müsli oder Joghurt!",
                "🍳 Rührei mit Räucherlachs ist ein klassisches, proteinreiches Frühstück für Feinschmecker!",
                "🥯 Bagels sind eine köstliche Basis für herzhafte Frühstückssandwiches!",
                "🥔 Rösti ist eine knusprige Kartoffelbeilage und perfekt für ein herzhaftes Frühstück!",
                "🌱 Tofu-Scramble ist eine vegane Alternative zu Rührei und reich an pflanzlichem Protein!"
            ]

            # Button für eine zufällige Emoji-Überraschung zum Thema Frühstück
            if st.button("Klicke hier für eine Frühstücksüberraschung!"):
                random_surprise = random.choice(emoji_surprises)
                st.write("Klicke erneut für eine andere Überraschung ;)")
                st.write(random_surprise)

        elif selected_tab == "Rezepte hinzufügen":
            # Bereich zum Hinzufügen neuer Rezepte
            st.subheader("Füge dein eigenes Rezept hinzu:")
            st.write("Fülle bitte alle Felder aus, um ein neues Rezept hinzuzufügen, einschließlich Bild-URL.")
            new_recipe_name = st.text_input("Name des Rezepts:")
            new_recipe_ingredients = st.text_area("Zutaten (getrennt durch Komma):")
            new_recipe_instructions = st.text_area("Anleitung:")
            new_recipe_difficulty = st.selectbox("Schwierigkeitsgrad:", ["Leicht", "Mittel", "Schwer"])
            new_recipe_duration = st.text_input("Dauer (z.B. 30 Minuten):")
            new_recipe_image_url = st.text_input("Bild-URL:")

            if st.button("Rezept hinzufügen"):
                if new_recipe_name and new_recipe_ingredients and new_recipe_instructions and new_recipe_difficulty and new_recipe_duration and new_recipe_image_url:
                    new_recipe_data = {
                        "Gericht": new_recipe_name,
                        "Zutaten": new_recipe_ingredients,
                        "Anleitung": new_recipe_instructions,
                        "Schwierigkeitsgrad": new_recipe_difficulty,
                        "Dauer": new_recipe_duration,
                        "Bild": new_recipe_image_url
                    }
                    # DataFrame für das neue Rezept erstellen
                    new_recipe_df = pd.DataFrame([new_recipe_data])
                    # Neues Rezept zur vorhandenen Rezeptdaten hinzufügen
                    recipe_data = pd.concat([recipe_data, new_recipe_df], ignore_index=True)
                    # Rezeptdaten speichern
                    save_recipe_data(recipe_data)
                    st.success("Das Rezept wurde erfolgreich hinzugefügt!")

        elif selected_tab == "Rezepte löschen":
            # Bereich zum Löschen von Rezepten
            st.subheader("Wähle Rezepte zum Löschen aus:")
            recipes_to_delete = st.multiselect("Rezepte:", list(recipe_data["Gericht"]))
            
            if st.button("Rezepte löschen"):
                delete_recipes(recipes_to_delete, recipe_data)

        elif selected_tab == "Über die App":
            st.markdown("""
            ## Über die FoodisGood App 🌟

            Die FoodisGood App bietet eine Vielzahl von Frühstücksrezepten, die dir helfen sollen, deinen Tag gesund und lecker zu beginnen. 
            Du kannst neue Rezepte hinzufügen, bestehende Rezepte anzeigen und sogar Rezepte löschen, die du nicht mehr benötigst.

            Die App enthält auch Informationen zu empfohlenen Nahrungsergänzungsmitteln, um deine Ernährung zu ergänzen.

            Genieße deine Mahlzeiten und viel Spaß beim Entdecken neuer Frühstücksideen!
            """)

        # Sidebar mit Nahrungsergänzungsmitteln
        st.sidebar.title("Nahrungsergänzungsmittel")
        st.sidebar.markdown("""
        - **Vitamin D:** Wichtig für die Knochengesundheit und das Immunsystem. Produktempfehlung: [Burgerstein Vitamin D3 600 IE](https://www.burgerstein.ch/de-DE/produkte/burgerstein-vitamin-d3-600-ie)
        - **Omega-3-Fettsäuren:** Unterstützen die Herzgesundheit und fördern die Gehirnfunktion. Produktempfehlung: [Burgerstein Omega-3 Liquid](https://www.burgerstein.ch/de-DE/produkte/burgerstein-omega-3-liquid)
        - **Probiotika:** Gut für die Darmgesundheit und die Verdauung. Produktempfehlung: [Burgerstein Biotics G](https://www.burgerstein.ch/de-DE/produkte/burgerstein-biotics-g)
        - **Magnesium:** Kann helfen, Muskelkrämpfe zu reduzieren und hilft bei Müdigkeit. Produktempfehlung: [Burgerstein Magnesiumvital Direct](https://www.burgerstein.ch/de-DE/produkte/burgerstein-magnesiumvital-direct)
        """)

        # Footer
        st.markdown("---")
        st.markdown("Erstellt von FoodisGood 🍳 Genieße deine Mahlzeiten und dein Studium! 😊")

if __name__ == "__main__":
    main()
