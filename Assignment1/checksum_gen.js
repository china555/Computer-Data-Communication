const input = process.argv;
const dataWord = String(input[2]);
const size = Number(input[3]);
const block = Number(input[4]);

checksum_gen(dataWord, size, block);

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

function checksum_gen(dataWord, size, block) {
    if (!isBit(dataWord)) {
        console.log("Is not a bit")
        return;
    }
    if (dataWord.length !== size * block) {
        print("Invalid input")
        return
    }
    let dat = []
    for (let i = 0; i < block; i++) {
        let temp = ""
        for (let j = i * size; j < i * size + size; j++) {
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
        for (let i = sum.length - size; i < sum.length; i++) {
            temp1 += sum[i]
        }
        let temp2 = ''
        for (let i = 0; i < sum.length - size; i++) {
            temp2 += sum[i]
        }
        sum = dec2bin(parseInt(temp1, 2) + parseInt(temp2, 2))
    }
    while (sum.length < size) {
        sum = '0' + sum
    }
    dat.push(inverse(sum))
    let bittt = ""
    dat.map((ele) => {
        bittt += ele + " "
    })
    // console.log(bittt)
    console.log("Dataword: " + dataWord + "\nSum: " + sum + "\nComplement: " + inverse(sum) + "\nCodeword: " + bittt)

}