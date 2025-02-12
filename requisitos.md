# Requisitos funcionais do sistema

## 1. Autenticação e acesso
- **[RF001]** Como usuário comum, eu gostaria de acessar o sistema de gestão por meio dessas credenciais: e-mail e senha ou certificado digital, para que eu possa utilizar os serviços oferecidos pela plataforma.
- **[RF002]** Como participante, gostaria de acessar a plataforma sem a necessidade de login e realizar compras utilizando diversos métodos de pagamento (cartão de crédito, cartão de débito, Pix, dinheiro) ou efetuando retiradas diretamente no local.
- **[RF003]** Como usuário comum, eu gostaria de recuperar minha senha caso a tenha esquecido, recebendo um link de redefinição no meu e-mail cadastrado, para que eu possa acessar a plataforma novamente de forma segura.

## 2. Gerenciamento de perfil e informações
- **[RF004]** Como expositor, gostaria de gerenciar os dados do meu perfil, incluindo informações sobre o número do estande, produtos vendidos, nome, e-mail, CPF e formas de pagamento aceitas (cartão de crédito, cartão de débito, Pix, dinheiro).
- **[RF005]** Como expositor, gostaria de acessar a plataforma para gerenciar meus produtos, incluindo a adição, atualização e exclusão quando necessário. O gerenciamento deve permitir a inserção de informações como nome, preço e quantidade dos produtos.
- **[RF006]** Como expositor, eu gostaria de visualizar o estoque dos produtos e de poder definir parâmetros relativos à quantidade para ser notificado automaticamente, a fim de saber qual produto está precisando ser reabastecido.

## 3. Transações e vendas
- **[RF007]** Como expositor, eu gostaria de poder listar as vendas que eu faço, com os dados: data, nome do produto, quantidade, valor, método de pagamento e descontos aplicados, para que eu possa saber quando um produto foi vendido.
- **[RF008]** Como expositor, eu gostaria de poder registrar as vendas que eu faço pessoalmente, com os dados: data, nome do produto, quantidade, valor, método de pagamento, para que eu possa acompanhar as transações realizadas no estande.
- **[RF009]** Como expositor, eu gostaria de ser notificado sobre o êxito na transação de um participante que está comprando na minha estande, para que eu possa acompanhar as vendas em tempo real.
- **[RF010]** Como participante, eu gostaria de visualizar um histórico detalhado de todas as minhas compras na feira, incluindo data, nome do produto, valor, método de pagamento e descontos aplicados.
- **[RF011]** Como participante, gostaria de realizar a busca pelos produtos disponíveis na feira, a fim de evitar o trabalho manual de busca dentro da plataforma. O filtro deve ser feito por nome do produto, segmento do produto e faixa de preço.

## 4. Comunicação e interação
- **[RF012]** Como participante, gostaria de acessar o perfil do expositor através de um ícone na tela de vendas e enviar uma mensagem assíncrona para consultar a disponibilidade de um produto na próxima feira. A tela de conversa exibirá o nome e foto do participante e do expositor, se houver, assim como o conteúdo da mensagem, data e hora de envio. O expositor poderá responder quando disponível, informando a disponibilidade do produto. O histórico de mensagens será mantido, com data, hora e status da mensagem (lida ou não), permitindo o acompanhamento das interações.
- **[RF013]** Como participante, desejo acessar um canal de suporte dentro da plataforma para solucionar dúvidas ou problemas relacionados ao evento. Esse canal deve oferecer uma seção de perguntas frequentes (FAQ) e a possibilidade de contato direto com a equipe de suporte. Ao selecionar a opção de envio de mensagem, a solicitação deve ser registrada, incluindo informações a descrição detalhada, facilitando o acompanhamento e a resolução do caso.
- **[RF014]** Como expositor, eu gostaria de receber suporte técnico imediato dentro da plataforma para solucionar falhas no sistema e evitar interrupções no atendimento aos participantes. Esse canal deve incluir uma seção de perguntas frequentes (FAQ) e possibilitar o contato direto com a equipe de suporte por meio do envio de mensagens. Ao optar pelo envio de mensagens, devo poder descrever detalhadamente o problema, selecionar a categoria da solicitação, anexar capturas de tela e/ou outros arquivos relevantes e registrar a solicitação, que será encaminhada automaticamente para a equipe de suporte técnico, garantindo uma resposta rápida e uma solução eficiente.

## 5. Experiência do usuário
- **[RF015]** Como participante, eu gostaria de criar uma lista de desejos com produtos e expositores favoritos, para facilitar minhas compras e interações futuras.
- **[RF016]** Como usuário comum, eu gostaria de poder personalizar a aparência da plataforma, ajustando temas e modo claro/escuro, para uma experiência mais confortável.

## 6. Avaliações e feedback
- **[RF017]** Como participante, eu gostaria de poder avaliar os produtos comprados na feira, com o propósito de opinar sobre o que foi consumido. As opiniões devem ser formuladas por estrelas (1 a 5), ter um comentário e poder enviar fotos.

## 7. Promoções e engajamento
- **[RF018]** Como expositor, eu gostaria de oferecer descontos em determinados produtos ou estandes, como forma de incentivar a fidelidade dos participantes ao evento.
- **[RF019]** Como participante, eu gostaria de ser notificado sobre promoções e descontos em produtos e estandes que estão na minha lista de desejos, para que eu possa aproveitar as oportunidades de compra.

