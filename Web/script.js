const display = document.getElementById('display');

function appendNumber(num) {
    if (display.value === '0') {
        display.value = num;
    } else {
        display.value += num;
    }
}

function appendOperator(operator) {
    display.value += ' ' + operator + ' ';
}

function clearDisplay() {
    display.value = '0';
}

function calculate() {
    try {
        // Usa eval de forma segura para o protótipo básico
        display.value = eval(display.value);
    } catch (error) {
        display.value = 'Erro';
    }
}