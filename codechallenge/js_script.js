const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});


function js_function() {

    readline.question('Enter the input: ', input => {
        let nums = [1, 2, 3];

        nums.push(4);
        nums.push(input);

        let SRE = nums.slice(1, 5).filter(n => n % 2 === 0).map(n => n * 2).reduce((a, n) => a + n, 0);

        console.log("output is: ", SRE >>>= 1)
        readline.close();
    });

}

// run the script
js_function()
