# importing important libraries
import mysql.connector
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Creating Python SQL connection
mydb = mysql.connector.connect(

    host='localhost',
    user='root',
    password='12345678',
    database='healthcare',
    autocommit=True
)
mycursor = mydb.cursor()

# Streamlit UI


# Side bar with case study selection
case_study = st.sidebar.selectbox(
    "Select Case study", ["Home", "Trends in Admissions Over Time", "Diagnosis Frequency Analysis", "Bed Occupancy Analysis","Length of Stay Distribution",
    "Seasonal Admission Patterns","Seasonal Disease Occurence","Doctor Patient Distribution","Patient Feedback Analysis",
    "Length of Stay and Bed Utilization Analysis","Average Billing vs. Insurance Coverage discepency by Diagnosis","Test and Diagnosis Relation",
    "Follow-Up Appointments and Patient Outcomes","Most common diseases with avg billing amount","Bed Occupancy Trends ans Peak Admission Periods",
    "Monitor Patient Recovery and Treatment Outcomes","Impact of Tests on Total Billing Amount"]
)

# Home Page content
if case_study == "Home":
    st.title("Healthcare Data Application")
    st.header("Welcome to the Healthcare Data Dashboard")
    st.write("""
    Here, you can explore detailed insights on various healthcare metrics such as 
    patient admissions, billing trends, diagnosis patterns, and much more. Interactive visualizations allow you to uncover 
    hidden trends, monitor critical metrics, and assess areas for improvement. Use the sidebar to dive into different 
    case studies and start making data-driven decisions today.
""")
    # Adding some spacing before the image to ensure it appears below the text
    st.markdown("<br>", unsafe_allow_html=True)  # Adding some space before the image

    st.markdown("""
            <style>
                img {
                     width : 800px;
                     height : 400px;
                }
            </style>
    """,unsafe_allow_html=True)

   


# Case study 1 : Trends in Admissions over time
elif case_study == "Trends in Admissions Over Time":
    st.header("Trends in Patients Admissions over time")
    st.write("This graph displays monthly patient admissions, helping to identify patterns and seasonality. Analyzing these trends aids in resource planning, staffing, and forecasting peak periods.")
    
    # SQL query to get trends in monthly admissions
    def get_admissions_trends():
        query = '''
            SELECT 
                YEAR(Admit_Date) AS Admission_Year,
                MONTH(Admit_Date) AS Admission_Month, 
                COUNT(*) AS Monthly_Admission_Count
            FROM healthcare_data
            GROUP BY YEAR(Admit_Date), MONTH(Admit_Date)
            ORDER BY Admission_Year, Admission_Month;
        '''

        # Execute the query and get the results
        mycursor.execute(query)
        result = mycursor.fetchall()
        df = pd.DataFrame(result, columns=['Admission_Year', 'Admission_Month', 'Monthly_Admission_Count'])
        return df

    # Fetch the data
    df = get_admissions_trends()

    # Plot the data
    
    # Create a new column 'Year-Month' for better readability on the x-axis
    df['Year-Month'] = df['Admission_Year'].astype(str) + '-' + df['Admission_Month'].astype(str)

    # Plot the data with Plotly
    fig = px.line(df, x='Year-Month', y='Monthly_Admission_Count',
                  title='Monthly Patient Admissions Over Time',
                  labels={'Year-Month': 'Year-Month', 'Monthly_Admission_Count': 'Admission Count'},
                  markers=True)
    
    # Update the color of the line trace to green
    fig.update_traces(line=dict(color='darkred'))
    
    # Update axis labels and numbers' font size and color
    fig.update_layout(
        xaxis = dict( 
            title = 'Year-Month',
            title_font = dict(size = 16, color = 'darkblue'),
            tickfont = dict(size = 16,color = 'darkblue'),
            tickangle = -30
        ),
        yaxis = dict(
            title = 'Monthly_Admission_Count',
            title_font = dict(size = 16, color = 'darkblue' ),
            tickfont = dict(size = 16, color = 'darkblue')
        ),
        title_font = dict(size = 20, color = 'darkgreen')
        )

    # Show the interactive plot in Streamlit
    st.plotly_chart(fig)

