public class Expreso extends Casillero {
    // Constantes
        private final static int TIEMPO = 2;
    // Constructores
    public Expreso(double peso, double tamanio){
        super(peso, tamanio);
    }
    public Expreso(double precioBase){
        super(precioBase);
    }
    public Expreso(){ 
    }
    // Metodos
        public double calcularPrecio(){ 
        // Calculos
        double precioFinal = super.getPrecioBase() + (super.getPeso() * super.getTamanio() *TIEMPO);
        return precioFinal;
        }
    // getters/setters de ser necesarios
}