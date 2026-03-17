Este script em Python realiza web scraping do site Atlas da Saúde para recolher informações sobre doenças organizadas de A a Z, utilizando as bibliotecas requests (para fazer pedidos HTTP) e BeautifulSoup (para fazer o parsing do HTML).

Um dos pontos importantes do código é a função extrair_pagina(url), que encapsula toda a lógica de extração de dados de cada página. Esta função:
- Obtém o conteúdo HTML da página;
- Identifica todas as entradas de doenças através da classe "views-row";
- Extrai o nome da doença, uma descrição breve e o link para a página detalhada;
- Faz um segundo pedido HTTP para cada doença, permitindo obter a descrição completa diretamente da página individual.

O script percorre automaticamente todas as letras do alfabeto (string.ascii_lowercase), construindo dinamicamente os URLs e agregando os resultados num único dicionário. A junção dos dados é feita usando o operador |, que permite combinar dicionários de forma simples e eficiente.

Outros aspetos relevantes:
- Uso de .strip() para limpar espaços em branco nas descrições;
- Estruturação dos dados em formato chave-valor, facilitando o acesso posterior;
- Exportação para JSON com ensure_ascii=False, garantindo suporte a caracteres especiais (como acentos);
- Organização clara do código, separando a lógica de extração da lógica de controlo do programa.

No final, todos os dados são guardados no ficheiro doencasTPC.json, já formatado e pronto para reutilização em outras aplicações.