#! python3 recommendation_program.pyw

import os

plano_de_beneficios = {"aposentadoria":
    {"aposentadoria por tempo de contribuição" : {"beneficiário": "segurado",
                                                 "carência": 180,
                                                 "idade mínima": 65},
    "aposentadoria especial": {"beneficiário": "segurado",
                               "carência": 180},
    "aposentadoria da pessoa portadora de deficiência": {"beneficiário": "segurado",
                                                         "carência": 180,
                                                         "tempo de contribuição deficiência grave": 25,
                                                         "tempo de contribuição deficiência moderada": 29,
                                                         "tempo de contribuição deficiência leve": 33},
     "aposentadoria por idade urbana": {"beneficiário": "segurado",
                                        "carência": 180},
     "aposentadoria por idade rural": {"beneficiário": "segurado",
                                       "carência": 180,
                                       "idade mínima": 60},
     "aposentadoria do professor": {"beneficiário": "segurado",
                                    "carência": 180,
                                    "tempo de contribuição": 30,
                                    "idade mínima": 60}},
    "benefício por incapacidade":
                           {"aposentadoria por incapacidade permanente": {"beneficiário": "segurado",
                                                  "carência": 180},
    "auxílio-acidente": {"beneficiário": "segurado",
                         "carência": 0},
    "auxílio por incapacidade temporária": {"beneficiário": "segurado",
                                            "carência": 12}},
    "pensão por morte": {"beneficiário": "dependente",
                         "carência": 18},
    "auxílio-reclusão": {"beneficiário": "dependente",
                         "carência": 24},
    "salário maternidade": {"beneficiário": "segurado",
                            "carência": 10},

    "salário-família": {"beneficiário": "segurado",
                        "carência": 0},
    "reabilitação profissional": {"beneficiário": "segurado",
                                  "carência": 0}
}

# Hash Map class
class HashMap:
    def __init__(self, array_size):
        self.array_size = array_size
        self.array = [None for item in range(array_size)]

    def hash(self, key,count_collisions=0):
        key_bytes = key.encode()
        hash_code = sum(key_bytes)
        return hash_code + count_collisions

    def compressor(self, hash_code):
        return hash_code % self.array_size

    def assign(self, key, value):
        array_index = self.compressor(self.hash(key))
        current_array_value = self.array[array_index]
        if current_array_value is None:
            self.array[array_index] = [key, value]
            return
        if current_array_value[0] == key:
            self.array[array_index] = [key, value]
            return
        number_collisions = 1
        while (current_array_value[0] != key):
            new_hash_code = self.hash(key, number_collisions)
            new_array_index = self.compressor(new_hash_code)
            current_array_value = self.array[new_array_index]
            if current_array_value is None:
                self.array[new_array_index] = [key, value]
                return
            if current_array_value[0] == key:
                self.array[new_array_index] = [key, value]
                return

            number_collisions += 1
        return

    def retrieve(self, key):
        array_index = self.compressor(self.hash(key))
        possible_return_value = self.array[array_index]
        if possible_return_value is None:
            return None
        if possible_return_value[0] == key:
            return possible_return_value[1]
        retrieval_collisions = 1

        while (possible_return_value != key):
            new_hash_code = self.hash(key, retrieval_collisions)
            retrieving_array_index = self.compressor(new_hash_code)
            possible_return_value = self.array[retrieving_array_index]
            if possible_return_value is None:
                return None
            if possible_return_value[0] == key:
                return possible_return_value[1]
            retrieval_collisions += 1
        return

plano_HM = HashMap(len(plano_de_beneficios))
for key, value in plano_de_beneficios.items():
    plano_HM.assign(key, value)
#print(plano_HM.array)

# linear search engine
def linear_search(lista):
    matches = []
    data = []
    target_chunk = input("Digite as iniciais do termo a pesquisar e pressione <enter>. \nSua escolha: ")
    for key, value in lista:
        if (target_chunk in key) or (target_chunk in value.values()):
            matches.append(key)
            data.append(value)
    if len(matches) == 0:
        raise ValueError(f"Nenhum tópico com as letras {target_chunk} foi encontrado.")
    else:
        if len(matches) > 1:
            print(f"Com essas letras, as opções são: {matches}")
            linear_search(lista)
        else:
            print(f"A opção disponível com essas letras é {matches[0]}. Você quer consultar {matches[0]}?"
                  f" Digite 'S' para sim e 'N' para sair.")
            answer = input("Sua escolha: ")
            if answer == "S":
                print(f"\nEstes são os dados do benefício escolhido: {matches[0]}")
                if type(list(data[0].values())[0]) is not str:
                    for beneficio, item in data[0].items():
                        print("\n", beneficio.upper())
                        for dado, valor in item.items():
                            print(f"- {dado}: {valor}")
                else:
                    print("\n", matches[0].upper())
                    for dado, valor in data[0].items():
                        print(f"- {dado}: {valor}")


def main():
    os.system('clear')
    welcome_message = "Plano de benefícios da Previdência Social"
    print()
    print((len(welcome_message) + 30) * '=')
    print((len(welcome_message) + 30) * '=')
    print()
    print(f"               {welcome_message:15}")
    print()
    print((len(welcome_message) + 30) * '=')
    print((len(welcome_message) + 30) * '=')
    print()
    try:
        linear_search(plano_HM.array)
    except ValueError as error_message:
        print("{}".format(error_message))
    finally:
        os.system('exit')

main()
