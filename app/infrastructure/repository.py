from app.infrastructure.fake_db import fake_db


def get_all():
    return fake_db


def get_by_id(spell_id):
    return next((s for s in fake_db if s.id == spell_id), None)


def add(spell):
    fake_db.append(spell)


def delete(spell_id):
    fake_db[:] = [s for s in fake_db if s.id != spell_id]
