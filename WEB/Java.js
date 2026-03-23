// Переменные let const
//let a =10
//a= 20
//const b = 5

// b = 6 оштбка тк b не изменяется
//console.log('let a =',a)
//console.log('const b -',b)

// Сравнение == и ===
//console.log('0 == false:', 0 == false);
//console.log('0 === false:', 0 === false);
//console.log('" == false:', "" == false);
//console.log('null == undefined:',null == undefined);

// Соединение строк
//let greeting = 9;
//let name = '9';
//console.log(name+name)

// Длина строки
//console.log('Спераупердлиннаястрока'.length)
//можно узнавать длинну строки даже в переменной
//let java = 'Java'
//console.log(java.length)

// Срез строки
//let longstring = 'это длинная строка ьакая длинная'
//console.log(longstring.slice(1,17))


// Вывод строки заглавными буквами
//console.log('Эй как дела'.toUpperCase())
//вывод строки низкими буквами
//console.log('Эй как дела'.toLowerCase())

//Булевы значения
//let javascriptiscool = true
//console.log(javascriptiscool)


// Логические операции

//&&, and, и 
//let hadShower = true
//let hasBackpack = false
//console.log(hadShower && hasBackpack)

// || или or 
//let hasApple = true
//let hasOrange = false
//console.log(hasApple || hasOrange)

// !, no, не
//let isWeekend = true
//let needToShowerToday = !isWeekend
//console.log(needToShowerToday)

//let isWeekend = false
//let hadShower = true
//let hasApple = false
//let hasOrabge = true
//let shouldGoToSchool = !isWeekend && hadShower && (hasApple || hadShower)
//console.log(shouldGoToSchool)

//let height = 155
//let heightRestriction = 150
//console.log(height > heightRestriction)

//let height = 150
//let heightRestriction = 150
//console.log(height >= heightRestriction)

//let height = 150
//let heightRestruction = 120
//console.log(height<heightRestruction)

// ОПЕРАТОР СТРОГОГО ПРИРАВНИВАНИЯ (приранивает с приведением типов)
//let mySecretNumber = 5
//let chicoGuess = 3
//console.log(mySecretNumber === chicoGuess)

//let haroGuess = 7
//console.log(mySecretNumber === chicoGuess)

//let grouchGuess = 5
//console.log(mySecretNumber === grouchGuess)

// Оператор приравнивания
//let stringNumber = '5'
//let actualString = 5
//console.log(stringNumber === actualString) //false потому что разнные типы
//console.log(stringNumber == actualString) // true потому что все приравнивается к числу

//['Разрешенно добавлять сообщения','Разрешенно банить пользователей','Разрешенно удалять пользователей']

// Массив
let fruits = ['яблоко','банан','Апельсин','манго']
//console.log(fruits[0])
//console.log(fruits[0]='груша')
//console.log(fruits)

// Вложенный массив
let dino_and_number = [3,'динозавры',['трицератопс','стегозавр',3627.5],10]
//console.log(dino_and_number[2][0]) //отображение элементов вложенногго массива 
//console.log(dino_and_number.length)

//добавление элемента в массив
let animals = []
animals.push('cat')
animals.push('dog')
animals.push('lama')
animals.unshift('monkey')

// Добавление в начало массива 
//animals.unshift('white bear')
//console.log(animals)
//console.log(animals.length)

// Удаление последнего элемента с возватом его значения
//lastAnimals = animals.pop()
//console.log(lastAnimals)
//console.log(animals)

// Удаление первого элемента массива с возватом его значения
first = animals.shift() 
console.log(animals)
console.log(first)
