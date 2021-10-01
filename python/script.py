from bottle import route, run, template
import psycopg2

@route('/script')
def index():
   #Establishing the connection
   conn = psycopg2.connect(
              user='postgres', password='123456Pp', host='127.0.0.1', port= '5432'
   )
   #Creating a cursor object using the cursor() method
   cursor = conn.cursor()

   #Doping EMPLOYEE table if already exists.
   cursor.execute("DROP TABLE IF EXISTS TEST")

   #Creating table as per requirement
   sql ='''CREATE TABLE TEST(
      FIRST_NAME CHAR(20) NOT NULL,
      LAST_NAME CHAR(20),
      AGE INT,
      SEX CHAR(1),
      INCOME FLOAT
      )'''
   cursor.execute(sql)
   conn.commit()
   #Closing the connection
   conn.close()
   return "Table created successfull!"

run(host='localhost', port=8080)
