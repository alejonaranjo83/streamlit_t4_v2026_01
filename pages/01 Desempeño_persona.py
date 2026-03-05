import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os

import io




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
    # for value in values:
    #     for (lower, upper), color in zip(ranges, colors):
    #         if lower <= value <= upper:
    #             color_dict[value] = color
    #             break  # Stop checking ranges once a match is found
    # return color_dict


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



# Función para crear gráfico con matplotlib

def plot_student_performance(df, student_name):
    # Get the row number of the student
    row = df[df['codigo_iniciales'] == student_name].index[1]

    # Set up a figure
    fig = plt.figure(figsize=(Wi, He), dpi=150)

    



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




    #Textos de apoyo perimetrales al círculo central
    plt.text(0, hec*1, 'R', fontsize=he_sep*20, fontweight='bold', color="#AAAAAA", ha='left', va='center')
    plt.text(np.pi/2, hec*1, 'A', fontsize=he_sep*20, fontweight='bold', color="#AAAAAA", ha='center', va='bottom')
    plt.text(np.pi, hec*1, 'F', fontsize=he_sep*20, fontweight='bold', color="#AAAAAA", ha='right', va='center')
    plt.text(np.pi*3/2, hec*1, 'S', fontsize=he_sep*20, fontweight='bold', color="#AAAAAA", ha='center', va='top')
    


    # Create a list to store the values of the student
    categ_list = []
    nivel_list = []
    colors_list = []

    # Get the nivel of the student and add them to the lists.
    for i in range(24):
        categ_list.append(df.iloc[row+i]['Categoría'])
        nivel_list.append(df.iloc[row+i]['Nivel'])
        colors_list.append(df.iloc[row+i]['Color'])

    # # Convert 'No aplica' to 0
    # nivel_list = [0 if x == 'No aplica' else x for x in nivel_list]
    # # Convert the nivel to integers
    # nivel_list = [int(x) for x in nivel_list]

    # print(categ_list)
    # print(nivel_list)
    # print(colors_list)

    # Create a DF with the values from categ_list, nivel_list and colors_list.

    # df_check = pd.DataFrame({'Categoría': categ_list, 'Nivel': nivel_list, 'Color': colors_list})
    # print(df_check)



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



    # ENSAYO DIVIDIENDO CUADRANTE EN 5 PARTES 
    # Plot the bars dividing the width by 5 (entrega 1 en todos los cuadrantes)
    # plt.bar(x=np.pi, height=[nivel_list[10]], width=np.pi/10, color=color_f, alpha=0.5, label='0.7')
    # plt.bar(x=0, height=[nivel_list[11]], width=np.pi/10, color=color_r, alpha=0.5, label='0.7')
    # plt.bar(x=np.pi/2, height=[nivel_list[12]], width=np.pi/10, color=color_a, alpha=0.5, label='0.7')
    # plt.bar(x=np.pi*1.5, height=[nivel_list[13]], width=np.pi/10, color=color_s, alpha=0.5, label='0.7')





    # Texts to reference the nivel of the bars
    plt.text(np.pi/3.9, 2.5, '3', fontsize=7, color='#444444', ha='right', va='bottom')
    plt.text(np.pi/3.9, 3.5, '4', fontsize=7, color='#444444', ha='right', va='bottom')
    plt.text(np.pi/3.9, 4.4, '5', fontsize=7, color='#444444', ha='right', va='bottom')




    # Texts to reference each bar 'entrega'
    # A
    plt.text(np.pi*0.7125, 5.5, 'e1', fontsize=7, color='#AAAAAA', ha='center', va='center')
    plt.text(np.pi*0.6125, 5.5, 'e2', fontsize=7, color='#AAAAAA', ha='center', va='center')
    plt.text(np.pi/2, 5.5, 'e3', fontsize=7, color='#AAAAAA', ha='center', va='center')
    plt.text(np.pi*0.425, 5.5, 'e4', fontsize=7, color='#AAAAAA', ha='center', va='center')
    plt.text(np.pi*0.3272, 5.5, 'e5', fontsize=7, color='#AAAAAA', ha='center', va='center')

    # R
    plt.text(np.pi*0.2125, 5.5, 'e1', fontsize=7, color='#AAAAAA', ha='center', va='center')
    plt.text(np.pi*0.1125, 5.5, 'e2', fontsize=7, color='#AAAAAA', ha='center', va='center')
    plt.text(0, 5.5, 'e3', fontsize=7, color='#AAAAAA', ha='center', va='center')
    plt.text(np.pi*-0.0755, 5.5, 'e4', fontsize=7, color='#AAAAAA', ha='center', va='center')
    plt.text(np.pi*-0.175, 5.5, 'e5', fontsize=7, color='#AAAAAA', ha='center', va='center')

    # S
    plt.text(np.pi*1.7139, 5.5, 'e1', fontsize=7, color='#AAAAAA', ha='center', va='center')
    plt.text(np.pi*1.6125, 5.5, 'e2', fontsize=7, color='#AAAAAA', ha='center', va='center')
    plt.text(np.pi*1.5, 5.5, 'e3', fontsize=7, color='#AAAAAA', ha='center', va='center')
    plt.text(np.pi*1.425, 5.5, 'e4', fontsize=7, color='#AAAAAA', ha='center', va='center')
    plt.text(np.pi*1.325, 5.5, 'e5', fontsize=7, color='#AAAAAA', ha='center', va='center')

    # F
    plt.text(np.pi*1.2125, 5.5, 'e1', fontsize=7, color='#AAAAAA', ha='center', va='center')
    plt.text(np.pi*1.1125, 5.5, 'e2', fontsize=7, color='#AAAAAA', ha='center', va='center')
    plt.text(np.pi, 5.5, 'e3', fontsize=7, color='#AAAAAA', ha='center', va='center')
    plt.text(np.pi*0.925, 5.5, 'e4', fontsize=7, color='#AAAAAA', ha='center', va='center')
    plt.text(np.pi*0.825, 5.5, 'e5', fontsize=7, color='#AAAAAA', ha='center', va='center')



    # plt.show()

    # st.pyplot(fig, use_container_width = 0)
    # st.pyplot(fig, use_container_width=True)
    
    return fig
    

    # with st.container(height=400, border=0):
    #     st.pyplot(fig, use_container_width=True)
