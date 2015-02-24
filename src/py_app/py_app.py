from py4j.java_gateway import JavaGateway


gateway = JavaGateway()
stack = gateway.entry_point.helloFromJava()

print(stack)