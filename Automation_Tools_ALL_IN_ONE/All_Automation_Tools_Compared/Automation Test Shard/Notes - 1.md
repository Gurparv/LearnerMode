Good — let’s build a **realistic industry-style sharding example**, not the toy “multiple XML files” approach.

We’ll design something close to what large automation frameworks actually do.

---

# ✅ Industry Pattern: **Dynamic Test Sharding**

Instead of maintaining:

❌ testng-shard1.xml  
❌ testng-shard2.xml  
❌ testng-shard3.xml

We let the framework decide **which tests belong to which shard** at runtime.

---

# ✅ High-Level Flow

```
CI / Docker → passes shardIndex + totalShards
        ↓
TestNG Listener → collects all tests
        ↓
Shard Algorithm → selects subset
        ↓
TestNG executes only those tests
```

---

# ✅ 1. Maven Command (Shard Control)

Each runner/container:

```bash
mvn test -DshardIndex=1 -DtotalShards=3
```

Other runners:

```bash
mvn test -DshardIndex=2 -DtotalShards=3
mvn test -DshardIndex=3 -DtotalShards=3
```

👉 No suite duplication needed.

---

# ✅ 2. TestNG Listener (Core of Sharding)

We intercept TestNG before execution.

---

### **ShardListener.java**

```java
import org.testng.*;
import java.util.*;

public class ShardListener implements IAlterSuiteListener {

    @Override
    public void alter(List<XmlSuite> suites) {

        int shardIndex = Integer.parseInt(System.getProperty("shardIndex", "1"));
        int totalShards = Integer.parseInt(System.getProperty("totalShards", "1"));

        for (XmlSuite suite : suites) {
            for (XmlTest test : suite.getTests()) {

                List<XmlClass> allClasses = test.getXmlClasses();
                List<XmlClass> shardClasses = new ArrayList<>();

                for (int i = 0; i < allClasses.size(); i++) {

                    // Simple deterministic split
                    if ((i % totalShards) == (shardIndex - 1)) {
                        shardClasses.add(allClasses.get(i));
                    }
                }

                test.setXmlClasses(shardClasses);

                System.out.println("Shard " + shardIndex +
                        " running classes: " + shardClasses.size());
            }
        }
    }
}
```

---

# ✅ 3. Why This is Industry-Grade

✔ No manual shard XMLs  
✔ Deterministic splitting  
✔ CI-friendly  
✔ Works with any suite  
✔ Easily extendable

---

# ✅ 4. Register Listener (testng.xml)

```xml
<suite name="UI Suite">
    <listeners>
        <listener class-name="framework.ShardListener"/>
    </listeners>

    <test name="All Tests">
        <classes>
            <class name="tests.LoginTest"/>
            <class name="tests.CartTest"/>
            <class name="tests.PaymentTest"/>
            <class name="tests.ProfileTest"/>
            <class name="tests.SearchTest"/>
        </classes>
    </test>
</suite>
```

👉 Full suite defined once.

---

# ✅ 5. What Happens at Runtime

If:

```
Total Classes = 5
Total Shards = 3
```

---

**Shard 1 → (i % 3 == 0)**  
Runs → LoginTest, ProfileTest

**Shard 2 → (i % 3 == 1)**  
Runs → CartTest, SearchTest

**Shard 3 → (i % 3 == 2)**  
Runs → PaymentTest

✔ Clean split  
✔ No overlap  
✔ No duplication

---

# ✅ 6. Docker Scaling (Real Industry Execution)

Each shard = container.

---

### **docker-compose.yml**

```yaml
services:

  shard1:
    image: test-runner
    command: mvn test -DshardIndex=1 -DtotalShards=3

  shard2:
    image: test-runner
    command: mvn test -DshardIndex=2 -DtotalShards=3

  shard3:
    image: test-runner
    command: mvn test -DshardIndex=3 -DtotalShards=3
```

👉 Massive horizontal scaling.

---

# ✅ 7. Selenium Grid Integration

Each shard still runs tests in parallel:

```xml
<suite parallel="methods" thread-count="4">
```

✔ Horizontal → Shards  
✔ Vertical → Threads

Ultimate scaling combo.

---

# ✅ 8. Industry Enhancement → Smart Balancing

Real companies improve the split logic:

Instead of:

```java
(i % totalShards)
```

They use:

✔ Historical runtime data  
✔ Slow test detection  
✔ Flaky test isolation  
✔ Tag-based grouping

Example:

```java
methods.sort(byExecutionTimeDesc());
```

Balance heavy tests across shards.

---

# ✅ 9. Advanced Industry Variant → Method-Level Sharding

Instead of splitting classes:

Split individual test methods:

```java
List<ITestNGMethod> methods = context.getAllTestMethods();
```

👉 Much finer balancing.

Used in:

✔ Very large suites  
✔ Microservice testing  
✔ Mobile/device farms

---

# ✅ Final Senior-Level Insight

Industry sharding is about:

✔ **Deterministic selection**  
✔ **Zero manual maintenance**  
✔ **CI scalability**  
✔ **Balanced execution**  
✔ **Infrastructure efficiency**

NOT about writing many XML files.

---

If you want next-level mastery, we can build:

✅ Runtime-balanced sharding engine  
✅ Execution-time aware splitting  
✅ Flaky-test quarantine shard  
✅ Cost vs speed optimization math  
✅ Netflix/Uber CI scaling model

Tell me your target:

👉 “Practical framework implementation”  
👉 “CI/Docker/Grid scaling math”  
👉 “Advanced smart sharding logic”