# st.pyplot(fig, use_container_width=True)




# Función para mostrar nombre de persona en el encabezado del main
def streamlit_name(df, student_name):
    row = df[df['codigo_iniciales'] == student_name].index[1]

    # st.subheader(df.iloc[row, 1].title())
    st.subheader(df.iloc[row, 0])
    
       

# Función para seleccionar comentario personal de la persona seleccionada
def streamlit_coment(df, student_name):
    row = df[df['codigo_iniciales'] == student_name].index[5]
    st.write(df.iloc[row, 6]) 


# Función para seleccionar rúbrica que le corresponde a la persona seleccionada
def streamlit_rub(df, student_name):
    st.write('*Habilidades transversales del ser*')
    row = df[df['codigo_iniciales'] == student_name].index[9]
    st.write(df.iloc[row, 6])

    # st.divider()
    st.write('  ')

    st.write('*Argumentación + coherencia*')
    row = df[df['codigo_iniciales'] == student_name].index[8]
    st.write(df.iloc[row, 6])

    # st.divider()
    st.write('  ')

    st.write('*Representación + comunicación*')
    row = df[df['codigo_iniciales'] == student_name].index[7]
    st.write(df.iloc[row, 6])

    # st.divider()
    st.write('  ')

    st.write('*Función*')
    row = df[df['codigo_iniciales'] == student_name].index[6]
    st.write(df.iloc[row, 6])




# 