# Case study 2 : Diagnosis Frequency Analysis
elif case_study == "Diagnosis Frequency Analysis":
    st.header("Diagnosis Frequency Analysis")
    st.write("This chart shows the top 5 most common diagnosis. It helps identify the most common health conditions, useful for healthcare planning and resource allocation.")
    

    # SQL query to get top 5 most common diagnosis
    def get_diagnosis_frequency():
        query2 = '''
            SELECT Diagnosis, COUNT(*) AS Diagnosis_Count
            FROM healthcare_data
            GROUP BY Diagnosis
            ORDER BY Diagnosis_Count DESC
            LIMIT 5;
        '''
        
        # Execute the query and get the results
        mycursor.execute(query2)
        result2 = mycursor.fetchall()
        df2 = pd.DataFrame(result2, columns=['Diagnosis', 'Diagnosis_Count'])
        return df2

    # Fetch the data
    df2 = get_diagnosis_frequency()

    # Plot the data as a bar chart
    # Custom color list
    custom_colors = ['#d62728', '#1f77b4', '#bcbd22', '#ff7f0e', '#9467bd']

    # Create the bar chart with custom colors
    fig = px.bar(df2,
                 x='Diagnosis',  # Diagnosis on the x-axis
                 y='Diagnosis_Count',  # Frequency of each diagnosis on the y-axis
                 color='Diagnosis',  # Color the bars by Diagnosis
                 title='Top 5 Most Common Diagnosis',
                 labels={'Diagnosis': 'Diagnosis', 'Diagnosis_Count': 'Frequency'},
                 color_discrete_sequence=custom_colors)  # Directly assign colors

    # Update axis labels and numbers font size and color
    fig.update_layout(
        xaxis = dict( 
            title = 'Diagnosis',
            title_font = dict(size = 16, color = 'darkblue'),
            tickfont = dict(size = 16,color = 'darkblue'),
            #tickangle = 25
        ),
        yaxis = dict(
            title = 'Frequency',
            title_font = dict(size = 16, color = 'darkblue' ),
            tickfont = dict(size = 16, color = 'darkblue')
        ),
        title_font = dict(size = 20, color = '#8c564b')
        )

    # Show the plot in Streamlit
    st.plotly_chart(fig)


# Case Study 3: Bed Occupancy Analysis
elif case_study == "Bed Occupancy Analysis":
    st.header("Bed Occupancy Distribution Analysis")
    st.write("This chart illustrates the distribution of bed occupancy types, providing insights into hospital bed usage patterns for effective resource management and planning.")
    
    
    # SQL query to get the distribution of bed occupancy types
    def get_bed_occupancy_distribution():
        query3 = '''
                 SELECT Bed_Occupancy, COUNT(*) AS Occupancy_Count
                 FROM healthcare_data
                 GROUP BY Bed_Occupancy
                 ORDER BY Occupancy_Count DESC;
              '''
        
        # Execute the query and get the results
        mycursor.execute(query3)
        result3 = mycursor.fetchall()
        df3 = pd.DataFrame(result3, columns = ['Bed_Occupancy','Occupancy_Count'])
        return df3
        
    # Fetch the data
    df3 = get_bed_occupancy_distribution()


    # Create a donut chart using Plotly
    fig = px.pie(df3, 
             names='Bed_Occupancy',  # Bed Occupancy type for the segments
             values='Occupancy_Count',  # Frequency of each Bed Occupancy type
             title='Bed Occupancy Distribution',
             color='Bed_Occupancy',  # Color the segments by Bed Occupancy type
             color_discrete_map={'Private': 'firebrick', 'General': 'darkseagreen', 'ICU': 'darksalmon'},  # Custom color mapping
             hole=0.3)  # The 'hole' argument creates the donut chart shape

    # Update the traces to modify text information (percentage and label) and font size
    fig.update_traces(
        textinfo='percent',  # Display both percentage and label
        textfont=dict(size=20, color='black')  # Increase font size for percentages and labels
    )

    # Update layout to improve the presentation
    fig.update_layout(
        title_font=dict(size=20, color='#8c564b'),
        legend_title=dict(font=dict(size=16, color='darkblue')),
        showlegend=True
    )

    # Show the donut chart in Streamlit
    st.plotly_chart(fig)



    
# Case Study 4: Length of Stay Distribution
elif case_study == "Length of Stay Distribution":
    st.header("Length of Stay Distribution Analysis")
    st.write("This analysis shows the average and maximum length of stay for patients. It provides insights into patient stay durations, which can help optimize hospital resource allocation and improve care management.")
    

    # SQL query to get the average and maximum length of stay
    def get_length_of_stay():
        query4 = '''SELECT 
                AVG(DATEDIFF(Discharge_Date, Admit_Date)) AS Avg_Length_of_Stay,
                MAX(DATEDIFF(Discharge_Date, Admit_Date)) AS Max_Length_of_Stay
                FROM healthcare_data
            '''
        
        # Execute the query and get the results
        mycursor.execute(query4)
        result4 = mycursor.fetchall()
        df4 = pd.DataFrame(result4, columns=['Avg_Length_of_Stay', 'Max_Length_of_Stay'])
        return df4
    
    # Fetch the data
    df4 = get_length_of_stay()


     # Create a new DataFrame with 'Stay_Type' and 'Days' columns
    df_plot = pd.DataFrame({
        'Stay_Type': ['Average Length of Stay', 'Maximum Length of Stay'],
        'Days': [df4['Avg_Length_of_Stay'][0], df4['Max_Length_of_Stay'][0]]
    })

    # Create a bar chart using Plotly Express
    fig = px.bar(df_plot,
                 x='Stay_Type',  # Stay type is on the x-axis
                 y='Days',  # Length of stay is on the y-axis
                 color='Stay_Type',  # Color bars by Stay_Type
                 color_discrete_map={'Average Length of Stay': 'salmon', 'Maximum Length of Stay': 'lightgreen'},
                 labels={'Stay_Type': 'Stay Type', 'Days': 'Length of Stay (in Days)'},
                 title='Length of Stay Distribution')

    # Update axis labels and numbers font size and color
    fig.update_layout(
        xaxis = dict( 
            title = 'Stay Type',
            title_font = dict(size = 16, color = 'darkblue'),
            tickfont = dict(size = 16,color = 'darkblue'),
            #tickangle = 25
        ),
        yaxis = dict(
            title = 'Length of Stay (in Days)',
            title_font = dict(size = 16, color = 'darkblue' ),
            tickfont = dict(size = 16, color = 'darkblue')
        ),
        title_font = dict(size = 20, color = '#8c564b')
        )

    # Show the plot in Streamlit
    st.plotly_chart(fig)


