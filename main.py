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
        customerssRows = cursor.fetchall()
        respone = jsonify(customersRows)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()  

# READ (cRud)
# this function uses the route /customers/<customerNumber> to get a specific customer
@app.route('/customers/<customer_number>')
def customer_details(customer_number):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("select customerNumber, customerName, contactLastName, contactFirstName, phone, addressLine1, addressLine2, city, state, postalCode, country, salesRepEmployeeNumber, creditLimit, gender FROM customers")
        customersRow = cursor.fetchone()
        respone = jsonify(customersRow)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close() 


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