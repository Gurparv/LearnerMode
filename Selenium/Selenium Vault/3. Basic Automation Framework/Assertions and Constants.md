
```bash title="Automation Framework skeleton"

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
```

```java title="AppConstants.java"
package constants;  
  
public enum AppConstants {  
    HOMEPAGE_URL("https://automationexercise.com/"),  
    HOMEPAGE_TITLE("Automation Exercise");    
    
    private final String value;  
  
    AppConstants(String value){  
        this.value = value;  
    }  
  
    public String getValue(){  
        return value;  
    }  
}
```