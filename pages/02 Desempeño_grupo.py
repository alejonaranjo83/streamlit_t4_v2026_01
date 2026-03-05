# Code for plotting the performance of the whole group, with less detail per student

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import streamlit as st

import os

import io 




st.subheader('Desempeño del grupo (2025.02)')

st.write('El texto que encabeza cada gráfico, corresponde al código del estudiante, eliminando el encabezado de "30000" pues es igual para todos.')

st.write('La letra que lo acompaña, corresponde a la inicial del primer nombre que aparece en la lista.')




# read the data from the corresponding file 

df = pd.read_excel('df_total_e5.xlsx')

# Convert values in the column 'Nivel' to numeric, coercing errors to NaN
df['Nivel'] = pd.to_numeric(df['Nivel'], errors='coerce') 

# Convert NaN values to 0 in the column 'Nivel'
df['Nivel'] = df['Nivel'].fillna(0)







# Colores con los que se trabajará
# color_dict = {0: '#ededed', 1: '#E76F51', 2: '#2db9a0', 3: '#264653'}

# Function to assign colors to values based on predefined ranges.
def assign_colors_to_ranges(values):
    """
    Assigns colors to values based on predefined ranges.

    Args:
        values (pd.Series or list): A pandas Series or list of numerical values.

    Returns:
        dict: A dictionary mapping values to their corresponding colors.
    """

    ranges = [
        (0, 0.1),
        (0.1, 2.99),
        (3, 3.5),
        (3.51, 3.9),
        (3.91, 4.98),
        (4.99, 5),
        (-3, -1)
    ]
    # colors = [
    #     '#ededed',
    #     '#E76F51',
    #     '#F4A261',
    #     '#E9C46A',
    #     '#2A9D8F',
    #     '#264653',
    #     '#AAAAAA',
    # ]
    colors = [
        '#ededed',
        '#264653',
        '#2A9D8F',
        '#E9C46A',
        '#F4A261',
        '#E76F51',
        '#AAAAAA',
    ]

    color_dict = {}

    for value in values:
        if isinstance(value, (int, float)):
            for (lower, upper), color in zip(ranges, colors):
                if lower <= value <= upper:
                    color_dict[value] = color
                    break
        else:  # If the value is not a number (e.g., string)
            color_dict[value] = '#ededed'

    return color_dict


df['Color'] = df['Nivel'].map(assign_colors_to_ranges(df['Nivel']))






# FUNCIONES QUE SE USARÁN PARA CREAR GRÁFICO

# En caso de querer filtrar resultados por una columna diferente, se deben cambiar los valores que están en 'df['codigo_iniciales']'. Se puede cambiar por 'df['NOMBRE']' o 'df['CÓDIGO']' por ejemplo






# Función para mostrar nombre de persona en el encabezado del main
def streamlit_name(df, student_name):
    row = df[df['codigo_iniciales'] == student_name].index[1]

    cod_inic = str(df.iloc[row, 7])

    if len(cod_inic) > 13:
        # cod_inic = cod_inic[:13]
        # Eliminate the first 5 characters of the string
        cod_inic = cod_inic[5:13]
        st.write(cod_inic)


        # Trying to pass a variable inside a modified HTML text
        # st.write("<div style='font-size:10px; line-height:1;'>`This text is small and has less spacing. ${cod_inic}`</div>", unsafe_allow_html=True) 
    



# Función para crear gráfico con matplotlib

