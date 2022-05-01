#! python3 recommendation_program.pyw
'''
=>PORT: O objetivo deste programa é localizar um determinado benefício previdenciário dentre os principais
 benefícios previstos na Lei n. 8.213/1991 e administrados pelo Instituto Naciona do Seguro Social de
 acordo com os parâmetros informados pelo usuário.
=> ENG: The goal of this program is recommending benefits among those offered by the Brazilian Social
Security agency according to the parameters given by the user.
This is my portfolio project in CS 102: Data Structures and Algorithms at Codecademy.
Algorithm used: linear search
'''

plano_de_beneficios = {
    "aposentadoria por tempo de contribuição" : {"beneficiário": "segurado",
                                                 "carência": 180,
                                                 "idade mínima": 65},
    "auxílio por incapacidade temporária": {"beneficiário": "segurado",
                                            "carência": 12},
    "aposentadoria por incapacidade permanente": {"beneficiário": "segurado",
                                                  "carência": 180},
    "auxílio-acidente": {"beneficiário": "segurado",
                         "carência": 0},
    "pensão por morte": {"beneficiário": "dependente",
                         "carência": 18},
    "aposentadoria especial": {"beneficiário": "segurado",
                               "carência": 180},
    "aposentadoria da pessoa portadora de deficiência": {"beneficiário": "segurado",
                                                         "carência": 180,
                                                         "tempo de contribuição deficiência grave": 25,
                                                         "tempo de contribuição deficiência moderada": 29,
                                                         "tempo de contribuição deficiência leve": 33},
    "auxílio-reclusão": {"beneficiário": "dependente",
                         "carência": 24},
    "salário maternidade": {"beneficiário": "segurado",
                            "carência": 10},
    "aposentadoria por idade urbana": {"beneficiário": "segurado",
                                       "carência": 180},
    "aposentadoria por idade rural": {"beneficiário": "segurado",
                                      "carência": 180,
                                      "idade mínima": 60},
    "salário-família": {"beneficiário": "segurado",
                        "carência": 0},
    "reabilitação profissional": {"beneficiário": "segurado",
                                  "carência": 0},
    "aposentadoria do professor": {"beneficiário": "segurado",
                                   "carência": 180,
                                   "tempo de contribuição": 30,
                                   "idade mínima": 60}
}

# TODO: searching engine
def linear_search(benefits, target):
    matches = []
    for key, value in list(plano_de_beneficios.items()):
        if target in value.values():
            matches.append(key)
    if len(matches) == 0:
        raise ValueError(f"{target} não encontrado.")
    else:
        return matches

print(linear_search(plano_de_beneficios, "segurado"))


