import os
from flask import Flask, jsonify
from sqlalchemy import create_engine
from dotenv import load_dotenv
from sqlalchemy import text

load_dotenv()

app = Flask(__name__)

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

@app.route('/')
def ping():
    data = {
        "code": 200,
        "response": "Respuesta desde API en Docker"
	}
    return jsonify(data)


@app.route('/productos')
def productos():
    query = text ("""SELECT * FROM Productos""")

    with engine.connect() as conn:
        result = conn.execute(query)
        data = [dict(row._mapping) for row in result]

    return jsonify({
        "code" : 200,
        "data" : data
    })

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
