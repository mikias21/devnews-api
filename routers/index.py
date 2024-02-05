from fastapi import APIRouter, status

# Local imports
from scrapper.scrapper import scrap_articles

router = APIRouter(prefix='/scrape')

@router.get('/', status_code=status.HTTP_200_OK)
async def scrap_articles_router():
    data = await scrap_articles()
    return data
