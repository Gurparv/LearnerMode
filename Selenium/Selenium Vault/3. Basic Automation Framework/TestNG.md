1. [[#Download TestNg and its dependency using Maven CLI]]
2. [[#HelloWorld TestNG program from CLI (without testng.xml)]]
3. [[#Logging to console]]
4. [[#Get the status of test at runtime]]
5. [[#Retry Mechanism]]
6. [[#Listeners in TestNG]]
7. [[#Running a TestNG program using testng.xml file]]
8. [[#Prioritizing or Sequencing Tests]]
9. [[#Grouping Tests]]
10. [[#Ignoring Tests]]
11. [[#Run only Failed Tests]]
12. [[#Basic `testng.xml` file]]
13. [[#Parallel Testing using Testng]]
14. [[#Sending Parameters from testng.xml]]


## Download TestNg and its dependency using Maven CLI
Go check -> [[Maven for CLI]]

---

## HelloWorld TestNG program from CLI (without testng.xml)

```
project/
 ├─ HelloTestNG.java
 └─ lib/
     ├─ testng.jar
     ├─ jcommander.jar
     └─ slf4j-api.jar
```


```Java title="HelloTestNG.java"
import org.testng.annotations.Test;

public class HelloTestNG{
	@Test
	public void demoTest(){
		System.out.println("Testng is running me.");
	}
}

```

```Bash
#Compile using 
javac -classpath ".\libs\*;" HelloTestNG.java

# Run using 
java -classpath ".\libs\*;"  org.testng.TestNG -testclass HelloTestNG
```

```Bash title="Output"
SLF4J(W): No SLF4J providers were found.
SLF4J(W): Defaulting to no-operation (NOP) logger implementation
SLF4J(W): See https://www.slf4j.org/codes.html#noProviders for further details.
Testng is running me.

===============================================
Command line suite
Total tests run: 1, Passes: 1, Failures: 0, Skips: 0
===============================================

```

---

## Logging to console.

Documentation->https://logging.apache.org/log4j/3.x/


```Java title="Main.java"

import org.testng.annotations.Test;
import org.apache.log4j.Logger;

public class Main{
        private static final Logger LOGGER = Logger.getLogger(Main.class);
        @Test
        public void test1(){
        LOGGER.debug("debug in test1");
        System.out.println("Hello from Test1");
        Reporter.log("Test1 is completed");
        }
    }
```

Specifying Formatting of log files.

```properties title="log4j.properties"
log4j.rootLogger=DEBUG, console, file

# Console Appender
log4j.appender.console=org.apache.log4j.ConsoleAppender
log4j.appender.console.layout=org.apache.log4j.PatternLayout
log4j.appender.console.layout.ConversionPattern=%d [%t] %-5p %c - %m%n

# File Appender
log4j.appender.file=org.apache.log4j.FileAppender
log4j.appender.file.File=automation.log
log4j.appender.file.layout=org.apache.log4j.PatternLayout
log4j.appender.file.layout.ConversionPattern=%d %-5p %c - %m%n

```

```Bash
#Compile java files 
javac -classpath ".\libs\*;" Main.java

# Run using 
java -classpath ".\libs\*;"  org.testng.TestNG -testclass Main
```

---

## Get the status of test at runtime

```Java title="Main.java"
mport org.testng.annotations.Test;
import org.testng.annotations.AfterMethod;
import org.testng.Assert;
import org.testng.ITestResult;

public class Main2{
        @Test
        public void TestToFail(){
                Assert.assertTrue(false,"failing Deliberating using Testng assert");
        }
        @AfterMethod
        public void after(ITestResult res){
        System.out.println(res.getStatus());
        }

}
```

Example 2 //Tries to get some info from `ITestResult` and `ITestContext`
```Java title="Main2.java"
import org.testng.annotations.AfterMethod;

public class Main4{

        @BeforeMethod
        public void before(ITestContext con, ITestResult res){
                System.out.println(con.getName());
                System.out.println(con.getHost());
                System.out.println(res.getTestClass().getName());
                System.out.println(res.getMethod().getMethodName());

                System.out.println("GetName ="+res.getName());
                System.out.println("GetInstanceName ="+res.getInstanceName());
                System.out.println("//////////");
        }
        @AfterMethod
        public void after(ITestResult res){
                System.out.println("GetName ="+res.getName());
                System.out.println("GetInstanceName ="+res.getInstanceName());
                System.out.println("GetTestName ="+res.getTestName());
                System.out.println("Host"+res.getHost());
                System.out.println("Testclass = "+res.getTestClass());
                System.out.println("Testcontext = "+res.getTestContext());
                System.out.println("-------------");
        }

        @Test
        public void myFirstTest(){
                System.out.println("test starting with alphabet - m");
        }
}
```

---

## Retry Mechanism

```Java title="Main.java"
import org.testng.annotations.Test;
import org.testng.Assert;

public class Main3{
        @Test(retryAnalyzer = MyRetryClass.class)
        public void myRetry(){
        System.out.println("Failing");
        Assert.assertTrue(false);

        }
}
```

```java title="MyRetryClass.java"
import org.testng.IRetryAnalyzer;
import org.testng.ITestResult;


public class MyRetryClass implements IRetryAnalyzer{

        private int MAX_RETRIES = 5;
        private int count = 1;

        @Override
        public boolean retry(ITestResult res){
                while (count< MAX_RETRIES){
                count ++;
                return true;
                }
                return false;
        }
}
```

---

## Listeners in TestNG

```java title="MyListeners.java"
import org.testng.ITestListener;
import org.testng.ITestContext;
import org.testng.ITestResult;

public class MyListeners implements ITestListener{
        @Override
        public void onFinish(ITestContext context){
                //code goes here.
                }

        @Override
        public void onStart(ITestContext context){
                }

        @Override
        public void onTestFailedButWithinSuccessPercentage(ITestResult result){}

        @Override
        public void onTestFailedWithTimeout(ITestResult result){}

        @Override
        public void onTestFailure(ITestResult result){}

        @Override
        public void onTestSkipped(ITestResult result){}

        @Override
        public void onTestStart(ITestResult result){}

        @Override
        public void onTestSuccess(ITestResult result){
                System.out.println("TestPassed from Listener");
        }

}
```

Attaching `listeners` to `code files` 
```xml title=testng.xml
<suite name="mysuite">
        <listeners>
                <listener class-name="MyListeners"/>
        </listeners>
    <test name="mytest">
        <classes>
            <class name="Main"/>
        </classes>
    </test>
</suite>

```

---

## Running a TestNG program using testng.xml file


```
project/
 ├─ HelloTestNG.java
 ├─ testng1.xml
 └─ lib/
     ├─ testng.jar
     ├─ jcommander.jar
     └─ slf4j-api.jar
```


```Java title="HelloTestNG.java"
import org.testng.annotations.Test;

public class HelloTestNG{
	@Test
	public void demoTest(){
		System.out.println("Testng is running me.");
	}
}

```

```Bash
#Compile the java files using 
javac -classpath ".\libs\*;" HelloTestNG.java

# Run the TestNG XML 
java -cp ".\libs\*;" org.testng.TestNG testng1.xml
```

```Bash title="Output"

SLF4J(W): No SLF4J providers were found.
SLF4J(W): Defaulting to no-operation (NOP) logger implementation
SLF4J(W): See https://www.slf4j.org/codes.html#noProviders for further details.
Testng is running me.

===============================================
Command line suite
Total tests run: 1, Passes: 1, Failures: 0, Skips: 0
===============================================


```

---

## Prioritizing or Sequencing Tests

```Java title="MainPriority"
import org.testng.annotations.Test;

@Test(groups = {"Ignore"})
public class MainPriority{

        @Test(dependsOnMethods = {"test2"})
        public void test1(){
        System.out.println("Test1");
        }

        @Test(dependsOnMethods = {"test3"})
        public void test2(){
        System.out.println("Test2");
        }

        @Test(dependsOnMethods={"test4"})
        public void test3(){
        System.out.println("Test3");
        }

        @Test(priority=3)
        public void test4(){
        System.out.println("Test4");
        }

        @Test(priority=2)
        public void test5(){
        System.out.println("Test5");
        }

        @Test(priority=1 , groups= {"RunMe6"})
        public void test6(){
        System.out.println("Test6");
        }
}

```

---

## Grouping Tests

```Java title=DemoGroup.java
import org.testng.annotations.Test;

@Test(groups = {"Ignore"})
public class MainPriority{

        @Test(groups={'Smoke'})
        public void test1(){
        System.out.println("Test1");
        }
        
        @Test 
        public void test2(){
        System.out.println("test2")
        }

        @Test(priority=1 , groups= {"RunMe6"})
        public void test6(){
        System.out.println("Test6");
        }
}
```

```xml title=
<!DOCTYPE suite SYSTEM "https://testng.org/testng-1.0.dtd">

<suite name="Suite">
    <test name="SmokeTests">
        <groups>
            <run>
                <include name="Smoke"/>
                <exclude name="RunMe6"/>
            </run>
        </groups>
        <classes>
            <class name="MainPriority"/>
        </classes>
    </test>
</suite>
```

💡 **Automation Framework Tip:**  
Most teams use these common groups:

- `smoke`
- `regression`
- `sanity`
- `api`
- `ui`

==If you want, I can also show **advanced TestNG group features used in real automation frameworks**, like:
- **group dependencies**
- **regex groups**
- **running groups in parallel**
- **grouping at method vs class level**.

---

## Ignoring Tests

```java title="Main_IgnoringTests"

import org.testng.annotations.Test;
import org.testng.annotations.Ignore;

public class Main_IgnoringTests{
        @Test
        public void test_1(){
        System.out.println("Test1");
        }

        @Ignore //wasnt mentioned in reports.
        public void test_2(){
        System.out.println("Test2");
        }

        @Test(enabled=false) //this was mentioned in reports
        public void test_3(){
        System.out.println("Test3");
        }
}

```

---

## Run only Failed Tests

Testng when runs if tests fails then it creates `failed` tests xml . You can just rerun that to run only failed tests.

---

## Basic `testng.xml` file

```xml title=testng.xml

<suite name="mysuite">
    <test name="mytest">
        <classes>
            <class name="Main"/>
        </classes>
    </test>
</suite>

```

### Explanation

- `<suite>` → Defines the test suite.
- `<test>` → Defines a test inside the suite.
- `<classes>` → Container for test classes.
- `<class>` → Fully qualified name of the TestNG test class.

---
---

## Parallel Testing using Testng

```Fol
```
```Bash title="Framework Skeleton"

SELENIUMPRACTICE
├───.idea
├───resources
├───src
│   ├───main
│   │   └───java
│   │       ├───base
│   │       ├───constants
│   │       └───utils
│   └───test
│       └───java
└───target
    ├───classes
    │   ├───base
    │   ├───constants
    │   └───utils
    ├───generated-sources
    │   └───annotations
    ├───generated-test-sources
    │   └───test-annotations
    ├───maven-status
    │   └───maven-compiler-plugin
    │       ├───compile
    │       │   └───default-compile
    │       └───testCompile
    │           └───default-testCompile
    ├───surefire-reports
    │   ├───DemoTesting
    │   └───junitreports
    └───test-classes

```
```java title="TestDemo.java"
import base.Base;  
import constants.AppConstants;  
import org.openqa.selenium.By;  
import org.testng.Assert;  
import org.testng.annotations.Test;  
import utils.DriverFactory;  
  
  
public class TestDemo extends Base {  
  
    @Test  
    public void verifyHomePageUrl(){  
        DriverFactory.getDriver().get("https://automationexercise.com/");  
        String actual_url = DriverFactory.getDriver().getCurrentUrl();  
        Assert.assertEquals(actual_url, AppConstants.HOMEPAGE_URL.getValue());  
    }  
  
    @Test  
    public void verifyTitle(){  
        DriverFactory.getDriver().get("https://automationexercise.com/");  
        String actual_title = DriverFactory.getDriver().getTitle();  
        Assert.assertEquals(actual_title, AppConstants.HOMEPAGE_TITLE.getValue());  
    }  
  
    @Test  
    public void verifyTestCasesHeader(){  
        DriverFactory.getDriver().get("https://automationexercise.com/");  
        DriverFactory.getDriver().findElement(By.xpath("//a[@href='/test_cases']")).click();  
        Assert.assertTrue(DriverFactory.getDriver().getCurrentUrl().contains("test_cases"));  
    }  
}

```

```java title="Base.java"
package base;  
  
import org.testng.annotations.AfterMethod;  
import org.testng.annotations.BeforeMethod;  
import org.testng.annotations.Optional;  
import org.testng.annotations.Parameters;  
import utils.DriverFactory;  
  
public class Base {  
  
    @Parameters({"browser"})  
    @BeforeMethod  
    public void setup(@Optional("chrome") String browser) {  
        DriverFactory.initBrowser(browser);  
        DriverFactory.getDriver().manage().window().maximize();  
    }  
  
    @AfterMethod  
    public void quitBrowser(){  
        DriverFactory.getDriver().quit();  
        DriverFactory.cleanDriverThread();  
    }  
}

```

```java title="DriverFactory.java"
package utils;  
  
import org.openqa.selenium.InvalidArgumentException;  
import org.openqa.selenium.WebDriver;  
import org.openqa.selenium.chrome.ChromeDriver;  
import org.openqa.selenium.firefox.FirefoxDriver;  
  
  
public class DriverFactory {  
  
    //static WebDriver driver = null;  
    private static ThreadLocal<WebDriver> driver = new ThreadLocal<>();  
  
    public static WebDriver initBrowser(String browserName){  
        browserName = browserName.toLowerCase().trim();  
        switch(browserName){  
            case "chrome":  
                //driver =  new ChromeDriver();  
                driver.set(new ChromeDriver());  
                break;  
            case "firefox":  
                //driver = new FirefoxDriver();  
                driver.set(new FirefoxDriver());  
                break;  
            default:  
                throw new InvalidArgumentException("Wrong browser value");  
        }  
        //return driver;  
        return driver.get();  
    }  
  
    public static WebDriver getDriver(){  
        return driver.get();  
    }  
  
    public static void cleanDriverThread(){  
        driver.remove();  
    }
```

Now TestNG files examples for parallel testing
Example 1
```xml title=ChromeTestParallel.xml
<suite name="CrossBrowserParallelTesting" parallel="methods">  
    <test name="ChromeOnlyTest">  
       <classes>           <class name="TestDemo"/>  
       </classes>    </test></suite>
```

Example 2
```xml title=CrossBrowser.xml
<suite name="CrossBrowserTesting">  
    <test name="ChromeTests">  
        <parameter name="browser" value="Chrome"/>  
       <classes>
	       <class name="TestDemo"/>  
       </classes>    
    </test>    
    <test name="FirefoxTests">  
        <parameter name="browser" value="Firefox"/>  
        <classes>
	        <class name="TestDemo"/>  
        </classes>    
    </test>
</suite>
```

Example 3
```xml title=CrossBrowserParallelTesting
<suite name="CrossBrowserParallelTesting" parallel="tests">  
    <test name="ChromeTests">  
        <parameter name="browser" value="Chrome"/>  
       <classes>
	       <class name="TestDemo"/>  
       </classes>
    </test>
    <test name="FirefoxTests">  
        <parameter name="browser" value="Firefox"/>  
        <classes>
	        <class name="TestDemo"/>  
        </classes>
    </test>
</suite>
```

---

## Sending Parameters from testng.xml

```xml 
<suite name="DemoTesting" >  
    <test name="ChromeOnlyTest">  
        <parameter name="browser" value="chrome" />  
        <parameter name="IsGrid" value="False" />  
       <classes>           <class name="Demo"/>  
       </classes>    </test></suite>
```

```java title="Demo.java"
<suite name="DemoTesting" >  
    <test name="ChromeOnlyTest">  
        <parameter name="browser" value="chrome" />  
        <parameter name="IsGrid" value="False" />  
       <classes>
	       <class name="Demo"/>  
       </classes>
    </test>
</suite>
```