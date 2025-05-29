import streamlit as st

st.title("🎯 Mis metas del mes")

metas = st.session_state.get("metas", [])

nueva_meta = st.text_input("Escribe una nueva meta:")

if st.button("Agregar meta"):
    if nueva_meta:
        metas.append({"texto": nueva_meta, "completada": False})
        st.session_state.metas = metas

st.write("### Lista de metas:")

for i, meta in enumerate(metas):
    completada = st.checkbox(meta["texto"], value=meta["completada"], key=i)
    metas[i]["completada"] = completada