def streamlit_entrega_com_rub(df, student_name, entrega):
    # Get the row number of the student
    row = df[df['codigo_iniciales'] == student_name].index[1]
    


    # Create a loop (if statement) which is going to store the corresponding row according to the entrega selected by the user. From that row, ahead in the code, will be selected a specific value. 

    if entrega == 'E1':
        row_coment = df[df['codigo_iniciales'] == student_name].index[0]
        row_func = df[df['codigo_iniciales'] == student_name].index[1]
        row_rep = df[df['codigo_iniciales'] == student_name].index[2]
        row_arg = df[df['codigo_iniciales'] == student_name].index[3]
        row_ser = df[df['codigo_iniciales'] == student_name].index[4]

    if entrega == 'E2':
        row_coment = df[df['codigo_iniciales'] == student_name].index[5]
        row_func = df[df['codigo_iniciales'] == student_name].index[6]
        row_rep = df[df['codigo_iniciales'] == student_name].index[7]
        row_arg = df[df['codigo_iniciales'] == student_name].index[8]
        row_ser = df[df['codigo_iniciales'] == student_name].index[9]

    if entrega == 'E3':
        row_coment = df[df['codigo_iniciales'] == student_name].index[10]
        row_func = df[df['codigo_iniciales'] == student_name].index[11]
        row_rep = df[df['codigo_iniciales'] == student_name].index[12]
        row_arg = df[df['codigo_iniciales'] == student_name].index[13]
        row_ser = df[df['codigo_iniciales'] == student_name].index[14]
    
    if entrega == 'E4':
        row_coment = df[df['codigo_iniciales'] == student_name].index[15]
        row_func = df[df['codigo_iniciales'] == student_name].index[16]
        row_rep = df[df['codigo_iniciales'] == student_name].index[17]
        row_arg = df[df['codigo_iniciales'] == student_name].index[18]
        row_ser = df[df['codigo_iniciales'] == student_name].index[19]

    if entrega == 'E5':
        row_coment = df[df['codigo_iniciales'] == student_name].index[20]
        row_func = df[df['codigo_iniciales'] == student_name].index[21]
        row_rep = df[df['codigo_iniciales'] == student_name].index[22]
        row_arg = df[df['codigo_iniciales'] == student_name].index[23]
        row_ser = df[df['codigo_iniciales'] == student_name].index[24]






    # Show the value of the 7th column according to the previous rows identified.
    st.write('*Comentarios*' + ' (' + entrega + ')')
    st.write(df.iloc[row_coment, 6])
    st.write('  ')

    st.divider()
    st.write('RÚBRICA EQUIVALENTE')
    
    st.write('*Habilidades transversales del ser*' + ' (' + entrega + ')')
    st.write(df.iloc[row_ser, 6])

    st.write('*Argumentación + coherencia*' + ' (' + entrega + ')')
    st.write(df.iloc[row_arg, 6])
    st.write('  ')
   
    st.write('*Representación +  comunicación*' + ' (' + entrega + ')')
    st.write(df.iloc[row_rep, 6])
    st.write('  ')

    st.write('*Función*' + ' (' + entrega + ')')
    st.write(df.iloc[row_func, 6])
    st.write('  ')


    




# Variables básicas en torno a las cuales se escala toda la figura:

He = 8.2 # Altura de la figura. Todo se escalará en función de esta altura

he_m = He/2 # Mitad de la altura
he_sep = He/7 # Un séptimo de la altura
hec = He - 2*he_sep # Altura de la caja central

Wi = hec # Ancho de la figura
wi = Wi/2

# print('He:', He, 'he_m:', he_m, 'he_sep:', he_sep, 'hec:', hec, 'Wi:', Wi, 'wi:',wi)




# CREACIÓN DE LA APLICACIÓN EN STREAMLIT

# Creating what is going to be shown in the app
st.set_page_config(layout='wide')








