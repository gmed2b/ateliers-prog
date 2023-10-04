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

class Robot {
    public final static int NORD = 1;
    public final static int EST = 2;
    public final static int SUD = 3;
    public final static int OUEST = 4;
    static int nbRobot = 0;
    String reference;
    String name;
    int x;
    int y;
    int orientation;

    public Robot(String name, int x, int y, int orientation) {
        this.reference = "ROB" + nbRobot;
        this.name = name;
        this.x = x;
        this.y = y;
        this.orientation = orientation;
        nbRobot++;
    }

    public Robot(String name) {
        this(name, 0, 0, NORD);
    }

    public void setOrientation(int orientation) {
        if (orientation >= NORD && orientation <= OUEST) {
            this.orientation = orientation;
        }
    }

    public String printOrientation(int orientation) {
        return switch (orientation) {
            case EST -> "EST";
            case SUD -> "SUD";
            case OUEST -> "OUEST";
            default -> "NORD";
        };
    }

    public void deplacer() {
        if (this.orientation == NORD) {
            this.y++;
        } else if (this.orientation == EST) {
            this.x++;
        } else if (this.orientation == SUD) {
            this.y--;
            if (this.y < 0) {
                this.y = 0;
            }
        } else if (this.orientation == OUEST) {
            this.x--;
            if (this.x < 0) {
                this.x = 0;
            }
        }
    }

    public void afficheToi() {
        System.out.println("Je suis " + this.reference + " alias " + this.name + ". Je me situe en (" + this.x + ", " + this.y + ") " + this.printOrientation(this.orientation));
    }

    public String toString() {
        return "Je suis " + this.reference + " alias " + this.name + ". Je me situe en (" + this.x + ", " + this.y + ") " + this.printOrientation(this.orientation);
    }
}