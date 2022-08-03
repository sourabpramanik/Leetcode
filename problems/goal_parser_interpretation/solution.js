/**
 * @param {string} command
 * @return {string}
 */
var interpret = function(command) {
    let str="";
    for(let i=0; i<command.length; i++){
        if(command[i]==="G"){
            str += "G"
        } else if(command[i]=="("){
            if(command[i+1]==")"){
                str += "o";
                i++
            } else{
                str += "al"
                i+3
            }
        }
    }
    return str
};