def plot_student_performance(df, student_name):
    # Get the row number of the student
    row = df[df['codigo_iniciales'] == student_name].index[1]

    # Set up a figure
    # Set up a figure
    fig = plt.figure(figsize=(Wi, He), dpi=150)

    
    # streamlit_name(df, student_name)


    # Plot with student performance
    ax = fig.add_subplot(2, 1, 1, projection='polar')
    # ax.set_ylim(0, hec+0.6)
    ax.set_ylim(-3, hec+0.1)
    ax.patch.set_facecolor('#ededed')
    fig.patch.set_facecolor('#ededed')
    ax.set_frame_on(False)
    ax.xaxis.grid(False)
    ax.yaxis.grid(False)
    ax.set_xticks([])
    ax.set_yticks([])

   

    #Círculos de referencia
    circle_3 = patches.Circle((0, 0), radius=7.95, edgecolor='#555555', facecolor='none', lw=1, ls='dotted', transform=ax.transData._b, zorder=10)
    ax.add_patch(circle_3)
    circle_2 = patches.Circle((0, 0), radius=7, edgecolor='#555555', facecolor='none', lw=1, ls='dotted', transform=ax.transData._b, zorder=10)
    ax.add_patch(circle_2)
    circle_1 = patches.Circle((0, 0), radius=6, edgecolor='#555555', facecolor='none', lw=1, ls='dotted', transform=ax.transData._b, zorder=10)
    ax.add_patch(circle_1)
    circle_0 = patches.Circle((0, 0), radius=3, edgecolor='#555555', facecolor='none', lw=1, ls='dotted', transform=ax.transData._b, zorder=10)
    ax.add_patch(circle_0)

    #Líneas de referencia (las que se percibe como una X que divide el gráfico)
    plt.axvline(x=np.pi/4, ymin=0.34, color='#555555', lw=1.5)
    plt.axvline(x=np.pi*3/4, ymin=0.34, color='#555555', lw=1.5)
    plt.axvline(x=np.pi*5/4, ymin=0.34, color='#555555', lw=1.5)
    plt.axvline(x=np.pi*7/4, ymin=0.34, color='#555555', lw=1.5)


    #Líneas divisorias entre entregas
    # A
    plt.axvline(x=np.pi*0.7125-(np.pi*0.075/2), ymin=0.33, color='#ededed', lw=0.7)
    plt.axvline(x=np.pi*0.615-(np.pi*0.126/2), ymin=0.33, color='#ededed', lw=0.7)
    plt.axvline(x=np.pi/2-(np.pi*0.1/2), ymin=0.33, color='#ededed', lw=0.7)
    plt.axvline(x=np.pi*0.425-(np.pi*0.05/2), ymin=0.33, color='#ededed', lw=0.7)

    # R
    plt.axvline(x=np.pi*0.2125-(np.pi*0.075/2), ymin=0.33, color='#ededed', lw=0.7)
    plt.axvline(x=np.pi*0.1125-(np.pi*0.126/2), ymin=0.33, color='#ededed', lw=0.7)
    plt.axvline(x=0-(np.pi*0.1/2), ymin=0.33, color='#ededed', lw=0.7)
    plt.axvline(x=np.pi*-0.075-(np.pi*0.05/2), ymin=0.33, color='#ededed', lw=0.7)

    # S
    plt.axvline(x=np.pi*1.7139-(np.pi*0.075/2), ymin=0.33, color='#ededed', lw=0.7)
    plt.axvline(x=np.pi*1.6125-(np.pi*0.126/2), ymin=0.33, color='#ededed', lw=0.7)
    plt.axvline(x=np.pi*1.5-(np.pi*0.1/2), ymin=0.33, color='#ededed', lw=0.7)
    plt.axvline(x=np.pi*1.425-(np.pi*0.05/2), ymin=0.33, color='#ededed', lw=0.7)

    # F
    plt.axvline(x=np.pi*1.2125-(np.pi*0.075/2), ymin=0.33, color='#ededed', lw=0.7)
    plt.axvline(x=np.pi*1.1125-(np.pi*0.126/2), ymin=0.33, color='#ededed', lw=0.7)
    plt.axvline(x=np.pi-(np.pi*0.1/2), ymin=0.33, color='#ededed', lw=0.7)
    plt.axvline(x=np.pi*0.925-(np.pi*0.05/2), ymin=0.33, color='#ededed', lw=0.7)




    # #Textos de apoyo perimetrales al círculo central
    # plt.text(0, hec*1, 'R', fontsize=he_sep*20, fontweight='bold', color="#AAAAAA", ha='left', va='center')
    # plt.text(np.pi/2, hec*1, 'A', fontsize=he_sep*20, fontweight='bold', color="#AAAAAA", ha='center', va='bottom')
    # plt.text(np.pi, hec*1, 'F', fontsize=he_sep*20, fontweight='bold', color="#AAAAAA", ha='right', va='center')
    # plt.text(np.pi*3/2, hec*1, 'S', fontsize=he_sep*20, fontweight='bold', color="#AAAAAA", ha='center', va='top')
    


    # Create a list to store the values of the student
    categ_list = []
    nivel_list = []
    colors_list = []

    # Get the nivel of the student and add them to the lists.
    for i in range(24):
        categ_list.append(df.iloc[row+i]['Categoría'])
        nivel_list.append(df.iloc[row+i]['Nivel'])
        colors_list.append(df.iloc[row+i]['Color'])

    

    # COMBO E1:
    # Create a variable that stores the color of the bars, according to the color of the category
    color_f = colors_list[0]
    color_r = colors_list[1]
    color_a = colors_list[2]
    color_s = colors_list[3]
    color_0 = colors_list[4]

    # Plot the bars
    plt.bar(x=np.pi*1.2125, height=[nivel_list[0]], width=np.pi*0.075, color=color_f, alpha=0.5, label='0.7')
    # plt.bar(x=np.pi*1.2125, height=-1.5, width=np.pi*0.075, color=color_0, alpha=0.5, label='0.7')
    plt.bar(x=np.pi*0.2125, height=[nivel_list[1]], width=np.pi*0.075, color=color_r, alpha=0.5, label='0.7')
    plt.bar(x=np.pi*0.7125, height=[nivel_list[2]], width=np.pi*0.075, color=color_a, alpha=0.5, label='0.7')
    plt.bar(x=np.pi*1.7139, height=[nivel_list[3]], width=np.pi*0.075, color=color_s, alpha=0.5, label='0.7')
    


    # COMBO E2 rows
    color_f = colors_list[5]
    color_r = colors_list[6]
    color_a = colors_list[7]
    color_s = colors_list[8]
    
    # # Plot the bars
    plt.bar(x=np.pi*1.1125, height=[nivel_list[5]], width=np.pi*0.125, color=color_f, alpha=0.5, label='0.7')
    plt.bar(x=np.pi*0.1125, height=[nivel_list[6]], width=np.pi*0.125, color=color_r, alpha=0.5, label='0.7')
    plt.bar(x=np.pi*0.6125, height=[nivel_list[7]], width=np.pi*0.125, color=color_a, alpha=0.5, label='0.7')
    plt.bar(x=np.pi*1.6125, height=[nivel_list[8]], width=np.pi*0.125, color=color_s, alpha=0.5, label='0.7')



    # COMBO E3 rows
    color_f = colors_list[10]
    color_r = colors_list[11]
    color_a = colors_list[12]
    color_s = colors_list[13]
    
    # # Plot the bars
    plt.bar(x=np.pi, height=[nivel_list[10]], width=np.pi*0.1, color=color_f, alpha=0.5, label='0.7')
    plt.bar(x=0, height=[nivel_list[11]], width=np.pi*0.1, color=color_r, alpha=0.5, label='0.7')
    plt.bar(x=np.pi/2, height=[nivel_list[12]], width=np.pi*0.1, color=color_a, alpha=0.5, label='0.7')
    plt.bar(x=np.pi*1.5, height=[nivel_list[13]], width=np.pi*0.1, color=color_s, alpha=0.5, label='0.7')



    # COMBO E4 rows
    color_f = colors_list[15]
    color_r = colors_list[16]
    color_a = colors_list[17]
    color_s = colors_list[18]
    
    # # Plot the bars
    plt.bar(x=np.pi*0.925, height=[nivel_list[15]], width=np.pi*0.05, color=color_f, alpha=0.5, label='0.7')
    plt.bar(x=np.pi*-0.075, height=[nivel_list[16]], width=np.pi*0.05, color=color_r, alpha=0.5, label='0.7')
    plt.bar(x=np.pi*0.425, height=[nivel_list[17]], width=np.pi*0.05, color=color_a, alpha=0.5, label='0.7')
    plt.bar(x=np.pi*1.425, height=[nivel_list[18]], width=np.pi*0.05, color=color_s, alpha=0.5, label='0.7')



    # COMBO E5 rows
    color_f = colors_list[20]
    color_r = colors_list[21]
    color_a = colors_list[22]
    color_s = colors_list[23]
    
    # # Plot the bars
    plt.bar(x=np.pi*0.825, height=[nivel_list[20]], width=np.pi*0.15, color=color_f, alpha=0.5, label='0.7')
    plt.bar(x=np.pi*-0.175, height=[nivel_list[21]], width=np.pi*0.15, color=color_r, alpha=0.5, label='0.7')
    plt.bar(x=np.pi*0.3272, height=[nivel_list[22]], width=np.pi*0.15, color=color_a, alpha=0.5, label='0.7')
    plt.bar(x=np.pi*1.325, height=[nivel_list[23]], width=np.pi*0.15, color=color_s, alpha=0.5, label='0.7')



    # plt.show()

    # st.pyplot(fig, use_container_width = 0)
    #st.pyplot(fig, use_container_width=True)
    
    return fig


    
   