# Case study 5: Seasonal Admission Patterns
elif case_study == "Seasonal Admission Patterns":
    st.header("Seasonal Admission Patterns")
    st.write("This analysis reveals seasonal trends in patient admissions by month, helping to understand hospital usage patterns and plan resource allocation for peak periods.")
    
    # SQL query to get admissions by month
    def get_seasonal_admissions():
        query5 = '''
             SELECT 
            MONTH(Admit_Date) AS Admission_Month,
            COUNT(*) AS Admission_Count
            FROM healthcare_data
            GROUP BY MONTH(Admit_Date)
            ORDER BY Admission_Count DESC;
        '''
        
        # Execute the query and get the results
        mycursor.execute(query5)
        result = mycursor.fetchall()
        df5 = pd.DataFrame(result, columns=['Admission_Month', 'Admission_Count'])
        return df5

    # Fetch the data
    df5 = get_seasonal_admissions()


    # Plot the data as an interactive bar chart using Plotly
    fig = px.bar(df5, 
                 x='Admission_Month', 
                 y='Admission_Count', 
                 labels={'Admission_Month': 'Month', 'Admission_Count': 'Admission Count'},
                 title='Seasonal Admission Patterns')

    # Customize hover data
    fig.update_traces(hovertemplate='Month: %{x}<br>Admissions: %{y}')

    # Update axis labels and numbers font size and color
    fig.update_layout(
        xaxis = dict( 
            title = 'Month',
            title_font = dict(size = 16, color = 'darkblue'),
            tickfont = dict(size = 16,color = 'darkblue'),
            #tickangle = 25
        ),
        yaxis = dict(
            title = 'Admission Count',
            title_font = dict(size = 16, color = 'darkblue' ),
            tickfont = dict(size = 16, color = 'darkblue')
        ),
        title_font = dict(size = 20, color = '#8c564b')
        )

    # Show the plot in Streamlit
    st.plotly_chart(fig)


# Case study 6 : Seasonal Disease Occurence

elif case_study == "Seasonal Disease Occurence":
    st.header("Seasonal Trends in Disease Occurence")
    st.write("This analysis identifies which diseases or diagnosis are more prevalent during different seasons. It helps healthcare providers understand seasonal patterns of diseases, enabling proactive measures to prevent outbreaks and improve patient care during high-risk periods.")
    


    # SQL query to get seasonal disease data
    def get_seasonal_disease_data():
        query6 = '''SELECT
               CASE
                   WHEN MONTH(Admit_Date) IN (12, 1, 2) THEN 'Winter'
                   WHEN MONTH(Admit_Date) IN (3, 4, 5) THEN 'Spring'
                   WHEN MONTH(Admit_Date) IN (6, 7, 8) THEN 'Summer'
                   ELSE 'Autumn'
                END AS Season,
                Diagnosis,
                COUNT(*) AS Disease_Count
                FROM healthcare_data
                GROUP BY Season, Diagnosis
                ORDER BY Disease_Count DESC
            '''

        # Execute the query
        mycursor.execute(query6)
        result6 = mycursor.fetchall()
        df6 = pd.DataFrame(result6, columns = ['Season','Diagnosis','Disease_Count'])
        return df6

    #Fetch the data
    df6 = get_seasonal_disease_data()


    # Stacked bar chart for seasonal disease occurrences
    fig = px.bar(df6,
             x='Diagnosis',
             y='Disease_Count',
             color='Season',
             title="Seasonal Disease Occurrence (Stacked)",
             labels={'Diagnosis': 'Disease', 'Disease_Count': 'Number of Occurrences'},
             color_discrete_map={"Winter": "#2F4F4F", "Spring": "#4682B4", "Summer": "#556B2F", "Autumn": "#B22222"},
             barmode='stack')  # Stacked bars

    # Update axis labels and numbers' font size and color
    fig.update_layout(
        xaxis = dict( 
            title = 'Disease',
            title_font = dict(size = 16, color = 'darkblue'),
            tickfont = dict(size = 16,color = 'darkblue'),
            #tickangle = 25
        ),
        yaxis = dict(
            title = 'Number of Occurences',
            title_font = dict(size = 16, color = 'darkblue' ),
            tickfont = dict(size = 16, color = 'darkblue')
        ),
        title_font = dict(size = 20, color = '#8c564b')
        )

    # Display the chart
    st.plotly_chart(fig)

   
