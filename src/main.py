from fastapi import FastAPI

app = FastAPI(
    title="Horoscope adviser App Backend",
    openapi_url="/api/openapi.json",
    docs_url="/api/swagger",
)