# Variables básicas en torno a las cuales se escala toda la figura:

He = 8.2 # Altura de la figura. Todo se escalará en función de esta altura

he_m = He/2 # Mitad de la altura
he_sep = He/7 # Un séptimo de la altura
hec = He - 2*he_sep # Altura de la caja central

Wi = hec # Ancho de la figura
wi = Wi/2

# print('He:', He, 'he_m:', he_m, 'he_sep:', he_sep, 'hec:', hec, 'Wi:', Wi, 'wi:',wi)




# Create a list with unique student names inside DF
students = df['codigo_iniciales'].unique().tolist()




# st.set_page_config(layout='wide')    


# The logic behind the following script which contains two loops, can be understood with an example using only numbers at the end of this code

# with st.container(height=900):
#     for i in range(5): # The graphs will be placed in 5 rows
#         for j in range(1): # Iterate over the columns just one time   
#             cols = st.columns(9, gap='small')


#             with cols[j]:
#                 with st.container(height=150, border=0):
#                     # streamlit_name(df, students[i*9]) 
#                     plot_student_performance(df, students[i*9])

#             with cols[j+1]: # The position of each column will increase by 1
#                 with st.container(height=150, border=0):
#                     # streamlit_name(df, students[i*9+1])
#                     plot_student_performance(df, students[i*9+1])

