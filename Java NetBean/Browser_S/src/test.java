
import java.util.ArrayList;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

public class test {

    public static void main(String[] args) throws InterruptedException {

        System.out.println("Execution after setting ChromeDriver path in System setProperty method");
        System.setProperty("webdriver.chrome.driver", "D:\\Code\\Browser\\chromedriver.exe");
        WebDriver driver = new ChromeDriver();
        Thread.sleep(500);
        openNewTab(driver);
        Thread.sleep(500);
        openNewTab(driver);
        ArrayList<String> tabs_windows = new ArrayList<String> (driver.getWindowHandles());
        Thread.sleep(2000);
        driver.switchTo().window(tabs_windows.get(1));
        Thread.sleep(2000);
        driver.switchTo().window(tabs_windows.get(2));
        Thread.sleep(2000);
        driver.switchTo().window(tabs_windows.get(0));
        System.out.println("Execution complete");
    }
    
    static void openNewTab(WebDriver driver) {
        ((JavascriptExecutor) driver).executeScript("window.open('https://google.com');"); 
    }
    
    static void closeTab(WebDriver driver){
        ((JavascriptExecutor)driver).executeScript("close();");
    }
}
