console.log("hi")
const idinput = document.querySelector('#username')
const checkInputValid = () => {
if (idinput.value.length > 10) {
    alert('아이디는 10자리 이하로 해주세요!')
}
}
checkInputValid()

console.log("hi");
