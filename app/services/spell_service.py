from app.domain.models import Spell
from app.domain.rules import calcular_dano
from app.infrastructure import repository
from app.api.responses import response


def create_spell(payload: dict):
    try:
        spell = Spell(**payload)
        repository.add(spell)
        return response(201, spell.dict())
    except Exception as e:
        return response(400, error=str(e))


def search_spells(nome=None, escola=None, nivel=None):
    spells = repository.get_all()

    if nome:
        spells = [s for s in spells if nome.lower() in s.nome.lower()]
    if escola:
        spells = [s for s in spells if s.escola == escola]
    if nivel is not None:
        spells = [s for s in spells if s.nivel == nivel]

    if not spells:
        return response(404, error="Nenhuma magia encontrada")

    return response(200, [s.dict() for s in spells])


def calcular_dano_escala(id_magia: int, nivel_slot: int):
    spell = repository.get_by_id(id_magia)

    if not spell:
        return response(404, error="Nenhuma Magia encontrada")

    try:
        dano = calcular_dano(spell, nivel_slot)
        return response(200, {
            "magia": spell.nome,
            "nivel_slot": nivel_slot,
            "dano": dano
        })
    except Exception as e:
        return response(400, error=str(e))