# st.sidebar.write('Persona')
persona = st.sidebar.selectbox( # En función de esta variable se modifica el resto de la página
    'Visualiza el desempeño de una persona seleccionando su nombre',
    df['codigo_iniciales'].unique()
)




# CONTENIDO PRINCIPAL

# Select the student to be shown in 'streamlit_name' function according to the selection in the sidebar
streamlit_name(df, persona)


# Dividing the main content into 3 columns
# col = st.columns((0.38, 0.31, 0.31), gap='small')
col = st.columns((0.38, 0.62), gap='small')






# INTENTOS DE AJUSTE DEL TAMAÑO DEL GRÁFICO EN STREAMLIT


# with col[0]: # Contenido de la columna 1
     
#     with st.container(height = 480, border=0):
        
#         # CREANDO GRÁFICO INDIVIDUAL CON MATPLOTLIB
#         # st.pyplot(fig, use_container_width=True)
#         plot_student_performance(df, persona)
#         # plot_student_performance(df, persona, entrega)


#     st.markdown(f"<div style='text-align: left;'><p>A: Argumentación + coherencia <br> R: Representación + comunicación <br> S: Habilidades transversales del ser <br> F: Función + técnica</p></div>", unsafe_allow_html=True)
    



# with col[0]: # Contenido de la columna 1
    
#     with st.container(height = 480, border=0):
        
#         # 1. Llama a la función y CAPTURA el objeto figura que retorna
#         fig_radar = plot_student_performance(df, persona)
        
#         # 2. Renderiza la figura CAPTURADA. Esto respeta figsize=(Wi, He)
#         #st.pyplot(fig_radar, use_container_width=True)
#         st.pyplot(fig_radar)

#         # 3. Cierra la figura de Matplotlib para liberar memoria
#         plt.close(fig_radar) 
        
#     st.markdown(f"<div style='text-align: left;'><p>A: Argumentación + coherencia <br> R: Representación + comunicación <br> S: Habilidades transversales del ser <br> F: Función + técnica</p></div>", unsafe_allow_html=True)



with col[0]: # Contenido de la columna 1
    
    # 1. Llama a la función y CAPTURA el objeto figura
    fig_radar = plot_student_performance(df, persona)
    
    # 🛑 CAMBIO: Guarda la figura en un buffer de memoria (o archivo temporal)
    buf = io.BytesIO()
    fig_radar.savefig(buf, format="png", bbox_inches='tight') 
    
    # 2. Renderiza la imagen. Esto es más respetuoso con el tamaño original.
    st.image(buf, use_container_width=True) # use_column_width aquí sí puede ser útil

    # 3. Cierra la figura de Matplotlib para liberar memoria
    plt.close(fig_radar) 






with col[1]:
    st.write('Selecciona la entrega que quieres ver en detalle')
    
    entrega = 'E5'

    e1, e2, e3, e4, e5, ex, ey, ez = st.columns(8)
    
    if e1.button("E1", use_container_width=True):
        entrega = 'E1'
    if e2.button("E2", use_container_width=True):
        entrega = 'E2'
    if e3.button("E3", use_container_width=True):
        entrega = 'E3'
    if e4.button("E4", use_container_width=True):
        entrega = 'E4'
    if e5.button("E5", use_container_width=True):
        entrega = 'E5'

    st.divider()



with col[1]: # a

    st.write('**COMENTARIOS Y RÚBRICA EQUIVALENTE SEGÚN ENTREGA SELECCIONADA:**')
    with st.container(height = 330, border=0):
        streamlit_entrega_com_rub(df, persona, entrega)
        
 









# Create a download button
# st.markdown('### Download data')
# st.write('Click the button below to download the data as a CSV file.')
# st.markdown('''
#     <a href="data:file/csv;base64,{{data}}" download="data.csv">
#         <button>Download CSV</button>
#     </a>
# ''', unsafe_allow_html=True)
