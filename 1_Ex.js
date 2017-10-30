/*
const question = "What are you really..?";
let answer = prompt(question);
alert(`I'm ${ answer }`);
const test = "Enter a number.?";
let num = prompt(test);
document.write(`<p>
	${num} is a <i>${(num%2 === 0)?'even':'odd'}</i> number
	</p>`)
*/

const Question = "Enter a number 1 to 6";
let answer = parseInt(prompt(Question));

switch (answer) {
	case 1:
		document.write(`You rolled ${answer}`);
		break;
	case 2:
		document.write(`You rolled ${answer}`);
		break;
	case 3:
		document.write(`You rolled ${answer}`);
		break;
	case 4:
		document.write(`You rolled ${answer}`);
		break;
	case 5:
		document.write(`You rolled ${answer}`);
		break;
	case 6:
		document.write(`You rolled ${answer}`);
		break;
	default:
		document.write(`You rolled Unknown`);
		break;
}

function tableNum() {
	lets number = parseInt(document.getElementById('Num').value);
	for(lets i = 1; i<11; i++){
		document.write(`<p>${number} * ${i} = ${number * i}`);
	}
}
