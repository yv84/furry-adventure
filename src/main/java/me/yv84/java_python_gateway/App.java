package me.yv84.java_python_gateway;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;
import py4j.GatewayServer;

/**
 * Hello world!
 *
 */
public class App 
{
    private static GatewayServer gatewayServer;
    private static ApplicationContext context;

    public App() {
        context = new ClassPathXmlApplicationContext("spring.xml");
    }

    public String helloFromJava() {
        return "Hello from java";
    }

    public SpringBean helloBean() {
        return (SpringBean) context.getBean("helloBean");
    }

    public static void main( String[] args )
    {
        gatewayServer = new GatewayServer(new App());
        gatewayServer.start();
        System.out.println("Gateway Server Started");
    }
}
