/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package tapraksbd;
import java.sql.Connection;
import java.sql.Driver;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
import java.sql.SQLException;
import java.util.logging.Level;
import java.util.logging.Logger;
/**
 *
 * @CINDI DILA APRILIANA_L200200106
 */
public class TAPRAKSBD {
    static final String JDBC_Driver = "com.mysql.jdbc.Driver";
    static final String DB_URL = "jdbc:mysql://localhost/dbperbankan";
    static final String USER = "root";
    static final String PASS = "";
    
    static Connection conn;
    static Statement statement;
    static ResultSet rs;

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) throws SQLException{
        try{
            System.out.println("melakukan koneksi ke" +JDBC_Driver);
            System.out.println("Loading driver");
            Class.forName(JDBC_Driver);
            conn = DriverManager.getConnection(DB_URL, USER, PASS);
            System.out.println("use" + conn.getCatalog());
            System.out.println("databae change");
            
            //INSERT
            //statement = conn.createStatement();
            //String insert = "INSERT INTO nasabah(id_nasabah, nama_nasabah, alamat_nasabah)"
            //        + " VALUE('%s','%s','%s')";
            //insert = String.format(insert,101,"Cindi Dila Apriliana","jl.Sriwijaya");
            
            //UPDATE
            String update = "UPDATE nasabah set alamat_nasabah= 'Jl.Mawar' where id_nasabah = 101";
            
           // DELETE
            //String delete = "delete from nasabah where id_nasabah = 101";
            
            
            statement = conn.createStatement();
            //statement.execute(insert);
            statement.execute(update);
            //statement.execute(delete);
            String sql = "Select * from nasabah";
            rs = statement.executeQuery(sql);
           
            String header = String.format("%2s | %-20s | %-40s", "ID", "Nama", "Alamat");
            System.out.println(header);
            
            while(rs.next()){
                String output = String.format("%2s | %-20s | %-40s",rs.getInt("id_nasabah"),
                        rs.getString("nama_nasabah"), rs.getString("alamat_nasabah"));
                System.out.println(output);
            }
            statement.close();
            conn.close();   
        
    }catch (Exception e){
        e.printStackTrace();
      }
    }
    
}



            