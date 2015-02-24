package me.yv84.java_python_gateway;

import java.util.*;
import java.util.concurrent.Callable;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;

/**
 * Created by yv84 on 2/24/15.
 */
public class SpringBeanFutureTask<T> {

    public String helloWorld() {
        return "Hello World";
    }

    public T helloWorld(T s) {
        return s;
    }

    public Future call(final T args, final Integer waitTime) throws Exception {
        ExecutorService executor = Executors.newSingleThreadExecutor();
        Callable<T> callable = new Callable<T>() {
            @Override
            public T call() throws InterruptedException {
                Thread.sleep(waitTime);
                return args;
            }
        };
        Future<T> future = executor.submit(callable);
        // future.get() returns args
        executor.shutdown();
        return future;
    }

}
