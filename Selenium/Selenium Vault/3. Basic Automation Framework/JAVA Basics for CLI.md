1. [[#Running Java Code from CLI]]
2. [[#Java 11+ shortcut (Directly compiles and Runs in one go)]]
3. [[#Java CLI Cheat Sheet]]
4. [[#Minimal Java CLI Project (Packages + Classpath + JAR)]]



## Running Java Code from CLI

```Java
//HelloWorld.java
public class Test{
        public static void main(String args[]){
                System.out.println("Hello");
        }
}
```

#### Compile it
Below command compiles the code and creates a `HelloWorld.class` bytecode file (platform-independent bytecode)
```Bash
javac HelloWorld.java 
```

#### Run it
Using below command you can run that `HelloWorld.class`
Note - `.class` file works on Windows, Linux , MacOS if JVM exists
```Bash
java HelloWorld
```

---

## Java 11+ shortcut (Directly compiles and Runs in one go)

```Bash
java HelloWorld.java
```

- Java **compiles in memory and runs immediately**
- **No reusable `.class` file produced**


---

## Java CLI Cheat Sheet
| Scenario                                    | Folder Structure                        | Compile (CLI)                                               | Run (CLI)                        | Notes                                                                       |
| ------------------------------------------- | --------------------------------------- | ----------------------------------------------------------- | -------------------------------- | --------------------------------------------------------------------------- |
| **Single Java file**                        | `HelloWorld.java`                       | `javac HelloWorld.java`                                     | `java HelloWorld`                | Creates `HelloWorld.class`.                                                 |
| **Single file (Java 11+ shortcut)**         | `HelloWorld.java`                       | _(no compile step)_                                         | `java HelloWorld.java`           | Java compiles in memory and runs.                                           |
| **Two files in same directory (dependent)** | `Main.java``Helper.java`                | `javac Main.java Helper.java` or `javac *.java`             | `java Main`                      | Current directory automatically in classpath.                               |
| **Two files: one in `./libs`**              | `Main.java``libs/Helper.java`           | `javac Main.java libs/Helper.java`                          | `java -cp .:libs Main`           | `.` = current dir. Use `;` instead of `:` on Windows.                       |
| **Create JAR from classes**                 | `.class files`                          | `javac *.java`                                              | `jar cf app.jar *.class`         | Bundles classes/resources for distribution.                                 |
| **Run executable JAR**                      | `app.jar`                               | _(already compiled)_                                        | `java -jar app.jar`              | Requires `Main-Class` in manifest.                                          |
| **Create package in Java file**             | `com/example/Helper.java`               | `javac -d . Helper.java`                                    | —                                | File contains `package com.example;`. `-d .` creates folders automatically. |
| **Use packaged class in another file**      | `Main.java` + `com/example/Helper.java` | `javac -d . com/example/Helper.java``javac -cp . Main.java` | `java -cp . Main`                | Import the package in `Main.java`.                                          |
| **Import from package**                     | In `Main.java`                          | —                                                           | —                                | `import com.example.Helper;`                                                |
| **Import from JAR**                         | `libs/utils.jar`                        | `javac -cp libs/utils.jar Main.java`                        | `java -cp .:libs/utils.jar Main` | Import works exactly the same as normal packages.                           |
### Key ideas

- **`.java`** → source code
- **`.class`** → compiled bytecode
- **`.jar`** → packaged collection of classes/resources
- **Classpath (`-cp`)** tells Java **where to find classes or jars**.

✅ **Important:**  
`import` works for **both `.class` files and `.jar` libraries** because a **JAR is just a packaged set of classes organized by packages**.

---

## Minimal Java CLI Project (Packages + Classpath + JAR)

### 1️⃣ Project structure

```
project/
 ├─ Main.java
 ├─ com/
 │   └─ utils/
 │       └─ Helper.java
 └─ libs/
```

---

### 2️⃣ Helper class (inside a package)

`com/utils/Helper.java`

```java
package com.utils;

public class Helper {
    public static void sayHello() {
        System.out.println("Hello from Helper");
    }
}
```

---

### 3️⃣ Main class using the package

`Main.java`

```java
import com.utils.Helper;

public class Main {
    public static void main(String[] args) {
        Helper.sayHello();
    }
}
```

---

# 4️⃣ Compile from CLI

Run from **project/**

```bash
javac -d . com/utils/Helper.java
javac -cp . Main.java
```

Explanation

- `-d .` → creates correct package folder structure
    
- `-cp .` → tells compiler where classes exist
    

---

# 5️⃣ Run the program

```bash
java -cp . Main
```

Output

```
Hello from Helper
```

---

# 6️⃣ Create a JAR for the Helper library

Move compiled class to jar:

```bash
jar cf libs/utils.jar com/utils/Helper.class
```

Now project looks like:

```
project/
 ├─ Main.java
 ├─ libs/
 │   └─ utils.jar
```

---

# 7️⃣ Compile using the JAR

```bash
javac -cp libs/utils.jar Main.java
```

---

# 8️⃣ Run using the JAR

```bash
java -cp .:libs/utils.jar Main
```

_(Windows: `.;libs/utils.jar`)_

---

# 🧠 Key idea demonstrated

|Concept|Example|
|---|---|
|Package|`package com.utils;`|
|Import|`import com.utils.Helper;`|
|Compile with classpath|`javac -cp libs/utils.jar Main.java`|
|Run with classpath|`java -cp .:libs/utils.jar Main`|
|JAR purpose|distribute compiled classes as a library|

---

⚡ **Mental model**

```
.java  → compile →  .class  → bundle →  .jar
```

Java loads classes from **directories OR jars listed in the classpath**.

---

If you'd like, I can also show **the 3 most common CLI mistakes with Java packages/classpath** (these confuse almost everyone at first).