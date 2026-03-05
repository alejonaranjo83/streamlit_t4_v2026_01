import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

import os



#LEER DATOS (cambiando el directorio de trabajo... genera error luego para leer directorio de 'pages')

# base_dir = os.path.dirname(__file__)

# sub_dir = "data" # subdirectory name

# path = os.path.join(base_dir, sub_dir)

# os.listdir(path)
# os.chdir(path)




st.set_page_config(
    page_title="Habitar Macondo", layout='wide',
    # page_icon="👋",  
    initial_sidebar_state='expanded'
)



# Use 'openpyxl' library to read the Excel file
# df = pd.read_excel("df_total_e3.xlsx", engine='openpyxl')

# st.write(df)
# st.write(path)


st.title("Habitar Macondo 2.0")


st.markdown(""" A través de esta aplicación podrás conocer el desempeño de 46 Macondianos en su misión de prepararse para un nuevo huracán, usando dos perspectivas: el desempeño individual y el desempeño grupal.""")



st.subheader("Tablero MIRO")
st.markdown("En este tablero se recopilan ejercicios relizados a lo lago del curso.")

# Create a link to a homepage
st.markdown("[Ir al tablero](https://miro.com/welcomeonboard/cDlFTHkwWDRMME80RnpQUnF6NUFHWmRuRGNWcm56aHJLblE5YUN1UExyb2t2ODdJSGMxQitUMCs5R2l0c1lyd1lYNTJWM1RrbGJGbnVMTzZPSmg0QThaSXd5ejRyazNiSEVzRW5XSGx6NzZua0FqcE9FRVRTdk9DZE81YWQ2UDJhWWluRVAxeXRuUUgwWDl3Mk1qRGVRPT0hdjE=?share_link_id=290650707684)")


with st.sidebar.container(height=470, border=0):
    st.write('Donde el Magdalena deja atrás el macizo colombiano y la alta montaña, para lanzarse hacia la llanura costera del caribe y posteriormente al mar, Macondo se prepara para un nuevo "Huracán" en Honda')


#CONTENIDO PRINCIPAL


# st.image('ImagenCentral.png', width=100, use_column_width=True)


# st.image('ImagenCentral.png', width=850, use_container_width='always')


# col = st.columns((0.33, 0.33, 0.33), gap='small')

# with col[0]:
#     st.image('Miniatura1_roles.png', use_container_width='always')

# with col[1]:
#     st.image('Miniatura2_equipos.png', use_container_width='always')

# with col[2]:
#     st.image('Miniatura3_entornos.png', use_container_width='always')

# st.image('Formulac_desafioB.png', use_container_width='always')