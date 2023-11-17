import numpy as np
import streamlit as st
import pandas as pd
import os
import re

# criei grupos com os nomes "extensao", "pesquisa" e "ensino" para facilitar a busca

pesquisa = ["Avaliação da qualidade ambiental por meio do bioensaio Trad-MCN e uso do Instagram como ferramenta de aprendizagem significativa.",
             "Cadeias de Markov.", "Estratégias de divulgação para impulsionar os acessos à REMAT.",
             "Cultura Maker em Práticas Escolares no Ensino Fundamental Anos Finais.", "Inclusão digital na sala de aula: educação programada para o futuro.",
             "Cultura maker: inserindo a robótica como prática pedagógica para os anos iniciais.",
             "Cultura Maker: como atividades práticas e a criatividade influenciam no aprendizado.",
             "Revolucionando o Ensino de Geografia: Geoprototipagem Tridimensional de modelos de terreno para uma Educação de Qualidade e Impacto.",
             "A Coleção geológica didática como recurso didático para ensino de temas de geologia no ensino médio.",
             "Elaboração de filmes biodegradáveis de alginato de sódio e quitosana incorporando extrato da casca de pinhão (Araucaria angustifolia) para uso como curativos antimicrobianos e antifúngicos.",
             "Estudo e desenvolvimento de robôs autônomos: atividades de pesquisa e práticas em robótica para estudantes do ensino médio técnico.",
             "Matemática na Wikipédia: avaliando e melhorando a qualidade do conteúdo disponível.", "O que é matemática? por que ensinar? como se ensina e como se aprende?: algumas concepções de professores de Matemática da Educação Básica.",
             "Formando especialistas em computação quântica: desenvolvimento de programas de capacitação."]

ensino = ["Tempo-Livro: promoção da leitura no IFRS - Campus Caxias do Sul.",
          "Gamificação, mídia digital e oficinas educativas no Ensino de Biologia: influência no processo de ensino e aprendizagem.",
          "Superando desafios: a sinergia entre esporte e educação.", "Experiência voluntária em projeto de inclusão por meio da cultura corporal.",
          "Ações desenvolvidas e auxiliadas pelo FabLab (Laboratório de Fabricação) do IFRS - Campus Caxias do Sul.",
          "Uso da balança de dois pratos como recurso pedagógico para o ensino das equações de 1° grau: estratégia para formação docente em didática e educação inclusiva.", "Ensino da multiplicação como estratégia para formação docente em didática e educação inclusiva.", "Utilização de recurso didático para o ensino das horas como estratégia para uma melhor formação didática e inclusiva docente.",
          "Uso da balança de dois pratos como recurso pedagógico para o ensino das equações de 1º grau: estratégia para formação docente em didática e educação inclusiva.",
          "Dois E.V.A’s e um molde: como facilitar o ensino das áreas e circunferências de um círculo.",
          "Recurso didático para o ensino de frações: estratégia para formação docente.",
          "Aprendizagem de Robótica por meio da construção e da programação de robôs.",
          "Tutoria de pares com foco na inclusão acadêmica de estudantes com necessidades educacionais específicas.",
          "Cosmos, uma Viagem pelo Universo.", "Estudos em didática: caminhos possíveis para a formação docente pelo ensino de análise combinatória.",
          "Laboratório de matemática:um ambiente para pesquisas no ensino e na prática da matemática.",
          "Fortalecendo as bases matemáticas: o curso de Pré-Cálculo como oportunidade para a transição da matemática do ensino médio para a do ensino superior.",
          "Monitoria de química: compartilhando saberes.", "Construção de recurso na formação de professores, estratégia para o ensino da geometria.",
          "Monitoria de Física para o Ensino Médio no Campus Caxias do Sul do IFRS.", "Jogo da Memória para a fixação do aprendizado das figuras geométricas.",
          "O saber e o âmbito profissional: desenvolvimento humano e compromisso social.", "Monitoria de física para estudantes com necessidades específicas: promovendo igualdade de oportunidades de aprendizado.",
          "Monitoria em filosofia.", "1a Edição (2022) - O saber e o âmbito profissional: desenvolvimento humano e compromisso social.",
          "Monitoria em Educação Física: aprendizagens e convivialidade.",
          "Transformações no ensino da geografia na educação básica: um projeto de integração didática no contexto do IFRS campus Caxias do Sul.",
          "História, cinema e ações afirmativas: aprendendo com o cinema.",
          "Cinema, história e ações afirmativas: pensar e produzir audiovisual no IFRS - Campus Caxias do Sul.", "Laboratório de Acessibilidade e Ações Inclusivas."]

