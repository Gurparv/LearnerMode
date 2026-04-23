
```Bash title=Framework skeleton
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

```xml title="pom.xml"
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