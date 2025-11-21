
### **Projeto Final: Gerenciador Financeiro Pessoal**

**Autor:** Bruno Junges

**Orientador:** Prof. Luciano Zanuz

**Curso:** Análise e Desenvolvimento de Sistemas

**Instituição:** Centro Universitário Senac-RS

### **Resumo do Projeto**

A ausência de ferramentas acessíveis e intuitivas para o controle financeiro pessoal representa um obstáculo significativo para a saúde financeira de muitos indivíduos. A complexidade de aplicativos existentes ou a insegurança de métodos manuais, como planilhas, frequentemente levam à falta de visibilidade sobre os padrões de gastos, dificultando o planejamento e a economia. Este projeto apresenta o desenvolvimento de uma aplicação web dedicada ao gerenciamento de despesas, que se destaca pela simplicidade de uso, autenticação segura com isolamento total dos dados de cada usuário, e funcionalidades inteligentes, como a conversão automática de moedas via API externa. A implementação desta solução proporciona aos usuários uma plataforma centralizada e clara para registrar, visualizar e analisar seus gastos, capacitando-os a tomar decisões financeiras mais informadas e a assumir o controle de suas finanças com maior eficácia e privacidade.

### **Definição do Problema**

O gerenciamento financeiro pessoal é um pilar fundamental para a estabilidade econômica e o bem-estar individual. No entanto, uma parcela expressiva da população enfrenta dificuldades em manter um controle efetivo sobre suas despesas. Segundo dados e especialistas, a falta de organização financeira é uma das principais causas de endividamento e estresse (CONFERÊNCIA NACIONAL DE DIRETORES DE ESCOLA, 2020). A etapa de *discovery* do projeto, realizada através de pesquisa informal com estudantes universitários, revelou que as soluções atuais se dividem em dois extremos: ou são sistemas excessivamente complexos, ou são métodos rudimentares e inseguros, que não oferecem automação, visualização de dados ou segurança adequada.

Os principais problemas identificados e que esta solução busca resolver são:
*   **Praticidade:** A ausência de um método rápido e centralizado para registrar gastos, especialmente em moedas estrangeiras.
*   **Segurança e Privacidade:** A utilização de planilhas ou aplicativos que não garantem o isolamento de dados expõe informações financeiras sensíveis. A solução proposta resolve diretamente este problema através de um sistema de autenticação robusto, onde cada usuário só tem acesso aos seus próprios dados, e as senhas são protegidas por *hashing*.
*   **Usabilidade:** Foco em uma interface limpa e intuitiva, evitando a sobrecarga de funcionalidades desnecessárias para o controle diário.
*   **Visualização de Dados:** Fornecimento de uma visualização clara e imediata dos padrões de gastos através de gráficos, permitindo uma análise rápida.

Uma análise de projetos correlatos no mercado brasileiro evidencia o espaço para a nova solução:

| Característica | Mobills | Organizze | **Nosso Gerenciador** |
| :--- | :--- | :--- | :--- |
| **Modelo de Negócio** | Freemium / Assinatura | Freemium / Assinatura | **Totalmente Gratuito / Open-Source** |
| **Sistema de Login** | Sim | Sim | **Sim (com dados isolados por usuário)** |
| **Interface Responsiva** | Sim | Sim | **Sim (design mobile-first)** |
| **Conversão de Moeda** | Funcionalidade Premium | Funcionalidade Premium | **Integrada e gratuita (via API externa)** |
| **Visualização Gráfica** | Sim | Sim | **Sim (gráfico de barras por categoria)** |
| **Hospedagem** | Nuvem proprietária | Nuvem proprietária | **Pronto para deploy em qualquer serviço de nuvem (Render, etc.)** |

A análise demonstra que o projeto desenvolvido oferece um diferencial competitivo claro ao integrar funcionalidades premium em uma plataforma gratuita, segura e de código aberto.

### **Objetivos**

#### **Objetivo Geral**
Desenvolver uma aplicação web completa e segura que permita aos usuários realizar o gerenciamento de seus gastos pessoais de forma simples, intuitiva e centralizada, com isolamento de dados por conta de usuário.

