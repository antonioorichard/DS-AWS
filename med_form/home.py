import streamlit as st

st.set_page_config(
    page_title = "Formulário médico"
    #page_icon = ""

)

api_gateway_endpoint = "" # Substitua pela URL correta do API Gateway

with st.form( key = 'form1'):
    col1, col2, col3 = st.columns([3,2,1])
    with col1:
            raiox_res  = st.text_input("raiox_res")
    with col2:
            fnt_in_cov = st.text_input("fnt_in_cov")
    with col3:
            delta_uti  = st.text_input("delta_uti")
    with col1:
            amostra    = st.text_input("amostra")
    with col2:
            hospital   = st.text_input("hospital")
#    st.form_submit_button()

        if st.form_submit_button():
                # Preparar os dados para a chamada do API Gateway
                input_data = {
                        'raiox_res' : raiox_res, 
                        'fnt_in_cov': fnt_in_cov,
                        'delta_uti' : delta_uti, 
                        'amostra'   : amostra, 
                        'hospital'  : hospital
                }

                # Enviar a requisição POST para o API Gateway
                response = requests.post( api_gateway_endpoint, json = input_data)

                # Tratar a resposta do API Gateway 
                if response.status_code == 200:
                        output_data = response.json()
                        st.write("Resultado da inferência: ")
                        st.write( output_data )
                else: 
                        st.write( "Erro ao chamar o API Gateway.")