let person = {
    name: 'Anna',
    age: 25,
    city:'Moscow'
}
//console.log(person['city'])
//console.log(Object.keys(person))
//console.log(Object.values(person))

let animals= [
    {name: 'кот', color: 'рыжий'},
    {name: 'Собака', color: 'черная'},
    {name: 'Лошадь', color: 'белая'}
]
//console.log(animals[0]['color'])

let anna = {name:'Анна',age:11,luckyNumbers:[2,4,8,16]};
let katya = {name:'Катя',age:5,luckuNumbers:[3,9,40]};
let sacha = {name:'Саша',age:9,luckuNumbers:[1,2,3]};
let friends = [anna,katya,sacha]
//console.log(friends[1])
//console.log(friends[1].luckuNumbers[1])
//console.log(friends)


let money = {};
money['Женя'] = 5;
money['Аня'] = 7;
money['Вася']=87
//console.log(money['Женя'])
//console.log(money['Аня'])
//console.log(money)


let moves ={
    'В поисках Немо':{
        releaseDate:2003,
        duration:100,
        actors:['Альберт Брукс','Элле Дедженес','Александр Гоулд'],
        format:'DVD'
    },
    
    'Звездные войны':{
        releaseDate:1983,
        duration:1134,
        actors:['Марк Хемил','Харрисон Форт','Керри Фишшер'],
        format:'DVD'
    },

    'Гарии Поттер и кубок огня':{
        releaseDate:2005,
        duration:157,
        actors:['Дэниел Редклифф','Эмма Уотсон','Руперт Гринт'],
        format:'Blu-ray'
    }
}

//console.log(Object.values(moves))
//console.log(Object.keys(moves))
//console.log(moves['Гарии Поттер и кубок огня']['actors'][2])

let nemo = moves['В поисках Немо']
//console.log(nemo.duration)
//console.log(nemo.format)

let harry = moves['Гарии Поттер и кубок огня']
console.log(harry.actors[2])
console.log(harry.releaseDate)