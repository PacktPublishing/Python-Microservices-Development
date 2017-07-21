from flask import Flask, jsonify, request 
 
app = Flask(__name__) 
 
@app.route('/api') 
def my_microservice(): 
    print(request) 
    print(request.environ) 
    response = jsonify({'Hello': 'World!'}) 
    print(response) 
    print(response.data) 
    return response 
 
if __name__ == '__main__': 
    print(app.url_map) 
    app.run() 