extensao = ["Trabalhando conhecimentos matemáticos com estudantes autistas no ensino médio do IFRS.",
            "Divulgação de temas da geografia por meio de um projeto de extensão no IFRS Caxias do Sul.",
            "Presença nas Escolas e nas Redes Sociais: relato das ações de extensão do Projeto Origens, Histórias e Trajetórias LGBTQIA+.",
            "Desenvolvendo o pensamento computacional de forma lúdica e desplugada com alunos do 6º e 7º ano do Ensino Fundamental de escolas públicas.",
            "II Curso de Educação Especial e a Gestão da Educação Especial na Escola Pública.",
            "Iniciação tecnológica com alunos do ensino fundamental utilizando programação em blocos.",
            "“Educação Especial e Educação Inclusiva: entre Mitos, o impossível e a vida”, no II curso de educação especial.",
            "Robótica no ensino fundamental.", "Oficina para formação de professores voltada para o desenvolvimento carros autônomos.",
            "Altas Habilidades e Superdotação (AHSD) - precisamos falar sobre isso!",
            "Práticas pedagógicas inclusivas: estratégias e possibilidades de ensino e aprendizagem.",
            "“(R)Existir: diálogos sobre gêneros e sexualidades”: relato das ações que concretizam a publicação do livro do projeto Origens, Histórias e Trajetórias LGBTQIA+.",
            "Mundo para os sentidos, sentidos para o mundo: divulgação científica para a promoção do aprendizado em geografia.", "Projeto Elas na metalurgia."]

# configurei o streamlit para abrir em wide mode
st.set_page_config(layout="wide")

if os.path.isfile("data.csv"):
    data = pd.read_csv("data.csv")
    st.subheader("Dataframe")
else:
    data = pd.DataFrame(columns=["trabalho", "avaliador", "soma"])

with st.sidebar:
    st.image("https://github.com/sid-almeida/vii_jornada/blob/main/image%20(3).png?raw=true", width=250)
    st.write('---')
    choice = st.radio("**Navegação:**", ("Avaliação de Trabalhos", "DataFrame","Ranking", "Sobre"))
    st.success("Esta aplicação tem como objetivo executar a **limpeza automatizada de dados** para a geração de **certificados**.")
    st.write('---')

