import os

from app import create_app


app = create_app()


if __name__ == "__main__":
    port = os.getenv("PORT", 8881)
    app.run(host="0.0.0.0", port=port, threaded=False, processes=4)
