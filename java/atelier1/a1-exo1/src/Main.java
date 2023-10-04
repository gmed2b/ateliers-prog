import java.util.Random;

public class Main {
    public static void main(String[] args) {
        De d1 = new De();
        De d2 = new De(12);
        De d3 = new De("De n°1");
        De.getNbDes();

        System.out.println(d1);
        System.out.println(d2);
        System.out.println(d3);

        System.out.println("Lancer de d1 : " + d1.lancer());
        System.out.println("Lancer de d2 : " + d2.lancer(10));
        System.out.println("Lancer de d3 : " + d3.lancer());

        System.out.println("d1 == d2 : " + d1.equals(d2));
        System.out.println("d2 == d3 : " + d2.equals(d3));
        System.out.println("d1 == d3 : " + d1.equals(d3));
    }
}