#             with cols[j+2]:
#                 with st.container(height=150, border=0):
#                     # streamlit_name(df, students[i*9+2])
#                     plot_student_performance(df, students[i*9+2])
#             with cols[j+3]:
#                 with st.container(height=150, border=0):
#                     # streamlit_name(df, students[i*9+3])
#                     plot_student_performance(df, students[i*9+3])

#             with cols[j+4]:
#                 with st.container(height=150, border=0):
#                     # streamlit_name(df, students[i*9+4])
#                     plot_student_performance(df, students[i*9+4])

#             with cols[j+5]:
#                 with st.container(height=150, border=0):
#                     # streamlit_name(df, students[i*9+5])
#                     plot_student_performance(df, students[i*9+5])

#             with cols[j+6]:
#                 with st.container(height=150, border=0):
#                     # streamlit_name(df, students[i*9+6])
#                     plot_student_performance(df, students[i*9+6])

#             with cols[j+7]:
#                 with st.container(height=150, border=0):
#                     # streamlit_name(df, students[i*9+7])
#                     plot_student_performance(df, students[i*9+7])

#             with cols[j+8]:
#                 with st.container(height=150, border=0):
#                     # streamlit_name(df, students[i*9+8])
#                     plot_student_performance(df, students[i*9+8])




def render_student_plot(df, student_name):
    # Prevenir errores si el estudiante no existe (ej. si la lista es más corta que 9*5)
    if student_name not in df['codigo_iniciales'].unique():
        st.write("---") # Opcional: marcador visual para gráficos faltantes
        return

    # 1. Generar la figura de Matplotlib
    fig_radar = plot_student_performance(df, student_name)
    
    # 2. Guardar la figura en un buffer de memoria como PNG
    buf = io.BytesIO()
    fig_radar.savefig(buf, format="png", bbox_inches='tight') 
    
    # 3. Mostrar el título/código del estudiante
    streamlit_name(df, student_name) 
    
    # 4. Mostrar la imagen (respetando figsize=(Wi, He))
    # use_column_width=True ayuda a que la imagen llene el ancho asignado por st.columns(9).
    st.image(buf, use_container_width=True) 

    # 5. Cerrar la figura para liberar memoria
    plt.close(fig_radar)


# --------------------------------------------------------------------------
# Bucle principal de Streamlit
# --------------------------------------------------------------------------

with st.container(height=900):
    for i in range(5): # Las filas (5)
        
        # Crear las 9 columnas para la fila actual
        cols = st.columns(9, gap='small')

        for k in range(9): # Las columnas (9)
            student_index = i * 9 + k
            
            if student_index < len(students):
                student_name = students[student_index]
                
                with cols[k]:
                    with st.container(height=150, border=0):
                        # Llamamos a la nueva función de renderizado para el estudiante actual
                        render_student_plot(df, student_name)









# Understanding the way the loop works

# Inside a streamlit container, create a grid of 4 rows and 9 columns, where each cell contains a number from 0 to 35. The first row will hold the first 9 numbers of the loop (0-8), the second row will hold the next 9 numbers (9-17), and so on. The last row will hold the last 9 numbers (27-35). The first number of each row will be the last number of the previous row + 1.

# with st.container(height=480):
#     for i in range(4): # The graphs will be placed in 4 rows
#         for j in range(1): # Iterate over the columns just one time   
#             cols = st.columns(9, gap='small')
#             cols[j].write(i*9) # The position of the first column will be the inital value of the column and the number to be plotted will be the product of the row number and 9
#             cols[j+1].write(i*9+1) # The position of each column will increase by 1 and the number to be plotted will be the product of the row number and 9 plus 1
#             cols[j+2].write(i*9+2) # (position)increase by 2... (number) plus 2
#             cols[j+3].write(i*9+3) # (position)increase by 3... (number) plus 3
#             cols[j+4].write(i*9+4) 
#             cols[j+5].write(i*9+5) 
#             cols[j+6].write(i*9+6) 
#             cols[j+7].write(i*9+7) 
#             cols[j+8].write(i*9+8) 
#             # Add a horizontal line to separate the circles
#         st.markdown("---")