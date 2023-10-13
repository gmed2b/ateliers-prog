package exo2;

import java.util.Random;

public class EntierFou extends Entier {
    private int niveauDeFolie;
    Random r = new Random();

    public EntierFou(int borneInf, int borneSup, int valeur, int niveauDeFolie) {
        super(borneInf, borneSup, valeur);
        this.niveauDeFolie = niveauDeFolie;
    }

    @Override
    public String toString() {
        return "EntierFou{" +
                "BORNE_INF=" + this.getBORNE_INF() +
                ", BORNE_SUP=" + this.getBORNE_SUP() +
                ", valeur=" + this.getValeur() +
                ", niveauDeFolie=" + niveauDeFolie +
                '}';
    }

    @Override
    public void incrementer() {
        if (this.getValeur() < this.getBORNE_SUP()) {
            int randomValue = r.nextInt(0, this.niveauDeFolie + 1);
            System.out.printf("Valeur aléatoire : %d%n", randomValue);
            this.setValeur(randomValue + this.getValeur());
        } else {
            System.out.println("La valeur ne peut pas dépasser " + this.getBORNE_SUP());
        }
    }
}


