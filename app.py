import streamlit as st
st.set_page_config(page_title="Disease Predictor & Diet App", 
                   layout="centered",
                  initial_sidebar_state="expanded",
                menu_items={
                    'Get Help': 'https://www.extremelycoolapp.com/help',
                    'Report a bug': "https://www.extremelycoolapp.com/bug",
                    'About': "# This is a header. This is an *extremely* cool app!"
                }) 
st.title("🩺 Disease Prediction & Diet Recommendations")

st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Go to", ["Disease Predictor", "Diet Recommendations"])

if page == "Disease Predictor":
    # Import and run the disease predictor page code here
    import pages.Disease_Predictor as predictor
    predictor.app()

elif page == "Diet Recommendations":
    # Import and run the diet recommendations page code here
    import pages.Diet_Recommendations as diet_page
    diet_page.app()
