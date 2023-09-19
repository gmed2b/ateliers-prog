# Exemple d'utilisation
import matplotlib.pyplot as plt


def graph(elem_lst: list):
    """
    Affiche un graphique à partir d'une liste d'éléments
    sous la forme : [ {
            "size_lst": [100, 500, ...],\n
            "avg_lst": [0.00553, 0.02365, ...],\n
            "label": "Perso"\n
        },
        ...
    ]
    :param elem_lst: (list) liste d'éléments
    :return: None
    """
    # elem_lst = [
    #     {
    #         "size_lst": [100, 500, 1000, 5000, 10000],
    #         "avg_lst": [0.00553, 0.02365, 0.27235, 0.59861, 3.56079],
    #         "label": "Perso"
    #     },
    #     {
    #         "size_lst": [100, 500, 1000, 5000, 10000],
    #         "avg_lst": [0.00034, 0.00122, 0.01056, 0.02126, 0.12261],
    #         "label": "Native"
    #     }
    # ]
    fig, ax = plt.subplots()
    for item in elem_lst:
        ax.plot(item["size_lst"], item["avg_lst"], item["color"], label=item["label"])

    ax.set(xlabel='Nombre elements', ylabel='Temps execution (s)',
           title='Tests comparatifs')
    ax.legend(loc='upper center', shadow=True,
              fontsize='x-large')  # fig.savefig("test.png")
    plt.show()
