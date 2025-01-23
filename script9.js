const button1 = document.querySelector("button.abrir1")
const modal1 = document.querySelector("dialog.caixa1")
const buttonclose1 = document.querySelector("button.sair1")
let alter = true;
button1.onclick = function(){
    modal1.showModal()
    if (alter === true){
    getConstrucaoByIndex(11,1);
    alter= false;  }
}
buttonclose1.onclick = function() {
    modal1.close()
}

