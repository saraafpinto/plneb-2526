O ficheiro pesquisar.html é a interface de busca avançada do MedDic. Esta página permite ao utilizador interagir com a base de dados JSON de forma dinâmica, aplicando filtros linguísticos específicos.

Componentes Principais
    1. Formulário de Pesquisa (Bootstrap 5)
    O topo da página apresenta um formulário que utiliza o sistema de Input Groups do Bootstrap.
    - Input Text: Captura a query (termo de pesquisa).
    - Switches de Opções: Dois interruptores modernos (form-switch) que permitem ao utilizador definir o comportamento da busca:
        - Case Sensitive: Ativa a distinção entre maiúsculas e minúsculas.
        - Palavra Exata (Word Boundary): Garante que a pesquisa não devolva sub-palavras (ex: procurar "dor" não encontrará "adormecer").

    2. Tabela de Resultados (DataTables)
    Os resultados são renderizados numa tabela que herda o comportamento do script.js.
    - ID tabela_conceitos: Este ID é o gatilho que ativa a biblioteca DataTables, permitindo ordenação instantânea e paginação.
    - Filtro | safe: Essencial para que as tags HTML <b> (geradas no backend para destacar o termo pesquisado) sejam interpretadas corretamente pelo navegador.
    - Estilo: Utiliza as classes table-hover e table-striped para garantir uma leitura confortável de descrições médicas longas.

Lógica de Funcionamento
O fluxo de dados para esta página funciona da seguinte forma:
- Envio: O utilizador submete o termo via método GET.
- Processamento (Python): * O backend verifica o estado dos switches (on/off).
    - Aplica a lógica de strings para encontrar correspondências no JSON.
    - Cria novas chaves no dicionário (desig_label e descricao) onde a palavra pesquisada é envolvida por tags de negrito.
- Renderização: O Jinja2 percorre a lista de resultados e preenche a tabela.