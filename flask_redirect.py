from flask import Flask, request, redirect
from sqlalchemy import create_engine, select
import time

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.args:
        try:
            username = request.args.get('username')
            db = create_engine('postgres:///testingdb')
            conn = db.connect()
            print(conn)
            # tables = conn.execute("SELECT * FROM pg_catalog.pg_tables;")
            # for t in tables:
            #     if "auth" in t[1]:
            #         print(t)
            query = "SELECT username FROM auth_user WHERE username='{}';".format(username)
            queue = conn.execute(query).fetchall()
            print(queue[0])
            if queue[0][0]:
                time.sleep(3)
                return redirect("http://www.example.com", code=302)
            return username
        except Exception as err:
            print(err)
            pass
        finally:
            conn.close()
            db.dispose()
    return 'Updating your license request'


if __name__ == '__main__':
    app.run()