## 8. Operações offline e sincronização
- **[RF020]** Como expositor, desejo que o sistema possa realizar operações diárias no modo offline, de forma que a ausência de uma conexão de dados não impeça a realização do evento. Além disso, gostaria que os dados sobre os produtos e operações do evento fossem sincronizados automaticamente assim que a conexão fosse restabelecida, permitindo a atualização sobre novos produtos, reposições e alterações nos produtos existentes.

## 9. Relatórios e gestão do evento
- **[RF021]** Como organizador, eu gostaria de visualizar relatórios detalhados sobre a participação no evento, incluindo horários de pico, total de vendas realizadas e quantidade de retiradas de produtos, para que eu possa analisar o desempenho do evento e aprimorar a organização da feira.

# Requisitos não funcionais

## Disponibilidade
- **[RNF001]** O sistema deverá estar disponível 24 horas por dia, 7 dias por semana, garantindo acesso contínuo para expositores, participantes e organizadores.

## Privacidade e segurança
- **[RNF002]** O sistema deve implementar autenticação segura, garantindo que apenas usuários autorizados possam acessar suas contas e realizar transações.
- **[RNF003]** Os dados dos usuários, incluindo informações pessoais e transações financeiras, devem ser criptografados para evitar acessos não autorizados.
- **[RNF004]** O sistema deve estar em conformidade com a Lei Geral de Proteção de Dados (LGPD) e outras regulamentações de privacidade aplicáveis.

## Usabilidade
- **[RNF005]** A interface do sistema deve ser intuitiva e acessível, permitindo que os usuários naveguem facilmente sem necessidade de treinamento extenso.
- **[RNF006]** O histórico de compras e os painéis de vendas devem ser apresentados de forma clara, utilizando gráficos e filtros para facilitar a análise de informações.

## Suportabilidade
- **[RNF007]** O sistema deve ser compatível com os principais navegadores (Google Chrome, Mozilla Firefox, Microsoft Edge e Safari), além de dispositivos móveis Android e iOS.

## Interoperabilidade
- **[RNF008]** O sistema deve permitir integração com serviços de pagamento, como gateways de cartão de crédito/débito, Pix e carteiras digitais.

## Manutenibilidade
- **[RNF009]** O sistema deve ser escalável, permitindo a adição de novos recursos e aumento da capacidade de armazenamento sem comprometer o desempenho.
- **[RNF010]** Atualizações e correções devem ser aplicadas de forma transparente para os usuários, minimizando interrupções no serviço.

# Não Requisitos

- **[NREQ001]** O sistema não será responsável pelo gerenciamento físico dos produtos, cabendo aos expositores o controle de estoque e reposição.
- **[NREQ002]** O sistema não garantirá a veracidade das avaliações e comentários feitos pelos participantes sobre os produtos, sendo de responsabilidade dos expositores monitorar esse conteúdo.
- **[NREQ003]** O sistema não fornecerá suporte técnico presencial, sendo o atendimento realizado exclusivamente por meio digital.


# Matriz GUT 

Os requisitos estão organizados em ordem decrescente de prioridade (G x U x T).  

| Requisito | Descrição | G | U | T | Prioridade (G x U x T) |
|-----------|------------|---|---|---|-----------------------|
| RF001     | Autenticação e acesso | 5 | 5 | 5 | 125 |
| RF014     | Suporte técnico imediato para expositores | 5 | 5 | 5 | 125 |
| RF020     | Operações offline e sincronização | 5 | 5 | 5 | 125 |
| RF003     | Recuperação de senha | 4 | 5 | 5 | 100 |
| RF005     | Gerenciamento de produtos pelo expositor | 5 | 5 | 4 | 100 |
| RF007     | Listagem de vendas realizadas | 5 | 5 | 4 | 100 |
| RF013     | Suporte técnico para participantes | 5 | 5 | 4 | 100 |
| RF002     | Acesso sem login para participantes e pagamentos diversos | 4 | 5 | 4 | 80 |
| RF009     | Notificação ao expositor sobre transações concluídas | 4 | 5 | 4 | 80 |
| RF006     | Notificação de baixo estoque | 4 | 4 | 4 | 64 |
| RF008     | Registro manual de vendas pelo expositor | 4 | 4 | 4 | 64 |
| RF012     | Mensagem entre participante e expositor | 4 | 4 | 4 | 64 |
| RF011     | Busca de produtos na feira | 4 | 4 | 3 | 48 |
| RF004     | Gerenciamento de perfil do expositor | 3 | 4 | 3 | 36 |
| RF010     | Histórico de compras do participante | 3 | 3 | 3 | 27 |
| RF015     | Lista de desejos para participantes | 3 | 3 | 3 | 27 |
| RF017     | Avaliação de produtos por participantes | 3 | 3 | 3 | 27 |
| RF018     | Expositores oferecerem descontos | 3 | 3 | 3 | 27 |
| RF019     | Notificação de promoções na lista de desejos | 3 | 3 | 3 | 27 |
| RF021     | Relatórios sobre fluxo de participantes | 3 | 3 | 3 | 27 |
| RF016     | Personalização da interface (tema claro/escuro) | 2 | 2 | 2 | 8 |
