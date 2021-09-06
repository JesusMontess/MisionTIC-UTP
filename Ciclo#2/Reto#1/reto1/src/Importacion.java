/**
 * Autor: Jesus Montes
 * Fecha: 31/Julio/2021
 */
/**
 * Clase que representa un Proyecto
 */
public class Importacion {
// ---------------------------------------------
// Atributos
// ---------------------------------------------
// ---------------------------------------------
// Métodos Constructor
// ---------------------------------------------
    public Importacion(){

    }

    //Metodos de clases
    public String compararInvImportacion(int tiempo, double capital, double interes){
        double respuesta;
        respuesta = calcularInteresCompuesto(tiempo, capital, interes) - calcularInteresSimple(tiempo, capital, interes);

        if (respuesta > 0){
            return "La diferencia en el total de intereses generados para el proyecto, si escogemos entre evaluarlo a una tasa de interés Compuesto y evaluarlo a una tasa de interés Simple, asciende a la cifra de: $"+respuesta;
        }else{
            return "Faltan datos para calcular la diferencia en el total de intereses generados para el proyecto.";
        }

    }
    //Metodos para calcular los Intereses
    private double calcularInteresCompuesto(int tiempo, double capital, double interes){
        return capital * ((Math.pow((1+interes), tiempo))-1);

    }

    private double calcularInteresSimple(int tiempo, double capital, double interes){
        return capital * interes * tiempo;

    }

    
}
