import pymysql
from app import app
from config import mysql
from flask import jsonify
from flask import flash, request          

# READ (cRud)
# this function uses the route /employees to get all employees
@app.route('/customers')
def employees():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("select * from customers")
        employeesRows = cursor.fetchall()
        respone = jsonify(employeesRows)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()  

# READ (cRud)
# this function uses the route /employees/<employeeId> to get a specific employee
#@app.route('/employees/<employees_id>')
#def employees_details(employees_id):
#    try:
#        conn = mysql.connect()
#        cursor = conn.cursor(pymysql.cursors.DictCursor)
#        cursor.execute("select employeeNumber, firstName, lastName, extension, email, officeCode, reportsTo, jobTitle FROM employees WHERE employeeNumber =%s", employees_id)
#        employeesRow = cursor.fetchone()
#        respone = jsonify(employeesRow)
#        respone.status_code = 200
#        return respone
#    except Exception as e:
#        print(e)
#    finally:
#        cursor.close() 
#        conn.close() 


# this method handles a 404 error returned from this service 
@app.errorhandler(404)
def showMessage(error=None):
    message = {
        'status': 404,
        'message': 'Record not found: ' + request.url,
    }
    respone = jsonify(message)
    respone.status_code = 404
    return respone
        
if __name__ == "__main__":
    app.run()