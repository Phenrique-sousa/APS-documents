## **Caso de Uso UC1 - Acessar o sistema**

**Objetivo**: Permitir que o ator acesse o sistema com suas credenciais para utilizar os serviços da plataforma.  
**Requisitos**: **RF001**  
**Atores**: Usuário Comum  
**Condição de entrada**: O ator deseja acessar a plataforma e está na tela de login.

**Fluxo principal**:
1. O ator acessa a página de login.
2. O ator insere o e-mail e senha ou utiliza um certificado digital.
3. **Se escolher e-mail e senha**:
   - 3.1. O ator insere seu e-mail e senha nos campos correspondentes.
4. **Se escolher certificado digital**:
   - 4.1. O ator conecta o dispositivo do certificado digital ao computador.
   - 4.2. O sistema detecta o certificado digital.
5. O ator clica no botão "Entrar".
6. O sistema valida as credenciais fornecidas. **RN1**
7. O sistema verifica se o ator possui permissão de acesso.
8. O sistema redireciona o ator para a página inicial.

**Fluxos alternativos**:
- **FA1 - Esqueci minha senha**:
   - O ator clica no link "Esqueci minha senha". 
   - O sistema inicia o caso de uso **UC3 - Recuperar senha**.

**Fluxos de exceção**:
- **RN1 - Credenciais inválidas**:
   - **E1**: O sistema exibe a mensagem **MSG01** e solicita que o ator tente novamente.
   - **E2**: Se o certificado digital não for reconhecido, o sistema exibe a mensagem **MSG02**.

---

## **Caso de Uso UC2 - Acesso sem login**

**Objetivo**: Permitir que o ator acesse a plataforma sem login e realize compras utilizando diferentes métodos de pagamento.  
**Requisitos**: **RF002**  
**Atores**: Participante  
**Condição de entrada**: O ator acessa a plataforma sem realizar login.

**Fluxo principal**:
1. O ator acessa a tela de produtos.
2. O ator navega pelos produtos disponíveis.
3. O ator adiciona produtos ao carrinho.
4. O ator seleciona um método de pagamento (cartão de crédito, cartão de débito, Pix ou dinheiro).
5. O ator confirma a compra.
6. O sistema processa o pagamento e exibe a mensagem **MSG03**.

**Fluxos alternativos**:
- Nenhum.

**Fluxos de exceção**:
- **E1 - Falha no pagamento**:
   - O sistema exibe a mensagem **MSG04** e retorna ao carrinho de compras.

---

## **Caso de Uso UC3 - Recuperar senha**

**Objetivo**: Permitir que o usuário recupere sua senha caso tenha esquecido.  
**Requisitos**: **RF003**  
**Atores**: Usuário Comum (Organizador, Expositor, Participante)  
**Condição de entrada**: O ator acessa a tela de login e seleciona "Esqueci minha senha".

**Fluxo principal**:
1. O sistema exibe a tela de recuperação de senha solicitando o e-mail cadastrado.
2. O ator insere seu e-mail cadastrado e clica “Enviar”.
3. O sistema verifica se o e-mail está cadastrado. **RN2**
4. O sistema envia um link de redefinição para o e-mail informado. **MSG05**
5. O ator acessa o e-mail e clica no link fornecido.
6. O sistema exibe a tela de redefinição de senha. 
7. O ator insere uma nova senha e confirma a alteração.
8. O sistema verifica a força da senha. **RN3**
9. O sistema atualiza a senha e exibe a mensagem **MSG06**.

**Fluxos alternativos**:
- **FA1 - E-mail não cadastrado**:
   - Se o e-mail não estiver cadastrado, o sistema exibe a mensagem **MSG07**.

**Fluxos de exceção**:
- **RN2 - Verificação e-mail**:
   - Todas as informações são obrigatórias.
- **RN3 - Verificação senha**:
   - A senha deve atender aos critérios de segurança (mínimo de 8 caracteres, incluindo letras e números).

---

## **Caso de Uso UC4 - Gerenciar perfil expositor**

**Objetivo**: Permitir que o ator gerencie os dados do seu perfil, incluindo informações sobre o estande, produtos vendidos e dados pessoais.  
**Requisitos**: **RF004**  
**Atores**: Expositor  
**Condição de entrada**: O ator deseja acessar a plataforma e selecionar a opção de gerenciamento de perfil.