#### **Objetivos Específicos (Concluídos)**
*   Implementação de um sistema de cadastro e login de usuários, garantindo a segurança das senhas através de técnicas de *hashing* (via Werkzeug) e a gestão de sessões (via Flask-Login).
*   Desenvolvimento de uma interface para o registro de novas despesas, incluindo descrição, valor, categoria, data e informações de parcelamento.
*   Criação de um dashboard principal para a visualização de gastos, com a capacidade de filtrar os dados por período (mês e ano).
*   Implementação de uma visualização gráfica (gráfico de barras) que exibe a distribuição percentual e absoluta dos gastos por categoria para análise rápida.
*   Integração bem-sucedida com uma API externa (ExchangeRate-API) para converter automaticamente despesas feitas em moedas estrangeiras (USD, EUR, GBP) para BRL.
*   Garantia de uma interface responsiva, que proporciona uma boa experiência de uso tanto em desktops quanto em dispositivos móveis.
*   Implementação das funcionalidades CRUD completas (Create, Read, Update, Delete) para os gastos registrados.
*   Criação de uma lógica de interface interativa com JavaScript para a exibição condicional do campo de parcelas.

### **Stack Tecnológico**

A seleção das tecnologias para este projeto foi guiada pelos princípios de leveza, robustez e facilidade de implantação.

*   **Python:** Escolhido como a linguagem de programação do backend devido à sua sintaxe limpa e vasto ecossistema. A versão 3.x foi utilizada.

*   **Flask:** Micro-framework web para Python, selecionado por sua simplicidade e flexibilidade, ideal para o escopo do projeto.

*   **Flask-Login:** Biblioteca para gerenciar as sessões dos usuários (login, logout, proteção de rotas), essencial para a funcionalidade de autenticação.

*   **Werkzeug:** Toolkit utilizado para implementar a segurança das senhas, especificamente para gerar e verificar os *hashes*.

*   **SQLite:** Sistema de gerenciamento de banco de dados relacional *serverless*, utilizado para armazenamento de dados em um único arquivo.

*   **HTML5, CSS3, JavaScript:** Tecnologias padrão para a estruturação, estilização e interatividade do frontend.

*   **Gunicorn:** Servidor HTTP WSGI para servir a aplicação Flask em ambiente de produção (Render).

*   **ExchangeRate-API:** API externa para obter taxas de câmbio em tempo real para a funcionalidade de conversão de moeda.

*   **Biblioteca `requests`:** Biblioteca Python para realizar as requisições HTTP para a API de câmbio.

### **Descrição da Solução**

A solução implementada é uma aplicação web completa e segura. O fluxo do usuário começa em uma página de login, onde ele pode acessar sua conta ou se registrar. A segurança é garantida desde o início, com o armazenamento das senhas em formato de hash, impedindo o acesso indevido.

Uma vez autenticado, o usuário é direcionado ao seu dashboard pessoal. A interface é dividida em uma barra lateral persistente (que se torna uma gaveta em dispositivos móveis) e uma área de conteúdo principal. A barra lateral permite a navegação entre os meses e o registro rápido de novas despesas. O formulário de adição é interativo, exibindo o campo de parcelas apenas quando a categoria correspondente é selecionada.

A área de conteúdo principal exibe as informações financeiras exclusivas daquele usuário. No topo, um resumo apresenta o total gasto e um gráfico de barras que ilustra a distribuição dos gastos por categoria. Abaixo, uma tabela detalhada lista todos os gastos individuais, com controles para editar ou excluir cada registro através de modais de confirmação.

<img width="1536" height="1024" alt="Visão Geral da Solução" src="https://github.com/user-attachments/assets/7e47f654-5cc2-4788-895c-01b364847e19" />

A tela principal do sistema está representada abaixo:

<img width="1916" height="904" alt="Tela Principal do Sistema" src="https://github.com/user-attachments/assets/37deef8f-7d79-4c6a-98da-ae9ebb70b3f6" />

### **Arquitetura**

O código-fonte do projeto está disponível no GitHub:
**https://github.com/BrunoJunges/Projeto-Gerenciamento-de-gastos**

A arquitetura da aplicação segue o padrão de 3 camadas (3-Tier Architecture):

<img width="1536" height="1024" alt="Diagrama de Arquitetura" src="https://github.com/user-attachments/assets/e70cda14-b515-4dc0-bb2b-00c4fa4fde06" />

Foram gerados os seguintes artefatos durante o desenvolvimento:

