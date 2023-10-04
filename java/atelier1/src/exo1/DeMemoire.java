package exo1;

public class DeMemoire extends De {
    private int dernierLancer;

    /**
     * Constructs a dice with the specified number of faces and a name.
     *
     * @param nbFaces the number of faces on the dice
     * @param nom     the name of the dice
     */
    public DeMemoire(int nbFaces, String nom) {
        super(nbFaces, nom);
    }

    /**
     * Constructs a dice with the specified number of faces and a default name.
     *
     * @param nbFaces the number of faces on the dice
     */
    public DeMemoire(int nbFaces) {
        super(nbFaces);
    }

    /**
     * Constructs a dice with a default number of faces and the specified name.
     *
     * @param nom the name of the dice
     */
    public DeMemoire(String nom) {
        super(nom);
    }

    /**
     * Constructs a dice with a default number of faces and a default name.
     */
    public DeMemoire() {
        super();
    }

    /**
     * Rolls the dice while the result is the same as the last one and returns the result.
     *
     * @return a random number between 1 and the number of faces on this dice
     */
    int lancer() {
        int lancer;
        do {
            lancer = super.lancer();
        } while (lancer == this.dernierLancer);
        this.dernierLancer = lancer;
        return lancer;
    }
}
