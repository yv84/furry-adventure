package me.yv84.java_python_gateway;

import py4j.GatewayServer;

/**
 * Hello world!
 *
 */
public class App 
{
    public String helloFromJava() {
        return "Hello from java";
    }

    public static void main( String[] args )
    {
        GatewayServer gatewayServer = new GatewayServer(new App());
        gatewayServer.start();
        System.out.println("Gateway Server Started");
        System.out.println( "Hello World!" );
    }
}
