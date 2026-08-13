##App for teaching alignment concepts for bioinformatics
#Create by Jorge Jonhson and adaptated with ChatGPT and Javier Alvarez instrutions
#2025
import streamlit as st
from global_alig import Alineador

st.title("Herramienta para visualización de un  Alineamiento Global")

# Entradas del usuario
seq1 = st.text_input("Secuencia 1 (máx. 50 caracteres)", "ACCGT")
seq2 = st.text_input("Secuencia 2 (máx. 50 caracteres)", "AACCTG")

# Validación
if st.button("Alinear"):
    if len(seq1) == 0 or len(seq2) == 0:
        st.error("❌ Ambas secuencias deben tener al menos 1 carácter.")
    elif len(seq1) > 50 or len(seq2) > 50:
        st.error("❌ Las secuencias no pueden superar los 50 caracteres.")
    else:
        # Guardar en archivo temporal
        with open("tmp.txt", "w") as f:
            f.write(seq1 + "\n" + seq2)

        # Procesar alineamiento
        obj = Alineador()
        obj.establecerArchivo("tmp.txt")
        obj.preparar()

        # Mostrar matriz
        st.subheader("Matriz de Puntuación")
        matriz = [
            [obj._Alineador__Matriz[i][j].valor for j in range(obj._Alineador__totalColumnas)]
            for i in range(obj._Alineador__totalFilas)
        ]
        st.table(matriz)

        # Mostrar alineamientos
        obj.alinear()
        st.subheader("Alineamientos posibles")
        for al in obj._Alineador__alineamientos:
            st.text(al[0])
            st.text(al[1])

