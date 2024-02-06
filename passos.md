
- entrar no ambiente virtual "source clone-env/bin/activate

(https://www.youtube.com/watch?v=9eHh946qTIk&t=10s)
- Criei Table no DynamoDB ("clone-jobs") primary key "cloneID" (string). Não esquecer de mudar para "requisição on demand".
- No IAM criar Role (função), criar perfil para lambda. CloudWatchFullAcess + AmazonDynamoDBFullAccess.
- Vai no lambda para começar a criar nova função. No settings, mudar a memória (500) e timeout (1 min).
- Seguida, criar uma APIGateway para conectar tudo. REST API (public). Build. Iremos então criar os recursos que a API vai ter (rotas). Marcar o CORS.
No método GET : marcar "funcao do lambda", "integracao do proxy do lambda", tempo limite padrão. Criar os métodos conforme necessário para as rotas.
Após criar os métodos, fazer o deploy da API. Escolher um nome para estágio, e após fazer a implantacao, será gerado uma URL que será o endpoint. Veja que com esse endpoint a API é aberta para acesso irrestrito, então temos que ativar autenticação.
Optamos por restringir o acesso usando Acess keys. Para tanto, vamos em cada método, por ex no GET de uma rota, solicitação de método (method request) na chave de API que está falsa, colocar para True. Depois de feita esta alteracao em todas as rotas, não eqsquecer de salvar e fazer novo deploy do estágio (stage). Assim, se tentar o acesso agora vai dar message: not permited.
Vamos então configurar as keys acess. Vamos na API keys, gerar automaticamente, e teremos uma key.
Copiar a chave, e ir ate planos de utilizacao. Na criacao podemos ate limitar a taxa de velocidade da utilizacao para este nivel de usuario, e finalizar criando o plano de uso.
Entre e configure o estágio e API para adicionar ao plano de uso.
Agora vamos na Chave de API para copiar a Key. Essa Key teremos que colocar no header da nossa requisicao feita no postman por ex (configurar key "x-api-key" e valor a key gerada na aws).

(outro vídeo https://www.youtube.com/watch?v=V-ac_ZvdAW4) - 

- Com tudo isso configurado, agora sim vamos escrever o código em Python.
- Agora vamos efetivmente ao código Python.
O nome do nosso arquivo tem que ser o mesmo da função que configurmos, ou seja, lambda_function.
E criamos a funcao lambda_handler, que será efetivamente o endpoint que chamará os métodos que criarmos.
Vamo simportar boto3, json, e logging.

Com o logger, vamos pegar o log do event para as informaçoes do request. Depois extrair o metodo HTTP do nosso objeto proveniente do evento. Em seguida, vamos capturar o path do evento tambem. 

(o objeto que recebemos do DynamoDB não é de um tipo suportado pelo json encoder default, então temos que codificar nosso custom decode para os numeros decimais vindos do Dynamo sejam convertidos para Float. Assim, criamos um arquivo separado que nomeamos custom_encoder.py)











links úteis: 
https://www.freecodecamp.org/portuguese/news/como-gerenciar-diversas-versoes-do-python-e-ambientes-virtuais/

https://stackoverflow.com/questions/70343666/python-boto3-float-types-are-not-supported-use-decimal-types-instead

