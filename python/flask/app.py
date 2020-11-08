import os
from http import HTTPStatus

from benchmark_common import emulator
from flask import Flask, jsonify


app = Flask("Flask Benchy")


@app.errorhandler(HTTPStatus.NOT_FOUND.value)
@app.errorhandler(HTTPStatus.BAD_REQUEST.value)
@app.errorhandler(HTTPStatus.INTERNAL_SERVER_ERROR.value)
def common_http_handler(err):
    return jsonify(message=str(err)), err.code


@app.route("/api/live")
def alive():
    return jsonify(message="We are live")


@app.route("/api/db-call")
def do_db_call():
    res = emulator.sync_database_request()
    return jsonify(res)


@app.route("/api/calculation")
def do_calculation():
    res = emulator.do_some_calculation()
    return jsonify(res)


@app.route("/api/complete")
def do_complete_scenario():
    res = emulator.sync_complete_scenario()
    return jsonify(res)


if __name__ == "__main__":
    port = os.getenv("PORT", 8881)
    app.run("0.0.0.0", port=port)
