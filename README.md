Sanic asyncpg
=============

Sanic web server with asyncpg Postgresql database interface and yoyo database migrations for raw sql. 

Also contain `databases` python lib support for PostgreSQL, MySQL, and SQLite



Getting started
---------------

- git clone this repository
- go to project directory `cd sanic-asyncpg`
- create python virtual environment, activate environment and install python libs from 
requirements.txt
```
python3 -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt 
```

- create postgresql user and database
```
sudo -u postgres psql
postgres=# create database testdb;
postgres=# create user testuser with encrypted password 'testpass';
postgres=# grant all privileges on database testdb to testuser;
postgres=# \q
```

- run sanic web server in develop mode
`sanic server.app --dev`

Manage commands
---------------
Activate python virtual environment `source ./venv/bin/activate`, if you haven't done it before.
Then you can run manage commands

`python manage.py` - show help info

`python manage.py run` - run this sanic web server

`python manage.py run --dev` - run this sanic web server in develop mode

`python manage.py migate` - run sql migrations from folder `migrations`

`python manage.py migrate --create 'migration_name'` - create new sql migrations in folder `migrations`,
running this command will open the default editor - vim. You can change editor for edit sql migrations in `yoyo.ini`

`python manage.py migrate --rollback` - rollback sql migrations


References
----------
https://sanic.dev - Sanic framework

https://magicstack.github.io/asyncpg/current/ - asyncpg database interface library designed specifically for PostgreSQL and Python/asyncio.

https://ollycope.com/software/yoyo/latest/ - Yoyo database sql migrations

https://www.encode.io/databases/ - databases lib support for PostgreSQL, MySQL, and SQLite