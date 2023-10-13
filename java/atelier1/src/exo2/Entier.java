package exo2;

public class Entier {
    private final int BORNE_INF, BORNE_SUP;
    private int valeur;

    public Entier(int borneInf, int borneSup, int valeur) {
        this.BORNE_INF = borneInf;
        this.BORNE_SUP = borneSup;
        this.setValeur(valeur);
    }

    public Entier(int borneInf, int borneSup) {
        this.BORNE_INF = borneInf;
        this.BORNE_SUP = borneSup;
        this.valeur = 0;
    }

    @Override
    public String toString() {
        return "Entier{" +
                "BORNE_INF=" + BORNE_INF +
                ", BORNE_SUP=" + BORNE_SUP +
                ", valeur=" + valeur +
                '}';
    }

    @Override
    public boolean equals(Object obj) {
        if (obj instanceof Entier e) {
            return this.getValeur() == e.getValeur();
        } else {
            return false;
        }
    }

    public int getBORNE_INF() {
        return BORNE_INF;
    }

    public int getBORNE_SUP() {
        return BORNE_SUP;
    }

    public int getValeur() {
        return valeur;
    }

    public void setValeur(int valeur) {
        if (valeur >= this.getBORNE_INF() && valeur <= this.getBORNE_SUP()) {
            this.valeur = valeur;
        } else {
            System.out.println("/!\\ La valeur doit être comprise entre " + BORNE_INF + " et " + BORNE_SUP);
        }
    }

    public void incrementer() {
        if (this.valeur < BORNE_SUP) {
            this.valeur++;
        } else {
            System.out.println("La valeur ne peut pas dépasser " + BORNE_SUP);
        }
    }

    public void incrementer(int step) {
        if (this.valeur + step <= BORNE_SUP) {
            this.valeur += step;
        } else {
            System.out.println("/!\\ La valeur ne peut pas dépasser " + BORNE_SUP);
        }
    }
}
