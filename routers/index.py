from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

# Local imports
from scrapper.scrapper import scrap_articles

router = APIRouter(prefix='/scrape')

@router.get('/', status_code=status.HTTP_200_OK)
async def scrap_articles_router():
    data = await scrap_articles()
    return JSONResponse(content=jsonable_encoder(data))
