import sqlalchemy
from .db_session import SqlAlchemyBase


class First_page(SqlAlchemyBase):
    __tablename__ = 'first_page'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    kol_vo = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    tema_vopr = sqlalchemy.Column(sqlalchemy.String, nullable=True)