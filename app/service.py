from sqlalchemy import create_engine
from db.config import DATABASE_URI
from db.books import Book
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

engine = create_engine(DATABASE_URI)

Session = sessionmaker(bind=engine)


@contextmanager
def session_scope():
    session = Session()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


class BooksService:
    def __init__(self):
        self.model = Book()

    def create(self, params):
        print(params)

        book = Book(**params)
        with session_scope() as s:
            s.add(book)
            print(book)
            return book

    def list(self):
        with session_scope() as s:
            books = s.query(Book).all()
            print(books)
        # return books