**Fluxo principal**:
1. O ator acessa a tela de edição do perfil.
2. O sistema exibe as informações cadastradas do expositor, incluindo número do estande, produtos vendidos, nome, e-mail, CPF e formas de pagamento aceitas (cartão de crédito, cartão de débito, Pix, dinheiro). **RN4**
3. O ator altera os dados desejados.
4. O ator confirma a atualização.
5. O sistema valida os dados inseridos.
6. Se os dados forem válidos, o sistema salva as alterações e exibe a mensagem de atualização. **MSG08**
7. O sistema retorna à tela de perfil com as informações atualizadas.

**Fluxos alternativos**:
- **FA1 - O ator decide cancelar a edição**:
   - O ator deseja cancelar a edição, os dados permanecem inalterados. **MSG09**.

**Fluxos de exceção**:
- **RN4 - Validação dos campos do perfil**:
   - Todas as informações são obrigatórias.

---

## **Caso de Uso UC5 - Gerenciar produtos**

**Objetivo**: Permitir que o ator gerencie seus produtos (adicionar, editar, remover).  
**Requisitos**: **RF005**  
**Atores**: Expositor  
**Condição de entrada**: O ator acessa a opção de gerenciamento de produtos.

**Fluxo principal**:
1. O ator visualiza a lista de produtos.
2. Escolhe adicionar, editar ou remover um produto.
3. **Se o ator escolher adição ou edição**:  
   - 3.1. Preenche os campos obrigatórios (Nome, Preço, Quantidade). **RN5**
4. **Se for remoção**, o ator clica no botão “Remover”.
5. O ator confirma a ação.
6. Se válida, o sistema salva e exibe a mensagem **MSG10**.

**Fluxos alternativos**:
- **FA1 - O ator decide cancelar a adição, edição ou remoção de um produto**:
   - O ator cancela a ação, e o sistema exibe a mensagem **MSG09**.

**Fluxos de exceção**:
- **RN5 - Validação dos campos de produto**:
   - Todas as informações são obrigatórias.

---

## **Caso de Uso UC6 - Notificar estoque**

**Objetivo**: Permitir que o ator visualize o estoque dos produtos e defina parâmetro para notificações automáticas quando um produto precisar ser reabastecido.  
**Requisitos**: **RF006**  
**Atores**: Expositor  
**Condição de entrada**: O ator acessa a plataforma e seleciona a opção de gerenciamento de estoque.

**Fluxo principal**:
1. O sistema exibe a lista de produtos com suas quantidades disponíveis.
2. O ator define o parâmetro de notificação para um produto (Quantidade mínima). **RN8**
3. O ator confirma as configurações.
4. O sistema salva as configurações e exibe a mensagem **MSG11**.
5. O sistema monitora o estoque e notifica o ator quando um produto atingir a quantidade mínima definida.

**Fluxos alternativos**:
- **FA1 - O ator decide não definir notificações**:
   - O ator cancela a ação, e o sistema exibe a mensagem **MSG12**.

**Fluxos de exceção**:
- **RN8 - Validação do parâmetro para notificação**:
   - O sistema verifica se o parâmetro é um número positivo maior que zero.

---

## **Caso de Uso UC7 - Visualizar o registro das vendas**

**Objetivo**: Permitir que o ator visualize todas as vendas realizadas para acompanhar quando um produto foi vendido.  
**Requisitos**: **RF007**  
**Atores**: Expositor  
**Condição de entrada**: O ator acessa a plataforma e seleciona a opção de listar as vendas realizadas.

**Fluxo principal**:
1. O sistema exibe uma lista das vendas realizadas, incluindo data, nome do produto, quantidade, valor, método de pagamento e descontos aplicados.
2. O ator visualiza a lista de transações realizadas com as informações detalhadas.

**Fluxos alternativos**:
- **FA1 - Nenhuma venda registrada**:  
   - O sistema exibe a mensagem **MSG13**.
- **FA2 - Adicionar manualmente um registro de venda**:  
   - O ator clica em “Inserir registro de venda”.
   - O sistema exibe um formulário para inserção- **UC8 - Registrar as vendas manualmente**.

**Fluxos de exceção**:
- Nenhum.

---

## **Caso de Uso UC8 - Registrar as vendas manualmente**

