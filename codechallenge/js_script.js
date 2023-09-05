let x = -6


function js_function(x) {
    let nums = [1, 2, 3];

    nums.push(4, 9);
    nums.push(x);

    let SRE = nums.slice(1, 4).filter(n => n % 2 === 0).map(n => n * 2).reduce((a, n) => a + n, 0);

    console.log("output is:", SRE >>>= 1)
    return SRE;
}

js_function(x)

