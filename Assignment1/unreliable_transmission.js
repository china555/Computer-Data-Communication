const input = process.argv;
const bit = String(input[2]);
const probability = Number(input[3])

function checkBit(bit) {
    for (let i = 0; i < bit.length; i++) {
        if (bit[i] !== '1' && bit[i] !== '0') {
            console.log("False")
            return false;
        }
    }
    return true;
}

function unreliable_transmission(bit, probability) {
    if (!checkBit(bit)) {
        console.log("Not a bit");
        return;
    }
    if (probability < 0 && probability > 100) {
        console.log("Probability is wrong")
        return;
    }
    let output = ""
    for (let i = 0; i < bit.length; i++) {
        let random = Math.floor(Math.random() * 100);
        // console.log(random);
        // console.log(bit[i])
        if (random < probability) {
            if (bit[i] === '1') {
                output += '0'
            } else {
                output += '1'
            }
        } else {
            output += bit[i];
        }
    }
    console.log(`Bit String is: ${bit}\nProbability is: ${probability}\nResult is: ${output}`);

}
const result = unreliable_transmission(bit, probability);