1.  **Benchmarking (Tabela Comparativa):** Apresentada na seção "Definição do Problema".
2.  **Personas:** Criação da persona "Ana", 25 anos, estudante, para guiar o design e as funcionalidades.
3.  **Histórias de Usuário:** O backlog foi guiado por histórias como: "Eu quero me cadastrar e ter uma conta segura para que meus dados financeiros sejam privados."
4.  **Diagrama Entidade-Relacionamento (DER):** O modelo de dados consiste em `usuarios` e `gastos`, com uma relação de um-para-muitos.
5.  **Protótipos de Interface:** O desenvolvimento foi iniciado a partir de wireframes de baixa fidelidade.

### **Validação**
A validação foi realizada através de um teste de usabilidade com 3 usuários. A cada participante foram dadas as seguintes tarefas:

#### **Estratégia**
1.  Criar uma nova conta.
2.  Fazer login.
3.  Adicionar três gastos: um em Reais, um em Dólares e um parcelado.
4.  Navegar para o mês anterior.
5.  Editar a descrição de um dos gastos.
6.  Excluir um dos gastos.

#### **Consolidação dos Dados Coletados**
Todos os participantes completaram 100% das tarefas com sucesso. O feedback foi consolidado abaixo:

| Tópico | Feedback Positivo | Sugestão de Melhoria |
| :--- | :--- | :--- |
| **Interface** | "Muito limpa e fácil de entender", "O gráfico é ótimo para ver o resumo" | A cor do botão de edição poderia ser mais contrastante. |
| **Funcionalidade** | "A conversão de moeda é incrível", "Adorei que o campo de parcela só aparece quando precisa" | "Seria legal poder cadastrar gastos recorrentes." |
| **Responsividade**| "Funciona bem no celular", "Gostei que o menu lateral vira um botão" | Nenhuma sugestão de melhoria foi apontada. |

A análise indica que os objetivos de simplicidade, usabilidade e funcionalidade foram plenamente atingidos.

### **Conclusões**

Este projeto logrou êxito em desenvolver uma aplicação de gerenciamento financeiro que atende aos objetivos propostos, solucionando os problemas identificados de complexidade e, principalmente, de insegurança e falta de privacidade das ferramentas existentes. A plataforma final oferece um sistema multi-usuário seguro, uma interface intuitiva e responsiva, e funcionalidades avançadas como a conversão de moedas e a visualização gráfica de dados, provando ser uma ferramenta eficaz para o controle financeiro pessoal.

#### **Limitações do Projeto e Perspectivas Futuras**
O uso do SQLite não é recomendado para uma aplicação em larga escala, e a API de câmbio possui um limite de requisições no plano gratuito.

Como trabalhos futuros, vislumbram-se as seguintes evoluções:
1.  **Migração para PostgreSQL:** Substituir o SQLite por um banco de dados mais robusto.
2.  **Implementação de Gastos Recorrentes:** Adicionar a funcionalidade para despesas que se repetem mensalmente.
3.  **Relatórios Avançados:** Criar uma seção de relatórios para comparar gastos entre diferentes períodos.
4.  **Testes Automatizados:** Implementar uma suíte de testes para garantir a estabilidade do código.

### **Referências Bibliográficas**

CONFERÊNCIA NACIONAL DE DIRETORES DE ESCOLA (CNDL); SERVIÇO DE PROTEÇÃO AO CRÉDITO (SPC Brasil). *Perfil e comportamento do endividamento brasileiro*. 2020.

FLASK DOCUMENTATION. *Flask: Web Development, One Drop at a Time*. Pallets. Disponível em: https://flask.palletsprojects.com/. Acesso em: 22 set. 2025.

FLASK-LOGIN DOCUMENTATION. *Flask-Login 0.6.2*. Disponível em: https://flask-login.readthedocs.io/. Acesso em: 23 set. 2025.

GRINBERG, Miguel. *Flask Web Development: Developing Web Applications with Python*. 2nd ed. O'Reilly Media, 2018.

PYTHON SOFTWARE FOUNDATION. *Python Language Reference, version 3.11*. Disponível em: https://docs.python.org/3/reference/. Acesso em: 22 set. 2025.

SQLITE. *SQLite Documentation*. Disponível em: https://www.sqlite.org/docs.html. Acesso em: 22 set. 2025.

WERKZEUG DOCUMENTATION. *Passwords*. Pallets. Disponível em: https://werkzeug.palletsprojects.com/en/3.0.x/utils/#passwords. Acesso em: 23 set. 2025.
