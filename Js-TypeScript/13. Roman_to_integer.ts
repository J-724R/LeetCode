
const RomanSymbolsValues: any = {
    I: 1,
    V: 5,
    X: 10,
    L: 50,
    C: 100,
    D: 500,
    M: 1000,
}

function romanToInt(string: string): number | void {
    const validRomanSymbols = checkRomanSymbolValidity(string);
    const validRomanNumber = checkRomanNumberValidity(string);
    let number = 0;

    if (!validRomanSymbols) {
        return console.log("Invalid roman symbols");
    }
    if (!validRomanNumber) {
        return console.log("Invalid roman number");
    }


    for (let i = 0; i < string.length; i++) {
        const current = RomanSymbolsValues[string[i]]
        const next = RomanSymbolsValues[string[i+1]]
        
        console.log(`Current: ${current} next: ${next}`);
        
        if (current < next){
            number += next - current
            i++
        }else{
            number += current
        }
    }

    return number
};

function checkRomanSymbolValidity(string: string): boolean {
    const regex = /[^IVXLCDM]/g ;// Match unallowed values
    return (string.match(regex)) ? false : true;
}

function checkRomanNumberValidity(string: string): boolean{
    
    for (let i = 1; i < string.length-2; i++) {
        const next = RomanSymbolsValues[string[i+1]]
        const twoAfter = RomanSymbolsValues[string[i+2]]
        
        if  ((string[i] == string[i+1]) && ( next < twoAfter ))
        {
            return false;
        }       
    };
    return true;
}


const testArray = "CXVXIV";

console.log(`Valid Roman Symbols: ${checkRomanSymbolValidity(testArray)}`);
console.log(`Valid Roman Number: ${checkRomanNumberValidity(testArray)}`);

console.log(romanToInt(testArray))
