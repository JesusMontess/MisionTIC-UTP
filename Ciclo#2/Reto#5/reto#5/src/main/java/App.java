import java.awt.EventQueue; // Importamos la clase EventQueue
import view.Vista; //Importamos la Vista

/**
 * Persistencia Proyectos Construcción
 *
 */
public class App {
    public static void main(String[] args) {
        EventQueue.invokeLater(new Runnable(){ //Generamos una instacia de la clase que vamos a utlizar de awt
            @Override
            public void run(){
                try {
                    Vista frame = new Vista();
                    frame.setVisible(true);//Marco de interfaz, sera visible
                } catch (Exception e) {
                    
                    e.printStackTrace();
                }
            }
        });

        // Casos de prueba

        // Requerimiento 1
        //Vista.vista_requerimiento_1();
        //Vista.vista_requerimiento_2();
        //Vista.vista_requerimiento_3();
        //Vista.vista_requerimiento_4();
        //Vista.vista_requerimiento_5();


    }
}
