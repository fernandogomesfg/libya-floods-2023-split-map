import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

st.title("Visualização das Enchentes na Líbia: Antes e Depois da Tragédia de Daniel")

st.sidebar.title("Informações")

st.sidebar.info(
    "Esta ferramenta interativa permite comparar as imagens de satélite da Líbia antes e depois da tragédia causada pela tempestade mediterrânica Daniel e o rompimento das barragens. "
    "Use os controles abaixo para ajustar a visualização e explorar as áreas afetadas pelas inundações. "
)

st.sidebar.markdown(
    """
    ---
    *Desenvolvido por Fernando Gomes, [LinkedIn](https://www.linkedin.com/in/fernandogomesfg) e veja meu [portfólio](https://fernandogomesfg.github.io/).*
    """
)



m = leafmap.Map()

before = "https://github.com/opengeos/datasets/releases/download/raster/Libya-2023-07-01.tif"
after = "https://github.com/opengeos/datasets/releases/download/raster/Libya-2023-09-13.tif"
m.split_map(
    left_layer=before, right_layer=after, left_label="Antes (July 1, 2023)", right_label="Depois (September 13, 2023)"
    )


with st.spinner("Carregando o mapa, isso pode levar alguns segundos dependendo da conexão..."):
    m.to_streamlit(height=700)
