package exo2;

public class Main {
    public static void main(String[] args) {
        // Test de la classe Entier
        Entier entier1 = new Entier(0, 10);
        System.out.println("Entier1 : " + entier1);

        Entier entier2 = new Entier(5, 15, 8);
        System.out.println("Entier2 : " + entier2);

        entier1.setValeur(3);
        System.out.println("Entier1 après setValeur : " + entier1);

        entier1.incrementer();
        System.out.println("Entier1 après incrementer : " + entier1);

        entier1.incrementer(5);
        System.out.println("Entier1 après incrementer(5) : " + entier1);
        entier1.incrementer(2);
        System.out.println("Entier1 après incrementer(2) : " + entier1);
        entier1.incrementer();
        System.out.println("Entier1 après incrementer : " + entier1);

        // Test de la classe EntierFou
        EntierFou entierFou1 = new EntierFou(0, 10, 2, 3);
        System.out.println("EntierFou1 : " + entierFou1);

        EntierFou entierFou2 = new EntierFou(5, 15, 8, 5);
        System.out.println("EntierFou2 : " + entierFou2);

        entierFou1.incrementer();
        System.out.println("EntierFou1 après incrementer : " + entierFou1);

        entierFou2.incrementer();
        System.out.println("EntierFou2 après incrementer : " + entierFou2);
    }
}
