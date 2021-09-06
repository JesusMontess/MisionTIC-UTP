package view;


import java.sql.SQLException;
import java.util.ArrayList;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;
import javax.swing.SwingConstants;
import javax.swing.border.EmptyBorder;

import controller.Controlador;
import model.vo.Lider;
import model.vo.Proyecto;

public class Vista extends JFrame {
    //Instanciamos el controlador de manera estatica
    public static final Controlador controlador = new Controlador();

    private static final long serialVersionUID = 1L;
    private JPanel contentPane; //variable de tipo privada para el panel del contenido
    private JTextArea textArea;  // variable de tipo rivada para el area de texto
    

    //CONSTRUCCION DE LA VENTANA
    public Vista(){
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);//Nos permite cerrar la opracion
        setBounds(450, 200, 850, 650);//Dimensionamos el tamaño de la ventana
        contentPane = new JPanel();//Creamos una instancia del JPanel
        contentPane.setBorder(new EmptyBorder(5,5,5,5));//seteamos los bordes
        setContentPane(contentPane);
        contentPane.setLayout(null);//Permitir mostrar el contenido aunque este vacio

        //Agregamos el titulo a mostrar en ventana
        JLabel lbTitulo = new JLabel("MISION TIC UTP ====> RETO #5", SwingConstants.CENTER);
        lbTitulo.setBounds(250, 6, 201, 16);//Dimensionamos el titulo
        //lbTitulo.setBounds(x, y, width, height);
        contentPane.add(lbTitulo);//Agregamos el titulo en el Panel

        //Agregamos el Autor a mostrar en Vnetana
        JLabel lbAutor = new JLabel(" AUTOR: JESUS MONTES SANCHEZ");
        lbAutor.setBounds(28, 34, 208, 16);
        contentPane.add(lbAutor);
        ///////////
        
 
  
        //Agregamos los componentes con scrollpane
        JScrollPane scrollPane = new JScrollPane();
        scrollPane.setBounds(28, 70, 737, 455);
        contentPane.add(scrollPane);

        //Agregamos el area de texto
        textArea = new JTextArea();
        scrollPane.setViewportView(textArea);

        //Agregamos el Boton requerimiento1
        JButton btnRequerimiento1 = new JButton("Query #1");
        btnRequerimiento1.addActionListener(new ActionListener(){
            @Override
            public void actionPerformed(ActionEvent e) {
                // TODO Auto-generated method stub
                vista_requerimiento_1();
            }
        });
        //seteamos los limites del boton para ubicarlos en la ventana
        btnRequerimiento1.setBounds(28, 537, 117, 29);
        contentPane.add(btnRequerimiento1);//adicionamos el boton al panel del contenido

        //Agregamos el Boton requerimiento2
        JButton btnRequerimiento2 = new JButton("Query #2");
        btnRequerimiento2.addActionListener(new ActionListener(){
            @Override//sobreescritura de motodos
            public void actionPerformed(ActionEvent e) {
                // TODO Auto-generated method stub
                vista_requerimiento_2();
            }
        });
        //seteamos los limites del boton para ubicarlos en la ventana
        btnRequerimiento2.setBounds(157, 537, 117, 29);
        contentPane.add(btnRequerimiento2);//adicionamos el boton al panel del contenido

        //Agregamos el Boton requerimiento3
        JButton btnRequerimiento3 = new JButton("Query #3");
        btnRequerimiento3.addActionListener(new ActionListener(){
            @Override//sobreescritura de motodos
            public void actionPerformed(ActionEvent e) {
                // TODO Auto-generated method stub
                vista_requerimiento_3();
                
            }
        });
        //seteamos los limites del boton para ubicarlos en la ventana
        btnRequerimiento3.setBounds(286, 537, 117, 29);
        contentPane.add(btnRequerimiento3);//adicionamos el boton al panel del contenido

        //Agregamos el Boton requerimiento4
        JButton btnRequerimiento4 = new JButton("Query #4");
        btnRequerimiento4.addActionListener(new ActionListener(){
            @Override//sobreescritura de motodos
            public void actionPerformed(ActionEvent e) {
                // TODO Auto-generated method stub
                vista_requerimiento_4();

            }
        });
        //seteamos los limites del boton para ubicarlos en la ventana
        btnRequerimiento4.setBounds(415, 537, 117, 29);
        contentPane.add(btnRequerimiento4);//adicionamos el boton al panel del contenido

        //Agregamos el Boton requerimiento5
        JButton btnRequerimiento5 = new JButton("Query #5");
        btnRequerimiento5.addActionListener(new ActionListener(){
            @Override
            public void actionPerformed(ActionEvent e) {
                // TODO Auto-generated method stub
               vista_requerimiento_5();
            }
        });
        //seteamos los limites del boton para ubicarlos en la ventana
        btnRequerimiento5.setBounds(544, 537, 117, 29);
        contentPane.add(btnRequerimiento5);//adicionamos el boton al panel del contenido

