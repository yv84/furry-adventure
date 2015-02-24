from py4j.java_gateway import JavaGateway


gateway = JavaGateway()
hello_from_java = gateway.entry_point.helloFromJava()
spring_bean = gateway.entry_point.helloBean()

print(hello_from_java)
print(spring_bean.helloWorld())