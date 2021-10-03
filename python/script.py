from bottle import route, run, template
import psycopg2

@route('/script')
def index():
   # conn = psycopg2.connect(
   #            user='postgres', password='123456Pp', host='127.0.0.1', port= '5432'
   # )
   # cursor = conn.cursor()
   # cursor.execute("DROP TABLE IF EXISTS TEST")
   # sql ='''CREATE TABLE TEST(
   #    FIRST_NAME CHAR(20) NOT NULL,
   #    LAST_NAME CHAR(20),
   #    AGE INT,
   #    SEX CHAR(1),
   #    INCOME FLOAT
   #    )'''
   # cursor.execute(sql)
   # conn.commit()
   # conn.close()
   return "Table created successfull!"

run(host='0.0.0.0', port=8080)