# Case study 7: Doctor Patient Distribution

elif case_study == "Doctor Patient Distribution":
    st.header("Top Doctors by Number of Patients Treated")
    st.write("This chart shows the doctors who have treated the most patients. Understanding which doctors have the highest patient load can assist in effective resource planning and ensure that staffing is aligned with demand.")
    
    
    # SQL query to get the top doctors by number of patients treated
    def get_top_doctors():
        query7 = '''
            SELECT Doctor, COUNT(*) AS Patient_Count
            FROM healthcare_data
            GROUP BY Doctor
            ORDER BY Patient_Count DESC;
        '''
    
        # Execute the query and fetch the result
        mycursor.execute(query7)
        result = mycursor.fetchall()
    
        # Convert the result into a DataFrame
        df7 = pd.DataFrame(result, columns=['Doctor', 'Patient_Count'])
        return df7

    # Fetch the data
    df7 = get_top_doctors()

    # Sort the DataFrame by 'Patient_Count' in descending order
    df7 = df7.sort_values(by='Patient_Count', ascending=False)

  
    # Create a horizontal bar chart using Plotly with color scale
    fig = px.bar(df7, 
                 x='Patient_Count',  # Patient count on the x-axis
                 y='Doctor',         # Doctor names on the y-axis
                 orientation='h',    # Horizontal bar chart
                 title="Top Doctors by Number of Patients Treated",
                 color='Patient_Count',  # Color bars based on the patient count
                 color_continuous_scale='Viridis',  # Color scale for bars
                 labels={'Doctor': 'Doctor', 'Patient_Count': 'Number of Patients'})

    # Update layout to improve the presentation
    fig.update_layout(
        xaxis = dict( 
            title = 'Number of Patients',
            title_font = dict(size = 16, color = 'darkblue'),
            tickfont = dict(size = 16, color = 'darkblue')
        ),
        yaxis = dict(
            title = 'Doctor',
            title_font = dict(size = 16, color = 'darkblue' ),
            tickfont = dict(size = 16, color = 'darkblue')
        ),
        title_font = dict(size = 20, color = '#8c564b'),
        showlegend=False  # Optionally, remove the color scale legend for simplicity
    )

    # Show the horizontal bar chart
    st.plotly_chart(fig)


# Case study 8: 
elif case_study == "Patient Feedback Analysis":
    st.header("Patient Feedback Analysis per Doctor")
    st.write("This chart analyzes the average patient feedback for each doctor. By identifying areas with lower satisfaction scores, healthcare providers can focus on improving patient care, communication, and facilities to enhance overall patient experience.")


    # SQL query to get average feedback for each doctor
    def get_patient_feedback():
        query8 = '''
            SELECT 
                Doctor, 
                AVG(Feedback) AS Avg_Feedback
            FROM healthcare_data
            GROUP BY Doctor
            ORDER BY Avg_Feedback DESC;
        '''
        mycursor.execute(query8)
        result = mycursor.fetchall()
        df8 = pd.DataFrame(result, columns=['Doctor', 'Avg_Feedback'])
        return df8

    # Fetch the data
    df8 = get_patient_feedback()


    # Plot the data as a bar chart using Plotly
    fig = px.bar(df8,
             x='Doctor',
             y='Avg_Feedback',
             labels={'Doctor': 'Doctor', 'Avg_Feedback': 'Average Feedback'},
             title='Average Patient Feedback per Doctor',
             color='Avg_Feedback',
             color_continuous_scale='cividis')

    # Update axis labels and numbers' font size and color
    fig.update_layout(
        xaxis = dict( 
            title = 'Doctor',
            title_font = dict(size = 16, color = 'darkblue'),
            tickfont = dict(size = 16,color = 'darkblue'),
            tickangle = -25
        ),
        yaxis = dict(
            title = 'Average Feedback',
            title_font = dict(size = 16, color = 'darkblue' ),
            tickfont = dict(size = 16, color = 'darkblue')
        ),
        title_font = dict(size = 20, color = '#8c564b')
        )


    # Show the chart in Streamlit
    st.plotly_chart(fig)

