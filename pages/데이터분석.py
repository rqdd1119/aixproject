import streamlit as st
import pandas as pd
import plotly.express as px

# Set page configuration
st.set_page_config(page_title="Student Grades Dashboard", layout="wide")

# Title and description
st.title("Student Grades Visualization")
st.markdown("This dashboard displays student grades across different subjects using Plotly Express.")

# Create DataFrame from the provided data
data = {
    'name': ['lee', 'park', 'kim'],
    'grade': [2, 2, 2],
    'number': [1, 2, 3],
    'kor': [90, 88, 99],
    'eng': [91, 89, 99],
    'math': [81, 77, 99],
    'info': [100, 100, 100]
}
df = pd.DataFrame(data)

# Display the raw data
st.subheader("Student Grades Data")
st.dataframe(df)

# Create a bar chart for grades comparison
st.subheader("Grades Comparison by Student")
fig = px.bar(
    df,
    x='name',
    y=['kor', 'eng', 'math', 'info'],
    barmode='group',
    title="Student Grades by Subject",
    labels={'name': 'Student Name', 'value': 'Score', 'variable': 'Subject'},
    height=500
)
fig.update_layout(
    xaxis_title="Student Name",
    yaxis_title="Score",
    legend_title="Subject",
    template="plotly_white"
)
st.plotly_chart(fig, use_container_width=True)

# Create individual subject bar charts
subjects = ['kor', 'eng', 'math', 'info']
st.subheader("Individual Subject Performance")
for subject in subjects:
    fig_subject = px.bar(
        df,
        x='name',
        y=subject,
        title=f"{subject.upper()} Scores",
        labels={'name': 'Student Name', subject: 'Score'},
        height=400,
        color='name'
    )
    fig_subject.update_layout(
        xaxis_title="Student Name",
        yaxis_title="Score",
        showlegend=False,
        template="plotly_white"
    )
    st.plotly_chart(fig_subject, use_container_width=True)

# Add some basic statistics
st.subheader("Basic Statistics")
st.write(df[['kor', 'eng', 'math', 'info']].describe())