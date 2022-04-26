21/04/2022

- [ ] Se puder usar pipenv, poetry ou pdm no projeto será muito benefíco, porque o pip porque se só dificulta o manuseio das dependências, mesmo criando arquivos separados como dev.txt, prop.txt e etc. Quando instalamos uma dependência, temos que ter cuidado em qual arquivo ela estará e isto aumentar a chance de vários erros em gerenciar as dependências.

- [ ] Separe Dockerfile de desenvolvimento e produção. O ambiente de desenvolvimento pode ser mais flexível, ter ferramentas e configurações para ajudar no desenvolvimento, enquanto a imagem de produção ficaria mais otimista até trabalhando-se com multi-stage e usando pacotes wheels com pip para gerar uma imagem menor.

- [ ] Importante também que no ambiente de desenvolvimento ao rodar "docker-compose up" tudo já suba de uma vez e a aplicação já estava disponível.

- [ ] Gere o venv dentro do próprio projeto, isto ajuda as IDE a entenderem os pacotes instalados, mesmo quando não estão conectadas com Docker.

- [ ] Imagem Python do tipo slim tem tipo melhor desempenho para executar o Python e acabam até ficando menores em produção.

- [ ] Usar o Pydantic para embutir a validação na própria entidade pode ser uma ideia muito interessante, já simplifica a validação no mesmo arquivo, porém o Pydantic tem problemas com validação alinhadas de subclasses, entre outras coisas, então tornar esta dependência dele direta para as entidades pode causar causar bug e dificuldades para manutenções posteriores, além de engessar a validação do domínio somente ao Pydantic. Use-o com bastante discernimento.

- [ ] Tenha como entre últimas opções usar libs externas dentro do domínio, ao fazer isto e romper o limite arquitetural tenha em mente as vantagens e desvantagens de tal ato.