        //Agregamos el boton Limpiar
        JButton btnClear = new JButton("LIMPIAR");
        btnClear.addActionListener(new ActionListener(){
            @Override
            public void actionPerformed(ActionEvent e) {
                // TODO Auto-generated method stub
                textArea.setText("");
            }
        });
        //seteamos los limites del boton para ubicarlos en la ventana
        btnClear.setBounds(673, 537, 117, 29);
        contentPane.add(btnClear);//adicionamos el boton al panel del contenido

    }


    //generamos la vista para el requerimiento 1
    
    public void vista_requerimiento_1() {

        try {
            //Lista para la consulta del requerimiento1
            ArrayList<Proyecto> proyectos = controlador.Solucionar_requerimiento_1();
            String info = "=======/ PROYECTOS EJECUTADOS EN LA CIUDAD DE MANIZALES /======== \n\nFecha_Inicio\tNumero_Habitaciones\tClasificación\n\n";
            //Recorremos la lista para mostrar la informacion de las consultas
            for (int i = 0; i < proyectos.size(); i++) {
                //Datos para mostrar en Consola
                //String info = "Fecha_Inicio: " + proyectos.get(i).getFecha_inicio();
                //info += " - Numero_Habitaciones: " + proyectos.get(i).getNum_habitaciones();
                //info += " - Clasificación: " + proyectos.get(i).getClasificacion();
                //Imprimir los datos iterador del array List
                //System.out.println(info);
                info += proyectos.get(i).getFecha_inicio();
                info += "\t";
                info += "\t";
                info += proyectos.get(i).getNum_habitaciones();
                info += "\t";
                info += proyectos.get(i).getClasificacion();
                info += "\n";
            }
            textArea.setText(info);
            //textArea.setText(info);

        } catch (SQLException e) {
            System.err.println("Ha ocurrido un error!" + e.getMessage());
        }

    }
    //generamos la vista para el requerimiento 2
    public void vista_requerimiento_2() {
        try {
            //Lista para la consulta del requerimiento2
            ArrayList<Proyecto> proyectos = controlador.Solucionar_requerimiento_2();
            String info = "=======/ PROYECTOS EJECUTADOS EN LA CIUDAD DE MANIZALES /======== \n\nFecha_Inicio\tNumero_Habitaciones\tClasificación\t\tNombre_Lider\t\tApellido_Lider\t\tEstrato_Proyecto\n\n";
            //Recorremos la lista para mostrar la informacion de las consultas
            for (int i = 0; i < proyectos.size(); i++) {
                //Datos para mostrar en Consola
                info += proyectos.get(i).getFecha_inicio();
                info += "\t";
                info += "\t";
                info += proyectos.get(i).getNum_habitaciones();
                info += "\t";
                info += proyectos.get(i).getClasificacion();
                info += "\t";
                info += proyectos.get(i).getLider().getNombre();
                info += "\t";
                info += "\t";
                info += proyectos.get(i).getLider().getApellido();
                info += "\t";
                info += "\t";
                info += proyectos.get(i).getEstrato_proyecto();
                info += "\n";
                //Imprimir los datos iterado del array List
                //System.out.println(info);
            }
            textArea.setText(info);

        } catch (SQLException e) {
            System.err.println("Ha ocurrido un error!" + e.getMessage());
        }
        

    }
    //generamos la vista para el requerimiento 3
    public  void vista_requerimiento_3() {
        try {
            //Lista para la consulta del requerimiento3
            ArrayList<Proyecto> proyectos = controlador.Solucionar_requerimiento_3();
            String info = "=======/ CANTIDAD TOTAL DE CODOMINIOS CONTRUIDOS POR CADA CONSTRUCTORAS /======== \n\nCondominios\t\tConstructora\n\n";
            //Recorremos la lista para mostrar la informacion de las consultas
            for (int i = 0; i < proyectos.size(); i++) {
                //Datos para mostrar en Consola
                info += proyectos.get(i).getNum_condominios();
                info += "\t";
                info += "\t";
                info += proyectos.get(i).getNombre_constructora();
                info += "\n";
                
                //Imprimir los datos iterado del array List
                //System.out.println(info);
            }
            textArea.setText(info);

        } catch (SQLException e) {
            System.err.println("Ha ocurrido un error!" + e.getMessage());
        }
   
        
    }

    public void vista_requerimiento_4() {
        try {
            //Lista para la consulta del requerimiento2
            ArrayList<Lider> lideres = controlador.Solucionar_requerimiento_4();
            String info = "=======/ LIDERES DE LA CIUDAD DE MANIZALES /======== \n\nNombre_Lider\t\tApellido_Lider\n\n";
            //Recorremos la lista para mostrar la informacion de las consultas
            for (int i = 0; i < lideres.size(); i++) {
                //Datos para mostrar en Consola
                info += lideres.get(i).getNombre();
                info += "\t";
                info += "\t";
                info += lideres.get(i).getApellido();
                info += "\n";
                //Imprimir los datos iterado del array List
                //System.out.println(info);
            }
            textArea.setText(info);

        } catch (SQLException e) {
            System.err.println("Ha ocurrido un error!" + e.getMessage());
        }
        
    }

    public  void vista_requerimiento_5() {
        try {
            //Lista para la consulta del requerimiento5
            ArrayList<Proyecto> proyectos = controlador.Solucionar_requerimiento_5();
            String info = "=======/ CANTIDAD TOTAL DE PROECTOS CLASIFICADOS POR CONDOMINIOS CONTRUIDOS POR CADA CONSTRUCTORAS /======== \n\nCondominios\t\tConstructora\n\n";
            //Recorremos la lista para mostrar la informacion de las consultas
            for (int i = 0; i < proyectos.size(); i++) {
                //Datos para mostrar en Consola
                info += proyectos.get(i).getNum_condominios();
                info += "\t";
                info += "\t";
                info += proyectos.get(i).getNombre_constructora();
                info += "\n";
                //Imprimir los datos iterado del array List
                //System.out.println(info);
            }
            textArea.setText(info);

        } catch (SQLException e) {
            System.err.println("Ha ocurrido un error!" + e.getMessage());
        }
        
    }
    
    

}
