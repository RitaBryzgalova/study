let name = "рита";
//console.log("Привет, " + name);

if (name.length >6){
    //console.log('Ну и длинющее же у вас имя')
}else{
    //console.log('Имя у вас не из длинных')
}    
if(condton){
    //console.log('Сделай это, если условие 1 истинно');
} else if(condton){
    //console.log('Сделай это, если условие 2 истинно');
}else if(condton){
    //console.log('Сделай это, если условие 3 истинно');
}else{
    //console.log("Иначе сделай это")
}

let apple = 0;
while(apple < 10){
    console.log('Яблоки' + apple)
    apple++;
}
//console.log('Собраны')

//for(настройка; условие; приращение){
//          тело цикла
//      }


let sayHello =3;
for(let i = 0; i < sayHello; i++){
    console.log('Привет')
}

let animals =['лев','фламинго','медведь','удав'];
for(let i = 0; i < animals.length; i++ ){
    console.log('В этом зоопарке есть' + animals[i]+'.');
}

for (let x = 2; x<10000;x=x*2){
    console.log(x)
}