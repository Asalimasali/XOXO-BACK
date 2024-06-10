from sqlalchemy.orm import Session
import models, schemas


def get_user_by_name(db: Session, user_name: str):
    return db.query(models.User).filter(models.User.name == user_name).first()

def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_users(db: Session, skip: int, limit: int):
    return db.query(models.User).order_by(models.User.score.desc()).offset(skip).limit(limit).all()

def get_users_top10(db: Session):
    return db.query(models.User).order_by(models.User.score.desc()).limit(10).all()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(name=user.name, score=user.score)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user_score(db: Session, user_name: str, value: int):
    db.query(models.User).filter(models.User.name == user_name).update({models.User.score: models.User.score + value})
    db.commit()
    return db.query(models.User).filter(models.User.name == user_name).first()