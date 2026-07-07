from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def home():
    return {
        "system": "TitanOS",
        "status": "online"
    }


@router.get("/assistant")
def assistant():
    return {
        "response": "Hello, I am TitanOS. How can I help?"
    }