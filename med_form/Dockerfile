FROM python:3.10

WORKDIR /app 
# criando uma pasta chamada app

COPY . /app 
# copiando tudo que eu tenho localmente para está pasta app 

#RUN pip install --no-cache-dir -r requirements.txt

RUN pip install streamlit pandas boto3

EXPOSE 8501 
# a porta exposta na máquina local - será ira passar as coisas para o container

CMD ["streamlit", "run", "--server.port", "8501", "home.py"] 
# executando o comando

# aws ecr get-login-password --region us-east | docker login --username AWS --password-stdin 325645464037.dkr.ecr.us-east-2.amazonaws.com 

# COMANDOS QUE IREMOS EXECUTAR 
# docker build -t ds-aws # ds-aws é nome do container

# Comando para verificar as images instaladas 
#docker images 

# COmando para verificar a se tem alguma imagem roldando/ lista containers
#docker ps

# Comando executar aplicação (-p paramentro port)/ por concidência minha porta local é a mesma do container
#docker run -p 8501:8501 ds-aws:latest

# COmando para parar o container é 
#docker stop id_do_container