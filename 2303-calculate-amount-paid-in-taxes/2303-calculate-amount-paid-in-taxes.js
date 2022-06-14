/**
 * @param {number[][]} brackets
 * @param {number} income
 * @return {number}
 */
var calculateTax = function(brackets, income) {
    let prevAmnt=0
    let amount=0
    let taxArr=[]
    for(let i=0; i<brackets.length; i++){
        if(amount===income){
            break
        }
        if(i!==0){
             prevAmnt=brackets[i-1][0]
        } 
        if(brackets[i][0]>=income){
            amount=income            
        }else if(brackets[i][0]<income){
            amount=brackets[i][0]            
        }
        console.log(amount)
        let tax=(amount-prevAmnt)*(brackets[i][1]/100)
        taxArr.push(tax)
    }
    return income===0? 0 : taxArr.length === 1?taxArr : taxArr.reduce((a,b)=>a+b)
    
};