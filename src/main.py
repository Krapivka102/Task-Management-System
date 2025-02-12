from fastapi import FastAPI


def create_app() -> FastAPI:
    app = FastAPI(
        title='113-backend',
        docs_url='/api/docs',
        debug=True,
    )

    return app
