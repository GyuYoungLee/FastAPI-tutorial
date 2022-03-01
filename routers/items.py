from typing import List

from fastapi import APIRouter, HTTPException, status, Response, Path
from pydantic import BaseModel, Field

inventory = [
    {
        "id": 1,
        "user_id": 1,
        "name": "shield",
        "price": 2500.0,
        "amount": 100,
    },
    {
        "id": 2,
        "user_id": 1,
        "name": "hat",
        "price": 300.0,
        "amount": 50,
    },
]


class Item(BaseModel):
    name: str = Field(..., min_length=1, max_length=100, title="이름")
    price: float = Field(None, ge=0)
    amount: int = Field(default=1, gt=0, le=100, title="수량", description="아이템 갯수. 1~100개 까지 소지 가능")


router = APIRouter()


@router.get("/users/{user_id}/items", response_model=List[Item])
def get_items(
        user_id: int = Path(..., gt=0, title="사용자 id", description="DB의 user.id")
) -> List[dict]:
    """
    아이템 리스트 조회
    """
    user_items = [item for item in inventory if item["user_id"] == user_id]

    if not user_items:
        raise HTTPException(detail="Item not found", status_code=status.HTTP_404_NOT_FOUND)

    return user_items


@router.post("/users/{user_id}/items", response_model=Item, status_code=status.HTTP_201_CREATED)
def insert_item(
        input_item: Item,
        user_id: int = Path(..., gt=0, title="사용자 id", description="DB의 user.id")
) -> dict:
    """
    아이템 추가
    """
    user_items = [item for item in inventory if item["user_id"] == user_id and item["name"] == input_item.name]

    if user_items:
        raise HTTPException(detail="Item is already exist", status_code=status.HTTP_400_BAD_REQUEST)

    new_item = dict(id=max([item["id"] for item in inventory]) + 1, user_id=user_id, **input_item.dict())
    inventory.append(new_item)

    return new_item


@router.get("/users/{user_id}/items/{name}", response_model=Item)
def get_item(
        user_id: int = Path(..., gt=0, title="사용자 id", description="DB의 user.id"),
        name: str = Path(None, min_length=1, max_length=2, title="아이템 이름")
) -> dict:
    """
    아이템 조회
    """
    user_items = [item for item in inventory if item["user_id"] == user_id and item["name"] == name]

    if not user_items:
        raise HTTPException(detail="Item not found", status_code=status.HTTP_404_NOT_FOUND)

    user_item, *_ = user_items
    return user_item


@router.patch("/users/{user_id}/items/{name}", response_model=Item)
def update_item(
        input_item: Item,
        user_id: int = Path(..., gt=0, title="사용자 id", description="DB의 user.id"),
        name: str = Path(None, min_length=1, max_length=2, title="아이템 이름")
) -> dict:
    """
    아이템 수정
    """
    user_items = [item for item in inventory if item["user_id"] == user_id and item["name"] == name]

    if not user_items:
        raise HTTPException(detail="Item not found", status_code=status.HTTP_404_NOT_FOUND)

    user_item, *_ = user_items
    for key, value in input_item.dict().items():
        user_item[key] = value

    return user_item


@router.delete("/users/{user_id}/items/{name}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(
        user_id: int = Path(..., gt=0, title="사용자 id", description="DB의 user.id"),
        name: str = Path(None, min_length=1, max_length=2, title="아이템 이름")
) -> Response:
    """
    아이템 삭제
    """
    user_items = [item for item in inventory if item["user_id"] == user_id and item["name"] == name]

    if not user_items:
        raise HTTPException(detail="Item not found", status_code=status.HTTP_404_NOT_FOUND)

    user_item, *_ = user_items
    inventory.remove(user_item)

    return Response(status_code=204)
