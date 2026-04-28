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
//let fruits = ['яблоко','банан','Апельсин','манго']
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
//first = animals.shift() 
//console.log(animals)
//console.log(first)

// Обьединение массивов
let furry_Animals = ['Альпака','Лемур','Йети']
let scaly_Animals =['Удав','Годзилла']
let furry_and_scaly_animals = furry_Animals.concat(scaly_Animals)
//console.log(furry_and_scaly_animals)


// Поиск индекса элемента
let colors = ['красный','зеленый','синий']
//console.log(colors.indexOf('синий'))

// Вывод массива в строку 
let boring_Animals = ['Мартышка','Кот','Рыба','Ящерица']
//console.log(boring_Animals.join('-'))
//console.log(boring_Animals.join(' и '))

// Генератор случайных чисел
//console.log(Math.random()) // random генерирует цисла от 0 до 1
//console.log(Math.floor(2134.4234))  //floor выделяет целую часть числа
//console.log(Math.floor(Math.random()*4)) // Генерирует число от 0 до 4 и выделяет целую часть


let Ramdom_words = ['Взрыв','Пещера','Принцесса','Карандаш']
let radom_index = Math.floor(Math.random()*4)
//console.log(Ramdom_words[radom_index])



let phases = [
    'Звучит неплохо',
    'Да, это определенно надо сделать',
    'Не думаю, что это хорошая идея',
    'Может, не сегодня',
    'Компьютер говорит нет'
]
// Мне выпить еще молочного коктейля?
//console.log(phases[Math.floor(Math.random()*5)])
console.log(43124)
 HEAD
let a = 'Первостепеная разработка'

//let fix = "Ветка fix"
//let s ='должно ругатся'

//let fi = "Ветка fix c изменениями"
//let h = 'должна быть ошибка'

//let = [8]
//let = "Второстепенная разработка"

//develop


let g = 'Слиянение с main'







// Создаём массив с именами четырёх студентов
//const students = ["Анна", "Борис", "Виктор", "Галина"];

// Выводим длину массива
//console.log("Длина массива:", students.length); // Длина массива: 4

// Выводим последнего студента, используя длину массива
//console.log("Последний студент:", students[students.length - 1]); // Последний студент: Галина


//let fruits = ["яблоко", "банан", "апельсин", "манго", "киви"];
//let numbers = [10, 20, 30];
//let mixed = [true, "привет", 42, null, {name: "Анна"}, [1, 2, 3]];
//let empty = [];

// Определяем длину каждого массива
//console.log("Длина fruits:", fruits.length);     // 5
//console.log("Длина numbers:", numbers.length);   // 3
//console.log("Длина mixed:", mixed.length);       // 6
//console.log("Длина empty:", empty.length);       // 0



//let queue = ["Анна", "Иван", "Мария", "Петр"];

// 1. Исходная очередь
//console.log("1. Исходная очередь:", queue);

// 2. Пришла Елена — в конец очереди (push)
//queue.push("Елена");
//console.log("2. После прихода Елены:", queue);

// 3. Анна обслужилась и ушла из начала (shift)
//queue.shift();
//console.log("3. После ухода Анны (обслужена):", queue);

// 4. Последний покупатель Пётр ушёл из конца (pop)
//queue.pop();
//console.log("4. После ухода Петра (конфликт):", queue);

// 5. Директор прошёл в начало (unshift)
//queue.unshift("Директор");
//console.log("5. После прихода Директора в начало:", queue);

// 6. Финальная очередь и её длина
//console.log("6. Финальная очередь:", queue);
//console.log("   Длина очереди:", queue.length);



//let ingredients = ["макароны", "гречку", "картошку", "рис", "овсянку", "капусту"];
//let actions = ["сварить", "пожарить", "запечь", "смешать с", "посыпать", "полить"];
//let additions = ["кетчупом", "сыром", "маслом", "зеленью", "соусом", "специями"];

//let randomIngredient = ingredients[Math.floor(Math.random() * ingredients.length)];
//let randomAction = actions[Math.floor(Math.random() * actions.length)];
//let randomAddition = additions[Math.floor(Math.random() * additions.length)];

//let randomPhrase = ["Сегодня готовим", randomIngredient, randomAction, randomAddition].join(" ");

//console.log(randomPhrase);



//let book = {
//  title: "Мастер и Маргарита",
//  author: "Михаил Булгаков",
//  year: 1966
//};

// Проверим содержимое объекта
//console.log(book);