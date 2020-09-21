const { Builder, By, Key, until } = require('selenium-webdriver');
const chrome = require('selenium-webdriver/chrome');
const { expect } = require('chai');


describe('Test selenium', ()=>{
    let driver;
    before(async ()=>{
       driver = await new Builder().forBrowser('chrome').setChromeOptions(new chrome.Options().headless()).build();
       await driver.manage().window().maximize();
    });

    after(async ()=>{
        console.log('Close browser');
        await driver.close();
        await driver.quit();
    })

    describe('Search in python org', async ()=>{
        it('Load python.org', async ()=>{
            await driver.get("http://www.python.org")
            const title = await driver.getTitle();
            console.log(`Title of http://www.python.org page: ${title}`);
            expect(title).contains('Python');
        });

        it('Search in python.org', async ()=>{
            const elem = await driver.findElement(By.name("q"))
            await elem.clear();
            console.log("Trying to find pycon on python.org")
            await elem.sendKeys("pycon")
            await elem.sendKeys(Key.RETURN);
            console.log("Current URL: " + (await driver).getCurrentUrl)
            const result = await driver.getPageSource();
            expect(result).not.contains("No results found");
        });
    });

    describe('Test on wiki page', async ()=>{
        it('Load wiki', async ()=>{
            await driver.get("https://en.wikipedia.org/wiki/Main_Page");
            const title = await driver.getTitle();
            expect(title).contains('Wikipedia');
        });

        it('Search on wiki', async ()=>{
            await driver.wait(until.elementLocated(By.id("searchInput")), 1000);
            const searchInput = await driver.findElement(By.id("searchInput"));
            await searchInput.sendKeys("Software");
            await driver.wait(until.elementLocated(By.className("suggestions-results")), 1000);
            const suggestionsResults = await (await driver.findElement(By.className("suggestions-results"))).getText();
            expect(suggestionsResults).contains("Software");
        });
    });

});