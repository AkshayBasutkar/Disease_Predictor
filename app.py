import streamlit as st

st.title("🩺 Disease Prediction & Diet Recommendations")

st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Go to", ["Disease Predictor", "Diet Recommendations"])

if page == "Disease Predictor":
    # Import and run the disease predictor page code here
    import pages.disease_predictor as predictor
    predictor.app()

elif page == "Diet Recommendations":
    # Import and run the diet recommendations page code here
    import pages.diet_recommendations as diet_page
    diet_page.app()