**Objetivo**: Permitir que o ator registre as vendas realizadas pessoalmente no estande para ter todos os registros.  
**Requisitos**: **RF008**  
**Atores**: Expositor  
**Condição de entrada**: O ator acessa a plataforma e seleciona a opção de listar as vendas realizadas.

**Fluxo principal**:
1. O ator clica em “Inserir registro de venda”.
2. O sistema solicita os dados da venda: data, nome do produto, quantidade, valor e método de pagamento. **RN9**
3. O ator confirma a venda.
4. O sistema registra a transação de venda e exibe uma mensagem **MSG14**.
5. O sistema atualiza a listagem de vendas com a nova transação.

**Fluxos alternativos**:
- **FA1 - Cancelamento do registro da venda**:  
   - O registro da venda é cancelado, exibindo a mensagem **MSG15**.

**Fluxos de exceção**:
- **RN9 - Validação dos dados de registro de venda**:  
   - Todas as informações são obrigatórias.

---

## **Caso de Uso UC9 - Notificar venda on-line**

**Objetivo**: Permitir que o ator seja notificado sobre o sucesso de uma transação realizada por um participante no estande virtual, possibilitando o acompanhamento em tempo real.  
**Requisitos**: **RF009**  
**Atores**: Expositor  
**Condição de entrada**: Uma compra é realizada no estande virtual.

**Fluxo principal**:
1. A compra é finalizada no estande virtual.
2. O sistema processa a transação.
3. Se a transação for concluída com sucesso, o sistema notifica o expositor sobre a venda realizada.
4. O ator recebe a notificação em tempo real com a mensagem **MSG14**.

**Fluxos alternativos**:
- **FA1 - O ator deseja visualizar todas as vendas anteriores**:  
   - O ator acessa a seção de notificações, clicando na notificação exibida após a venda.
   - O sistema exibe o histórico de transações bem-sucedidas. **UC7 - Visualizar o registro das vendas**.

**Fluxos de exceção**:
- Nenhum.

---

## **Caso de Uso UC10 - Visualizar histórico de compras**

**Objetivo**: Permitir que o ator visualize um histórico detalhado de todas as suas compras na feira, incluindo valores, métodos de pagamento e descontos aplicados.  
**Requisitos**: **RF010**  
**Atores**: Participante  
**Condição de entrada**: O ator acessa a plataforma e seleciona a opção de visualizar o histórico de compras.

**Fluxo principal**:
1. O ator acessa a tela de histórico de compras.
2. O sistema exibe a lista de compras realizadas, incluindo nome do produto, valor pago, método de pagamento utilizado e descontos aplicados.
3. O ator visualiza os detalhes de suas compras.

**Fluxos alternativos**:
- **FA1 - Nenhuma compra registrada**:  
   - O sistema exibe a mensagem **MSG16**.

**Fluxos de exceção**:
- Nenhum.

---

## **Caso de Uso UC11 - Filtrar produtos**

**Objetivo**: Permitir que o ator realize a busca pelos produtos disponíveis na feira de forma filtrada, evitando a busca manual dentro da plataforma.  
**Requisitos**: **RF011**  
**Atores**: Participante  
**Condição de entrada**: O ator acessa a barra de busca de produtos.

**Fluxo principal**:
1. O ator seleciona a opção de filtrar produtos.
2. O sistema exibe um campo de pesquisa e opções de filtro (nome do produto, segmento do produto e faixa de preço).
3. O ator insere um termo de pesquisa ou aplica filtros.
4. O sistema exibe a lista de produtos disponíveis que atendem aos critérios informados.
5. O ator visualiza os detalhes de um produto, segmento ou faixa de preço específico.

**Fluxos alternativos**:
- **FA1 - Nenhum produto encontrado**:  
   - O sistema exibe a mensagem **MSG17**.

**Fluxos de exceção**:
- Nenhum.

---

## **UC12: Enviar mensagem ao expositor**

**Objetivo**: Permitir que o ator envie mensagens assíncronas para o expositor, a fim de consultar a disponibilidade de um produto na próxima feira.

**Requisitos**: RF012

**Atores**: Participante

**Condição de entrada**: O ator acessa a plataforma e seleciona a opção de visualizar expositores.