# Case study 9 : Length of Stay and Bed Utilization Analysis
elif case_study == "Length of Stay and Bed Utilization Analysis":
    st.header("Length of Stay and Bed Utilization Analysis")
    st.write("This analysis calculates the average length of stay for patients by bed occupancy type, helping to identify which bed types are occupied longer. This insight aids in optimizing bed management and resource allocation.")
    
    
    # SQL query to get the average length of stay by bed occupancy type
    def get_length_of_stay_bed_utilization():
        query9 = '''
            SELECT 
                Bed_Occupancy,
                AVG(DATEDIFF(Discharge_Date, Admit_Date)) AS Avg_Length_of_Stay
            FROM healthcare_data
            WHERE Discharge_Date IS NOT NULL
            GROUP BY Bed_Occupancy
            ORDER BY Avg_Length_of_Stay DESC;
        '''

        # Execute the query and fetch results
        mycursor.execute(query9)
        result = mycursor.fetchall()

        # Convert the result into a pandas DataFrame
        df9 = pd.DataFrame(result, columns=['Bed_Occupancy', 'Avg_Length_of_Stay'])
        return df9

    # Fetch the data
    df9 = get_length_of_stay_bed_utilization()


    # Plot the data using Plotly
    fig = px.pie(df9,
             names='Bed_Occupancy',  # Bed Occupancy type
             values='Avg_Length_of_Stay',  # Average Length of Stay
             title='Proportional Distribution of Length of Stay by Bed Occupancy Type'
             )
    # Update title font size and color
    fig.update_layout(
    title_font=dict(size=20, color='#8c564b'))  # Set title font size and color
    st.plotly_chart(fig)


# Case study 10 : Average Billing vs. Insurance Coverage discepency by Diagnosis
elif case_study == "Average Billing vs. Insurance Coverage discepency by Diagnosis":
    st.header("Average Billing vs. Insurance Coverage Discrepency by Diagnosis")
    st.write("This analysis compares the average billing and insurance coverage by diagnosis, highlighting discrepancies. It helps in identifying areas where insurance coverage is insufficient compared to billing amounts, aiding in better resource management and negotiation strategies.")
    
    
    # SQL query to get the data for the case study
    def get_billing_vs_insurance_discrepancy():
        query_discrepancy = '''
        SELECT
            Diagnosis,
            AVG(`Billing Amount`) AS Avg_Billing_Amount,
            AVG(`Health Insurance Amount`) AS Avg_Insurance_Coverage,
            AVG(`Billing Amount`) - AVG(`Health Insurance Amount`) AS Avg_Discrepancy,
            (AVG(`Billing Amount`) - AVG(`Health Insurance Amount`)) / AVG(`Billing Amount`) * 100 AS Discrepancy_Percentage
        FROM healthcare_data
        GROUP BY Diagnosis
        ORDER BY Discrepancy_Percentage DESC;
        '''
        
        # Execute the query and fetch results
        mycursor.execute(query_discrepancy)
        result = mycursor.fetchall()

        # Convert the data to a DataFrame
        df10 = pd.DataFrame(result, columns=['Diagnosis', 'Avg_Billing_Amount', 'Avg_Insurance_Coverage', 'Avg_Discrepancy', 'Discrepancy_Percentage'])
        return df10

    # Fetch the data
    df10 = get_billing_vs_insurance_discrepancy()


    # Scatter Plot for Billing Amount vs. Insurance Coverage
    fig_scatter = px.scatter(df10, 
                             x='Avg_Billing_Amount', 
                             y='Avg_Insurance_Coverage',
                             color='Discrepancy_Percentage', 
                             size='Discrepancy_Percentage',  # Adjust the size of the points based on the discrepancy percentage
                             title="Billing Amount vs. Insurance Coverage by Diagnosis",
                             labels={'Avg_Billing_Amount': 'Billing Amount', 'Avg_Insurance_Coverage': 'Insurance Coverage'},
                             color_continuous_scale='viridis',  # Color by discrepancy percentage
                             hover_name='Diagnosis',  # Hover text showing the Diagnosis
                             height=600)

    # Update axis labels and numbers' font size and color
    fig_scatter.update_layout(
        xaxis = dict( 
            title = 'Billing Amount',
            title_font = dict(size = 16, color = 'darkblue'),
            tickfont = dict(size = 16,color = 'darkblue'),
            #tickangle = -25
        ),
        yaxis = dict(
            title = 'Insurance Coverage',
            title_font = dict(size = 16, color = 'darkblue' ),
            tickfont = dict(size = 16, color = 'darkblue')
        ),
        title_font = dict(size = 20, color = '#8c564b')
        )

    # Show the scatter plot
    st.plotly_chart(fig_scatter)

    # Bubble Chart for Discrepancy Percentage by Diagnosis
    fig_bubble = px.scatter(df10, 
                            x='Diagnosis', 
                            y='Discrepancy_Percentage',
                            size='Discrepancy_Percentage',  # Bubble size based on discrepancy
                            color='Discrepancy_Percentage',  # Color by discrepancy percentage
                            title="Discrepancy Percentage by Diagnosis",
                            labels={'Discrepancy_Percentage': 'Discrepancy Percentage'},
                            color_continuous_scale='viridis', 
                            hover_name='Diagnosis',  # Hover text showing the Diagnosis
                            height=600)
    
    # Update axis labels and numbers' font size and color
    fig_bubble.update_layout(
        xaxis = dict( 
            title = 'Diagnosis',
            title_font = dict(size = 16, color = 'darkblue'),
            tickfont = dict(size = 16,color = 'darkblue'),
            tickangle = -90
        ),
        yaxis = dict(
            title = 'Discepency Percentage',
            title_font = dict(size = 16, color = 'darkblue' ),
            tickfont = dict(size = 16, color = 'darkblue')
        ),
        title_font = dict(size = 20, color = '#8c564b')
        )


    # Show the bubble chart
    st.plotly_chart(fig_bubble)


