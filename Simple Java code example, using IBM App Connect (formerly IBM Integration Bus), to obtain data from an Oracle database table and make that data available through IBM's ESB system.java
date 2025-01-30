import com.ibm.broker.javacompute.MbJavaComputeNode;
import com.ibm.broker.plugin.*;

public class FormatResponse_JavaCompute extends MbJavaComputeNode
{
    public void evaluate(MbMessageAssembly inAssembly) throws MbException
    {
        MbOutputTerminal out = getOutputTerminal("out");
        MbMessage inMessage = inAssembly.getMessage();

        try
        {
            // Clonar a mensagem de entrada
            MbMessage outMessage = new MbMessage(inMessage);
            MbElement root = outMessage.getRootElement();
            
            // Acessar o JSON retornado do banco de dados
            MbElement jsonData = root.getLastChild();
            
            // Exemplo: Adicionar um campo extra ao JSON de saída
            jsonData.createElementAsLastChild(MbElement.TYPE_NAME_VALUE,
                "processedBy", "IBM App Connect");

            // Criar uma nova mensagem de saída
            MbMessageAssembly outAssembly = new MbMessageAssembly(inAssembly, outMessage);
            out.propagate(outAssembly);
            
        }
        catch (Exception e)
        {
            throw new MbUserException(this, "evaluate()", "", "", e.toString(), null);
        }
    }
}
