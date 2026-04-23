Documentation link -> https://www.selenium.dev/documentation/grid/

### Run locally Selenium Grid
java -jar selenium-server-4.40.0.jar hub

Now open default URL  (Selenium Grid hub is up) - 
Grid Console link:   http://192.168.1.6:4444/ui/

### Now start Node
java -jar selenium-server-4.40.0.jar node --detect-drivers true 
OR
java -jar selenium-server-4.40.0.jar node --port 5556

### Basic code to run SeleniumGrid
URL url = new URL("http://192.168.1.6:4444/");
DesiredCapabilities caps = new DesiredCapabilities();
caps.setBrowserName("chrome");
WebDriver driver = new RemoteWebDriver(url,caps);

### Debugging logs
java -jar selenium-server.jar hub --log hub.log
java -jar selenium-server.jar node --log node.log
These logs are NOT test reports.
They are debugging / infra telemetry.

connect remote machine as node on your hub
On Linux:
java -jar selenium-server.jar node --hub http://192.168.1.10:4444
Boom.
Linux node registers remotely.

---

How to Force Machine-Level Distribution

### Use platformName capability.

✔ Windows-only execution
caps.setBrowserName("chrome");
caps.setPlatformName("Windows");

✔ Linux-only execution
caps.setBrowserName("chrome");
caps.setPlatformName("Linux");

✔ Grid Matching Logic

Hub filters nodes by:
✔ browserName
✔ platformName

-------------

Clean Mental Model (Very Important)

Grid = Router
Test Runner = Work Distributor
Reports = Test Framework responsibility

Grid never “assigns test cases to machines”.

It assigns sessions.

```java title="SeleniumGrid1.java"
import org.testng.annotations.Test;  
  
import java.net.MalformedURLException;  
import java.net.URL;  
  
public class SeleniumGrid1 {  
    @Test  
    public void testSeleniumGrid1() throws MalformedURLException {  
        URL url = new URL("http://192.168.1.6:4444/");  
        DesiredCapabilities caps = new DesiredCapabilities();  
        caps.setBrowserName("chrome");  
        WebDriver driver = new RemoteWebDriver(url,caps);  
  
        driver.get("https://practicetestautomation.com/");  
        driver.manage().window().maximize();  
        String title = driver.getTitle();  
        System.out.println(title);  
        driver.quit();  
  
    }  
  
    @Test  
    public void testDockerSeleniumGrid() throws MalformedURLException, InterruptedException {  
        URL url2 = new URL("http://localhost:4444/");  
        DesiredCapabilities caps2 = new DesiredCapabilities();  
        caps2.setBrowserName("chrome");  
        WebDriver driver =  new RemoteWebDriver(url2,caps2);  
  
        driver.get("https://practicetestautomation.com/");  
        driver.manage().window().maximize();  
        Thread.sleep(15_000);  
        String title = driver.getTitle();  
        System.out.println(title);  
        driver.quit();  
  
  
    }  
}
```