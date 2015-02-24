import code
import sys
import threading

from py4j.java_gateway import JavaGateway


gateway = JavaGateway()
hello_from_java = gateway.entry_point.helloFromJava()
spring_bean = gateway.entry_point.helloBean()

JVM_LIST = gateway.jvm.java.util.ArrayList # append/del
def jvm_list(*args):
    l = JVM_LIST()
    for arg in args:
        l.append(arg)
    return l

JVM_SET = gateway.jvm.java.util.HashSet # add/remove
def jvm_set(*args):
    l = JVM_SET()
    for arg in args:
        l.add(arg)
    return l

JVM_MAP = gateway.jvm.java.util.HashMap # put/del
def jvm_map(map):
    l = JVM_MAP()
    for k,v in map.items():
        l[k] = v
    return l


#http://stackoverflow.com/questions/4511763/how-can-i-start-the-python-console-within-a-program-for-easy-debugging
def DebugKeyboard(banner="Debugger started (CTRL-D to quit)"):

    # use exception trick to pick up the current frame
    try:
        raise None
    except:
        frame = sys.exc_info()[2].tb_frame.f_back

    # evaluate commands in current namespace
    namespace = frame.f_globals.copy()
    namespace.update(frame.f_locals)

    print("START DEBUG")
    code.interact(banner=banner, local=namespace)
    print("END DEBUG")

class HelloBeanFutureTask(threading.Thread):
    def __init__(self, args, wait_time):
        super(HelloBeanFutureTask, self).__init__()
        self.future = None
        self.args = args
        self.wait_time = wait_time
        self.sb = gateway.entry_point.helloBeanFutureTask()

    def run(self):
        self.future = self.sb.call(self.args, self.wait_time)


if __name__ == '__main__':
    print(hello_from_java)
    print(spring_bean.helloWorld())
    print(spring_bean.helloWorld("Hello from python!"))
    print(spring_bean.helloWorld(jvm_list(1,2,3)))
    print(spring_bean.helloWorld(jvm_set(1,1,2,2,3)))
    print(spring_bean.helloWorld(jvm_map({'a':1,'b':2})))
    thread1 = HelloBeanFutureTask(jvm_list(1,2,3), 1000)
    thread2 = HelloBeanFutureTask("Hello from python!", 2000)
    [i.start() for i in [thread1, thread2]]
    [i.join() for i in [thread1, thread2]]
    print(thread1.future.get())
    print(thread2.future.get())
    DebugKeyboard()



