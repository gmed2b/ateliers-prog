import java.util.Random;

public class Main {
    public static void main(String[] args) {
        De d1 = new De();
        De d2 = new De(12);
        De d3 = new De("De");
        De d4 = new DePipe(8, "Super De", 6);
        De d5 = new DeMemoire();
        De.getNbDes();

        System.out.println(d1);
        System.out.println(d2);
        System.out.println(d3);
        System.out.println(d4);
        System.out.println(d5);

        for (int i = 0; i < 10; i++) {
        System.out.println("Lancer de d1 : " + d1.lancer());
            System.out.println("Lancer de d2 : " + d2.lancer(10));
            System.out.println("Lancer de d3 : " + d3.lancer());
            System.out.println("Lancer de d4 : " + d4.lancer());
            System.out.println("Lancer de d5 : " + d5.lancer());
        }

        System.out.println("d1 == d2 : " + d1.equals(d2));
        System.out.println("d2 == d3 : " + d2.equals(d3));
        System.out.println("d1 == d3 : " + d1.equals(d3));
        System.out.println("d1 == d5 : " + d1.equals(d5));
    }
}

