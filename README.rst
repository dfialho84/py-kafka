.. contents:: Conteúdo
    :depth: 2

Instalação do Ambiente
======================

Utilizamos o virtualenv para executar o projeto. Por isso, depois de instalados os pacotes referentes ao **Python3** e
**Virtualenv**, siga os passos a seguir:

.. code:: console
    
    cd diretorio/do/projeto
    mkdir venv
    vitualenv -p $(which python3.6) venv
    source venv/bin/activate
    pip install -r requirements.txt

Gerando a Documentação
======================

Utilizamos a biblioteca **sphinx** para gerar a documentação. Sempre que quiser
gerar uma nova versão utilize os comandos abaixo:

.. code:: console

    sphinx-apidoc -o docs src
    cd docs
    make html

A documentação será salva na pasta *docs/build/html*.

Inicializando os conteiners
===========================

Para realizar os testes utilizaremos containers docker. As máquinas são executadas utilizando
dokcer e docker-comopose. Para inicializar as máquinas, execute o comando abaixo:

.. code:: console

    docker-compose up

