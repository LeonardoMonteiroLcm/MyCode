import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class EventDrivenExample
{
    public static void main(String[] args)
    {
        // Criando a janela
        JFrame frame = new JFrame("Exemplo de Programação por Eventos");
        frame.setSize(300, 200);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(null);

        // Criando o botão
        JButton button = new JButton("Clique em mim!");
        button.setBounds(80, 70, 140, 30);

        // Adicionando um ouvinte de evento ao botão
        button.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e)
            {
                JOptionPane.showMessageDialog(frame, "Botão clicado!");
            }
        });

        // Adicionando o botão à janela
        frame.add(button);

        // Exibindo a janela
        frame.setVisible(true);
    }
}
