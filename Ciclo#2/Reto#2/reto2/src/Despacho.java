public class Despacho extends Casillero {
    // Constantes
        private static final double CAPACIDAD = 8.0;
    // Constructores
    public Despacho(double peso, double tamanio){
        super(peso, tamanio);
    }

    public Despacho(double precioBase){
        super(precioBase);
    }
    public Despacho(){

    }

    // Metodos
        public double calcularPrecio(){
    // Calculos
        double precioFinal = super.getPrecioBase() + (super.getPeso()* super.getTamanio() *CAPACIDAD);
        return precioFinal;
        }
    // getters/setters de ser necesarios
}