**Fluxo principal:**  
1. O sistema exibe a lista dos expositores.  
2. O ator acessa o perfil do expositor procurado através de um ícone de perfil na tela de listagem.  
3. O sistema exibe as informações do expositor, incluindo nome, produtos vendidos e foto (se disponível), e a opção de enviar mensagem.  
4. O ator seleciona a opção de enviar mensagem.  
5. O sistema exibe a tela de conversa, com nome e foto do ator e do expositor (se houver), assim como o conteúdo da mensagem, data e hora de envio.  
6. O ator insere a mensagem e a envia.  
7. O sistema registra a mensagem com data, hora e status "não lida".  
8. O expositor recebe a notificação e pode responder quando disponível.  
9. O sistema exibe a página do histórico de mensagens com data, hora e status atualizado para "lida" quando visualizada.

**Fluxos alternativos:**  
- **FA1: Cancelar envio de mensagem:**  
  O envio da mensagem é cancelado, exibindo a mensagem MSG18.

**Fluxos de exceção:**  
- **RN10: Falha ao enviar a mensagem:**  
  - E1: Se houver erro ao enviar a mensagem, o sistema exibe a mensagem MSG19.

---

## **UC13 - Suporte técnico ao participante**

**Objetivo**: Permitir que o ator acesse um canal de suporte dentro da plataforma para resolver dúvidas ou problemas relacionados ao evento.

**Requisitos**: RF013

**Atores**: Participante

**Condição de entrada**: O ator acessa a plataforma e seleciona a opção de suporte.

**Fluxo principal:**  
1. O ator acessa a tela de suporte dentro da plataforma.  
2. O sistema exibe opções de ajuda, incluindo perguntas frequentes (FAQ) e um canal de contato com a equipe de suporte.  
3. O ator seleciona uma opção de suporte ou envia uma mensagem com sua dúvida/problema.  
4. O sistema solicita que o ator forneça informações detalhadas para registrar a solicitação de suporte, como:  
    - **Informações de contato:**  
        - **Telefone:** O sistema permite que o participante adicione um número de contato.  
        - **E-mail:** O sistema pode pré-preencher esse campo com o e-mail do participante, ou permitir que o participante altere essa informação.  
    - **Descrição do problema:** Campo de texto livre onde o participante pode fornecer detalhes adicionais sobre sua dúvida ou problema.  
5. O sistema registra a solicitação e gera um número de atendimento único, enviando uma confirmação por e-mail ou mensagem na plataforma.  
6. O suporte recebe a solicitação e responde ao ator, oferecendo uma solução ou orientações adicionais.  
7. O ator visualiza a resposta e pode continuar a conversa, se necessário.

**Fluxos alternativos:**  
- **FA1 - O ator procura a resposta na aba FAQ:**  
  O ator resolve sua dúvida sem precisar enviar uma solicitação.

**Fluxos de exceção:**  
- **RN11: Falha no envio da solicitação:**  
  - E1: Se houver erro ao registrar a solicitação, o sistema exibe a mensagem MSG20.

---

## **UC14 - Suporte técnico ao expositor**

**Objetivo**: Permitir que o ator receba suporte técnico imediato em caso de falhas no sistema para evitar interrupções no atendimento aos participantes.

**Requisitos**: RF014

**Atores**: Expositor

**Condição de entrada**: O ator acessa a plataforma para solicitar suporte técnico.

**Fluxo principal:**  
1. O ator acessa a opção de suporte técnico na plataforma.  
2. O sistema exibe a seção de Perguntas Frequentes (FAQ) e opções de contato com a equipe de suporte.  
3. O ator opta por enviar uma solicitação de suporte via mensagem.  
4. O sistema solicita que o ator forneça as seguintes informações:  
    - **Categoria do Problema:**  
        - Exemplo 1: Dificuldade ao registrar uma venda → Prioridade Alta  
        - Exemplo 2: Erro no processamento de pagamento → Prioridade Alta  
        - Exemplo 3: Erro ao atualizar perfil → Prioridade Baixa  
    - **Descrição do problema:** Campo para detalhamento da solicitação  
    - **Anexos:** Opcional - Captura de tela e/ou outros arquivos relevantes  
    - **Preferências de Contato:** O ator pode indicar se deseja ser contatado por telefone, mas a decisão final cabe ao suporte.  
5. O sistema registra automaticamente a prioridade da solicitação com base na categoria.  
6. O ator confirma e registra a solicitação de suporte.  
7. O sistema registra a solicitação e gera um número de atendimento único, enviando uma confirmação por e-mail ou mensagem na plataforma.  
8. O suporte técnico analisa a solicitação, considerando a prioridade cadastrada, e fornece uma resposta com a solução ou instruções adicionais.  
    - Caso necessário, o suporte pode optar por entrar em contato com o ator via telefone para esclarecer o problema.  