# Case study 11 : Test and Diagnosis Relation
elif case_study == "Test and Diagnosis Relation":
    st.header("Relation Between Test and Diagnosis")
    st.write("""
              This analysis identifies the most commonly ordered tests for each diagnosis, helping optimize test selection and improve patient care. It streamlines workflows and reduces unnecessary testing.
            """)


    # sql query to fetch the Test and Diagnosis Relation data
    def get_test_diagnosis_relation():
        query11 = '''SELECT Diagnosis, Test, COUNT(*) AS Test_Count
                     FROM healthcare_data
                     GROUP BY Diagnosis, Test
                     ORDER BY Test_Count DESC
                '''

        # Execute the query and get results
        mycursor.execute(query11)
        result11 =  mycursor.fetchall()

        # Convert the results into a pandas dataframe
        df11 = pd.DataFrame(result11,columns = ['Diagnosis','Test','Test_Count'])
        return df11
        
    # Fetch the data
    df11 = get_test_diagnosis_relation()


    # Stacked Bar Chart to represent Diagnosis, Test, and Test Count on a single graph
    
    fig_stacked_bar = px.bar(df11,
                             x = 'Diagnosis',
                             y = 'Test_Count',
                             color = 'Test',
                             title="Test Frequency by Diagnosis and Test Type",
                             labels = {'Test Count':'Test Frequency','Diagnosis':'Diagnosis'},
                             barmode = 'stack',   # stacking the bars
                             height = 600 )
   
    fig_stacked_bar.update_layout(
    xaxis=dict(
        title='Diagnosis',
        title_font=dict(size=16, color='darkblue'),
        tickfont=dict(size=16, color='darkblue'),
        tickangle=-45
    ),
    yaxis=dict(
        title='Test Frequency',
        title_font=dict(size=16, color='darkblue'),
        tickfont=dict(size=16, color='darkblue')
    ),
    title_font=dict(size=20, color='#8c564b'),
    template='plotly_dark',  # Apply template here
    showlegend=True  # Place showlegend at the top level, not inside xaxis or yaxis
)
    
    # Show the figure
    st.plotly_chart(fig_stacked_bar)


# Case study 12 : Track Follow-Up Appointments and Patient Outcomes
elif case_study == "Follow-Up Appointments and Patient Outcomes":
    st.header("Track Follow-up Appointments and Patient Outcomes")
    st.write("""
              This analysis tracks follow-up appointments and calculates the average time to follow-up for each diagnosis. It helps ensure continuity of care and improve treatment outcomes.
            """)
    

    # SQL query to fetch total follow-ups and average days to follow-up by diagnosis
    def get_followup_data():
        query12 = '''SELECT
                     Diagnosis,
                     COUNT(*) AS Total_Followups,
                     AVG(DATEDIFF(`Followup Date`, Discharge_Date)) AS Avg_Days_To_Followup
                     FROM healthcare_data
                     WHERE `Followup Date` IS NOT NULL
                     GROUP BY Diagnosis
                     ORDER BY Total_Followups DESC
                '''

        # Execute the query and get results
        mycursor.execute(query12)
        result12 = mycursor.fetchall()

        # Convert the data into the dataframe
        df12 = pd.DataFrame(result12,columns=['Diagnosis','Total_Followups','Avg_Days_To_Followup'])
        return df12

    # Fetch the data
    df12 = get_followup_data()


    # Bubble Chart for filtered data (Follow-ups for selected diagnosis)
    fig_filtered = px.scatter(df12,
                              x = 'Total_Followups',
                              y = 'Avg_Days_To_Followup',
                              size = 'Total_Followups',
                              color = 'Diagnosis',
                              hover_name = 'Diagnosis',
                              title=f"Follow-ups vs Days to Follow-up by Diagnosis",
                              labels={'Total_Followups': 'Total Follow-ups', 'Avg_Days_To_Followup': 'Average Days to Follow-up'},
                              size_max=60,
                              color_discrete_sequence=px.colors.qualitative.Set2)
    # Update the layout
    fig_filtered.update_layout(
    xaxis=dict(
        title='Total Follow-ups',
        title_font=dict(size=16, color='darkblue'),
        tickfont=dict(size=16, color='darkblue'),
        #tickangle=-45
    ),
    yaxis=dict(
        title='Avg_Days_To_Followup',
        title_font=dict(size=16, color='darkblue'),
        tickfont=dict(size=16, color='darkblue')
    ),
    title_font=dict(size=20, color='#8c564b')
    )
    st.plotly_chart(fig_filtered)


