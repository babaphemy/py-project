import os

from starlette.responses import PlainTextResponse
from fastapi import FastAPI, APIRouter, Request
from fastapi.middleware.cors import CORSMiddleware
import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("app.log"), logging.StreamHandler()],
)

logger = logging.getLogger(__name__)


app = FastAPI(title="Horace API", description="Horace API", version="1.0.10")
welcome_router = APIRouter(tags=["Welcome"])

app_name = os.getenv("app_name", "api")


@welcome_router.get("/")
def welcome() -> dict[str, str]:
    return {"message": f"Welcome to the {app_name} API"}


@welcome_router.get("/health")
async def health_check(req: Request):
    return {"status": "healthy", "version": req.app.version}


@welcome_router.get("/robots.txt", response_class=PlainTextResponse)
def robots_txt():
    return "User-agent: *\nDisallow: /"


app.include_router(welcome_router)
allowed_origins = [
    "http://horace.local:3000",
    "http://localhost:3000",
    os.getenv("UI"),
    f"https://{os.getenv('DOMAIN')}",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_methods=["*"],
    allow_credentials=True,
    allow_headers=["*"],
)
