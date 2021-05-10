# pw-django-01

# Web app da aula de 10.5 de Programação Web

### Passos para lançar e editar a aplicação
1. Abra a linha de comandos (PowerShell ou cmd)
1. Descarregue uma cópia (clone) do repositório com o comando `git clone https://github.com/ULHT-PW-2020-21/pw-django-01` 
1. Entre na pasta  `cd pw-django-01`
1. Crie um ambiente virtual `pipenv install django`
1. Active o ambiente virtual `pipenv shell`
1. Lance a aplicação no browser com o comando `python manage.py runserver`. 
1. Tem disponíveis as aplicações hello no link `http://127.0.0.1:8000/hello/` e pw no link `http://127.0.0.1:8000/pw/` 
1. abra a pasta com o Pycharm, para a explorar, ou com o comando `pycharm .`

### Passos para brincar e criar uma nóva página na aplicação
1. no ficheiro `views.py` crie uma nova função que renderize a nova página
2. na pasta `website\templates\pw` crie uma página HTML correspondente para ser renderizada, extendendo a base.html (veja como é feito nas outras páginas)
3. no ficheiro `website\urls.py` crie um novo `path` para o novo URL
4. no ficheiro `base.html` (que está na pasta `website\templates\website`) atualize o menu de navegação, inlcuindo um link para a nova página
