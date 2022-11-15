const { chromium } = require('playwright');

let person = 'the rock';

let prompts = [
    `who is ${person}`,
    `who did ${person}`,
    `how did ${person}`,
    `what does ${person}`,
    `can ${person}`,    
]

async function main() {
    const browser = await chromium.launch();
    const page = await browser.newPage();
    await page.goto('https:\\google.com');

    for (let i = 0; i < prompts.length; ++i) {
        await page.type("[aria-label='Search']", prompts[i]);
        await page.waitForTimeout(2000);
        await page.screenshot({ path: `images/${i}.png`});
    }
    await browser.close();
}

main();