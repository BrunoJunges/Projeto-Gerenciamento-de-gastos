**Projeto Final: Gerenciador Financeiro Pessoal**

**Autor: Bruno Junges**

**Orientador: Prof. Luciano Zanuz**

**Curso: Análise e Desenvolvimento de Sistemas**

**Instituição: Centro Universitário Senac-RS**

### **Resumo do Projeto**

A ausência de ferramentas acessíveis e intuitivas para o controle financeiro pessoal representa um obstáculo significativo para a saúde financeira de muitos indivíduos. A complexidade de aplicativos existentes ou a insegurança de métodos manuais, como planilhas, frequentemente levam à falta de visibilidade sobre os padrões de gastos, dificultando o planejamento e a economia. Este projeto apresenta o desenvolvimento de uma aplicação web dedicada ao gerenciamento de despesas, que se destaca pela simplicidade de uso, segurança de dados do usuário e funcionalidades inteligentes, como a conversão automática de moedas via API externa. A implementação desta solução proporciona aos usuários uma plataforma centralizada e clara para registrar, visualizar e analisar seus gastos, capacitando-os a tomar decisões financeiras mais informadas e a assumir o controle de suas finanças com maior eficácia.

### **Definição do Problema**

O gerenciamento financeiro pessoal é um pilar fundamental para a estabilidade econômica e o bem-estar individual. No entanto, uma parcela expressiva da população enfrenta dificuldades em manter um controle efetivo sobre suas despesas. Segundo dados e especialistas, a falta de organização financeira é uma das principais causas de endividamento e estresse (CONFERÊNCIA NACIONAL DE DIRETORES DE ESCOLA, 2020). A etapa de *discovery* do projeto, realizada através de pesquisa informal com estudantes universitários, revelou que as soluções atuais se dividem em dois extremos: ou são sistemas excessivamente complexos, com curvas de aprendizado íngremes e modelos de assinatura custosos, ou são métodos rudimentares e inseguros, como planilhas em nuvem ou cadernos de anotações, que não oferecem automação, visualização de dados ou segurança adequada.

Os principais problemas identificados com diversos esntrevistados e que esta solução busca resolver são:
*   **Praticidade:** A ausência de um método rápido e centralizado para registrar gastos, especialmente aqueles realizados em moedas estrangeiras durante viagens ou compras online, torna o processo tedioso e propenso a erros.
*   **Segurança e Privacidade:** A utilização de planilhas ou aplicativos que não garantem o isolamento de dados e a segurança das credenciais expõe informações financeiras sensíveis. A implementação de um sistema de autenticação robusto, com hashing de senhas, é um requisito não negociável.
*   **Usabilidade:** Muitas ferramentas de mercado sobrecarregam o usuário com funcionalidades avançadas que não são necessárias para um controle diário, gerando frustração e abandono. A solução proposta foca em uma interface limpa e intuitiva.
*   **Visualização de Dados:** A simples listagem de despesas é insuficiente. É necessário fornecer ao usuário uma visualização clara e imediata de seus padrões de gastos, como a distribuição por categoria, para permitir uma análise rápida e eficaz.

Uma análise de projetos correlatos no mercado brasileiro evidencia o espaço para uma nova solução, conforme a tabela comparativa abaixo:

| Característica | Mobills | Organizze | **Nosso Gerenciador** |
| :--- | :--- | :--- | :--- |
| **Modelo de Negócio** | Freemium / Assinatura | Freemium / Assinatura | **Totalmente Gratuito / Open-Source** |
| **Sistema de Login** | Sim | Sim | **Sim (com dados isolados por usuário)** |
| **Interface Responsiva** | Sim | Sim | **Sim (design mobile-first)** |
| **Conversão de Moeda** | Funcionalidade Premium | Funcionalidade Premium | **Integrada e gratuita (via API externa)** |
| **Visualização Gráfica** | Sim | Sim | **Sim (gráfico de barras por categoria)** |
| **Hospedagem** | Nuvem proprietária | Nuvem proprietária | **Pronto para deploy em qualquer serviço de nuvem (Render, etc.)** |

A análise demonstra que o projeto desenvolvido oferece um diferencial competitivo claro ao integrar funcionalidades premium (como conversão de moeda) em uma plataforma gratuita, segura e de código aberto, atendendo a uma necessidade latente do público, especialmente estudantes e jovens profissionais.

### **Objetivos**

