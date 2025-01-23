const button1 = document.querySelector("button.abrir1")
const modal1 = document.querySelector("dialog.caixa1")
const buttonclose1 = document.querySelector("button.sair1")
let alter = true;
let alter1 = true;
let alter2 = true;
let alter3 = true;
let alter4 = true;
let alter5 = true;
let alter6 = true;
let alter7 = true;
let alter8 = true;
let alter9 = true;
let alter10 = true;
let alter11 = true;
let alter12 = true;
button1.onclick = function(){
    modal1.showModal()
    if (alter === true){
    getTropaByIndex(7,1);
    alter= false;  }
}
buttonclose1.onclick = function() {
    modal1.close()
}


const button2 = document.querySelector("button.abrir2")
const modal2 = document.querySelector("dialog.caixa2")
const buttonclose2 = document.querySelector("button.sair2")
button2.onclick = function(){
    modal2.showModal()
    if (alter1 === true){
    getTropaByIndex(38,2);
    alter1= false;  }
}
buttonclose2.onclick = function() {
    modal2.close()
}


const button3 = document.querySelector("button.abrir3");
const modal3 = document.querySelector("dialog.caixa3");
const buttonclose3 = document.querySelector("button.sair3");

button3.onclick = function() {
    modal3.showModal()
    if (alter2 === true){
    getTropaByIndex(2,3);
    alter2= false;  }
}

buttonclose3.onclick = function() {
    modal3.close();
}

const button4 = document.querySelector("button.abrir4");
const modal4 = document.querySelector("dialog.caixa4");
const buttonclose4 = document.querySelector("button.sair4");

button4.onclick = function() {
    modal4.showModal()
    if (alter3 === true){
    getTropaByIndex(3,4);
    alter3= false;  }
    
}

buttonclose4.onclick = function() {
    modal4.close();
}

const button5 = document.querySelector("button.abrir5");
const modal5 = document.querySelector("dialog.caixa5");
const buttonclose5 = document.querySelector("button.sair5");

button5.onclick = function() {
    modal5.showModal()
    if (alter4 === true){
    getTropaByIndex(4,5);
    alter4= false;  }
}

buttonclose5.onclick = function() {
    modal5.close();
}

const button6 = document.querySelector("button.abrir6");
const modal6 = document.querySelector("dialog.caixa6");
const buttonclose6 = document.querySelector("button.sair6");

button6.onclick = function() {
    modal6.showModal()
    if (alter5 === true){
    getTropaByIndex(17,6);
    alter5= false;  }
}

buttonclose6.onclick = function() {
    modal6.close();
}

const button7 = document.querySelector("button.abrir7");
const modal7 = document.querySelector("dialog.caixa7");
const buttonclose7 = document.querySelector("button.sair7");

button7.onclick = function() {
    modal7.showModal()
    if (alter6 === true){
    getFeiticoByIndex(3,7);
    alter6 = false;  }
}

buttonclose7.onclick = function() {
    modal7.close();
}

const button8 = document.querySelector("button.abrir8");
const modal8 = document.querySelector("dialog.caixa8");
const buttonclose8 = document.querySelector("button.sair8");

button8.onclick = function() {
    modal8.showModal()
    if (alter7 === true){
    getTropaByIndex(57,8);
    alter7= false;  }
}

buttonclose8.onclick = function() {
    modal8.close();
}

const button9 = document.querySelector("button.abrir9");
const modal9 = document.querySelector("dialog.caixa9");
const buttonclose9 = document.querySelector("button.sair9");

button9.onclick = function() {
    modal9.showModal()
    if (alter8 === true){
    getFeiticoByIndex(8,9);
    alter8= false;  }
}

buttonclose9.onclick = function() {
    modal9.close();
}

const button10 = document.querySelector("button.abrir10");
const modal10 = document.querySelector("dialog.caixa10");
const buttonclose10 = document.querySelector("button.sair10");

button10.onclick = function() {
    modal10.showModal()
    if (alter9 === true){
    getTropaByIndex(46,10);
    alter9= false;  }
}

buttonclose10.onclick = function() {
    modal10.close();
}

const button11 = document.querySelector("button.abrir11");
const modal11 = document.querySelector("dialog.caixa11");
const buttonclose11 = document.querySelector("button.sair11");

button11.onclick = function() {
    modal11.showModal()
    if (alter10 === true){
    getConstrucaoByIndex(0,11);
    alter10= false;  }
}

buttonclose11.onclick = function() {
    modal11.close();
}

const button12 = document.querySelector("button.abrir12");
const modal12 = document.querySelector("dialog.caixa12");
const buttonclose12 = document.querySelector("button.sair12");

button12.onclick = function() {
    modal12.showModal()
    if (alter11 === true){
    getTropaByIndex(30,12);
    alter11= false;  }
}

buttonclose12.onclick = function() {
    modal12.close();
}