if choice == "Avaliação de Trabalhos":
    st.subheader("Avaliação de Trabalhos")
    st.write('---')
    # selectbox para escolher o avaliador
    avaliador = st.selectbox("**Avaliador:**", [" ",
                                                "Melina Bolfe",
                                                "Jaqueline Sirena",
                                                "Marla Regina Vieira",
                                                "Cristiane Guazzelli Boschi",
                                                "Gisele Bacarim",
                                                "Josimar Vargas",
                                                "Ana Claudia",
                                                "Vinicius Waechter Dias",
                                                "André Ricardo Furlan",
                                                "Darlã Nogara Oliveira",
                                                "Diomar Caríssimo Selli Deconto",
                                                "Kelen Katlen Staehler Indicatti",
                                                "Juvenal Ballista Kleinowski",
                                                "João Verges",
                                                "Joanir Luís Kalnin",
                                                "Ana Caroline Dzulinski"])
    st.info("Selecione o nome do avaliador.")
    st.write('---')

    # selectbox para escolher o trabalho
    trabalho = st.selectbox("**Trabalho:**", [" ",
                               "Transformações no ensino da geografia na educação básica: um projeto de integração didática no contexto do IFRS campus Caxias do Sul.",
                               "Utilização de recurso didático para o ensino das horas como estratégia para uma melhor formação didática e inclusiva docente.",
                               "Ensino da multiplicação como estratégia para formação docente em didática e educação inclusiva.",
                               "Uso da balança de dois pratos como recurso pedagógico para o ensino das equações de 1° grau: estratégia para formação docente em didática e educação inclusiva.",
                               "Monitoria em filosofia.",
                               "Dois E.V.A’s e um molde: como facilitar o ensino das áreas e circunferências de um círculo.",
                               "1a Edição (2022) - O saber e o âmbito profissional: desenvolvimento humano e compromisso social.",
                               "Estudos em didática: caminhos possíveis para a formação docente pelo ensino de análise combinatória.",
                               "Superando desafios: a sinergia entre esporte e educação.",
                               "Monitoria em Educação Física: aprendizagens e convivialidade.",
                               "História, cinema e ações afirmativas: aprendendo com o cinema.",
                               "Recurso didático para o ensino de frações: estratégia para formação docente.",
                               "Laboratório de matemática:um ambiente para pesquisas no ensino e na prática da matemática.",
                               "Experiência voluntária em projeto de inclusão por meio da cultura corporal.",
                               "Tempo-Livro: promoção da leitura no IFRS - Campus Caxias do Sul.",
                               "Cinema, história e ações afirmativas: pensar e produzir audiovisual no IFRS - Campus Caxias do Sul.",
                               "Aprendizagem de Robótica por meio da construção e da programação de robôs.",
                               "Laboratório de Acessibilidade e Ações Inclusivas.",
                               "Tutoria de pares com foco na inclusão acadêmica de estudantes com necessidades educacionais específicas.",
                               "Cosmos, uma Viagem pelo Universo.",
                               "Monitoria de química: compartilhando saberes.",
                               "Uso da balança de dois pratos como recurso pedagógico para o ensino das equações de 1º grau: estratégia para formação docente em didática e educação inclusiva.",
                               "Fortalecendo as bases matemáticas: o curso de Pré-Cálculo como oportunidade para a transição da matemática do ensino médio para a do ensino superior.",
                               "Monitoria de física para estudantes com necessidades específicas: promovendo igualdade de oportunidades de aprendizado.",
                               "Construção de recurso na formação de professores, estratégia para o ensino da geometria.",
                               "Monitoria de Física para o Ensino Médio no Campus Caxias do Sul do IFRS.",
                               "O saber e o âmbito profissional: desenvolvimento humano e compromisso social.",
                               "Jogo da Memória para a fixação do aprendizado das figuras geométricas.",
                               "Gamificação, mídia digital e oficinas educativas no Ensino de Biologia: influência no processo de ensino e aprendizagem.",
                               "Ações desenvolvidas e auxiliadas pelo FabLab (Laboratório de Fabricação) do IFRS - Campus Caxias do Sul.",
                               "A Coleção geológica didática como recurso didático para ensino de temas de geologia no ensino médio.",
                               "Revolucionando o Ensino de Geografia: Geoprototipagem Tridimensional de modelos de terreno para uma Educação de Qualidade e Impacto.",
                               "Trabalhando conhecimentos matemáticos com estudantes autistas no ensino médio do IFRS.",
                               "Avaliação da qualidade ambiental por meio do bioensaio Trad-MCN e uso do Instagram como ferramenta de aprendizagem significativa.",
                               "Cultura Maker em Práticas Escolares no Ensino Fundamental Anos Finais.",
                               "Elaboração de filmes biodegradáveis de alginato de sódio e quitosana incorporando extrato da casca de pinhão (Araucaria angustifolia) para uso como curativos antimicrobianos e antifúngicos.",
                               "Estudo e desenvolvimento de robôs autônomos: atividades de pesquisa e práticas em robótica para estudantes do ensino médio técnico.",
                               "Cultura Maker: como atividades práticas e a criatividade influenciam no aprendizado.",
                               "Matemática na Wikipédia: avaliando e melhorando a qualidade do conteúdo disponível.",
                               "O que é matemática? por que ensinar? como se ensina e como se aprende?: algumas concepções de professores de Matemática da Educação Básica.",
                               "Formando especialistas em computação quântica: desenvolvimento de programas de capacitação.",
                               "Cultura maker: inserindo a robótica como prática pedagógica para os anos iniciais.",
                               "Estratégias de divulgação para impulsionar os acessos à REMAT.",
                               "Cadeias de Markov.",
                               "Divulgação de temas da geografia por meio de um projeto de extensão no IFRS Caxias do Sul.",
                               "Presença nas Escolas e nas Redes Sociais: relato das ações de extensão do Projeto Origens, Histórias e Trajetórias LGBTQIA+.",
                               "Desenvolvendo o pensamento computacional de forma lúdica e desplugada com alunos do 6º e 7º ano do Ensino Fundamental de escolas públicas.",
                               "II Curso de Educação Especial e a Gestão da Educação Especial na Escola Pública.",
                               "Iniciação tecnológica com alunos do ensino fundamental utilizando programação em blocos.",
                               "“Educação Especial e Educação Inclusiva: entre Mitos, o impossível e a vida”, no II curso de educação especial.",
                               "Robótica no ensino fundamental.",
                               "Oficina para formação de professores voltada para o desenvolvimento carros autônomos.",
                               "Inclusão digital na sala de aula: educação programada para o futuro.",
                               "Altas Habilidades e Superdotação (AHSD) - precisamos falar sobre isso!",
                               "Práticas pedagógicas inclusivas: estratégias e possibilidades de ensino e aprendizagem.",
                               "“(R)Existir: diálogos sobre gêneros e sexualidades”: relato das ações que concretizam a publicação do livro do projeto Origens, Histórias e Trajetórias LGBTQIA+.",
                               "Mundo para os sentidos, sentidos para o mundo: divulgação científica para a promoção do aprendizado em geografia.",
                               "Projeto Elas na metalurgia."])
    st.info("Selecione o trabalho que deseja avaliar.")
    st.write('---')

    # Critérios de avaliação insert
    st.subheader("**Critérios de Avaliação:**")
    crit1 = st.number_input("1. Clareza do texto escrito ou apresentado capacidade de síntese, correçao e de linguagem.", min_value=0, max_value=10, value=0, step=1)
    crit2 =st.number_input("2. Domínio do conteúdo apresentado.", min_value=0, max_value=15, value=0, step=1)
    crit3 =st.number_input("3. Relevância e originalidade.", min_value=0, max_value=15, value=0, step=1)
    crit4 =st.number_input("4. Coerência entre o tema, o(s) objetivo(s) e o trabalho apresentado.", min_value=0, max_value=10, value=0, step=1)
    crit5 =st.number_input("5. Descrição da metodologia de forma concisa e clara.", min_value=0, max_value=10, value=0, step=1)
    crit6 =st.number_input("6. Síntese dos resultados (parciais/finais) e perspectivas futuras coerentes e relacionadas aos objetivos propostos.", min_value=0, max_value=5, value=0, step=1)
    crit7 =st.number_input("7. Distribuição adequada do conteúdo ao tempo disponível.", min_value=0, max_value=5, value=0, step=1)
    crit8 =st.number_input("8. Uso adequado de tópicos (gráficos, tabelas, quadros, fotos, figuras) visando auxiliar na apresentação do trabalho.", min_value=0, max_value=5, value=0, step=1)
    crit9 =st.number_input("9. Experiência e competência demonstrada, especialmente na área da pesquisa proposta.", min_value=0, max_value=10, value=0, step=1)
    crit10 =st.number_input("10. Qualidade e regularidade da produção científica.", min_value=0, max_value=5, value=0, step=1)
    crit11 =st.number_input("11. Caráter interdisciplinar.", min_value=0, max_value=5, value=0, step=1)
    crit12 =st.number_input("12. Impacto na formação do estudante.", min_value=0, max_value=5, value=0, step=1)
    # verifiquei em qual grupo "extensao", "pesquisa" e "ensino" o trabalho escolhido se encaixa e adicionei o nome do grupo em str na variável "projeto"
    projeto = ""
    if trabalho in pesquisa:
        projeto = "Pesquisa"
    elif trabalho in ensino:
        projeto = "Ensino"
    elif trabalho in extensao:
        projeto = "Extensão"
    else:
        projeto = " "
    st.write('---')
    # Criei um dataframe com as colunas "trabalho" ,"avaliador" e "media" e adicionei os valores das variáveis coletadas
    data_collected = pd.DataFrame(columns=["trabalho", "avaliador", "projeto", "soma"])
    data_collected["trabalho"] = [trabalho]
    data_collected["avaliador"] = [avaliador]
    data_collected["soma"] = [crit1 + crit2 + crit3 + crit4 + crit5 + crit6 + crit7 + crit8 + crit9 + crit10 + crit11 + crit12]
    data_collected["projeto"] = [projeto]

    # Botão para avalilar
    if st.button("Avaliar"):
        # Verifiquei se o nome do trabalho já está no dataframe
        if trabalho in data["trabalho"].values:
            # Se estiver, somei o valor da avaliação com o valor já existente e dividir por 2
            data.loc[data["trabalho"] == trabalho, "soma"] = (data.loc[data["trabalho"] == trabalho, "soma"] + (crit1 + crit2 + crit3 + crit4 + crit5 + crit6 + crit7 + crit8 + crit9 + crit10 + crit11 + crit12)) / 2
            # Adicionei o nome do novo avaliador na coluna "avaliador" desta forma "valor antigo" + "&" + " novo valor"
            data["avaliador"] = data["avaliador"].str.cat(data_collected["avaliador"], sep="&")
            st.success("Avaliação realizada com sucesso!")
        else:
            # Se não estiver, cocatene o dataframe data_collected com o dataframe data
            data = pd.concat([data, data_collected], ignore_index=True)
            st.success("Avaliação realizada com sucesso!")
        # Salvei o dataframe em um arquivo csv
        data.to_csv("data.csv", index=False)

