import streamlit as st
st.set_page_config(page_title="Disease Predictor & Diet App", 
                   layout="centered",
                  initial_sidebar_state="expanded") 
st.title("🩺 Disease Prediction & Diet Recommendations")

st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Go to", ["Disease Predictor", "Diet Recommendations", "Medicine Recommender"])

if page == "Disease Predictor":
    # Import and run the disease predictor page code here
    import pages.Disease_Predictor as predictor
    predictor.app()

elif page == "Diet Recommendations":
    # Import and run the diet recommendations page code here
    import pages.Diet_Recommendations as diet_page
    diet_page.app()

elif page == "Medicine Recommender":
    # Import and run the diet recommendations page code here
    import pages.med as med_page
    med_page.app()