9. O ator visualiza a resposta e pode continuar a conversa, se necessário.

**Fluxos alternativos:**  
- **FA1: O ator procura a resposta na aba FAQ:**  
  O ator resolve sua dúvida sem precisar enviar uma solicitação.  
- **FA2: O suporte decide entrar em contato via ligação:**  
  Se a equipe de suporte avaliar que o problema exige atendimento por telefone, um técnico pode entrar em contato com o ator.  
- **FA3: O suporte opta por responder apenas via mensagem:**  
  Se a equipe de suporte avaliar que a solicitação pode ser resolvida sem uma ligação, a resposta será enviada apenas por mensagem na plataforma.

**Fluxos de exceção:**  
- **RN11: Falha no envio da solicitação:**  
  - E1: Se houver erro ao registrar a solicitação, o sistema exibe a mensagem MSG20.

---

## **UC15: Adicionar à lista de desejos**

**Objetivo**: Permitir que o ator crie uma lista de produtos dos quais possa comprar na feira.

**Requisitos**: RF015

**Atores**: Participante

**Condição de entrada**: O ator seleciona a opção “Lista de Desejos”.

**Fluxo principal:**  
1. O ator visualiza a lista de produtos.  
2. O ator seleciona o produto.  
3. O sistema retorna o produto presente na plataforma.  
4. O ator seleciona a opção de adicionar à lista de desejos.  
5. O sistema adiciona o produto à lista de desejos.  
6. O ator acessa a opção lista de desejos na plataforma.  
7. O sistema exibe uma página com uma lista de produtos (podendo estar vazia ou não).  
8. O ator seleciona o produto na lista.  
9. O sistema o direciona para a tela do produto em questão.

**Fluxos alternativos:**  
- **FA1 - O ator pode apagar um produto adicionado à lista:**  
  O ator acessa a lista de desejos, seleciona a opção de remover um produto e o sistema remove o produto da lista, exibindo uma mensagem de confirmação (MSG21).  
- **FA2 - O ator pode adicionar um novo produto diretamente pela página do produto:**  
  O ator acessa a página de um produto, seleciona a opção de adicionar à lista de desejos, e o sistema adiciona o produto à lista e exibe uma mensagem de confirmação (MSG10).

**Fluxos de exceção:**  
Nenhum

---

## **UC16: PERSONALIZAR INTERFACE**

**Objetivo**: Permitir que o ator personalize a aparência da plataforma, ajustando temas e o modo claro/escuro, para uma experiência mais confortável.

**Requisitos**: RF016

**Atores**: Usuário comum

**Condição de entrada**: O ator acessa a opção de personalização da plataforma.

**Fluxo principal:**  
1. O ator seleciona a opção de personalização de aparência no menu de configurações.  
2. O sistema exibe as opções disponíveis, incluindo temas e a escolha entre modo claro e escuro.  
3. O ator escolhe um tema e/ou alterna entre modo claro e escuro.  
4. O sistema aplica as alterações imediatamente e salva a preferência do ator.  
5. O ator visualiza a nova aparência da plataforma.

**Fluxos alternativos:**  
- **FA1 - O ator decide reverter as alterações:**  
  O ator acessa novamente a opção de personalização.  
  O sistema permite restaurar as configurações padrão.

**Fluxos de exceção:**  
- **RN12: Falha ao salvar as preferências:**  
  - E1: Se houver erro ao salvar a personalização, o sistema exibe a mensagem MSG22 e mantém as configurações anteriores.

---

## **UC17: Avaliar compra**

**Objetivo**:  Permitir que o ator avalie os produtos comprados na feira, fornecendo uma nota por estrelas, um comentário e a opção de anexar fotos.

**Requisitos**: RF017

**Atores**: Participante

**Condição de entrada**:  O ator deve estar autenticado na plataforma e ter realizado pelo menos uma compra, desejando avaliar um dos produtos.

**Fluxo principal:**  
1. O ator acessa a plataforma e entra na seção “Histórico de Compras”.  
2. O ator seleciona um produto para avaliar.  
3. O sistema exibe um formulário de avaliação contendo as seguintes informações:  
   - **Seletor de estrelas**  
   - **Campo de texto para o comentário**  
   - **Opção de anexar imagens do produto**  
