import java.awt.Container;
import java.awt.FlowLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.JPasswordField;
import javax.swing.JTextField;
import javax.swing.JButton;
public class Mi
{
	/*long long verybig = 12344567890842;
	System.out.println(verybig);*/
 private static String username;
 private static String password ;
 private static JTextField []t={
   new JTextField("账号",8),new JTextField(10),
   new JTextField("密码",8),new JPasswordField(10),};
public static void main (String args[]){
  JFrame app=new JFrame("账号密码演示程序");
   app.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
   app.setSize(280,160);
   Container c=app.getContentPane();
   c.setLayout(new FlowLayout());      
t[0].setEditable(false);
   t[2].setEditable(false);
   for(int i=0;i<4;i++)
    c.add(t[i]);t[1].setText("What");
   
   JButton[]b={new JButton("OK"),new JButton("Reset")};
   c.add(b[0]);c.add(b[1]);
   app.setLocationRelativeTo(null);
   app.setVisible(true);
   
   b[1].addActionListener(new ActionListener() {
       public void actionPerformed(ActionEvent e) {
       t[1].setText("");
       t[3].setText("");
	   t[5].setText("");
       }
      });
		//听器
     b[0].addActionListener(new ActionListener() {
      public void actionPerformed(ActionEvent e) {
       username = t[1].getText();
       password = t[3].getText();
       //判断用户名码是否正确
       if (username.equals("123") && password.equals("123")) {
        JOptionPane.showMessageDialog(null, "登陆成功!", "消息",
          JOptionPane.INFORMATION_MESSAGE);
        
       } else {
        JOptionPane.showMessageDialog(null, "用户名或密码错误!", "错误",
          JOptionPane.ERROR_MESSAGE);
       }
      }
     });}
}