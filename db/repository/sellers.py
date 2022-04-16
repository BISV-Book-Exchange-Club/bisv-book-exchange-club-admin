from db.models.sellers import Sellers
from schemas.sellers import SellerCreate
from sqlalchemy.orm import Session


def create_new_seller(seller: SellerCreate, db: Session):
    seller_object = Sellers(**seller.dict())
    db.add(seller_object)
    db.commit()
    db.refresh(seller_object)
    return seller_object


def retrieve_seller(id: int, db: Session):
    item = db.query(Sellers).filter(Sellers.id == id).first()
    return item


def get_seller_id_from_collection(collection: str, db: Session):
    item = db.query(Sellers).filter(Sellers.collection == collection).first()
    return item


def list_sellers(db: Session):
    sellers = db.query(Sellers).all()
    return sellers


def update_seller_by_id(id: int, seller: SellerCreate, db: Session):
    existing_seller = db.query(Sellers).filter(Sellers.id == id).first()
    if not existing_seller:
        return 0

    #seller.__dict__.update(
    #    owner_id=owner_id
    #)  # update dictionary with new key value of owner_id
    #existing_seller.update(seller.__dict__)

    for var, value in vars(seller).items():
        setattr(existing_seller, var, value) if value else None

    db.add(existing_seller)
    db.commit()
    db.refresh(existing_seller)
    return 1


def delete_seller_by_id(id: int, db: Session):
    existing_seller = db.query(Sellers).filter(Sellers.id == id).first()
    if not existing_seller:
        return 0
    existing_seller.delete(synchronize_session=False)
    db.commit()
    return 1


def search_seller(query: str, db: Session):
    sellers = db.query(Sellers).filter(Sellers.title.contains(query))
    return sellers
