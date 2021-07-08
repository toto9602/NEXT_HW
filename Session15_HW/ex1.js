const $ulElement = document.querySelector('ul');
let checked = 0;
let len = 0;

$ulElement.addEventListener("click",(event) => {
    const $target = event.target;
    if ($target.classList.contains('close')){
        const $parentTarget = $target.parentElement;
        $parentTarget.style.display = "none";
        len = len-1;
        if ($parentTarget.classList.contains('checked')) {
            checked--;
        }
        
        console.dir($parentTarget)
        const deleteItem = $parentTarget.childNodes[1].innerText;
        deleteTodoList('todoList', deleteItem);
        
        
    }
    else {
    $target.classList.toggle('checked');
    if ($target.classList.contains('checked')) {
        checked++;
    }
    else {
        checked--;
    }
}
    bar(checked, len);
})

function newElement() {
    const inputValue = document.getElementById("myInput").value;

    if (inputValue === '') {
        alert("You must write something!");
    } else {
        $ulElement.insertAdjacentHTML('beforeend', `
        <li>
            <span>${inputValue}</span>
            <span class="close">&#215;</span>
        </li>`)
        addTodoList('todoList', inputValue);
        len++;
    }
    
    document.getElementById("myInput").value = "";
    // const $liElement = document.createElement("li");

    // const $textElement = document.createElement("span");
    
    // $textElement.innerText = inputValue;

    // const $closeElement = document.createElement("span");
    // const $closeText = document.createTextNode("\u00D7");
    // $closeElement.className = "close";
    // $closeElement.appendChild($closeText);

    // $liElement.appendChild($textElement);
    // $liElement.appendChild($closeElement);

    
}


// 두번째 실습
function bar(checked, len) {
    let bar = document.getElementById("bar");
    if (len !== 0) {
        bar.style.width = ((checked/len) * 100) + '%';
    }
    else {
        bar.style.width = 0;
    }
    
}


function init() {
    checked = 0;
    len = 0;
    let todoList = getTodoList('todoList');
    for(let i=0; i<todoList.length; i++){
        $liElement = `
            <li>
                <span>${todoList[i]}</span>
                <span class="close">&#215;</span>
            </li>
        `

        $ulElement.insertAdjacentHTML('beforeend', $liElement);

    }
    
    len = todoList.length
    bar(checked, len);

}

function getTodoList(key) {
    return localStorage.getItem(key) ? localStorage.getItem(key).split(',') : [];

}

function addTodoList(key, value) {
    const todoList = getTodoList(key);
    return localStorage.setItem(key, [...todoList, value])

}

function deleteTodoList(key,value) {
    const todoList = getTodoList(key)
    return localStorage.setItem(key,todoList.filter(todo => todo !== value)) //?

}



function changetheme() {
    const background = document.body;
    const h_background = document.getElementById("myDIV");
    background.classList.toggle("dark_mode");
    h_background.classList.toggle("dark_mode");

    const button = document.getElementsByClassName("dark")[0];
    button.classList.toggle("darkmodebutton");

    if (button.classList.contains('darkmodebutton')) {
        button.innerText = 'Bright Mode'

    }
    else {
        button.innerText = 'Dark mode'
    }
}

init()