1. [[#Downloading Jars using Maven CLI]]
2. [[#Running Testng.xml from Maven CLI]]
3. [[#Creating archetype from Maven CLI]]
4. [[#Creating a minimalist pom.xml]]
5. [[#SureFire Plugin]]
6. [[#Maven commands to run]]
## Downloading Jars using Maven CLI

```Prompt
from cli when i get testng jars and try to use it .. it gives error that sl4j , jcommander is needed so i had to get them too seperately. its manual task cant i just download testng and its dependency in some easy way from CLI only? be concise
```

Yes. **You can use Maven purely as a downloader from CLI** — no `pom.xml`, no archetype.

Yes. Use a **dependency manager** instead of downloading jars manually.

#### Option 1 (Most common): **Maven**

Install Maven, then run:
```bash
mvn dependency:get -Dartifact=org.testng:testng:7.10.2
```

Maven will automatically download:
- **TestNG**
- **jcommander**
- **slf4j**
- any other dependencies

They go to:

```
~/.m2/repository/
```

You can then reference them in classpath.

---

#### Option 2: **Download with dependencies automatically**

```bash
mvn dependency:copy-dependencies
```

(with a `pom.xml`) and Maven downloads all required jars.

✅ **Summary**

Without tools:
```
download jars manually → painful
```
With Maven/Gradle:
```
declare dependency → tool downloads all transitive dependencies automatically
```

TestNG **does not ship a fully fat jar**, so **jcommander + slf4j are always required** unless you use Maven/Gradle.

---

```Prompt
but i want to learn testng in isolation i dont want to meddle with mvn . just the jar part i want. i dont want pom.xml or any other thing like archetype etc. be concise
```

```Prompt
you didnt answer my question. cant i use maven download capability without archetype and pom.xml from cli?
```


Yes. **You can use Maven purely as a downloader from CLI** — no `pom.xml`, no archetype.

Use:
```bash
mvn dependency:get -Dartifact=org.testng:testng:7.10.2
```

This will download **TestNG and all its transitive dependencies** (jcommander, slf4j, etc.) into:
```
~/.m2/repository/
```

Then build your classpath from there.
Example run:
```bash
java -cp ".:~/.m2/repository/org/testng/testng/7.10.2/*:~/.m2/repository/com/beust/jcommander/1.82/*" org.testng.TestNG testng.xml
```

---

✅ **Summary**

|Goal|Command|
|---|---|
|Download jar + dependencies|`mvn dependency:get -Dartifact=group:artifact:version`|
|No pom.xml needed|✔|
|No archetype needed|✔|
|Works purely from CLI|✔|

So Maven can be used **just as a dependency downloader**, nothing else.

---

```Prompt
what if i want the download to be in my custom location like ./lib and not ./m2/repo
```

Yes. Use Maven’s **copy goal** to download directly into your folder.
### Download to `./lib`

```bash
mvn dependency:copy \
-Dartifact=org.testng:testng:7.10.2 \
-DoutputDirectory=lib
```
### Download **with dependencies**

```bash
mvn dependency:copy-dependencies \
-DoutputDirectory=lib \
-DincludeArtifactIds=testng
```

Then your project becomes:

```
project/
 ├─ Main.java
 └─ lib/
     ├─ testng.jar
     ├─ jcommander.jar
     └─ slf4j-api.jar
```

Run:
```bash
java -cp ".:lib/*" org.testng.TestNG testng.xml
```

✅ **Key point:**  
Maven will still **cache in `~/.m2/repository` internally**, but it **copies the jars to `./lib` for your use**.

---
---

## Running Testng.xml from Maven CLI

```Bash
mvn test -DsuiteXmlFile=testng.xml

# Multiple xml files
mvn test -Dsurefire.suiteXmlFiles=testng1.xml,testng2.xml,testng3.xml
```

---
---

## Creating archetype from Maven CLI

```Bash
mvn archetype:generate \
-DgroupId=com.example \
-DartifactId=my-project \
-DarchetypeArtifactId=maven-archetype-quickstart \
-DinteractiveMode=false
```

```Bash
mvn -B archetype:generate -DgroupId=com.test -DartifactId=selenium-project -DarchetypeArtifactId=maven-archetype-quickstart
```

---

## Creating a minimalist pom.xml

You have to create it manully
```xml title="pom.xml"
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
         https://maven.apache.org/xsd/maven-4.0.0.xsd">

  <modelVersion>4.0.0</modelVersion>

  <groupId>com.example</groupId>
  <artifactId>demo</artifactId>
  <version>1.0</version>

</project>
```

Minimal required fields in a Maven POM

|Tag|Purpose|
|---|---|
|`modelVersion`|POM model version|
|`groupId`|project namespace|
|`artifactId`|project name|
|`version`|project version|

---

## SureFire Plugin

From Intellij , you can run `testng tests` simply using 
- GUI Run button OR
- `mvn test` -> because Maven automatically uses the **default Surefire plugin** during the `test` phase.

**Summary**
- Surefire **not required explicitly**
- Maven uses **default Surefire automatically**
- TestNG dependency **must exist**.

But if you have mutiple testng.xml files and you have complex test orchestration like groupings, priority , parallel etc. then you need to have SureFire plugin . For automation projects it is recommended.

```xml title="pom.xml"
<project xmlns="http://maven.apache.org/POM/4.0.0">
  <modelVersion>4.0.0</modelVersion>

  <groupId>com.example</groupId>
  <artifactId>demo</artifactId>
  <version>1.0</version>

  <dependencies>
    <dependency>
      <groupId>org.testng</groupId>
      <artifactId>testng</artifactId>
      <version>7.9.0</version>
      <scope>test</scope>
    </dependency>
  </dependencies>

  <build>
    <plugins>
      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-surefire-plugin</artifactId>
        <version>3.2.5</version>
        <configuration>
          <suiteXmlFiles>
            <suiteXmlFile>testng.xml</suiteXmlFile>
          </suiteXmlFiles>
        </configuration>
      </plugin>
    </plugins>
  </build>

</project>
```

```java title="TestExample.java"
import org.testng.annotations.Test;

public class TestExample {

    @Test
    public void test1() {
        System.out.println("TestNG running with Maven");
    }
}
```

```xml title="testng.xml"
<suite name="Suite">
  <test name="Test">
    <classes>
      <class name="TestExample"/>
    </classes>
  </test>
</suite>
```

```Bash
mvn test
```

Execution flow
```
mvn test
   ↓
Surefire Plugin
   ↓
TestNG
   ↓
Runs testng.xml
```

### Another way is from CLI

```Bash
mvn test -Dsurefire.suiteXmlFiles=testng.xml
```

It **omits the Surefire plugin configuration block** from `pom.xml`.
### Normally you would have

```xml
<build>
  <plugins>
    <plugin>
      <artifactId>maven-surefire-plugin</artifactId>
      <configuration>
        <suiteXmlFiles>
          <suiteXmlFile>testng.xml</suiteXmlFile>
        </suiteXmlFiles>
      </configuration>
    </plugin>
  </plugins>
</build>
```

### When using CLI instead

```bash
mvn test -Dsurefire.suiteXmlFiles=testng.xml
```

You **don’t need that entire block**.

Your `pom.xml` can be just:

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0">
  <modelVersion>4.0.0</modelVersion>

  <groupId>demo</groupId>
  <artifactId>demo</artifactId>
  <version>1.0</version>

  <dependencies>
    <dependency>
      <groupId>org.testng</groupId>
      <artifactId>testng</artifactId>
      <version>7.9.0</version>
      <scope>test</scope>
    </dependency>
  </dependencies>
</project>
```

### Why it works

**Apache Maven** automatically runs the **Maven Surefire Plugin** during the `test` phase.  
The CLI flag simply **passes the TestNG suite file to Surefire at runtime**.

✅ So what’s omitted:
- `<build>`
- `<plugins>`
- `<plugin>`
- `<configuration>` for **TestNG**.

#### Also
If you run:
```bash
mvn test -Dsurefire.suiteXmlFiles=testng.xml
```

and you **already have the Maven Surefire Plugin in `pom.xml` but without `<suiteXmlFiles>` configured**, then:

✅ **It will still run `testng.xml`.**
### Why

The CLI property:
```
-Dsurefire.suiteXmlFiles=testng.xml
```

**overrides / supplies the configuration at runtime** to **Apache Maven**.
### So Maven does:

```text
mvn test
   ↓
Surefire plugin (from pom.xml)
   ↓
Reads CLI property
   ↓
Runs TestNG using testng.xml
```

### Rule

|Situation|Result|
|---|---|
|Surefire in pom but no suiteXmlFiles|CLI property works|
|Surefire not in pom|Default Surefire runs|
|suiteXmlFiles in pom|pom config used unless overridden|

✅ **CLI `-D` properties override missing or default configuration.**

---

## Maven commands to run

As an **SDET**, you mainly use a small set of **Apache Maven** commands.
### Core commands (must know)

|Command|Purpose|
|---|---|
|`mvn clean`|Removes previous build (`target/`)|
|`mvn compile`|Compiles project code|
|`mvn test`|Runs tests (via **Maven Surefire Plugin**)|
|`mvn clean test`|Clean build + run tests|
|`mvn package`|Builds `.jar` / `.war`|
|`mvn clean install`|Build + install artifact to local repo|

### Test execution (very common in automation)

With **TestNG**:
```bash
mvn test -Dsurefire.suiteXmlFiles=testng.xml
```

Run specific test:
```bash
mvn test -Dtest=LoginTest
```

### Debug / dependency commands

|Command|Purpose|
|---|---|
|`mvn dependency:tree`|See dependency hierarchy|
|`mvn dependency:resolve`|Download dependencies|
|`mvn help:effective-pom`|See final merged POM|

---

✅ **Realistically used daily by SDETs**

```text
mvn clean test
mvn test
mvn clean install
mvn test -Dsurefire.suiteXmlFiles=testng.xml
mvn dependency:tree
```

---

💡 If you're doing **Selenium + TestNG automation**, there are **about 8 Maven commands that cover ~95% of real work**. I can show that minimal list if you want.

