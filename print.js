console.log("My name is ahmed ");

// document.write("<h1>My name is Ahmed <h1>");

// window.alert("I am there")
b=15
a=10;
d="Ahmed";

console.log(a,d);

console.log("My name is ahmed {}", a)

console.log("My name is ahmed {}  "+ a)

console.log("Ahmed is ", a+b)

console.table({
    name: "Ahmed",
    age: 25,
    gender:"male",
    bool: true,
})

console.log("%c Wellcome Ahmed to Javascript" , 'color:red; font-wegiht:bold ; font-size:20px');

console.log("%c This is another way to do business" , `
color:green;
font-weight:bold ; 
font-size:10px`);
console.log("log") // console.log expands things as html object
console.debug("debug")
console.error("error")
console.info("info")
console.warn("warn")

Data="Hello";

console.log("%s  World", Data) //%i for integers, %f for float , 
let name="Ali"
let num=10
console.log(`my name is Ahmed
I am 25 yeras his name is ${name} his number is ${num} `)


const name1="John";
const age=44;
function getName(){
    return name1
}

const message=`My name is ${getName()}, I amd twice the age of ${age/2}`
console.log(message)

let num8=41;
let str1=`"\t and \n " are escaping sequence. ${num8}`;

let str2= `"\\t nad \\n" are sequence escaping. ${num8} `;

let str3=String.raw`"\t ans \n" are escaping sequences. ${num8}`;

let str4=` the meaning of life is ${num8}.`;

console.log(str1);
console.log(str2);
console.log(str3);
console.log(str4);

let first="ham";
let second="pinapple";

let txt = f`I do not like piza with ${first} and  ${second}.`;

console.log(txt);

function f(){
    return 'Hello' ; 
}

f()
let first1="ham";
let second1="pinapple";
let txt1 = m`I do not like piza with ${first1} and  ${second1}.`;

console.log(txt1);

function m(strings){
    return strings ; 
}

m()


let first2="ham";
let second2="pinapple";
let txt2 = z`I do not like piza with ${first2} and  ${second2}.`;

console.log(txt2);

function z(strings, ...expressions){
    return expressions ; 
}

z()

let first3="ham";
let second3="pinapple";
let txt3 = g`${first3} and  ${second3}.`;

console.log(txt3);

function g(strings, ...expressions){
    return strings ; 
}

g()

let first4="ham";
let second4="pinapple";
let txt4 = l`${first4} and  ${second4}.`;

console.log(txt4);

function l(strings, ...expressions){
    return 'I do not like  ' + expressions[0] ; 
}

l()


let first5="ham";
let second5="pinapple";
let txt5 = h`${first5} and  ${second5}.`;

console.log(txt5);

function h(strings, ...expressions){
    return 'I do not like  ' + expressions.join(' and '); 
}

h()





//************************************************************************************************************************************************** *

// console.dir("Ahmed")

// console.dir(document.body) // console.dir expands things an a json object

// console.log(document.body) 

const people=[{name: "Kyle", age:27, programmer: true},
{name: "Sally", age:30, programmer: false},
{name: "John", age:47, programmer: true},
{name: "beth", age:18, programmer: false},
]
console.table(people)

console.log("Outside Group")
console.group("Name")
console.log("Inside Group")
console.log("Still Inside Group")
console.groupEnd()
console.log("Start of Stas Group")
console.groupCollapsed("Stats")
console.log("Begin Group")
console.group("Nested Group")
console.log("Print from Nested Group")
console.groupEnd()
console.log("Second Begin")
console.log("Last")
console.groupEnd()


console.time("Name");
 for(let i=0 ; i<100000 ; i++);
 console.timeLog("Name");
 for(let i=0 ; i<100000 ; i++);
 console.timeEnd("Name");

 console.profile("Nouny")
 for(let i=0 ; i<100000 ; i++);
 console.timeStamp("Nouny");
 for(let i=0 ; i<100000 ; i++);
 console.profileEnd("Nouny");

console.assert(1==0 , 'Hello');
console.assert(1==1, "Hello");

console.clear()

console.count("Name")
function main(){

    console.trace()
}
//main()

const data1={prop1: "hello",
prop2: [{id:1, name:"Ahmed" , actor:"Jason"},
{id:2, name:"Nouny" , actor:"Champ"},
{id:3, name:"NounyCCO" , actor:"Chief"},
{id:4, name:"Nounyss" , actor:"JBig Boss"},
],};

console.table(data1);
console.table(data1.prop2);

const funcs= {
f1(){ console.log("inside f1");
funcs.f2()},

f2(){ console.log("Inside f2");
funcs.f3()},

f3(){console.log("Insdie f3");
funcs.f4()},
f4(){console.trace("Inside f4")}}

funcs.f4();

funcs.f1();
