const input = process.argv;
const dataWord = String(input[2]);
const size = Number(input[3]);
const block = Number(input[4]);

checksum_check(dataWord, size, block);

function inverse(bit) {
    let out = ''
    for (let i = 0; i < bit.length; i++) {
        if (bit[i] === '1') {
            out += '0'
        } else {
            out += '1'
        }
    }
    return out
}

function dec2bin(dec) {
    return (dec >>> 0).toString(2);
}

function isBit(bit) {
    for (let i = 0; i < bit.length; i++) {
        if (bit[i] !== '1' && bit[i] !== '0') {
            console.log("False")
            return false;
        }
    }
    return true;
}

function checksum_check(dataWord, size, block) {
    if (!isBit(dataWord)) {
        console.log("Is not a bit")
        return;
    }
    if (dataWord.length !== size * (block + 1)) {
        print("Invalid")
        return
    }
    let dat = []
    for (let i = 0; i < block + 1; i++) {
        let temp = ""
        for (let j = i * size; j < i * size + size; j++) {
            // console.log(dataWord[j])
            temp += dataWord[j]
        }
        dat.push(temp)
    }
    let sum = '0'
    for (let i = 0; i < dat.length; i++) {
        sum = dec2bin(parseInt(sum, 2) + parseInt(dat[i], 2))
    }
    while (sum.length > size) {
        let temp1 = ''
        for (let i = sum.length - size + 2; i < sum.length; i++) {
            temp1 += sum[i]
        }
        let temp2 = ''
        for (let i = 0; i < sum.length - size; i++) {
            temp2 += sum[i]
        }
        sum = dec2bin(parseInt(temp1, 2) + parseInt(temp2, 2))
    }
    console.log(sum)
    while (sum.length < size) {
        sum = '0' + sum
    }
    let ans = ''
    for (let i = 0; i < size; i++) {
        ans += '0'
    }
    console.log(`CodeWord: ${dat}\nSum: ${sum}`)
    if (inverse(sum) === ans) {
        console.log("Valid True")
    } else {
        console.log("Valid False")
    }
}