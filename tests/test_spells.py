from app.services.spell_service import create_spell


def test_magia_material_sem_custo():
    payload = {
        "id": 10,
        "nome": "Ressurreição",
        "nivel": 7,
        "escola": "Necromancia",
        "tipo": "Divina",
        "descricao": "Ressuscita um aliado.",
        "execucao": "10 minutos",
        "alcance": "toque",
        "duracao": "instantânea",
        "material": True
    }

    res = create_spell(payload)
    assert res["status_code"] == 400
