let num_cards_revealed = 0;

$("#reset").on("click", function () {
    $('option').prop('selected', function() {
        return this.defaultSelected;
	});
	num_cards_revealed = 0;
});

let allSelects = document.getElementsByTagName('select')
let flop = document.getElementsByClassName('flop');
let turn = document.getElementsByClassName('turn');
let river = document.getElementsByClassName('river');
let i;

const valueDict = {
	"2": "2",
	"3": "3",
	"4": "4",
	"5": "5",
	"6": "6",
	"7": "7",
	"8": "8",
	"9": "9",
	"10": "10",
	"11": "J",
	"12": "Q",
	"13": "K",
	"14": "A"
};
const suitDict = {
	"heart": "&hearts;",
	"diamond": "&diams;",
	"spade": "&spades;",
	"club": "&clubs;"
};

for (i = 0; i < allSelects.length; i++) {
	allSelects[i].onchange = function() {
		document.getElementById('1cardsuit').textContent = suitDict[flop[0].value];
	}
}

for (i = 0; i < flop.length; i++) {
	flop[i].onchange = function() {
		if(flop_check()) {
			prepare_api(Array.from(flop).concat(Array.from(turn)).concat(Array.from(river)));
		}
	}
}

for (i = 0; i < turn.length; i++) {
	turn[i].onchange = function() {
		if(turn_check() && flop_check()) {
			prepare_api(Array.from(flop).concat(Array.from(turn)).concat(Array.from(river)));
		}
	}
}

for (i = 0; i < river.length; i++) {
	river[i].onchange = function() {
		if (river_check() && turn_check() && flop_check()) {
			prepare_api(Array.from(flop).concat(Array.from(turn)).concat(Array.from(river)));
		}
	}
}

function river_check() {
	for (i = 0; i < river.length; i++) {
		let index = river[i].selectedIndex;
		if (index == 0) {
			return false;
		}
	}
	return true;
}

function turn_check() {
	for (i = 0; i < turn.length; i++) {
		let index = turn[i].selectedIndex;
		if (index == 0) {
			return false;
		}
	}
	return true;
}

function flop_check() {
	for (i = 0; i < flop.length; i++) {
		let index = flop[i].selectedIndex;
		if (index == 0) {
			return false;
		}
	}
	return true;
}

function prepare_api(selects) {
	let i;
	let cards = []

	for (i = 0; i < selects.length; i += 2) {
		let suit = selects[i].selectedIndex - 1;

		let number = selects[i + 1].selectedIndex + 1;

		if (number == 14) {
			number = 1;
		}

		if (suit != -1) {
			cards.push(suit + ' ' + number);
		}
	}

	call_api(cards);
}

function call_api(cards) {
	let url = 'https://rsbiisnv12.execute-api.us-east-2.amazonaws.com/default/analyze';

	let xhr = new XMLHttpRequest();

	xhr.onreadystatechange = function () {
		if (xhr.readyState === 4) {
			console.log(xhr.status);
			receive_data(xhr.response);
		}
	};

	console.log(cards);

	xhr.open('POST', url);
	xhr.send([JSON.stringify(cards)]);
}

function receive_data(response) {
	parsedResponse = JSON.parse(response);

	console.log(response);

	for (let obj in parsedResponse) {
		chance = document.getElementById(obj);

		chance.innerHTML = String(parsedResponse[obj]) + '%';
	}
}