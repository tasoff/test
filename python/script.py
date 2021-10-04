from bottle import route, run
import psycopg2

@route('/script')
def index():
    conn = None
    try:
        conn = psycopg2.connect(
                  user='postgres', password='123456Pp', host='postgres', port='5432'
        )
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS TEST")
        sql ='''CREATE TABLE TEST(
          FIRST_NAME CHAR(20) NOT NULL,
          LAST_NAME CHAR(20),
          AGE INT,
          SEX CHAR(1),
          INCOME FLOAT
          )'''
        cursor.execute(sql)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        return error
    finally:
        if conn is not None:
            conn.close()
    return "Table created successfully!\n"

run(host='0.0.0.0', port=8080)
