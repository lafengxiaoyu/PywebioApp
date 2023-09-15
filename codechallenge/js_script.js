const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});


function js_function() {
    readline.question('Enter the input: ', input => {
        let nums = [1, 2, 4, 6];
        nums.push(Number(input));
        let SRE = nums.slice(2, 4).filter(n => n % 2 === 0).map(n => n * 2).reduce((a, b) => a + b);
        console.log("output is: ", SRE >>>= 2)
        readline.close();
    });
}

// run the script
js_function()
