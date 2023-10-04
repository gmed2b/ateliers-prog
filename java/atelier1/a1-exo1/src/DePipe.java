public class DePipe extends De {
    private int borneMin;

    public DePipe(int nbFaces, String nom, int borneMin) {
        super(nbFaces, nom);
        this.borneMin = borneMin;
    }

    public DePipe(int borneMin) {
        this(De.NB_FACES_DEFAUT, "", borneMin);
    }

    public void setBorneMin(int borneMin) {
        if (borneMin >= 1 && borneMin <= this.getNbFaces()) {
            this.borneMin = borneMin;
        } else {
            System.err.println("(" + this + ") La borne minimum doit être compris entre 1 et " + this.getNbFaces());
        }
    }

    int lancer() {
        int lancer;
        do {
            lancer = super.lancer();
        } while (lancer < this.borneMin);
        return lancer;
    }
}