#### **Objetivo Geral**
Desenvolver uma aplicação web completa e segura que permita aos usuários realizar o gerenciamento de seus gastos pessoais de forma simples, intuitiva e centralizada, com isolamento de dados por conta de usuário.

#### **Objetivos Específicos**
*   Implementar um sistema de cadastro e login de usuários, garantindo a segurança das senhas através de hashings.
*   Desenvolver uma interface para o registro de novas despesas, incluindo descrição, valor, categoria e data.
*   Criar um dashboard principal para a visualização de gastos, com filtros por período (mês).
*   Implementar uma visualização gráfica (gráfico de barras) que exiba a distribuição percentual e absoluta dos gastos por categoria.
*   Integrar uma API externa de taxa de câmbio para converter e registrar automaticamente despesas feitas em moedas estrangeiras (USD, EUR, GBP) para BRL.
*   Garantir que a interface da aplicação seja responsiva, proporcionando uma boa experiência de uso tanto em desktops quanto em dispositivos móveis.
*   Implementar funcionalidades de edição e exclusão para os gastos registrados.
*   Adicionar uma lógica de interface interativa para campos condicionais, como o de registro de parcelas.

### **Stack Tecnológico**

A seleção das tecnologias para este projeto foi guiada pelos princípios de leveza, robustez, popularidade e facilidade de implantação.