4. O ator preenche os campos desejados e confirma a avaliação.  
5. O sistema valida os dados inseridos.  
6. O sistema armazena a avaliação e a vincula ao produto avaliado.  
7. O sistema exibe uma mensagem de confirmação e a avaliação passa a ser visível para os demais participantes.

**Fluxos alternativos:**  
- **FA1 - Avaliação sem comentário e/ou sem imagem:**  
  O participante pode optar por não adicionar um comentário ou imagens, preenchendo apenas a nota por estrelas.  
  O fluxo segue normalmente a partir do passo 4.

**Fluxos de exceção:**  
- **RN13 - Erros na avaliação:**  
  - E1: Se o participante tentar enviar uma avaliação sem selecionar ao menos uma estrela, o sistema exibe a mensagem MSG23.  
  - E2: Se houver falha no envio da imagem (formato inválido, tamanho excedido, etc.), o sistema exibe a mensagem MSG24.

---

## **UC18: Oferecer descontos**

**Objetivo**: Permitir que o ator configure descontos em determinados produtos ou estandes, incentivando a fidelidade dos participantes ao evento.

**Requisitos**: RF018

**Atores**: Expositor

**Condição de entrada**: O ator acessa a opção de gerenciamento de descontos na plataforma.

**Fluxo principal:**  
1. O ator acessa a tela de gerenciamento de descontos.  
2. O sistema exibe a lista de produtos cadastrados e suas quantidades.  
3. O ator seleciona um produto e define um desconto percentual ou valor fixo.  
4. O sistema valida os dados inseridos.  
5. Se os dados forem válidos, o sistema aplica o desconto e salva as alterações.  
6. O sistema exibe uma mensagem de confirmação (MSG25) e os participantes podem visualizar a promoção no catálogo de produtos.

**Fluxos alternativos:**  
- **FA1 - O ator decide cancelar a ação:**  
  O ator cancela a configuração antes de confirmar, mantendo os valores anteriores e exibindo a mensagem MSG09.

**Fluxos de exceção:**  
- **RN14 - Verificação valor da promoção inserido:**  
  O sistema verifica se o parâmetro é um número positivo maior que zero.

---

## **UC19: Notificar desconto**

**Objetivo**: Notificar o ator sobre promoções e descontos em produtos e estandes que estão na sua lista de desejos, permitindo que aproveite oportunidades de compra.

**Requisitos**: RF019

**Atores**: Participante

**Condição de entrada**: O expositor cadastra um desconto em pelo menos um de seus produtos.

**Fluxo principal:**  
1. O sistema monitora as promoções cadastradas pelos expositores.  
2. Quando um produto ou estande da lista de desejos recebe um desconto, o sistema gera uma notificação para o ator.  
3. O ator recebe a notificação em tempo real via aplicativo no celular.

**Fluxos alternativos:**  
- **FA1 - O ator decide clicar na notificação:**  
  O sistema abre a página de lista de desejos do ator com a exibição dos produtos com informações referentes ao desconto (valor percentual ou fixo).

**Fluxos de exceção:**  
Nenhum

---

## **UC20: REALIZAR OPERAÇÕES OFFLINE**

**Objetivo**: Permitir que o sistema funcione no modo offline, garantindo a continuidade das operações diárias mesmo sem conexão com a internet. Além disso, sincronizar automaticamente os dados quando a conexão for restabelecida, mantendo as informações do evento atualizadas.

**Requisitos**: RF020

**Atores**: Expositor

**Condição de entrada**: O ator acessa a plataforma em um ambiente sem conexão à internet.

**Fluxo principal:**  
1. O ator acessa o sistema sem conexão à internet.  
2. O sistema verifica a ausência de conexão e ativa o modo offline.  
3. O ator realiza operações permitidas no modo offline, como:  
   - **Visualizar produtos e informações previamente carregadas**  
   - **Registrar vendas**  
   - **Editar informações locais de produtos e estoques**  
4. O sistema armazena os dados localmente até que a conexão seja restabelecida.  
5. Assim que a conexão for restaurada:  
   - **O sistema inicia a sincronização automática dos dados offline com o servidor**  
   - **As operações realizadas offline são enviadas para o banco de dados principal**  
   - **As informações atualizadas no servidor são baixadas para os dispositivos dos usuários**  
