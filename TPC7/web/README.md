O objetivo deste TPC7 é transformar um dicionário médico estruturado em formato JSON numa aplicação web interativa e fácil de navegar utilizando o Bootstrap.

***Funcionalidades***
- Exploração A-Z: Navegação intuitiva através de um índice alfabético dinâmico.
- Interface Responsiva: Otimizada para dispositivos móveis e desktop.
- Filtro Inteligente: Agrupamento automático de termos por letra inicial.
- Páginas de Detalhe: Visualização clara da designação e da respetiva descrição técnica.

***Tecnologias Utilizadas***
O projeto utiliza uma stack moderna de Python para o backend e as tecnologias web mais recentes para o frontend:
- Python 3.12: Lógica de processamento de dados.
- Flask: Micro-framework para gestão de rotas e renderização de templates.
- Jinja2: Motor de templates para lógica dinâmica no HTML.
- Bootstrap 5.3: Framework de CSS para design responsivo e componentes modernos.

***O Papel do Bootstrap 5***
Para este projeto, foi utilizado o Bootstrap 5, a versão mais recente e robusta da framework. A escolha deveu-se a:
- Componentes Modernos: Utilização de Cards, Badges, Navbars e o sistema de Grid para uma organização visual limpa.
- Acessibilidade: Garantia de que os termos médicos são fáceis de ler, com tipografia adequada e contraste de cores.
- Links oficiais do Bootstrap utilizados:
    - Componente "Heroes" (Home Page): https://getbootstrap.com/docs/5.3/examples/heroes/
    - Sistema de Grelha na lista de conceitos (Grid System): https://getbootstrap.com/docs/5.3/layout/grid/ 
    - Cards (Lista de Conceitos): https://getbootstrap.com/docs/5.3/components/card/
    - Utilitários de Flexbox no índice alfabético: https://getbootstrap.com/docs/5.3/utilities/flex/

***Estrutura do Projeto***

- aula7_2.py - Este é o servidor backend em Flask. Ele é responsável por:
    - Carregamento de Dados: Lê o ficheiro dicionario_medico.json e converte-o num dicionário Python.
    - Gestão de Rotas: Define o que acontece quando o utilizador acede a /, /conceitos ou /saber_mais.
    - Lógica de Negócio: Filtra as chaves do dicionário (as designações) e envia-as para os templates HTML.
    - Tratamento de Erros: Garante que, se um conceito não existir, o servidor não falha.

- templates/layout.html
    - Este é o ficheiro "pai" que usa o conceito de Template Inheritance.
    - Bootstrap 5 Setup: Contém os links do CDN para o CSS e JS do Bootstrap.
    - Elementos Globais: Define a navbar (menu) e o footer (rodapé) que aparecem em todas as páginas.
    - Blocos Dinâmicos: Usa {% block body %} para que as outras páginas possam injetar o seu conteúdo específico sem repetir o código do menu.

- templates/home.html 
    - Focado na experiência do utilizador.
    - Bootstrap Heroes: Utiliza um layout de impacto com um título grande e botões de chamada para ação (Call to Action).
    - Explica brevemente o que é o dicionário médico antes do utilizador mergulhar nos dados técnicos.

- templates/conceitos.html
    - Navegação A-Z: Implementa um índice alfabético "sticky" (que persegue o scroll) para facilitar a consulta.
    - Lógica de Agrupamento: Usa ciclos for e if do Jinja2 para separar os termos por letra, criando secções visuais claras.
    - Grid Responsiva: Usa o sistema de colunas do Bootstrap para mostrar os termos em grelha, otimizando o espaço no ecrã.

- templates/conceito.html - A página final onde o conhecimento é entregue.
    - Foco no Conteúdo: Apresenta a designação e a descrição de forma destacada.
    - Breadcrumbs: Inclui trilhos de navegação para que o utilizador possa voltar facilmente à lista sem usar o botão "retroceder" do browser.

- templates/sober_mais.html - A página de suporte e documentação do projeto.
    - Informação Técnica: Detalha as bibliotecas utilizadas e o propósito do trabalho para a cadeira de PLN.
    - Estética: Usa componentes informativos como "Cards" e listas estilizadas para explicar o fluxo de dados (JSON ➔ Python ➔ Web).