*   **Python:** Escolhido como a linguagem de programação do backend devido à sua sintaxe limpa, vasta gama de bibliotecas e forte ecossistema para desenvolvimento web. A versão 3.x foi utilizada. (Referência: Python Software Foundation. *Python Language Reference*. Disponível em: https://docs.python.org/3/)

*   **Flask:** É um micro-framework web para Python. Foi selecionado por sua simplicidade, minimalismo e flexibilidade, permitindo a construção de uma aplicação web robusta sem o peso de frameworks maiores. Sua abordagem "micro" é ideal para projetos que necessitam de controle total sobre os componentes utilizados. (Referência: GRINBERG, Miguel. *Flask Web Development*. O'Reilly Media, 2018.)

*   **SQLite:** Um sistema de gerenciamento de banco de dados relacional contido em uma biblioteca C. Foi escolhido para o desenvolvimento local e para a versão de demonstração em nuvem devido à sua natureza *serverless* (sem servidor), que elimina a necessidade de configuração complexa. Os dados são armazenados em um único arquivo, facilitando o desenvolvimento e o deploy inicial. (Referência: *SQLite Documentation*. Disponível em: https://www.sqlite.org/docs.html)

*   **HTML5, CSS3, JavaScript:** Compõem a base do frontend. O HTML5 foi usado para a estruturação semântica do conteúdo, o CSS3 para a estilização (incluindo Flexbox para layout e Media Queries para responsividade), e o JavaScript para a interatividade do lado do cliente, como o controle de modais e a exibição condicional de campos de formulário.

*   **Gunicorn (Green Unicorn):** Um servidor HTTP WSGI para Python. É o padrão da indústria para servir aplicações Flask em produção. Foi escolhido para ser usado no ambiente de deploy (Render) por sua eficiência, estabilidade e capacidade de gerenciar múltiplos processos de trabalho. (Referência: *Gunicorn Documentation*. Disponível em: https://gunicorn.org/)

*   **ExchangeRate-API:** Uma API externa que fornece dados de taxas de câmbio em tempo real. Foi integrada ao projeto para a funcionalidade de conversão de moeda, demonstrando a capacidade da aplicação de interagir com serviços de terceiros para enriquecer seus dados. (Referência: *ExchangeRate-API Documentation*. Disponível em: https://www.exchangerate-api.com/docs)

*   **Biblioteca `requests`:** Uma biblioteca Python para realizar requisições HTTP. Foi a ferramenta escolhida para consumir a ExchangeRate-API a partir do backend Flask, devido à sua API simples e poderosa.

### **Descrição da Solução**

A solução implementada é uma aplicação web completa, projetada para resolver os problemas de gerenciamento financeiro de forma direta e segura. O fluxo do usuário começa em uma página de login, onde ele pode acessar sua conta ou se registrar. A segurança é garantida desde o início, com o armazenamento das senhas em formato de hash, impedindo o acesso indevido.

Uma vez autenticado, o usuário é direcionado ao dashboard principal. A interface é dividida em duas seções: uma barra lateral persistente (que se torna uma gaveta em dispositivos móveis) e uma área de conteúdo principal. A barra lateral serve como o centro de comando, permitindo a navegação entre os meses e, mais importante, o registro rápido de novas despesas através de um formulário intuitivo. Este formulário inclui campos para descrição, valor, moeda (com conversão automática para BRL via API externa), categoria (com uma lista pré-definida para garantir consistência) e um campo condicional para informações de parcelas, que aparece dinamicamente via JavaScript.

A área de conteúdo principal exibe as informações financeiras do período selecionado. No topo, um card de resumo apresenta o total gasto e um gráfico de barras que ilustra a distribuição dos gastos por categoria, oferecendo uma visão analítica imediata. Abaixo, uma tabela detalhada lista todos os gastos individuais, com informações claras sobre data, descrição, categoria (incluindo a parcela, se aplicável) e o valor em BRL, com o valor original em moeda estrangeira exibido para referência. Cada linha da tabela possui controles para editar ou excluir o registro, ações que são confirmadas através de modais para prevenir operações acidentais.

A figura abaixo ilustra a visão geral da solução:

`[Figura 1: Visão Geral da Solução - Um diagrama mostrando o fluxo: Usuário acessa via Navegador, que interage com a Aplicação Flask. A Aplicação Flask, por sua vez, se comunica com o Banco de Dados SQLite para dados internos e com a ExchangeRate-API para dados externos.]`

Um exemplo da lógica de conversão de moeda implementada no backend:
```python
def obter_valor_convertido(valor_original, moeda_original):
    if moeda_original == 'BRL':
        return valor_original
    try:
        url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{moeda_original}/BRL"
        response = requests.get(url)
        response.raise_for_status()
        dados_taxa = response.json()
        if dados_taxa.get('result') == 'success':
            taxa_conversao = dados_taxa['conversion_rate']
            return valor_original * taxa_conversao
    except Exception as e:
        print(f"ERRO: API de conversão falhou. {e}")
        return valor_original
```

A tela principal do sistema esta representada abaixo:

`[Figura 2: Tela]`


### **Arquitetura**

Todos os artefatos e o código-fonte do projeto estão disponíveis no repositório do GitHub:
**https://github.com/BrunoJunges/Projeto-Gerenciamento-de-gastos**

A arquitetura da aplicação segue o padrão de 3 camadas (3-Tier Architecture), como ilustrado na figura abaixo:

`[Figura 6: Arquitetura em Camadas - Um diagrama com três blocos: 1. Camada de Apresentação (Frontend: HTML, CSS, JavaScript, Renderização no Navegador); 2. Camada de Aplicação/Lógica (Backend: Python, Flask, Gunicorn, Lógica de Negócio); 3. Camada de Dados (Data Layer: SQLite, Banco de Dados). Setas indicam a comunicação entre as camadas.]`

Foram gerados os seguintes artefatos durante o desenvolvimento:

1.  **Benchmarking (Tabela Comparativa):** Apresentada na seção "Definição do Problema", comparando a solução desenvolvida com aplicativos de mercado.
2.  **Personas:** Foi criada uma persona principal para guiar o design e as funcionalidades: *Ana, 25 anos, estudante universitária. Precisa de uma ferramenta simples para controlar seus gastos mensais com alimentação, transporte e lazer, sem a complexidade de apps de investimento. Ocasionalmente faz compras online em dólar.*
3.  **Histórias de Usuário:** O backlog foi guiado por histórias de usuário, como:
    *   *Eu quero me cadastrar e ter uma conta segura para que meus dados financeiros sejam privados.*
    *   *Eu quero registrar um gasto em dólar para que a aplicação o converta automaticamente para reais.*
    *   *Eu quero ver um gráfico dos meus gastos por categoria para entender rapidamente para onde meu dinheiro está indo.*
4.  **Diagrama Entidade-Relacionamento (DER):** O modelo de dados consiste em duas tabelas principais:
    *   `users (id PK, username, password_hash)`
    *   `gastos (id PK, user_id FK, descricao, categoria, ..., valor_brl, info_parcela)`
    *   A relação é de *um-para-muitos* (um usuário pode ter muitos gastos).
5.  **Protótipos de Interface:** O desenvolvimento foi iniciado a partir de wireframes de baixa fidelidade desenhados para o dashboard principal e o fluxo de adição de gastos, focando na simplicidade e na disposição dos elementos.

### **Validação**
A validação da solução foi realizada através de um teste de usabilidade qualitativo. Uma amostra de 3 usuários com perfil semelhante à persona "Ana" (estudantes universitários com conhecimento básico de tecnologia) foi convidada a interagir com a aplicação hospedada no Render. A cada participante foram dadas as seguintes tarefas, sem instrução prévia:
#### **Estratégia**

1.  Criar uma nova conta.
2.  Fazer login.
3.  Adicionar três gastos: um em Reais, um em Dólares e um parcelado.
4.  Navegar para o mês anterior.
5.  Editar a descrição de um dos gastos.
6.  Excluir um dos gastos.

O objetivo era observar a facilidade de uso, a clareza da interface e identificar quaisquer pontos de fricção ou confusão.

#### **Consolidação dos Dados Coletados**
Os resultados foram extremamente positivos. Todos os 3 participantes completaram 100% das tarefas com sucesso e sem assistência. O feedback verbal coletado foi consolidado abaixo:

| Tópico | Feedback Positivo | Sugestão de Melhoria |
| :--- | :--- | :--- |
| **Interface** | "Muito limpa e fácil de entender", "O gráfico é ótimo para ver o resumo" | A cor do botão de edição poderia ser mais contrastante. |
| **Funcionalidade** | "A conversão de moeda é incrível, muito prático", "Adorei que o campo de parcela só aparece quando precisa" | "Seria legal poder cadastrar gastos recorrentes, como o aluguel." |
| **Responsividade**| "Funciona muito bem no celular." | Nenhum. |

A análise dos dados indica que os objetivos de simplicidade, usabilidade e funcionalidade foram plenamente atingidos. A principal sugestão para trabalho futuro é a implementação de despesas recorrentes.

### **Conclusões**

Este projeto logrou êxito em desenvolver uma aplicação de gerenciamento financeiro que atende aos objetivos propostos, solucionando os problemas identificados de complexidade e insegurança das ferramentas existentes. A plataforma final oferece um sistema seguro de múltiplos usuários, uma interface intuitiva e responsiva, e funcionalidades avançadas como a conversão de moedas em tempo real e a visualização gráfica de dados, provando ser uma ferramenta eficaz para o controle financeiro pessoal.

#### **Limitações do Projeto e Perspectivas Futuras**
Apesar do sucesso, o projeto possui limitações inerentes às escolhas tecnológicas feitas para este escopo. O uso do SQLite, embora ideal para desenvolvimento e demonstração, não é recomendado para uma aplicação em larga escala com alta concorrência de acesso. A dependência de um plano gratuito da ExchangeRate-API impõe um limite no número de conversões de moeda.

Como trabalhos futuros, vislumbram-se as seguintes evoluções:
1.  **Migração para PostgreSQL:** Substituir o SQLite por um banco de dados mais robusto como o PostgreSQL para suportar um ambiente de produção real.
2.  **Implementação de Gastos Recorrentes:** Adicionar a funcionalidade, sugerida pelos usuários, de cadastrar despesas que se repetem mensalmente.
3.  **Relatórios Avançados:** Criar uma nova seção de relatórios que permita ao usuário comparar gastos entre diferentes meses ou visualizar a evolução de uma categoria ao longo do tempo.
4.  **Desenvolvimento de API Pública:** Expor a API interna criada como uma API pública documentada, permitindo que outras aplicações interajam com a plataforma.

### **Referências Bibliográficas**

CONFERÊNCIA NACIONAL DE DIRETORES DE ESCOLA (CNDL); SERVIÇO DE PROTEÇÃO AO CRÉDITO (SPC Brasil). *Perfil e comportamento do endividamento brasileiro*. 2020. Disponível em: [Inserir link para a pesquisa, se encontrado].

FLASK DOCUMENTATION. *Flask: Web Development, One Drop at a Time*. Pallets. Disponível em: https://flask.palletsprojects.com/. Acesso em: 22 set. 2025.

GRINBERG, Miguel. *Flask Web Development: Developing Web Applications with Python*. 2nd ed. O'Reilly Media, 2018.

PYTHON SOFTWARE FOUNDATION. *Python Language Reference, version 3.11*. Disponível em: https://docs.python.org/3/reference/. Acesso em: 22 set. 2025.

SQLITE. *SQLite Documentation*. Disponível em: https://www.sqlite.org/docs.html. Acesso em: 22 set. 2025.
