package exo1;

public class Main {
    public static void main(String[] args) {
        // write some test with 2 robots
        Robot r1 = new Robot("R2D2");
        Robot r2 = new Robot("C3PO", 2, 3, Robot.SUD);
        r1.afficheToi();
        r2.afficheToi();
        r1.deplacer();
        r2.deplacer();
        r1.afficheToi();
        r2.afficheToi();
        r1.setOrientation(Robot.EST);
        r2.setOrientation(Robot.OUEST);
        r1.deplacer();
        r2.deplacer();
        System.out.println(r1);
        System.out.println(r2);
    }
}
