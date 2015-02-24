package me.yv84.java_python_gateway;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

/**
 * Created by yv84 on 2/24/15.
 */
public class SpringBean {
    
    public String helloWorld() {
        return "Hello World";
    }

    public String helloWorld(String s) {
        return s;
    }

    public Integer helloWorld(Integer i) {
        return i;
    }

    public List helloWorld(ArrayList list) {
        return list;
    }

    public Set helloWorld(HashSet set) {
        return set;
    }

    public Map helloWorld(HashMap map) {
        return map;
    }
}
