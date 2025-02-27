<h1>Desafio técnico - Fidelity Pesquisas</h1>
<h2><strong>Para testar a aplicação, acesse o link a seguir:</strong> https://testefidelitypesquisas-2.onrender.com/login/ </h2>
<h2> <strong>Para visualizar usuários cadastrados, acesse o link a seguir (necessário logar como administrador):</strong> https://testefidelitypesquisas-2.onrender.com/admin/login/?next=/admin/</h2>

<h2>Passo a passo para rodar a aplicação manualmente</h2>

<H3>1. CLONE O REPOSITÓRIO</H3>
<LI>No terminal, execute: git clone https://github.com/LucianoBruno1/desafio-login , em seguida: 
cd TesteFidelityPesquisas</LI>
<h3>2. CRIE E ATIVE UM AMBIENTE VIRTUAL</h3>
<li>No terminal, execute: python -m venv venv , em seguida: 
venv\Scripts\activate
</li>
<h3>3. INSTALE AS DEPENDÊNCIA</h3>
<li>Execute o comando: pip install -r requirements.txt</li>
<h3>4. APLIQUE AS MIGRAÇÕES DO BANCO DE DADOS</h3>
<li>python manage.py makemigrations em seguida python manage.py migrate</li>
<h3>5. CRIE UM SUPERUSUÁRIO PARA ACESSAR O DJANGO ADMIN (OPCIONAL)</h3>
<li>python manage.py createsuperuser</li>
<h3>6. COLETE OS ARQUIVOS ESTÁTICOS</h3>
<li>NO terminal, execute: python manage.py collectstatic</li>
<h3>7. RODE A APLICAÇÃO</h3>
<li>No terminal, execute: python manage.py runserver</li>
<li>Link para a home: 127.0.0.1:8000</li>
<li>link para o administrador django: 127.0.0.1:8000/admin</li>