6. O sistema confirma a sincronização bem-sucedida e notifica o usuário.

**Fluxos alternativos**: Nenhum.

**Fluxos de exceção:**  
- **E1 - Falha na sincronização:**  
  O sistema exibe MSG22.  
- **E2 - Dados corrompidos ou incompatíveis:**  
  O sistema exibe um aviso MSG26.

---

## **UC21: Visualizar relatórios**

**Objetivo**: Permitir que o organizador visualize relatórios detalhados sobre o fluxo de participantes durante o evento, identificando horários de pico e auxiliando na melhoria da organização da feira.

**Requisitos**:  RF021

**Atores**: Organizador

**Condição de entrada:**  
O ator deve estar autenticado na plataforma com permissões de acesso aos relatórios do evento.  
O evento deve estar cadastrado no sistema e finalizado para que os dados estejam disponíveis.  
O sistema deve conter registros de participação dos visitantes.  
O módulo de geração de relatórios deve estar acessível na plataforma.

**Fluxo principal:**  
1. O ator acessa a área de relatórios na plataforma por meio do menu.  
2. O sistema exibe opções de relatórios detalhados sobre a participação e vendas do evento.  
3. O ator seleciona o período desejado (Ex: evento inteiro, dia específico, horários de pico).  
4. O sistema gera um relatório detalhado com as seguintes informações:  
   - **Horários de pico:** Exibe os períodos de maior fluxo de participantes.  
   - **Total de Vendas:** Apresenta o número total de vendas realizadas pelos expositores.  
   - **Quantidade de retiradas de produtos:** Indica a quantidade de retiradas realizadas durante o evento.  
5. O ator pode visualizar as informações e analisar o desempenho geral do evento.  
6. O sistema permite a exportação do relatório para formatos como PDF ou Excel.

**Fluxos alternativos:**  
Nenhum.

**Fluxos de exceção:**  
- **E1 - Dados não encontrados para o período selecionado:**  
  Se não houver dados disponíveis para o período ou categoria escolhidos, o sistema exibe a MSG27.  
- **E2 - Erro ao gerar o relatório:**  
  Se ocorrer um erro ao tentar gerar o relatório, o sistema exibe a MSG28.


---

# Mensagens do Sistema

- **MSG01**: "Credenciais inválidas."
- **MSG02**: "Certificado digital não foi reconhecido."
- **MSG03**: "Compra realizada com sucesso! Seu código de retirada é *."
- **MSG04**: "Falha no pagamento. Por favor, tente novamente."
- **MSG05**: "Um e-mail de recuperação foi enviado para o seu endereço."
- **MSG06**: "Senha redefinida com sucesso."
- **MSG07**: "E-mail não cadastrado no sistema."
- **MSG08**: "Perfil atualizado com sucesso."
- **MSG09**: "Alterações canceladas. Nenhuma modificação foi realizada."
- **MSG10**: "Produto salvo com sucesso."
- **MSG11**: "Alarme de estoque salvo com sucesso."
- **MSG12**: "Criação de notificação de estoque cancelada."
- **MSG13**: "Ainda não há vendas registradas para seus produtos."
- **MSG14**: "Venda realizada com sucesso."
- **MSG15**: "Criação de registro de venda cancelada."
- **MSG16**: "Não há compras registradas."
- **MSG17**: "Nenhum produto encontrado."
- **MSG18**: "Envio de mensagem cancelado."
- **MSG19**: "Erro ao enviar mensagem."
- **MSG20**: "Erro ao registrar solicitação ao suporte."
- **MSG21**: "Produto removido com sucesso."
- **MSG22**: "Falha na sincronização dos dados. Tente novamente mais tarde."
- **MSG23**: "Você precisa selecionar ao menos uma estrela para enviar sua avaliação."
- **MSG24**: "Erro no envio da imagem. Verifique o formato e o tamanho do arquivo e tente novamente."
- **MSG25**: "Promoção aplicada com sucesso."
- **MSG26**: "Não foi possível sincronizar alguns dados devido a incompatibilidades. Verifique as informações antes de tentar novamente."
- **MSG27**: "Não há dados disponíveis para o período selecionado. Tente escolher um intervalo diferente."
- **MSG28**: "Ocorreu um erro ao tentar gerar o relatório. Por favor, tente novamente mais tarde."