# Case study 13 : Most common diseases with avg billing amount
elif case_study == "Most common diseases with avg billing amount":
    st.header("Most Common Diseases and their Average Billing Amount")
    st.write("""
            This analysis identifies the most common diseases and their average billing amounts, helping hospitals plan financial resources and allocate funds effectively.
            """)
    

    # sql query to get the data
    def get_disease_data():
        query13 = '''SELECT
                     Diagnosis,
                     COUNT(*) AS Disease_Count,
                     AVG(`Billing Amount`) AS Avg_Billing_Amount
                     FROM healthcare_data
                     GROUP BY Diagnosis
                     ORDER BY Disease_Count DESC;
                '''

        # Execute the query and get results
        mycursor.execute(query13)
        result13 = mycursor.fetchall()

        # Convert the data to dataframe
        df13 = pd.DataFrame(result13,columns = ['Diagnosis','Disease_Count','Avg_Billing_Amount'])
        return df13

    # Fetech the data
    df13 = get_disease_data()

    # Create a bar chart showing the most common diseases with their average billing amount
    fig = px.bar(df13,
             x='Diagnosis',
             y='Disease_Count',
             color='Avg_Billing_Amount',
             hover_name='Diagnosis',
             title="Most Common Diseases and Their Average Billing Amount",
             labels={'Disease_Count': 'Disease Count', 'Avg_Billing_Amount': 'Average Billing Amount'},
             color_continuous_scale='Viridis')
    
    # Update the layout
    fig.update_layout(
    xaxis=dict(
        title='Diagnosis',
        title_font=dict(size=16, color='darkblue'),
        tickfont=dict(size=16, color='darkblue'),
        #tickangle=-45
    ),
    yaxis=dict(
        title='Disease Count',
        title_font=dict(size=16, color='darkblue'),
        tickfont=dict(size=16, color='darkblue')
    ),
    title_font=dict(size=20, color='#8c564b')
    )
    # Show the figure
    st.plotly_chart(fig)


# Case study 14: Bed Occupancy Trends and Peak Admission Periods
elif case_study == "Bed Occupancy Trends ans Peak Admission Periods":
    st.header("Track Bed Occupancy Trends and Identify Peak Admission Periods")
    st.write("This analysis tracks bed occupancy trends over time and identifies peak admission periods, helping hospitals optimize bed management, staffing, and resource allocation. By understanding these trends, hospitals can better prepare for high-demand periods and ensure efficient care delivery.")
    


    # Fetch the data based on the SQL query
    def get_bed_occupancy_data():
        query14 = '''
        SELECT
            YEAR(Admit_Date) AS Year,
            MONTH(Admit_Date) AS Month,
            COUNT(*) AS Total_Admissions,
            SUM(CASE WHEN Bed_Occupancy = 'ICU' THEN 1 ELSE 0 END) AS ICU_Beds_Occupied,
            SUM(CASE WHEN Bed_Occupancy = 'General' THEN 1 ELSE 0 END) AS General_Beds_Occupied,
            SUM(CASE WHEN Bed_Occupancy = 'Private' THEN 1 ELSE 0 END) AS Private_Beds_Occupied
        FROM healthcare_data
        GROUP BY YEAR(Admit_Date), MONTH(Admit_Date)
        ORDER BY Year DESC, Month DESC;
        '''
         
        # Execute the query and fetch results
        mycursor.execute(query14)
        result14 = mycursor.fetchall()

        # Convert the data to dataframe
        df14 = pd.DataFrame(result14, columns = ['Year','Month','Total_Admissions','ICU_Beds_Occupied','General_Beds_Occupied','Private_Beds_Occupied'])
        return df14

    # Fetch the data
    df14 = get_bed_occupancy_data()

    # Convert Year and Month into a single Date column for better plotting
    df14['Date'] = pd.to_datetime(df14[['Year', 'Month']].assign(DAY=1))

    # Plot the data using Plotly (line chart for trends)
    fig = px.line(df14, 
                  x='Date', 
                  y=['ICU_Beds_Occupied', 'General_Beds_Occupied', 'Private_Beds_Occupied'],
                  title="Bed Occupancy Trends Over Time",
                  labels={'value': 'Beds Occupied', 'Date': 'Date'},
                  markers=True)

    # Update the layout
    fig.update_layout(
    xaxis=dict(
        title='Date',
        title_font=dict(size=16, color='darkblue'),
        tickfont=dict(size=16, color='darkblue'),
        #tickangle=-45
    ),
    yaxis=dict(
        title='Beds Occupied',
        title_font=dict(size=16, color='darkblue'),
        tickfont=dict(size=16, color='darkblue')
    ),
    title_font=dict(size=20, color='#8c564b')
    )

    # Show the plot
    st.plotly_chart(fig)


