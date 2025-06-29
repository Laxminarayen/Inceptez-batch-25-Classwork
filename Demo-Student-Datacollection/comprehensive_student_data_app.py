import streamlit as st
import pandas as pd
import plotly.express as px
import os
from wordcloud import WordCloud
import matplotlib.pyplot as plt

st.set_page_config(page_title="Comprehensive Student Data Collector", layout="wide")

EXCEL_FILE = "comprehensive_student_data.xlsx"
COLUMNS = [
    "Name", "Age", "Mobile", "Email", "Educational Background",
    "Years of Experience", "Coding Exposure", "CS Exposure", "Expectations"
]

# Helper: Load data from Excel
def load_data():
    if os.path.exists(EXCEL_FILE):
        return pd.read_excel(EXCEL_FILE)
    else:
        return pd.DataFrame(columns=COLUMNS)

# Helper: Append a row to Excel
def append_data(row):
    df = load_data()
    df = pd.concat([df, pd.DataFrame([row])], ignore_index=True)
    df.to_excel(EXCEL_FILE, index=False)

# Load data for display
data = load_data()

# Role selection via URL query parameter
query_params = st.experimental_get_query_params()
role = query_params.get("role", [None])[0]

if not role:
    st.title("Comprehensive Student Data Collection")
    st.markdown(
        """
        ## Welcome!
        Please select your role:
        - [Teacher View (Visualizations Only)](?role=teacher)
        - [Student View (Submit Responses)](?role=student)
        """
    )
    st.stop()

if role == "student":
    st.title("Student Data Submission Form")
    with st.form("student_data_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Name", max_chars=50)
            age = st.number_input("Age", min_value=10, max_value=100, step=1)
            mobile = st.text_input("Mobile Number", max_chars=15)
            email = st.text_input("Email", max_chars=100)
            edu_bg = st.selectbox(
                "Educational Background",
                ["Engineering", "Science", "Arts", "Commerce", "Other"]
            )
        with col2:
            years_exp = st.number_input("Years of Experience", min_value=0, max_value=50, step=1)
            coding_exp = st.selectbox(
                "Coding Exposure",
                ["None", "Beginner", "Intermediate", "Advanced"]
            )
            cs_exp = st.selectbox(
                "Computer Science Exposure",
                ["None", "Basic Concepts", "Some Courses", "Extensive"]
            )
            expectations = st.text_area("What are your expectations from this class?", max_chars=500)
        submitted = st.form_submit_button("Submit Response")

        if submitted:
            if not name.strip():
                st.warning("Please enter your name.")
            elif not mobile.strip().isdigit() or len(mobile.strip()) < 8:
                st.warning("Please enter a valid mobile number.")
            elif "@" not in email or "." not in email:
                st.warning("Please enter a valid email address.")
            elif not expectations.strip():
                st.warning("Please share your expectations from the class.")
            else:
                new_row = {
                    "Name": name.strip(),
                    "Age": int(age),
                    "Mobile": mobile.strip(),
                    "Email": email.strip(),
                    "Educational Background": edu_bg,
                    "Years of Experience": int(years_exp),
                    "Coding Exposure": coding_exp,
                    "CS Exposure": cs_exp,
                    "Expectations": expectations.strip()
                }
                append_data(new_row)
                st.success("Response submitted!")

elif role == "teacher":
    # Teacher dashboard (no auto-refresh)
    st.title("Teacher Dashboard: Live Class Insights")
    st.markdown(
        """
        Share this link with students for submitting responses:  
        [Student Link](?role=student)
        """
    )
    data = load_data()
    st.markdown("---")
    if data.empty:
        st.info("No responses yet. Ask students to fill out the form!")
    else:
        col1, col2 = st.columns(2)
        # Bar chart: Educational Background
        with col1:
            edu_counts = data["Educational Background"].value_counts().reset_index()
            edu_counts.columns = ["Educational Background", "Count"]
            fig1 = px.bar(
                edu_counts,
                x="Educational Background",
                y="Count",
                labels={"Educational Background": "Educational Background", "Count": "Count"},
                title="Educational Background Distribution",
                color="Educational Background",
                color_discrete_sequence=px.colors.qualitative.Pastel
            )
            st.plotly_chart(fig1, use_container_width=True)
        # Histogram: Years of Experience
        with col2:
            fig2 = px.histogram(
                data,
                x="Years of Experience",
                nbins=10,
                title="Years of Experience Distribution",
                color_discrete_sequence=px.colors.sequential.RdBu
            )
            st.plotly_chart(fig2, use_container_width=True)
        col3, col4 = st.columns(2)
        # Bar chart: Coding Exposure
        with col3:
            code_counts = data["Coding Exposure"].value_counts().reset_index()
            code_counts.columns = ["Coding Exposure", "Count"]
            fig3 = px.bar(
                code_counts,
                x="Coding Exposure",
                y="Count",
                labels={"Coding Exposure": "Coding Exposure", "Count": "Count"},
                title="Coding Exposure Distribution",
                color="Coding Exposure",
                color_discrete_sequence=px.colors.qualitative.Set2
            )
            st.plotly_chart(fig3, use_container_width=True)
        # Bar chart: CS Exposure
        with col4:
            cs_counts = data["CS Exposure"].value_counts().reset_index()
            cs_counts.columns = ["CS Exposure", "Count"]
            fig4 = px.bar(
                cs_counts,
                x="CS Exposure",
                y="Count",
                labels={"CS Exposure": "CS Exposure", "Count": "Count"},
                title="Computer Science Exposure Distribution",
                color="CS Exposure",
                color_discrete_sequence=px.colors.qualitative.Set3
            )
            st.plotly_chart(fig4, use_container_width=True)
        # Word Cloud: Expectations
        st.markdown("### Expectations from the Class (Word Cloud)")
        all_expectations = " ".join(data["Expectations"].dropna().astype(str))
        if all_expectations.strip():
            wordcloud = WordCloud(width=800, height=300, background_color="white").generate(all_expectations)
            fig, ax = plt.subplots(figsize=(10, 4))
            ax.imshow(wordcloud, interpolation="bilinear")
            ax.axis("off")
            st.pyplot(fig)
        else:
            st.info("No expectations submitted yet.")
        # (Raw data table removed as per request)