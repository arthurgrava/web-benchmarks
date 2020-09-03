import os

from benchmark_common import db

from app import create_app


if __name__ == "__main__":
    port = os.getenv("PORT", 8881)
    app = create_app()
    app.es = db.DB()
    app.run(host="0.0.0.0", port=port, threaded=False, processes=4)
