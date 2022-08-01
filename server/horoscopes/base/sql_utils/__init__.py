from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session


def try_flush_commit(session: Session, commit: bool = True) -> bool:
    """Try to flush commit to db and commit it if needed."""
    try:
        session.flush()
    except IntegrityError as e:
        session.rollback()
        raise e
    else:
        if commit:
            session.commit()
            return True
    return False
