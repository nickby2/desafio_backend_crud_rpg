from app.domain.models import Spell

fake_db = [

    Spell(
        id=1,
        nome="Bola de Fogo",
        nivel=2,
        escola="Evocação",
        tipo="Arcana",
        dano_base="8d6",
        progressao_slot={4: "9d6", 5: "10d6"},
        descricao = "Esta famosa magia de ataque cria uma poderosa explosão, causando 6d6 pontos de dano de fogo em todas as criaturas e objetos livres na área.",
        execucao= "padrão",
        alcance= "médio",
        duracao= "instantânea"

    ),

    Spell(
        id=2,
        nome="Armadura Arcana",
        nivel=1,
        escola="Abjuração",
        tipo="Arcana",
        descricao = "Esta magia cria uma película protetora invisível, mas tangível, fornecendo +5 na Defesa. Esse bônus é cumulativo com outras magias, mas não com bônus fornecido por armaduras.",
        execucao= "padrão",
        alcance= "médio",
        duracao= "cena"

    ),

    Spell(
        id=3,
        nome="Oração",
        nivel=2,
        escola="Encantamento",
        tipo="Divina",
        descricao = "Você e os seus aliados no alcance recebem +2 em testes de perícia e rolagens de dano, e todos os seus inimigos no alcance sofrem –2 em testes de perícia e rolagens de dano.",
        execucao= "padrão",
        alcance= "curto",
        duracao= "sustentada",
        exige_material=True,
        custo_em_ouro=25

    )
]