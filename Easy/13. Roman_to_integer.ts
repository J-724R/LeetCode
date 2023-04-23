const RomanSymbolsValues: any = {
    I: 1,
    V: 5,
    X: 10,
    L: 50,
    C: 100,
    D: 500,
    M: 1000,
};

function romanToInt(string: string): number | string {
    const validRomanSymbols = checkRomanSymbolValidity(string);
    const validRomanNumber = checkRomanNumberValidity(string);
    let number = 0;

    if (!validRomanSymbols) return "Invalid roman symbols";
    if (!validRomanNumber) return "Invalid roman number";

    for (let i = 0; i < string.length; i++) {
        const current = RomanSymbolsValues[string[i]];
        const next = RomanSymbolsValues[string[i+1]];
        
        console.log(`Current: ${current} next: ${next}`);
        
        if (current < next){
            number += next - current;
            i++
        }else{
            number += current;
        }
    };

    return number;
};

function checkRomanSymbolValidity(string: string): boolean {
    const regex = /[^IVXLCDM]/g ;// Match unallowed values
    return (string.match(regex)) ? false : true;
};

function checkRomanNumberValidity(string: string): boolean{
    for (let i = 0; i < string.length-1; i++) {
        if ((!checkRules(string[i], string[i+1]))  
            && (( i <= string.length-2)
                && (string[i] == string[i+2]) && (string[i] != string[i+1])
                && (string[i+1] != "C" && string[i+1] != "D" && string[i+1] != "M"))
        ) return false
    };
    return true;
};

function checkRules(currentChar: string, nextChar: string): boolean{
    // Rules
    // I can be placed before V (5) and X (10) to make 4 and 9. 
    // X can be placed before L (50) and C (100) to make 40 and 90. 
    // C can be placed before D (500) and M (1000) to make 400 and 900

    if((currentChar == "I") 
        && ((nextChar == "L" || nextChar == "C" || nextChar == "D" || nextChar == "M"))){

        return false;
    } else if((currentChar == "V") 
        && ((nextChar == "V" || nextChar == "X" || nextChar == "L" || nextChar == "C" || nextChar == "D" || nextChar == "M"))){

        return false
    } else if ((currentChar == "X") 
        && (nextChar == "D" || nextChar == "M")){

        return false;
    } else if((currentChar == "L") 
        && ((nextChar == "C" || nextChar == "D" || nextChar == "M"))){

        return false
    }
    return true;
};

const testArray = "MCMXCIV";

console.log(romanToInt(testArray))