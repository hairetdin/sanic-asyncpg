from sanic import Sanic, response
from database import DBAsyncPg
# from databases import Database
import settings
from utils import sql_jsonify


app = Sanic(__name__)
app.config.update_config(settings.db_settings)

"""
HOWTO: create postgresql user and database
sudo -u postgres psql
postgres=# create database testdb;
postgres=# create user testuser with encrypted password 'testpass';
postgres=# grant all privileges on database testdb to testuser;
"""


@app.listener('after_server_start')
async def start_db_connection(app, loop):
    # for databases lib uncomment
    # app.ctx.db = Database('postgresql+asyncpg://danis:danis@localhost:5432/danissanic')
    # await app.ctx.db.connect()

    # for asyncpg lib
    app.ctx.db = DBAsyncPg(settings.db_settings)
    app.ctx.pool = await app.ctx.db.create_pool()


@app.listener('after_server_stop')
async def close_db_connection(app, loop):
    # for databases lib uncomment
    # await app.ctx.db.disconnect()

    # for asyncpg lib
    await app.ctx.db.pool.close()


@app.get("/")
async def root_page(request):
    user_id = 1
    # for databases lib uncomment
    # result = await database.fetch_one(query="SELECT * FROM notes WHERE id = :id", values={"id": 1})

    # for asyncpg lib
    async def get_username():
        return await app.ctx.db.execute("SELECT name FROM users WHERE id = $1", user_id, fetchval=True)
    result = await get_username()
    if not result and app.ctx.db:
        # add new user to db
        await app.ctx.db.execute("insert into users values (1, 'testuser');", fetchval=True)
        result = await get_username()

    return response.text(f'Hello, {result}')


@app.route("/api/user/")
async def user(request):
    pool = app.ctx.pool
    async with pool.acquire() as connection:
        sql = '''
                SELECT *
                FROM public.users; 
            '''
        rows = await connection.fetch(sql)
        return response.json(sql_jsonify(rows))


