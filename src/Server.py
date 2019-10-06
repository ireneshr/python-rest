'''
Created on Oct 4, 2019

@author: Irene Hermosilla
'''
from flask import Flask, jsonify, request, abort

app = Flask(__name__)

empDB = [
  {
    "id": "0",
    "name": "Josephine Hawkins",
    "phone": "+1 (862) 428-2160"
  },
  {
    "id": "1",
    "name": "Barrett Fulton",
    "phone": "+1 (881) 496-2875"
  },
  {
    "id": "2",
    "name": "Erin Lynch",
    "phone": "+1 (827) 524-3459"
  },
  {
    "id": "3",
    "name": "Valerie Potter",
    "phone": "+1 (965) 586-2319"
  },
  {
    "id": "4",
    "name": "Brandi Douglas",
    "phone": "+1 (817) 422-3504"
  }
]


@app.route('/employee', methods=['GET'])
def getAllEmp():
    return jsonify({'emps':empDB})


@app.route('/employee/<empId>', methods=['GET'])
def getEmp(empId):
    usr = [ emp for emp in empDB if (emp['id'] == empId) ] 
    return jsonify({'emp':usr})


@app.route('/employee/<empId>', methods=['PUT'])
def updateEmp(empId):
    em = [ emp for emp in empDB if (emp['id'] == empId) ]
    if 'name' in request.json : 
        em[0]['name'] = request.json['name']
    if 'phone' in request.json:
        em[0]['phone'] = request.json['phone']
    return jsonify({'emp':em[0]})


@app.route('/employee', methods=['POST'])
def createEmp():
    dat = {
    'id':request.json['id'],
    'name':request.json['name'],
    'phone':request.json['phone']
    }
    empDB.append(dat)
    return jsonify(dat)


@app.route('/employee/<empId>', methods=['DELETE'])
def deleteEmp(empId):
    em = [ emp for emp in empDB if (emp['id'] == empId) ]
    if len(em) == 0:
        abort(404)
    empDB.remove(em[0])
    return jsonify({'response':'Success'})


if __name__ == '__main__':
    app.run()
