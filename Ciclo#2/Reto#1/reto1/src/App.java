public class App {
    public static void main(String[] args) throws Exception {
        //System.out.println("Hello, World!");

        //Importacion investment = new  Importacion();

        //String result = investment.compararInvImportacion(12, 2000000, 0.05);
        //System.out.println(result+"\n");

        //result = investment.compararInvImportacion(18, 3000000, 0);
        //System.out.println("\n"+result);

        Importacion objImportacion = new Importacion();
        System.out.println(objImportacion.compararInvImportacion(12, 1000000, 0.1));
        //Importacion objImportacion = new Importacion();
        System.out.println(objImportacion.compararInvImportacion(10, 2000000, 0.12));
    }
}
