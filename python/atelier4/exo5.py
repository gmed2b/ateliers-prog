# Exemple d'utilisation
import matplotlib.pyplot as plt


def graph(elem_lst: list, title="Test comparatif"):
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
    :param title: (str) titre du graph
    :return: None
    """
    fig, ax = plt.subplots()
    for item in elem_lst:
        ax.plot(item["size_lst"], item["avg_lst"], item["color"], label=item["label"])

    ax.set(xlabel='Nombre elements', ylabel='Temps execution (s)',
           title=title)
    ax.legend(loc='upper center', shadow=True,
              fontsize='x-large')  # fig.savefig("test.png")
    plt.show()
