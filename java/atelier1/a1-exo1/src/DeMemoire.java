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

    int lancer() {
        int lancer;
        do {
            lancer = super.lancer();
        } while (lancer == this.dernierLancer);
        this.dernierLancer = lancer;
        return lancer;
    }
}
