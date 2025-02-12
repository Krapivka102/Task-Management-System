from fastapi import FastAPI


def create_app() -> FastAPI:
    app = FastAPI(
        title='task-management-system',
        docs_url='/api/docs',
        debug=True,
    )

    return app
