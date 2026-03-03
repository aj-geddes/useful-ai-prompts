# JMH for Java Benchmarking

## JMH for Java Benchmarking

```java
// PerformanceBenchmark.java
import org.openjdk.jmh.annotations.*;
import java.util.*;
import java.util.concurrent.TimeUnit;

@BenchmarkMode(Mode.AverageTime)
@OutputTimeUnit(TimeUnit.MICROSECONDS)
@State(Scope.Benchmark)
@Fork(value = 1, warmups = 1)
@Warmup(iterations = 3, time = 1)
@Measurement(iterations = 5, time = 1)
public class CollectionPerformanceBenchmark {

    @Param({"100", "1000", "10000"})
    private int size;

    private List<Integer> arrayList;
    private List<Integer> linkedList;
    private Set<Integer> hashSet;

    @Setup
    public void setup() {
        arrayList = new ArrayList<>();
        linkedList = new LinkedList<>();
        hashSet = new HashSet<>();

        for (int i = 0; i < size; i++) {
            arrayList.add(i);
            linkedList.add(i);
            hashSet.add(i);
        }
    }

    @Benchmark
    public void arrayListIteration() {
        int sum = 0;
        for (Integer num : arrayList) {
            sum += num;
        }
    }

    @Benchmark
    public void linkedListIteration() {
        int sum = 0;
        for (Integer num : linkedList) {
            sum += num;
        }
    }

    @Benchmark
    public void arrayListRandomAccess() {
        for (int i = 0; i < size; i++) {
            arrayList.get(i);
        }
    }

    @Benchmark
    public void linkedListRandomAccess() {
        for (int i = 0; i < size; i++) {
            linkedList.get(i);
        }
    }

    @Benchmark
    public boolean hashSetContains() {
        return hashSet.contains(size / 2);
    }

    public static void main(String[] args) throws Exception {
        org.openjdk.jmh.Main.main(args);
    }
}

// Run: mvn clean install
//      java -jar target/benchmarks.jar
```
