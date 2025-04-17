 
 
<p align="center"> <img src="imagem/Ecommerce-Website.jpg" alt="Analyzing customer groups"> </p>

Este é um projeto fictício. Com dados públicos dos [E-commerce](https://billionaire365.com/2019/02/25/what-is-an-ecommerce-website/) das empresas Amazon, Bestbuy, barcodable , bhphotovideo, ebay, kmart e Walmart.
# 0 Resumo sobre o projeto

## 0.1 Modelo de Negócio

* E-commerce

## 0.2 Sede da empresa



1. **Amazon**
   - Sede: Seattle, Washington, EUA
   - Site: [Amazon](https://www.amazon.com)

2. **Best Buy**
   - Sede: Richfield, Minnesota, EUA
   - Site: [Best Buy](https://www.bestbuy.com)

3. **Barcodable**
   - Sede: Orlando, Florida, EUA
   - Site: [Barcodable](https://www.barcodable.com)

4. **B&H Photo Video**
   - Sede: Nova York, Nova York, EUA
   - Site: [B&H Photo Video](https://www.bhphotovideo.com)

5. **eBay**
   - Sede: San José, Califórnia, EUA
   - Site: [eBay](https://www.ebay.com)

6. **Kmart**
   - Sede: Hoffman Estates, Illinois, EUA
   - Site: [Kmart](https://www.kmart.com)

7. **Walmart**
   - Sede: Bentonville, Arkansas, EUA
   - Site: [Walmart](https://www.walmart.com)

## 0.3 Tipo de produto
 
* tv, television, video,
* laptop, computer
* speaker, portable, bluetooth
* camera, mirrorless, photo
* car, speaker e subwoofer
* receiver, amplifier, home
* camera, shoot
* drive, storage, hard
* drive, storage, internal
* car, receiver, dash
* player, home, audio
* headphone, earbud, ear
* headphone
* ipod, player
* ...

## 0.4 Problema

A empresa HealthBridge Solutions criou um formulário que faz um
primeiro check-up em seus pacientes que estão com algum tipo de
desconforto na respiração, no momento que ocorre o primeiro atendimento
tentam classiﬁcar a possível doença para fazer o melhor direcionamento
interno e também criar métricas para avaliar a assertividade da sua equipe
com um modelo de ML como baseline, caso ocorra algum falso positivo ou
verdadeiro negativo não será afetado a saúde do paciente.
O CTO que lhe contratou precisa que seja criado um modelo para
classiﬁcar os 5 tipos de doenças respiratórias com base no formulário que foi
criado em papel, após o desenvolvimento do modelo deve ser criado uma
ferramenta para informatizar esse formulário e no ﬁnal do preenchimento ele
classiﬁca as doenças entre essas 5 categorias.
 

## 0.5 Solução

* A solução inicial - Calcular a elasticidade dos preços.
  * Insights

## 0.6 Impacto da solução

* Personalizar a experiência ou adptar
  * Comunição.
  * Ofertas.
  * Recomendação.
* Segmentação de Marketing mais eficientes.
* Otimização do Estoque.

   ... 



*****************************************************************************************************************************************************************************



  

## 1. Problema de negócios 

### 1.1 Problema 

Uma empresa pretende alterar os preços dos produtos vendidos, mas tem receio dessa alteração impactar na demanda desses produtos e por consequência no faturamento. Essa demanda foi submetida para mim e como analista/cientista de dados preciso determinar a elasticidade dos preços usando a metodologia científica embasado nos dados dos preços dos produtos vendidos pela empresa.

  

### 1.2 Motivação 

Maximizar o lucro por meio dos melhores ajustes dos preços. 

  

  

### 1.3 Demandas de negócio 

  

Produto de dados solicitado: 

* Estudo do impacto da alteração de preço sobre a vendas do produto, em primeiro momento concentrado na categoria speaker, portable, bluetooth. O produto speaker. 

  

  

## 2. Premissas de negócio 

  
### 2.1 Entrega
- Todos os produtos de dados entregues devem ser acessíveis via internet.
- O planejamento da solução será validado com os times de negócio, visando garantir que as soluções desenvolvidas sejam úteis na sua tomada de decisão.
### 2.2 Validação estatística

#### 2.1 R² ou R-squared
* Tende a 1 quando o modelo trabalha com somente um produto.  
* Vária de 0.13 a 0.50 quando com vários produtos.
#### 2.2 p-value
Foram filtrados os resultados da elasticidade do preço para somente produtos com uma p-value estatística menor a 15%.


  

## 3. Planejamento da solução 

* Baixar os dados e ler os dados

* Executar o processo de limpeza de dados como:

	* renomear colunas

	* renomear categorias mudar de tipo de variável, caso necessário

* Estatística descritiva com visualização

* Feature Engineering

* Machine Learning

* Elasticidade

* Business Performance

* Cross Price Elasticity

### 3.1. Produto final 

  

O que será entregue efetivamente? 


- Um gráfico com a elesticidade de preços e os nomes do produtos
- Uma tabela com as elasticidade de preços e os nomes do produtos


  

### 3.2. Ferramentas 

  

Quais ferramentas serão usadas no processo? 

- Pyenv; 

- Jupyter Notebook; 

- Git, Github; 

- Python; 

- streamlit; 

- Sistema Linux. 

  

  

  

## 4. Resultados para o negócio 

  

### 4.1 Resultados 

  
####  <p align = "center"> Imagem - Resultado.	</p>		
<p align="center"> <img src="imagem/df_elasticity_resultado.jpg" alt="Resultado"> </p>

  


Interpretando os resultados da imagem resultado. Para casos com a elasticidade negativa ou inelástica, traz a informação que os clientes não são muitos sensíveis à variação do preço do produto, para empresa representar uma maior flexibilidade para definir o preço, podendo aumentar sem afetar significativamente a quantidade demandada. Entretanto, a redução do preço não necessariamente resultarão em um aumento da quantidade demandada.  Produtos do index 0 (BOOM 2 Wireless Bluetooh Speaker -Indigo), 1, 2 e 7. Para os produtos, elástico, deve ter um cuidado com aumento do preço, pois, seus clientes são sensíveis. Se aumentar o preço, reduzirá drasticamente a demanda, contudo, se reduzir, pode gerar um aumento significativo de vendas. Exemplo dos produtos com o index 3, 4, 5 e 6.
  

Como resultado para o negócio foram criados: 

  

* Dataset ou conjunto de dados com a elasticidade dos preço e outras informações estatística como p-value. 

  

 ## 4.2 Business Performance
 
 ### 4.2.1 Simulação sem levar em conta a elasticidade de preço - situação de aumento
 O aumento nos preços dos produtos em 15% sem analisar a elasticidade do preço da demanda, gerou o seguinte resultado na imagem - "Situação de aumento, resultado total". E ainda na imagem abaixo desta, imagem - "Situação de aumento, resultado detalhado." 
 
#### <p align="center"> Imagem - Situação de aumento, resultado total </p>
<p align="center"> <img src="imagem/total_aumento.jpg" alt="Situação de aumento em 15%, resultado total"> </p>


####							<p align = "center"> Imagem - Situação de aumento, resultado detalhado. </p>
<p align="center"> <img src="imagem/aumento_promo.jpg" alt="Situação de aumento, resultado detalhado"> </p>


 ### 4.2.2 Simulação com a elasticidade de preço
 O desconto de 15%  para produtos com a elasticidade do preço da demanda maior do que 1, e ainda aumento de 15% para os produtos com a elasticidade de preço da demanda menor do que 1. Os resultados estão nas imagens abaixo "[Levando em conta a elasticidade, resultado total](#resultado-total)" e "[Levando em conta a elasticidade, resultado detalhado](#resultado-detalhado)": 

  
#### 							<p align = "center">	Imagem - Levando em conta a elasticidade, resultado total. </p> 
<p id="resultado-total" align="center"> <img src="imagem/total_desconto.jpg" alt="Situação de desconto em 15%, resultado total"> </p>


####                                                    <p align ="center"> Imagem - Levando em conta a elasticidade, resultado detalhado. </p>

<p id="resultado-detalhado" align="center"> <img src="imagem/inteligente_promo.jpg" alt="Situação de desconto, resultado detalhado"> </p>





 ## 4.3 Cross Price Elasticity
A seguir o [resultado do Cross Price](#resultado) dos produtos entre sí, entre eles o BOOM 2 Wireless Bluetooth Speaker - Indigo, como mostra a imagem - [Cross price com BOOM 2 Wireless Bluetooth Speaker - Indigo](#boom2). Além disso, a imagem - Resultado de cross price com BOOM 2 Wireless Bluetooth Speaker - Indigo, mostra o resultado do cross Price que nos diz se existe uma relação entre os produtos.
  

####								<p id= "boom2" align = "center"> Imagem - BOOM 2 Wireless Bluetooth Speaker - Indigo </p>
<p align="center"> <img src="imagem/boom2.jpg" alt="Situação de cross price com BOOM 2 Wireless Bluetooth Speaker - Indigo"> </p>

#### 								<p id="resultado" align = "center"> Imagem - Resultado de cross price dos produtos da categória speaker</p>
![Situação de cross price com BOOM 2 Wireless Bluetooth Speaker - Indigo](imagem/cross_price_elasticity.jpg) 

### 4.3.1 Interpretação

* 0 ou próximo deste valor significa que os produtos não a relação.
* Quando a elasticidade-preço cruzada é positiva, isso indica que os produtos x e y são substitutos. Em outras palavras, o aumento o preço y leva a um aumento na quantidade demandada de x.
* < 0 Quando a elasticidade-preço cruzada é negativa, isso indica que os produtos x e y são complementares. Deste modo, ao aumentar o preço de x leva a uma diminuição na quantidade damandada de y.
   
## 5. Conclusão 

  

* O objetivo foi alcançado, dado que o produto de dados foram gerados com sucesso. O funcionário pode utilizar a ferramenta criado para fazer a elasticidade de preço. 

  


  

  

[Dashbord no streamlit](https://elasticidade-dashbord.streamlit.app/) 

  

  

## 6. Próximos passos 

  

Algumas melhorias no projeto podem ser incrementadas no futuro: 

  

* Carregar os dados em servidor. 

* Deploy do modelo. 

* Criar um botão com api do modelo de Machine Learning no google sheets para que resultado seja emitido por lá ao carregar um novo dataset. 

* Fazer um filtro no dashbord hospedado no streamlit ou metabase em categorias. 

  

## 7 Referências 

* Este Projeto foi feito como parte do curso "DS em Produção", da [Comunidade DS](https://www.comunidadedatascience.com/). 

* O Dataset foi obtido no curso de Ciência de dados da [Comunidade DS](https://alunos.comunidadeds.com/auth/login?redirect=%2F%3Futm_source%3Dinstall). 

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

  

#### Observação:  

**Python 3.12.3** 

#### Contatos:
* [LinkedIn](www.linkedin.com/in/antonio-richard-hc)
* [Portfolio](https://antonioorichard.github.io/portfolio_projetos/)


