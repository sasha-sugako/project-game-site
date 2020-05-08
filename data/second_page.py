import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Second_page(SqlAlchemyBase):
    __tablename__ = 'second_page'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    otve = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    kol_isp = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    vopr_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("first_page.id"))
    first_pag = orm.relation('First_page')
    second_pag = orm.relation("Second_page", back_populates='first_pag')