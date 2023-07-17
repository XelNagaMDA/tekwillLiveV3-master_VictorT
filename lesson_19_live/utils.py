def safe_index_get(max_index):
    """
    O functie care va extrage din input o valoare care poate fi folosita ca indice pentru o lista
    :param max_index: limita de sus pentru indice
    :return:
    """
    while True:
        try:
            selected_index = int(input('Input the index of the task: '))
            if selected_index > max_index:
                # Indecele este mai mare decat limita
                print('Selected index is out of range')
                raise ValueError('')
            if selected_index < -max_index - 1:
                # Indecele este mai mic decat limita pentru indice negativ
                print('Selected index is out of range')
                raise ValueError('')
            # Indicele este valid
            return selected_index
        except ValueError:
            # Valoarea introdusa la consola nu este un int
            print('Value is not valid')