if choice == "DataFrame":
    st.subheader("DataFrame")
    st.write("**Aqui você pode visualizar os dados coletados até o momento.**")
    st.write('---')
    # Mostrei o dataframe
    if os.path.isfile("data.csv"):
        st.subheader("**Dataframe:**")
        st.dataframe(data)
        st.write('---')
    else:
        st.warning("Não há dados para exibir.")
        data = pd.DataFrame(columns=["trabalho", "avaliador", "soma"])

if choice == "Ranking":
    st.subheader("Ranking")
    st.write('---')
    # Se o dataframe não estiver vazio, mostrei os rankings
    if os.path.isfile("data.csv"):
        # Criei um PIVOT TABLE para mostrar o top 3 trabalhos com projeto de pesquisa
        st.subheader("**Ranking de Trabalhos com Projeto de Pesquisa:**")
        st.write("**Top 3:**")
        st.write(data[data["projeto"] == "Pesquisa"].pivot_table(index=["trabalho"], values=["soma"], aggfunc=np.sum).sort_values(by="soma", ascending=False).head(3))
        st.write('---')
        # Criei um PIVOT TABLE para mostrar o top 3 trabalhos com projeto de ensino
        st.subheader("**Ranking de Trabalhos com Projeto de Ensino:**")
        st.write("**Top 3:**")
        st.write(data[data["projeto"] == "Ensino"].pivot_table(index=["trabalho"], values=["soma"], aggfunc=np.sum).sort_values(by="soma", ascending=False).head(3))
        st.write('---')
        # Criei um PIVOT TABLE para mostrar o top 3 trabalhos com projeto de extensão
        st.subheader("**Ranking de Trabalhos com Projeto de Extensão:**")
        st.write("**Top 3:**")
        st.write(data[data["projeto"] == "Extensão"].pivot_table(index=["trabalho"], values=["soma"], aggfunc=np.sum).sort_values(by="soma", ascending=False).head(3))
        st.write('---')
        # Criei um Top 3 geral de todos os trabalhos
        st.subheader("**Ranking Geral:**")
        st.write("**Top 3:**")
        st.write(data.pivot_table(index=["trabalho"], values=["soma"], aggfunc=np.sum).sort_values(by="soma", ascending=False).head(3))
        st.write('---')
    else:
        st.warning("Faça a avaliação dos trabalhos para exibir o resultado.")

if choice == "Sobre":
    st.subheader("Sobre o Projeto")
    st.write('---')
    st.write("**Sobre o App**:\nEste aplicativo é um Software criado com o objetivo de automatizar a limpeza de dados para a geração de certificados no **IFRS - Campus Caxias do Sul**.")
    st.write("**Tenologia**:\nEle utiliza **Python** em conjunto com a biblioteca **Pandas** para executar a limpeza dos dados de forma automática.")
    st.write("**Implementação**:\nA implementação foi feita em forma de **WebApp** na plataforma **Streamlit** para facilitar o acesso.")
    st.write('---')
st.write('Made with ❤️ by [Sidnei Almeida](https://www.linkedin.com/in/saaelmeida93/)')