# Case Study 15 : Monitor Patient Recovery and Treatment Outcomes
elif case_study == "Monitor Patient Recovery and Treatment Outcomes":
    st.header("Monitor Patient Recovery and Treatment Outcomes")
    st.write("This analysis evaluates recovery times and treatment outcomes for different diseases, providing insights into how treatment strategies impact recovery. It aids in refining treatment plans and enhancing patient care by optimizing recovery processes.")
    

    # SQL query to fetch the data
    def get_recovery_time():
        query15 = '''SELECT 
                     Diagnosis,
                     AVG(DATEDIFF(Discharge_Date, Admit_Date)) AS Avg_Recovery_Time,
                     AVG(DATEDIFF(`Followup Date`, Discharge_Date)) AS Avg_Followup_Time
                     FROM healthcare_data
                     WHERE Discharge_Date IS NOT NULL AND `Followup Date` IS NOT NULL
                     GROUP BY Diagnosis
                     ORDER BY Avg_Recovery_Time DESC 
                  '''
        
        # Execute the query and fetch results
        mycursor.execute(query15)
        result15 = mycursor.fetchall()

        # Convert the data to dataframe
        df15 = pd.DataFrame(result15, columns =['Diagnosis','Avg_Recovery_Time','Avg_Followup_Time'])
        return df15

    # Fetch the data
    df15 = get_recovery_time()


    # Reshape the dataframe for combined plotting (melt)
    df_melted = pd.melt(df15, id_vars=['Diagnosis'], 
                    value_vars=['Avg_Recovery_Time', 'Avg_Followup_Time'],
                    var_name='Metric', value_name='Days')

    # Visualizing both metrics (recovery time and follow-up time) in one plot
    fig_combined = px.bar(df_melted,
                      x='Diagnosis',
                      y='Days',
                      color='Metric',
                      barmode='group',  # Use 'stack' for stacked bar chart
                      title="Average Recovery Time and Follow-up Time by Diagnosis",
                      labels={'Days': 'Days (Recovery/Follow-up)', 'Metric': 'Metric'},
                      color_discrete_sequence=px.colors.qualitative.Set2)

    # Update the layout
    fig_combined.update_layout(
    xaxis=dict(
        title='Diagnosis',
        title_font=dict(size=16, color='darkblue'),
        tickfont=dict(size=16, color='darkblue'),
        #tickangle=-45
    ),
    yaxis=dict(
        title='Days (Recovery/Follow-up)',
        title_font=dict(size=16, color='darkblue'),
        tickfont=dict(size=16, color='darkblue')
    ),
    title_font=dict(size=20, color='#8c564b')
    )
    st.plotly_chart(fig_combined)


# Case study 16 : Impact of Tests on Total Billing Amount
elif case_study == "Impact of Tests on Total Billing Amount":
    st.header("Impact of Tests on Total Billing Amount")
    st.write("This analysis identifies the medical tests that contribute most to patient billing amounts. By understanding the tests that lead to higher costs, hospitals can optimize resource allocation and cost management strategies.")
    

    # sql query to fetch the data
    def get_test_billing_data():
        query16 = '''SELECT 
                    Test,
                    AVG(`Billing Amount`) AS Avg_Billing_Amount,
                    COUNT(*) AS Test_Count
                    FROM healthcare_data
                    GROUP BY Test
                    ORDER BY Avg_Billing_Amount DESC
                '''
        
        # Execute the query and fetch results
        mycursor.execute(query16)
        result16 = mycursor.fetchall()

        # Convert the data to dataframe
        df16 = pd.DataFrame(result16,columns=['Test','Avg_Billing_Amount','Test_Count'])
        return df16

    # Fetch data
    df16 = get_test_billing_data()


    # Scatter plot
    fig_scatter = px.scatter(df16,
                         x='Test_Count',  # X-axis: Number of Tests
                         y='Avg_Billing_Amount',  # Y-axis: Average Billing Amount
                         color='Test',  # Color points based on the test type
                         title="Test Count vs. Average Billing Amount",
                         labels={'Test_Count': 'Number of Tests', 'Avg_Billing_Amount': 'Average Billing Amount'},
                         color_continuous_scale='Viridis')  # Optional color scale

    # Update layout for better appearance
    fig_scatter.update_layout(
        xaxis=dict(
            title='Number of Tests',
            title_font=dict(size=16, color='darkblue'),
            tickfont=dict(size=14, color='darkblue')
        ),
        yaxis=dict(
            title='Average Billing Amount',
            title_font=dict(size=16, color='darkblue'),
            tickfont=dict(size=14, color='darkblue')
        ),
        title_font=dict(size=20, color='#8c564b')
    )

    # Display the scatter plot
    st.plotly_chart(fig_scatter)

