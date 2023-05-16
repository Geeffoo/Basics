let first5="ham";
let second5="pinapple";
let txt5 = h`${first5} and  ${second5}.`;

console.log(txt5);

function h(strings, ...expressions){
    return 'I do not like  ' + expressions.join(' and '); 
}

h()